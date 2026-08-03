"""
Single-regulator ingestion pipeline: detect -> fetch -> version -> record.

``run_regulator`` is the deterministic unit the scheduler (Epic 4) fans out
over. It is stateless (all state in Postgres + object storage), idempotent, and
safe to rerun: unchanged content is skipped, changed content follows the archive
protocol. Network IO is injected (``source_opener`` for feeds/sitemaps/APIs,
``fetcher`` for documents) so the whole path runs offline against fixtures.
"""

from __future__ import annotations

import time
import xml.etree.ElementTree as ET
from datetime import date, datetime, timezone
from typing import Callable, Dict, List, Optional

from sqlalchemy import select

from sajha.regagg import ids
from sajha.regagg.config_models import RegulatorConfig
from sajha.regagg.connectors import get_connector
from sajha.regagg.events import DetectionEvent, RunManifest
from sajha.regagg.fetch import Fetcher
from sajha.regagg.models import Run, SeenUrl
from sajha.regagg.versioning import CorpusVersioning, IngestInput

# source_opener(url) -> bytes  (fetches a feed / sitemap / API endpoint)
SourceOpener = Callable[[str], bytes]


def build_api_url(config: RegulatorConfig) -> str:
    api = config.sources.api
    if api and api.provider == "federal_register":
        agencies = "".join(f"&conditions[agencies][]={a}" for a in (api.agencies or []))
        return f"{api.base}/documents.json?per_page=100&order=newest{agencies}"
    return api.base if api else ""


def _fetch_source_payloads(config: RegulatorConfig, opener: SourceOpener) -> Dict:
    """Fetch the connector's source inputs (with sitemap-index recursion)."""
    payloads: Dict = {}
    s = config.sources
    if config.connector == "sitemap_diff":
        if s.sitemap:
            payloads["sitemap"] = _resolve_sitemap(s.sitemap.url, opener)
        if s.listing_pages:
            payloads["listings"] = [opener(lp.url) for lp in s.listing_pages]
            payloads["listing_base"] = s.listing_pages[0].url
    elif config.connector == "rss":
        payloads["feeds"] = [opener(f.url) for f in s.feeds]
    elif config.connector == "api":
        import json
        # paginate (federal_register: next_page_url) until backfill cutoff or page cap
        url, merged, pages = build_api_url(config), {"results": []}, 0
        while url and pages < 5:
            data = json.loads(opener(url).decode("utf-8"))
            results = data.get("results", [])
            merged["results"].extend(results)
            pages += 1
            cutoff = config.backfill_cutoff
            if cutoff and results:
                oldest = min((r.get("publication_date") or "9999") for r in results)
                if oldest < cutoff.isoformat():
                    break
            url = data.get("next_page_url")
        merged["count"] = len(merged["results"])
        payloads["api"] = merged
    return payloads


def _extract_pdf_links(html: bytes, base_url: str, limit: int = 3) -> List[str]:
    """Same-domain .pdf hrefs from an ingested HTML page (policy-doc harvesting)."""
    from urllib.parse import urljoin, urlparse
    from bs4 import BeautifulSoup
    try:
        soup = BeautifulSoup(html.decode("utf-8", "replace"), "html.parser")
    except Exception:  # noqa: BLE001
        return []
    host = urlparse(base_url).netloc
    out: List[str] = []
    for a in soup.find_all("a", href=True):
        full = urljoin(base_url, a["href"]).split("#")[0]
        if full.lower().endswith(".pdf") and urlparse(full).netloc == host and full not in out:
            out.append(full)
            if len(out) >= limit:
                break
    return out


def _title_from_url(url: str) -> str:
    """Human-readable fallback title from the URL's last path segment —
    'IAIS-Press-Release-2026-07.pdf' -> 'IAIS Press Release 2026 07'.
    (Untitled PDFs previously showed raw URLs in the UI.)"""
    from urllib.parse import unquote, urlparse
    seg = unquote(urlparse(url).path.rstrip("/").rsplit("/", 1)[-1])
    seg = seg.rsplit(".", 1)[0] if "." in seg else seg
    words = seg.replace("-", " ").replace("_", " ").strip()
    return words[:180] if words else url


def _find_by_reference(session, reference_number: str, exclude_regulator: str):
    from sqlalchemy import select
    from sajha.regagg.models import Document
    return session.scalars(select(Document).where(
        Document.reference_number == reference_number,
        Document.regulator_id != exclude_regulator)).first()


def _flush_run(session, run_id: str, manifest: RunManifest) -> None:
    """Mid-run counter flush so the tracking UI can poll live progress."""
    run = session.get(Run, run_id)
    if run:
        run.detected = manifest.detected
        run.fetched = manifest.fetched
        run.ingested = manifest.ingested
        run.archived = manifest.archived
        run.errors = manifest.errors
        session.commit()


MAX_SITEMAP_BYTES = 8_000_000    # refuse pathological sitemaps outright
MAX_SITEMAP_CHILDREN = 30        # cap index recursion (hang guard, logged)


def _resolve_sitemap(url: str, opener: SourceOpener, depth: int = 0) -> bytes:
    """Return a urlset sitemap; if given a sitemapindex, merge child urlsets.
    Hardened: byte cap + child cap so one regulator's monster sitemap can never
    hang the fleet (the truncation is logged, never silent)."""
    data = opener(url)
    if len(data) > MAX_SITEMAP_BYTES:
        import logging
        logging.getLogger(__name__).warning(
            "sitemap %s is %dB > cap %d — truncating parse", url, len(data),
            MAX_SITEMAP_BYTES)
        data = data[:MAX_SITEMAP_BYTES]
        # keep XML well-formed by cutting at the last complete <url> entry
        cut = data.rfind(b"</url>")
        if cut > 0:
            data = data[:cut + 6] + b"</urlset>"
    if depth > 3:
        return data
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return data
    tag = root.tag.split("}")[-1]
    if tag != "sitemapindex":
        return data
    # merge children into a synthetic urlset
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    merged = ['<?xml version="1.0"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    locs = (root.findall(".//sm:loc", ns) or root.findall(".//loc"))
    if len(locs) > MAX_SITEMAP_CHILDREN:
        import logging
        logging.getLogger(__name__).warning(
            "sitemap index %s has %d children — resolving first %d",
            url, len(locs), MAX_SITEMAP_CHILDREN)
        locs = locs[:MAX_SITEMAP_CHILDREN]
    for loc in locs:
        child = _resolve_sitemap(loc.text.strip(), opener, depth + 1)
        try:
            croot = ET.fromstring(child)
        except ET.ParseError:
            continue
        for url_el in (croot.findall(".//sm:url", ns) or croot.findall(".//url")):
            u = url_el.findtext("sm:loc", namespaces=ns) or url_el.findtext("loc")
            lm = url_el.findtext("sm:lastmod", namespaces=ns) or url_el.findtext("lastmod") or ""
            if u:
                merged.append(f"<url><loc>{u.strip()}</loc><lastmod>{lm}</lastmod></url>")
    merged.append("</urlset>")
    return "\n".join(merged).encode("utf-8")


def run_regulator(
    session,
    storage,
    config: RegulatorConfig,
    source_opener: SourceOpener,
    fetcher: Fetcher,
    run_id: str,
    logical_date: str,
    trigger: str = "schedule",
    now: Optional[datetime] = None,
    operator: Optional[str] = None,
    max_docs: Optional[int] = None,
) -> RunManifest:
    now = now or datetime.now(timezone.utc)
    started = time.monotonic()
    manifest = RunManifest(run_id=run_id, regulator_id=config.id,
                           logical_date=logical_date, trigger=trigger)

    # persist a 'running' run row up front (visible on admin page)
    run_row = Run(run_id=run_id, regulator_id=config.id,
                  logical_date=date.fromisoformat(logical_date), trigger=trigger,
                  status="running", operator=operator)
    session.merge(run_row)
    session.commit()

    versioning = CorpusVersioning(session, storage)
    seen = _load_seen(session, config.id)

    HARVEST_PER_PAGE, HARVEST_CAP = 3, 40
    try:
        payloads = _fetch_source_payloads(config, source_opener)
        connector = get_connector(config, run_id, seen)
        events: List[DetectionEvent] = connector.detect(payloads)
        manifest.detected = len(events)
        queue = list(events if max_docs is None else events[:max_docs])
        queued_urls = {e.url for e in queue}
        manifest.detected_urls = [e.url for e in queue]
        harvested = 0
        processed = 0
        i = 0
        while i < len(queue):
            ev = queue[i]
            i += 1
            try:
                # meta-source dedup: an agency copy of this reference already exists
                if config.meta_source and ev.reference_number:
                    dup = _find_by_reference(session, ev.reference_number,
                                             exclude_regulator=config.id)
                    if dup is not None:
                        _record_seen(session, config.id, ev.url, dup.content_hash,
                                     dup.doc_id, now)
                        manifest.deduped += 1
                        continue
                fr = fetcher.fetch(ev.url, method=config.fetch)
                manifest.fetched += 1
                seen_row = session.get(SeenUrl, {"regulator_id": config.id, "url": ev.url})
                doc_id = ids.stable_doc_id(
                    ev.reference_number, ev.url,
                    existing=seen_row.doc_id if seen_row else None)
                inp = IngestInput(
                    regulator_id=config.id,
                    doc_type=ev.doc_type_hint or "announcement",
                    title=ev.title or fr.title or _title_from_url(ev.url),
                    content_md=fr.content_md, source_url=ev.url,
                    raw=fr.raw, raw_ext=fr.raw_ext,
                    reference_number=ev.reference_number,
                    published_date=ev.published_date, ocr=fr.ocr,
                    tags=list(config.default_tags), doc_id=doc_id,
                    source_kind="policy_pdf" if fr.raw_ext == "pdf" else "web",
                    # governance: record the post-redirect URL + fetch method
                    meta_extra={"final_url": fr.final_url,
                                "fetch_method": fr.fetch_method})
                result = versioning.ingest(inp, run_id=run_id, now=now)
                if result.action in ("created", "updated"):
                    manifest.ingested += 1
                    # deterministic enrichment (reference number + rule-based edges)
                    from sajha.regagg import rules
                    from sajha.regagg.models import Document
                    doc = session.get(Document, {"regulator_id": config.id,
                                                 "doc_id": result.doc_id})
                    if doc is not None:
                        rules.apply_rules(session, doc, fr.content_md)
                if result.action == "updated":
                    manifest.archived += 1
                lastmod = ev.published_date.isoformat() if ev.published_date else None
                _record_seen(session, config.id, ev.url, fr.content_hash,
                             result.doc_id, now, lastmod)
                # policy-PDF harvesting from ingested HTML pages
                if (config.harvest_pdfs and fr.raw_ext == "html"
                        and harvested < HARVEST_CAP
                        and (max_docs is None or len(queue) < max_docs * 2)):
                    for pu in _extract_pdf_links(fr.raw, ev.url, HARVEST_PER_PAGE):
                        if pu in queued_urls or pu in seen:
                            continue
                        queued_urls.add(pu)
                        harvested += 1
                        queue.append(DetectionEvent(
                            regulator_id=config.id, url=pu, run_id=run_id,
                            title=None, published_date=ev.published_date,
                            doc_type_hint=ev.doc_type_hint, source="pdf_harvest"))
                        manifest.detected += 1
            except Exception as e:  # noqa: BLE001 — one bad doc must not fail the run
                manifest.errors += 1
                manifest.error_list.append({"url": ev.url, "error": str(e)})
            processed += 1
            if processed % 10 == 0:
                _flush_run(session, run_id, manifest)   # live progress for the UI
        session.commit()
    except Exception as e:  # noqa: BLE001 — source-level failure
        manifest.errors += 1
        manifest.error_list.append({"stage": "source", "error": str(e)})

    manifest.duration_s = round(time.monotonic() - started, 3)
    manifest.finalize()
    _finalize_run(session, storage, config.id, run_id, manifest, now)
    return manifest


# ── seen_urls ───────────────────────────────────────────────────────────────

def _load_seen(session, regulator_id: str) -> Dict[str, str]:
    rows = session.scalars(select(SeenUrl).where(SeenUrl.regulator_id == regulator_id)).all()
    # signal used for lastmod fast-path (falls back to content hash)
    return {r.url: (r.last_modified or r.content_hash or "") for r in rows}


def _record_seen(session, regulator_id: str, url: str, content_hash: str,
                 doc_id: str, now: datetime, last_modified: Optional[str] = None) -> None:
    row = session.get(SeenUrl, {"regulator_id": regulator_id, "url": url})
    if row is None:
        row = SeenUrl(regulator_id=regulator_id, url=url)
        session.add(row)
    row.content_hash = content_hash
    row.doc_id = doc_id
    if last_modified:
        row.last_modified = last_modified
    row.last_checked = now
    row.http_status = 200


# ── run finalize ────────────────────────────────────────────────────────────

def _finalize_run(session, storage, regulator_id: str, run_id: str,
                  manifest: RunManifest, now: datetime) -> None:
    # write manifest to _state/run_manifests/{run_id}.json
    import json
    state = storage.state_prefix(regulator_id)
    storage.backend.write_text(f"{state}/run_manifests/{run_id}.json",
                               json.dumps(manifest.to_dict(), indent=2, default=str))
    run = session.get(Run, run_id)
    if run:
        run.status = manifest.status
        run.detected = manifest.detected
        run.fetched = manifest.fetched
        run.ingested = manifest.ingested
        run.archived = manifest.archived
        run.errors = manifest.errors
        run.finished_at = now
        run.manifest_path = f"{state}/run_manifests/{run_id}.json"
        session.commit()
