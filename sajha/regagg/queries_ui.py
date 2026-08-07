"""
Read-layer queries backing the tracking UI (coverage tree, corpus browser,
changes feed, version diffs, live runs). Stateless; SQL + storage reads only.
"""

from __future__ import annotations

import difflib
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional

from sqlalchemy import case, func, select

from sajha.regagg.models import (
    Document, DocumentVersion, Regulator, Run,
)

REGION_OF = {
    "CA": "Canada", "US": "United States",
    "EU": "EU & UK", "UK": "EU & UK",
    "SG": "APAC", "HK": "APAC", "AU": "APAC", "JP": "APAC", "IN": "APAC",
    "INTL": "International",
}
REGION_ORDER = ["Canada", "United States", "EU & UK", "APAC", "International",
                "Financial News"]   # news category = its own top-level section


def region_of(reg) -> str:
    """The single region rule: news sources form their own section; everything
    else maps by jurisdiction. Used by the tree, corpus browse and exec pages."""
    if getattr(reg, "category", "regulatory") == "news":
        return "Financial News"
    return REGION_OF.get(reg.jurisdiction, "International")


def _tzaware(dt: Optional[datetime]) -> Optional[datetime]:
    if dt is not None and dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt


# ── coverage tree ───────────────────────────────────────────────────────────

def coverage_tree(session, days: int = 7, now: Optional[datetime] = None) -> dict:
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)

    regs = {r.regulator_id: r for r in session.scalars(select(Regulator)).all()}

    # doc counts by (regulator, source_kind)
    counts: Dict[str, Dict[str, int]] = defaultdict(lambda: {"web": 0, "policy_pdf": 0})
    for reg, kind, n in session.execute(
            select(Document.regulator_id, Document.source_kind, func.count())
            .group_by(Document.regulator_id, Document.source_kind)).all():
        counts[reg][kind or "web"] = n

    # new docs in window by (regulator, source_kind)
    new_counts: Dict[str, Dict[str, int]] = defaultdict(lambda: {"web": 0, "policy_pdf": 0})
    for reg, kind, n in session.execute(
            select(Document.regulator_id, Document.source_kind, func.count())
            .where(Document.ingested_at >= cutoff)
            .group_by(Document.regulator_id, Document.source_kind)).all():
        new_counts[reg][kind or "web"] = n

    # last run + status per regulator
    last_runs: Dict[str, Run] = {}
    for run in session.scalars(select(Run).order_by(Run.started_at)).all():
        last_runs[run.regulator_id] = run

    # latest ingest per regulator (staleness)
    last_docs = dict(session.execute(
        select(Document.regulator_id, func.max(Document.ingested_at))
        .group_by(Document.regulator_id)).all())

    regions: Dict[str, dict] = {r: {"region": r, "institutions": []} for r in REGION_ORDER}
    for rid, reg in sorted(regs.items()):
        region = region_of(reg)
        run = last_runs.get(rid)
        li = _tzaware(last_docs.get(rid))
        stale_days = (now - li).days if li else None
        c, nc = counts[rid], new_counts[rid]
        status = "never_run"
        if run:
            status = {"success": "ok", "success_empty": "ok_empty",
                      "failed": "failed", "running": "running"}.get(run.status, run.status)
        if stale_days is not None and reg.staleness_alert_days and \
                stale_days > reg.staleness_alert_days and status.startswith("ok"):
            status = "stale"
        n_docs = c["web"] + c["policy_pdf"]
        detected = max((r.detected or 0) for r in [run]) if run else 0
        regions[region]["institutions"].append({
            "regulator_id": rid, "name": reg.name, "jurisdiction": reg.jurisdiction,
            "connector": reg.connector, "active": reg.active,
            "web": {"docs": c["web"], "new": nc["web"]},
            "pdf": {"docs": c["policy_pdf"], "new": nc["policy_pdf"]},
            "last_run": run.started_at.isoformat() if run and run.started_at else None,
            "last_run_status": run.status if run else None,
            "status": status,
            "stale_days": stale_days,
            # coverage vs what the source advertised in the latest run
            "last_detected": detected,
            "coverage_pct": (min(100, round(100 * n_docs / detected))
                             if detected else None),
        })

    out = []
    for rname in REGION_ORDER:
        insts = regions[rname]["institutions"]
        if not insts:
            continue
        out.append({
            "region": rname,
            "institutions": insts,
            "rollup": {
                "institutions": len(insts),
                "web": sum(i["web"]["docs"] for i in insts),
                "pdf": sum(i["pdf"]["docs"] for i in insts),
                "new": sum(i["web"]["new"] + i["pdf"]["new"] for i in insts),
                "attention": sum(1 for i in insts if i["status"] not in ("ok", "ok_empty")),
            },
        })
    total_docs = session.scalar(select(func.count()).select_from(Document)) or 0
    total_new = session.scalar(select(func.count()).select_from(Document)
                               .where(Document.ingested_at >= cutoff)) or 0
    web_total = sum(r["rollup"]["web"] for r in out)
    pdf_total = sum(r["rollup"]["pdf"] for r in out)
    return {"days": days, "regions": out,
            "totals": {"regulators": len(regs), "documents": total_docs,
                       "web": web_total, "pdf": pdf_total, "new": total_new}}


# ── corpus browser ──────────────────────────────────────────────────────────

def browse(session, regulator_id: str, *, kind: Optional[str] = None,
           doc_type: Optional[str] = None, status: Optional[str] = None,
           q: Optional[str] = None, limit: int = 50, offset: int = 0) -> dict:
    base = select(Document).where(Document.regulator_id == regulator_id)
    if kind:
        base = base.where(Document.source_kind == kind)
    if doc_type:
        base = base.where(Document.doc_type == doc_type)
    if status:
        base = base.where(Document.status == status)
    if q:
        like = f"%{q}%"
        base = base.where(Document.title.ilike(like) | Document.reference_number.ilike(like))

    rows = list(session.scalars(
        base.order_by(Document.published_date.desc().nullslast(),
                      Document.ingested_at.desc())
        .limit(limit).offset(offset)).all())

    # facet counts (over the regulator, pre-filter, so the UI shows the shape)
    def _facet(col):
        return {k or "—": v for k, v in session.execute(
            select(col, func.count()).where(Document.regulator_id == regulator_id)
            .group_by(col)).all()}

    total = session.scalar(select(func.count()).select_from(Document)
                           .where(Document.regulator_id == regulator_id)) or 0
    return {
        "regulator_id": regulator_id, "total": total, "offset": offset,
        "facets": {"doc_type": _facet(Document.doc_type),
                   "status": _facet(Document.status),
                   "source_kind": _facet(Document.source_kind)},
        "documents": [_doc_row(d) for d in rows],
    }


def _doc_row(d: Document) -> dict:
    return {
        "doc_id": d.doc_id, "title": d.title, "doc_type": d.doc_type,
        "status": d.status, "source_kind": d.source_kind,
        "reference_number": d.reference_number, "version_n": d.version_n,
        "published_date": d.published_date.isoformat() if d.published_date else None,
        "effective_date": d.effective_date.isoformat() if d.effective_date else None,
        "comment_deadline": d.comment_deadline.isoformat() if d.comment_deadline else None,
        "source_url": d.source_url, "ocr": d.ocr,
        "materiality_score": d.materiality_score,
        "materiality_band": d.materiality_band,
        "materiality_reason": d.materiality_reason,
        "ingested_at": d.ingested_at.isoformat() if d.ingested_at else None,
    }


# ── full corpus browser (cross-institution, its own page) ───────────────────

def _excerpt(storage, s3_prefix: str, max_chars: int = 220) -> str:
    """Deterministic description: first meaningful body text from content.md
    (headings/links/blank lines skipped). Not an LLM summary — an excerpt."""
    text = storage.read_content(s3_prefix) or ""
    out = []
    for line in text.splitlines():
        l = line.strip()
        if not l or l.startswith(("#", "|", "!", "```", "---", "* [", "- [")):
            continue
        out.append(l)
        if sum(len(x) for x in out) >= max_chars:
            break
    import re as _re
    joined = " ".join(out)
    # strip residual markdown tokens + nav fragments that survive line filtering
    joined = _re.sub(r"[#*_>`|]+", " ", joined)
    joined = _re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", joined)
    joined = _re.sub(r"\s{2,}", " ", joined).strip()
    return (joined[:max_chars] + "…") if len(joined) > max_chars else joined


def corpus_browse(session, storage=None, *, region: Optional[str] = None,
                  category: Optional[str] = None,
                  regulator_ids: Optional[List[str]] = None,
                  kind: Optional[str] = None, doc_type: Optional[str] = None,
                  status: Optional[str] = None, q: Optional[str] = None,
                  band: Optional[str] = None,
                  date_from: Optional[str] = None, date_to: Optional[str] = None,
                  limit: int = 50, offset: int = 0) -> dict:
    """Filterable browse across the whole corpus: continent/region, institution,
    file type (source_kind), doc_type, status, date range, text search."""
    allowed: Optional[set] = set(regulator_ids) if regulator_ids else None
    if category:   # lane scope: regulatory | news
        in_cat = {r.regulator_id for r in session.scalars(select(Regulator)).all()
                  if getattr(r, "category", "regulatory") == category}
        allowed = (allowed & in_cat) if allowed is not None else in_cat
    if region:
        in_region = {r.regulator_id for r in session.scalars(select(Regulator)).all()
                     if region_of(r) == region}
        allowed = (allowed & in_region) if allowed is not None else in_region

    def _scope(stmt):
        if allowed is not None:
            stmt = stmt.where(Document.regulator_id.in_(allowed or [""]))
        return stmt

    stmt = _scope(select(Document))
    if kind:
        stmt = stmt.where(Document.source_kind == kind)
    if doc_type:
        stmt = stmt.where(Document.doc_type == doc_type)
    if status:
        stmt = stmt.where(Document.status == status)
    if band:
        stmt = stmt.where(Document.materiality_band == band)
    if q:
        like = f"%{q}%"
        stmt = stmt.where(Document.title.ilike(like)
                          | Document.reference_number.ilike(like))
    if date_from:
        stmt = stmt.where(Document.published_date >= date_from)
    if date_to:
        stmt = stmt.where(Document.published_date <= date_to)

    total = session.scalar(select(func.count()).select_from(stmt.subquery())) or 0
    rows = list(session.scalars(
        stmt.order_by(Document.published_date.desc().nullslast(),
                      Document.ingested_at.desc())
        .limit(limit).offset(offset)).all())

    # facets over the region/institution scope (pre other filters -> shows shape)
    def _facet(col):
        fstmt = _scope(select(col, func.count()).group_by(col))
        return {k or "—": v for k, v in session.execute(fstmt).all()}

    out_rows = []
    for d in rows:
        r = _doc_row(d)
        r["regulator_id"] = d.regulator_id
        if storage is not None:
            r["excerpt"] = _excerpt(storage, d.s3_prefix)
        out_rows.append(r)
    return {"total": total, "offset": offset, "limit": limit,
            "facets": {"doc_type": _facet(Document.doc_type),
                       "status": _facet(Document.status),
                       "source_kind": _facet(Document.source_kind),
                       "materiality_band": _facet(Document.materiality_band),
                       "regulator": _facet(Document.regulator_id)},
            "documents": out_rows}


# ── changes feed ────────────────────────────────────────────────────────────

def changes(session, days: int = 7, now: Optional[datetime] = None,
            limit: int = 200, *,
            region: Optional[str] = None,
            category: Optional[str] = None,
            regulator_ids: Optional[List[str]] = None,
            source_kind: Optional[str] = None,
            kinds: Optional[List[str]] = None,
            min_band: Optional[str] = None,
            date_from: Optional[str] = None,
            date_to: Optional[str] = None) -> dict:
    """Change feed with the same dimensions as the coverage tree:
    region -> institution -> source_kind, plus an explicit date range
    (date_from/date_to override the rolling `days` window)."""
    now = now or datetime.now(timezone.utc)
    if date_from:
        cutoff = datetime.fromisoformat(date_from).replace(tzinfo=timezone.utc)
    else:
        cutoff = now - timedelta(days=days)
    ceil = None
    if date_to:
        ceil = datetime.fromisoformat(date_to).replace(
            tzinfo=timezone.utc) + timedelta(days=1)

    # lane (category) + region -> allowed regulator set
    allowed: Optional[set] = set(regulator_ids) if regulator_ids else None
    if category:
        in_cat = {r.regulator_id for r in session.scalars(select(Regulator)).all()
                  if getattr(r, "category", "regulatory") == category}
        allowed = (allowed & in_cat) if allowed is not None else in_cat
    if region:
        in_region = {r.regulator_id for r in session.scalars(select(Regulator)).all()
                     if region_of(r) == region}
        allowed = (allowed & in_region) if allowed is not None else in_region

    out: List[dict] = []

    # new + updated: versions created in window.
    # NB: regulator scope MUST be applied in SQL, before the limit — filtering
    # after the fetch made institutions whose rows aren't among the newest N
    # silently vanish from the feed (filter-after-limit bug).
    vstmt = select(DocumentVersion).where(DocumentVersion.created_at >= cutoff)
    if allowed is not None:
        vstmt = vstmt.where(DocumentVersion.regulator_id.in_(allowed or [""]))
    if ceil:
        vstmt = vstmt.where(DocumentVersion.created_at < ceil)
    versions = session.scalars(
        vstmt.order_by(DocumentVersion.created_at.desc()).limit(limit * 4)).all()
    seen = set()
    for v in versions:
        key = (v.regulator_id, v.doc_id)
        if key in seen:
            continue
        seen.add(key)
        doc = session.get(Document, {"regulator_id": v.regulator_id, "doc_id": v.doc_id})
        if doc is None:
            continue
        if source_kind and doc.source_kind != source_kind:
            continue
        kind = "revised" if doc.version_n > 1 else "new"
        if doc.status == "superseded":
            kind = "superseded"
        out.append({
            "kind": kind, "regulator_id": doc.regulator_id,
            "doc": _doc_row(doc),
            "at": (v.created_at.isoformat() if v.created_at else None),
            "has_diff": doc.version_n > 1,
        })

    # deadlines approaching (only when no explicit upper date bound)
    if not date_to:
        horizon = (now + timedelta(days=60)).date()
        dl = session.scalars(select(Document).where(
            Document.comment_deadline.isnot(None),
            Document.comment_deadline >= now.date(),
            Document.comment_deadline <= horizon)).all()
        for doc in dl:
            if allowed is not None and doc.regulator_id not in allowed:
                continue
            if source_kind and doc.source_kind != source_kind:
                continue
            out.append({"kind": "deadline", "regulator_id": doc.regulator_id,
                        "doc": _doc_row(doc), "at": doc.comment_deadline.isoformat(),
                        "has_diff": False})

    # counts BEFORE the kind filter so the tiles stay meaningful as toggles
    counts = defaultdict(int)
    for c in out:
        counts[c["kind"]] += 1
    if kinds:
        want = set(kinds)
        out = [c for c in out if c["kind"] in want]

    # priority filter + ordering: materiality first, recency second, so the
    # analyst's queue leads with what matters rather than what is newest
    if min_band:
        from sajha.regagg.materiality import BAND_ORDER
        allowed_bands = set(BAND_ORDER[:BAND_ORDER.index(min_band) + 1])
        out = [c for c in out if c["doc"].get("materiality_band") in allowed_bands]
    band_counts = defaultdict(int)
    for c in out:
        band_counts[c["doc"].get("materiality_band") or "Informational"] += 1
    out.sort(key=lambda x: (-(x["doc"].get("materiality_score") or 0),
                            x["at"] or ""), reverse=False)
    return {"days": days, "counts": dict(counts),
            "band_counts": dict(band_counts), "changes": out[:limit],
            "filters": {"region": region, "regulator_ids": regulator_ids,
                        "source_kind": source_kind, "kinds": kinds,
                        "min_band": min_band,
                        "date_from": date_from, "date_to": date_to}}


# ── version diff ────────────────────────────────────────────────────────────

def version_diff(session, storage, regulator_id: str, doc_id: str) -> dict:
    doc = session.get(Document, {"regulator_id": regulator_id, "doc_id": doc_id})
    if doc is None:
        return {"error": "not found"}
    if doc.version_n < 2:
        return {"error": "only one version exists"}
    prev = session.scalars(select(DocumentVersion).where(
        DocumentVersion.regulator_id == regulator_id,
        DocumentVersion.doc_id == doc_id,
        DocumentVersion.state == "archived")
        .order_by(DocumentVersion.version_n.desc())).first()
    if prev is None or not prev.archive_prefix:
        return {"error": "archived version not found"}
    old = (storage.read_content(prev.archive_prefix) or "").splitlines()
    new = (storage.read_content(doc.s3_prefix) or "").splitlines()
    diff = list(difflib.unified_diff(
        old, new, fromfile=f"v{prev.version_n}", tofile=f"v{doc.version_n}", lineterm=""))
    added = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
    removed = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
    return {"doc_id": doc_id, "regulator_id": regulator_id,
            "from_version": prev.version_n, "to_version": doc.version_n,
            "added_lines": added, "removed_lines": removed,
            "diff": "\n".join(diff[:2000])}


def overview(session, days: int = 1, priority_days: int = 7,
             now: Optional[datetime] = None) -> dict:
    """First-time-user landing data: one plain-English headline, four numbers,
    the priority items that actually need attention, and one flat table of
    regulators. Everything else on the dashboard is a drill-in from here."""
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)
    tree = coverage_tree(session, days=days, now=now)
    tot = tree["totals"]

    # what landed in the window, by priority band
    band_counts = {b: n for b, n in session.execute(
        select(Document.materiality_band, func.count())
        .where(Document.ingested_at >= cutoff)
        .group_by(Document.materiality_band)).all()}

    # Items worth a human's attention. Uses a wider lookback than the daily
    # delta so the panel stays useful on quiet days — a day with 400 routine
    # notices and nothing material is the normal case, not an error.
    pri_cutoff = now - timedelta(days=priority_days)
    priority_docs = [_doc_row(d) | {"regulator_id": d.regulator_id}
                     for d in session.scalars(
        select(Document).where(Document.ingested_at >= pri_cutoff,
                               Document.materiality_band.in_(["Critical", "High"]))
        .order_by(Document.materiality_score.desc()).limit(10)).all()]

    # flat regulator table (no nesting) with a single health signal
    rows = []
    for region in tree["regions"]:
        for i in region["institutions"]:
            healthy = i["status"] in ("ok", "ok_empty")
            rows.append({
                "regulator_id": i["regulator_id"], "name": i["name"],
                "region": region["region"], "jurisdiction": i["jurisdiction"],
                "web": i["web"]["docs"], "pdf": i["pdf"]["docs"],
                "new": i["web"]["new"] + i["pdf"]["new"],
                "healthy": healthy,
                "health_label": ("Up to date" if i["status"] == "ok"
                                 else "No new documents" if i["status"] == "ok_empty"
                                 else "Stale" if i["status"] == "stale"
                                 else "Collection issue" if i["status"] == "failed"
                                 else "Not yet collected"),
                "coverage_pct": i["coverage_pct"],
            })
    rows.sort(key=lambda r: (-r["new"], r["regulator_id"]))
    attention = [r for r in rows if not r["healthy"]]

    news_ids = {r.regulator_id for r in session.scalars(select(Regulator)).all()
                if getattr(r, "category", "regulatory") == "news"}
    for r in rows:
        r["category"] = "news" if r["regulator_id"] in news_ids else "regulatory"
    collecting = sum(1 for r in rows
                     if r["category"] == "regulatory" and r["web"] + r["pdf"] > 0)
    news_collecting = sum(1 for r in rows
                          if r["category"] == "news" and r["web"] + r["pdf"] > 0)
    n_reg_total = tot["regulators"] - len(news_ids)
    headline = (f"Tracking {collecting} of {n_reg_total} regulators"
                + (f" and {news_collecting} of {len(news_ids)} news sources"
                   if news_ids else "") + " · "
                f"{tot['documents']:,} documents · "
                f"{tot['new']:,} new in the last {days} day"
                f"{'s' if days != 1 else ''} · "
                + ("all sources healthy" if not attention
                   else f"{len(attention)} need attention"))

    return {"headline": headline, "days": days,
            "priority_days": priority_days,
            "totals": {"regulators_tracking": collecting,
                       "regulators_total": n_reg_total,
                       "news_tracking": news_collecting,
                       "news_total": len(news_ids),
                       "documents": tot["documents"], "web": tot["web"],
                       "pdf": tot["pdf"], "new": tot["new"]},
            "priority": {"counts": band_counts, "items": priority_docs},
            "regulators": rows, "attention": attention}


# ── expected-inventory reconciliation ───────────────────────────────────────

def inventory(session, regulator_id: str,
              inventories_dir: str = "config/regulators/_inventories") -> dict:
    """Reconcile the corpus against the regulator's expected inventory (if one
    is defined). Answers "do we have every chapter?" with per-series
    present/missing lists. Match order: reference slug -> title substring."""
    import yaml
    from pathlib import Path
    from sajha.regagg import ids as _ids
    path = Path(inventories_dir) / f"{regulator_id}.yaml"
    if not path.exists():
        return {"regulator_id": regulator_id, "available": False,
                "note": "no expected-inventory file defined"}
    spec = yaml.safe_load(path.read_text(encoding="utf-8"))

    docs = list(session.scalars(select(Document).where(
        Document.regulator_id == regulator_id)).all())
    by_slug = {}
    for d in docs:
        if d.reference_number:
            by_slug[_ids.slugify_ref(d.reference_number)] = d
        by_slug.setdefault(d.doc_id, d)
    titles = [((d.title or "").lower(), d) for d in docs]

    series_out = []
    for series in spec.get("series", []):
        items = []
        present = 0
        for item in series.get("items", []):
            slug = _ids.slugify_ref(item["ref"])
            hit = by_slug.get(slug)
            if hit is None:   # fallback: title substring
                want = item["title"].split("—")[-1].strip().lower()
                for t, d in titles:
                    if want and want in t:
                        hit = d
                        break
            items.append({"ref": item["ref"], "title": item["title"],
                          "present": hit is not None,
                          "doc_id": hit.doc_id if hit else None,
                          "version_n": hit.version_n if hit else None,
                          "status": hit.status if hit else None})
            present += hit is not None
        series_out.append({"name": series["name"], "expected": len(items),
                           "present": present, "complete": present == len(items),
                           "items": items})
    return {"regulator_id": regulator_id, "available": True,
            "verified_against_site": bool(spec.get("verified_against_site")),
            "series": series_out,
            "summary": {"expected": sum(s["expected"] for s in series_out),
                        "present": sum(s["present"] for s in series_out)}}


# ── live runs ───────────────────────────────────────────────────────────────

def runs_overview(session, history: int = 15) -> dict:
    active = [r for r in session.scalars(
        select(Run).where(Run.status == "running")).all()]
    recent = list(session.scalars(
        select(Run).order_by(Run.started_at.desc()).limit(history)).all())

    def _run(r: Run) -> dict:
        return {"run_id": r.run_id, "regulator_id": r.regulator_id,
                "logical_date": r.logical_date.isoformat(), "trigger": r.trigger,
                "status": r.status, "detected": r.detected, "fetched": r.fetched,
                "ingested": r.ingested, "archived": r.archived, "errors": r.errors,
                "operator": r.operator,
                "started_at": r.started_at.isoformat() if r.started_at else None,
                "finished_at": r.finished_at.isoformat() if r.finished_at else None}

    # daily delta: aggregate by logical_date (fetched included for pass-rate)
    delta = []
    for day, n_runs, fetched, ingested, archived, errors in session.execute(
            select(Run.logical_date, func.count(), func.sum(Run.fetched),
                   func.sum(Run.ingested), func.sum(Run.archived), func.sum(Run.errors))
            .group_by(Run.logical_date)
            .order_by(Run.logical_date.desc()).limit(10)).all():
        f, err = int(fetched or 0), int(errors or 0)
        attempts = f + err
        delta.append({"date": day.isoformat(), "runs": n_runs,
                      "fetched": f, "new_docs": int(ingested or 0),
                      "archived": int(archived or 0), "errors": err,
                      "pass_rate": round(100 * f / attempts, 1) if attempts else 100.0})

    # today's summary incl. what failed (regulator + error count)
    today = delta[0] if delta and delta[0]["date"] == now_date_iso() else None
    failing = []
    if today:
        for r in recent:
            if r.logical_date.isoformat() == today["date"] and (r.errors or 0) > 0:
                failing.append({"regulator_id": r.regulator_id, "errors": r.errors,
                                "ingested": r.ingested, "status": r.status})
    return {"active": [_run(r) for r in active],
            "recent": [_run(r) for r in recent],
            "daily_delta": delta,
            "today": today, "today_failing": failing}


def now_date_iso() -> str:
    return datetime.now(timezone.utc).date().isoformat()


# ── financial-news dashboard (credit-analyst lens) ──────────────────────────
# Deterministic topic buckets ordered by how directly they move obligor credit
# risk. Keyword classification, no LLM — same explainability bar as materiality.

NEWS_TOPICS = [
    ("credit", "Ratings & credit events", 50,
     ["downgrade", "upgrade", "rating", "default", "bankruptcy", "insolven",
      "restructur", "chapter 11", "creditor", "distressed", "missed payment",
      "junk bond", "high-yield", "credit spread", "delinquen", "write-down",
      "writedown", "impairment", "covenant", "receivership"]),
    ("rates", "Central banks & rates", 40,
     ["fed ", "federal reserve", "bank of canada", "ecb", "bank of england",
      "boj", "rate cut", "rate hike", "interest rate", "policy rate",
      "inflation", "cpi", "rate decision", "monetary policy", "yield curve",
      "treasury yield", "bond yield"]),
    ("banking", "Banking & financials", 30,
     ["bank", "lender", "loan", "mortgage", "deposit", "credit card",
      "capital ratio", "provision", "loan loss", "insurer", "insurance",
      "pension", "private credit", "private equity", "hedge fund"]),
    ("economy", "Economy & macro", 22,
     ["gdp", "recession", "unemployment", "jobs report", "payroll", "housing",
      "tariff", "trade war", "consumer spending", "retail sales",
      "manufacturing", "exports", "deficit", "stimulus"]),
    ("deals", "Deals & capital raising", 18,
     ["merger", "acquisition", "takeover", "ipo", "buyout", "leveraged",
      "debt sale", "bond issue", "refinanc", "spin-off", "stake"]),
    ("energy", "Energy & commodities", 14,
     ["oil", "crude", "gas", "opec", "gold", "copper", "commodit", "pipeline",
      "lng", "uranium", "lithium"]),
    ("markets", "Markets", 8,
     ["stocks", "equities", "s&p", "tsx", "nasdaq", "dow", "sell-off",
      "rally", "futures", "earnings", "shares", "dollar", "currency"]),
]
# home-market bonus: a Canadian bank's book is CAD/USD-heavy
_NEWS_REGION_BONUS = {"Canada": 6, "US": 3}


def _classify_news(text: str):
    """Best topic bucket for a headline+summary; (key, label, weight, hits)."""
    low = (text or "").lower()
    best = ("general", "General", 0, 0)
    for key, label, weight, kws in NEWS_TOPICS:
        hits = sum(1 for k in kws if k in low)
        if hits and (weight + hits) > (best[2] + best[3]):
            best = (key, label, weight, hits)
    return best


def news_dashboard(session, storage=None, day: Optional[str] = None,
                   days_back: int = 14) -> dict:
    """One day of financial news, ranked for a credit analyst, plus history.

    Rank = topic weight (credit events > rates > banking > ...) + keyword
    density + home-market bonus + materiality score. Fully explainable.
    """
    regs = {r.regulator_id: r for r in session.scalars(
        select(Regulator).where(Regulator.category == "news")).all()}
    if not regs:
        return {"day": None, "days": [], "stories": [], "topics": [],
                "sources": [], "regions": []}

    day_col = func.coalesce(Document.published_date, func.date(Document.ingested_at))
    rows = session.execute(
        select(day_col, func.count()).where(Document.regulator_id.in_(regs))
        .group_by(day_col).order_by(day_col.desc()).limit(days_back)).all()
    days = [{"day": str(d), "count": c} for d, c in rows if d]
    if not days:
        return {"day": None, "days": [], "stories": [], "topics": [],
                "sources": [], "regions": []}
    day = day if day in {x["day"] for x in days} else days[0]["day"]

    docs = session.scalars(
        select(Document).where(Document.regulator_id.in_(regs),
                               day_col == day)).all()
    stories, topic_counts, source_counts = [], defaultdict(int), defaultdict(int)
    for d in docs:
        reg = regs[d.regulator_id]
        excerpt = _excerpt(storage, d.s3_prefix, max_chars=260) if storage else ""
        # the shipped attribution line is boilerplate, not a summary
        if excerpt.startswith("Read the full story"):
            excerpt = ""
        key, label, weight, hits = _classify_news(f"{d.title} {excerpt}")
        region = reg.jurisdiction if reg.jurisdiction in _NEWS_REGION_BONUS             else ("UK/EU" if reg.jurisdiction in ("UK", "EU") else "World")
        score = weight + 2 * hits + _NEWS_REGION_BONUS.get(reg.jurisdiction, 0)             + (d.materiality_score or 0)
        topic_counts[key] += 1
        source_counts[d.regulator_id] += 1
        stories.append({
            "regulator_id": d.regulator_id, "doc_id": d.doc_id,
            "source": reg.name, "region": region, "title": d.title,
            "url": d.source_url, "excerpt": excerpt,
            "time": str(d.ingested_at or ""), "topic": key, "topic_label": label,
            "rank": score,
            "why": f"{label.lower()} +{weight}"
                   + (f"; {hits} signal term{'s' if hits > 1 else ''}" if hits else "")
                   + (f"; {reg.jurisdiction} market" if reg.jurisdiction in _NEWS_REGION_BONUS else ""),
        })
    stories.sort(key=lambda s: (-s["rank"], s["source"], s["title"] or ""))
    labels = {k: l for k, l, _, _ in NEWS_TOPICS}
    labels["general"] = "General"
    order = [k for k, *_ in NEWS_TOPICS] + ["general"]
    return {
        "day": day, "days": days, "stories": stories,
        "topics": [{"key": k, "label": labels[k], "count": topic_counts[k]}
                   for k in order if topic_counts.get(k)],
        "sources": sorted(({"regulator_id": rid, "name": regs[rid].name,
                            "count": c} for rid, c in source_counts.items()),
                          key=lambda s: -s["count"]),
        "regions": sorted({s["region"] for s in stories}),
    }


# ── executive pages (home + the two lane deep-dives) ────────────────────────
# Every section of those pages is one key in these payloads — the HTML holds no
# numbers of its own, so the pages are always as current as the database.

def _lane_ids(session):
    regs = list(session.scalars(select(Regulator)).all())
    news = {r.regulator_id for r in regs if getattr(r, "category", "regulatory") == "news"}
    return regs, news, {r.regulator_id for r in regs} - news


def _band_counts(session, ids) -> dict:
    rows = session.execute(
        select(Document.materiality_band, func.count())
        .where(Document.regulator_id.in_(ids or [""]))
        .group_by(Document.materiality_band)).all()
    return {b: c for b, c in rows}


def _collecting(session, ids) -> int:
    rows = session.execute(
        select(Document.regulator_id, func.count())
        .where(Document.regulator_id.in_(ids or [""]))
        .group_by(Document.regulator_id)).all()
    return sum(1 for _, c in rows if c)


def exec_summary(session, days: int = 1) -> dict:
    """Home page: the whole product in six tiles and three charts."""
    regs, news_ids, reg_ids = _lane_ids(session)
    by_name = {r.regulator_id: r for r in regs}
    docs = session.scalar(select(func.count()).select_from(Document)) or 0
    pdfs = session.scalar(select(func.count()).select_from(Document)
                          .where(Document.source_kind == "policy_pdf")) or 0
    versions = session.scalar(select(func.count()).select_from(DocumentVersion)) or 0
    archived = session.scalar(select(func.count()).select_from(DocumentVersion)
                              .where(DocumentVersion.state == "archived")) or 0
    runs = session.scalar(select(func.count()).select_from(Run)) or 0
    ok_runs = session.scalar(select(func.count()).select_from(Run)
                             .where(Run.status.like("success%"))) or 0

    region_rows = session.execute(
        select(Document.regulator_id, func.count()).group_by(Document.regulator_id)).all()
    regions: Dict[str, int] = defaultdict(int)
    for rid, c in region_rows:
        if rid in by_name:
            regions[region_of(by_name[rid])] += c
    order = [r for r in REGION_ORDER if regions.get(r)]

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    new_docs = session.scalar(select(func.count()).select_from(Document)
                              .where(Document.ingested_at >= cutoff)) or 0
    return {
        "tiles": {"documents": docs, "sources": len(regs),
                  "regulators": len(reg_ids), "news_sources": len(news_ids),
                  "policy_pdfs": pdfs, "versions": versions, "archived": archived,
                  "critical": _band_counts(session, reg_ids).get("Critical", 0),
                  "runs": runs,
                  "pass_rate": round(100 * ok_runs / runs) if runs else 0,
                  "new": new_docs, "days": days},
        "regions": [{"region": r, "count": regions[r]} for r in order],
        "bands": _band_counts(session, reg_ids),
        "news_volume": news_daily_volume(session, news_ids),
        "lanes": {
            "regulatory": {"sources": len(reg_ids),
                           "collecting": _collecting(session, reg_ids),
                           "documents": sum(c for rid, c in region_rows if rid in reg_ids)},
            "news": {"sources": len(news_ids),
                     "collecting": _collecting(session, news_ids),
                     "documents": sum(c for rid, c in region_rows if rid in news_ids)},
        },
    }


def news_daily_volume(session, news_ids=None, limit: int = 14) -> List[dict]:
    if news_ids is None:
        _, news_ids, _ = _lane_ids(session)
    day_col = func.coalesce(Document.published_date, func.date(Document.ingested_at))
    rows = session.execute(
        select(day_col, func.count()).where(Document.regulator_id.in_(news_ids or [""]))
        .group_by(day_col).order_by(day_col.desc()).limit(limit)).all()
    return [{"day": str(d), "count": c} for d, c in reversed(rows) if d]


def exec_regulatory(session, top: int = 10) -> dict:
    """Regulatory lane deep-dive: league table, mix, bands, top holdings."""
    regs, _, reg_ids = _lane_ids(session)
    by_id = {r.regulator_id: r for r in regs}

    league_rows = session.execute(
        select(Document.regulator_id, func.count(),
               func.sum(case((Document.source_kind == "policy_pdf", 1), else_=0)))
        .where(Document.regulator_id.in_(reg_ids or [""]))
        .group_by(Document.regulator_id).order_by(func.count().desc())).all()
    league = [{"regulator_id": rid,
               "name": by_id[rid].name if rid in by_id else rid,
               "jurisdiction": by_id[rid].jurisdiction if rid in by_id else "",
               "documents": c, "policy_pdfs": int(p or 0)}
              for rid, c, p in league_rows]

    types = [{"doc_type": dt, "count": c} for dt, c in session.execute(
        select(Document.doc_type, func.count())
        .where(Document.regulator_id.in_(reg_ids or [""]))
        .group_by(Document.doc_type).order_by(func.count().desc())).all()]

    top_docs = [{"regulator_id": d.regulator_id, "doc_id": d.doc_id, "title": d.title,
                 "score": d.materiality_score, "band": d.materiality_band,
                 "reason": d.materiality_reason, "doc_type": d.doc_type}
                for d in session.scalars(
                    select(Document).where(Document.regulator_id.in_(reg_ids or [""]),
                                           Document.materiality_band == "Critical")
                    .order_by(Document.materiality_score.desc(),
                              Document.ingested_at.desc()).limit(5)).all()]

    arch_rows = session.execute(
        select(DocumentVersion.regulator_id, func.count())
        .where(DocumentVersion.state == "archived")
        .group_by(DocumentVersion.regulator_id)
        .order_by(func.count().desc()).limit(6)).all()

    versions = session.scalar(select(func.count()).select_from(DocumentVersion)
                              .where(DocumentVersion.regulator_id.in_(reg_ids or [""]))) or 0
    archived = sum(c for _, c in arch_rows)
    return {
        "tiles": {"documents": sum(x["documents"] for x in league),
                  "sources": len(reg_ids), "collecting": _collecting(session, reg_ids),
                  "policy_pdfs": sum(x["policy_pdfs"] for x in league),
                  "versions": versions, "archived": archived},
        "league": league[:top], "league_rest": len(league) - min(top, len(league)),
        "doc_types": types, "bands": _band_counts(session, reg_ids),
        "top_docs": top_docs,
        "archived_by": [{"regulator_id": rid,
                         "name": by_id[rid].name if rid in by_id else rid,
                         "count": c} for rid, c in arch_rows],
    }


def exec_news(session, storage=None) -> dict:
    """News lane deep-dive: the ranking lens, volume, reach, today's proof."""
    regs, news_ids, _ = _lane_ids(session)
    by_id = {r.regulator_id: r for r in regs}
    caps = {r.regulator_id for r in regs}

    rows = session.execute(
        select(Document.regulator_id, func.count())
        .where(Document.regulator_id.in_(news_ids or [""]))
        .group_by(Document.regulator_id)).all()
    counts = {rid: c for rid, c in rows}
    sources = sorted(({"regulator_id": rid,
                       "name": by_id[rid].name if rid in by_id else rid,
                       "jurisdiction": by_id[rid].jurisdiction if rid in by_id else "",
                       "count": counts.get(rid, 0)} for rid in news_ids),
                     key=lambda s: (-s["count"], s["name"]))

    regions: Dict[str, int] = defaultdict(int)
    for rid, c in rows:
        j = by_id[rid].jurisdiction if rid in by_id else ""
        regions[{"Canada": "Canada", "US": "United States",
                 "UK": "UK & EU", "EU": "UK & EU"}.get(j, "World / APAC")] += c

    today = news_dashboard(session, storage=storage)
    topic_counts = {t["key"]: t["count"] for t in today.get("topics", [])}
    lens = [{"key": k, "label": label, "weight": w, "count": topic_counts.get(k, 0)}
            for k, label, w, _ in NEWS_TOPICS]
    return {
        "tiles": {"stories": sum(counts.values()), "sources": len(news_ids),
                  "today": len(today.get("stories", [])),
                  "reporting_today": len(today.get("sources", [])),
                  "cap": 50, "regions": len(regions), "scraped": 0},
        "day": today.get("day"), "lens": lens,
        "volume": news_daily_volume(session, news_ids),
        "regions": sorted(({"region": r, "count": c} for r, c in regions.items()),
                          key=lambda x: -x["count"]),
        "sources": sources,
        "proof": today.get("stories", [])[:3],
    }
