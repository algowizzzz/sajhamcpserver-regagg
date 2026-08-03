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
        payloads["api"] = json.loads(opener(build_api_url(config)).decode("utf-8"))
    return payloads


def _resolve_sitemap(url: str, opener: SourceOpener, depth: int = 0) -> bytes:
    """Return a urlset sitemap; if given a sitemapindex, merge child urlsets."""
    data = opener(url)
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
    for loc in (root.findall(".//sm:loc", ns) or root.findall(".//loc")):
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

    try:
        payloads = _fetch_source_payloads(config, source_opener)
        connector = get_connector(config, run_id, seen)
        events: List[DetectionEvent] = connector.detect(payloads)
        manifest.detected = len(events)
        if max_docs is not None and len(events) > max_docs:
            # sample cap (live sampling / polite crawl); full run drops the cap
            events = events[:max_docs]
        manifest.detected_urls = [e.url for e in events]

        for ev in events:
            try:
                fr = fetcher.fetch(ev.url, method=config.fetch)
                manifest.fetched += 1
                seen_row = session.get(SeenUrl, {"regulator_id": config.id, "url": ev.url})
                doc_id = ids.stable_doc_id(
                    ev.reference_number, ev.url,
                    existing=seen_row.doc_id if seen_row else None)
                inp = IngestInput(
                    regulator_id=config.id,
                    doc_type=ev.doc_type_hint or "announcement",
                    title=ev.title or fr.title or ev.url,
                    content_md=fr.content_md, source_url=ev.url,
                    raw=fr.raw, raw_ext=fr.raw_ext,
                    reference_number=ev.reference_number,
                    published_date=ev.published_date, ocr=fr.ocr,
                    tags=list(config.default_tags), doc_id=doc_id)
                result = versioning.ingest(inp, run_id=run_id, now=now)
                if result.action in ("created", "updated"):
                    manifest.ingested += 1
                if result.action == "updated":
                    manifest.archived += 1
                lastmod = ev.published_date.isoformat() if ev.published_date else None
                _record_seen(session, config.id, ev.url, fr.content_hash,
                             result.doc_id, now, lastmod)
            except Exception as e:  # noqa: BLE001 — one bad doc must not fail the run
                manifest.errors += 1
                manifest.error_list.append({"url": ev.url, "error": str(e)})
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
