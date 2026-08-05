"""
Read-layer queries backing the tracking UI (coverage tree, corpus browser,
changes feed, version diffs, live runs). Stateless; SQL + storage reads only.
"""

from __future__ import annotations

import difflib
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional

from sqlalchemy import func, select

from sajha.regagg.models import (
    Document, DocumentVersion, Regulator, Run,
)

REGION_OF = {
    "CA": "Canada", "US": "United States",
    "EU": "EU & UK", "UK": "EU & UK",
    "SG": "APAC", "HK": "APAC", "AU": "APAC", "JP": "APAC", "IN": "APAC",
    "INTL": "International",
}
REGION_ORDER = ["Canada", "United States", "EU & UK", "APAC", "International"]


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
        region = REGION_OF.get(reg.jurisdiction, "International")
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
                  regulator_ids: Optional[List[str]] = None,
                  kind: Optional[str] = None, doc_type: Optional[str] = None,
                  status: Optional[str] = None, q: Optional[str] = None,
                  band: Optional[str] = None,
                  date_from: Optional[str] = None, date_to: Optional[str] = None,
                  limit: int = 50, offset: int = 0) -> dict:
    """Filterable browse across the whole corpus: continent/region, institution,
    file type (source_kind), doc_type, status, date range, text search."""
    allowed: Optional[set] = set(regulator_ids) if regulator_ids else None
    if region:
        in_region = {r.regulator_id for r in session.scalars(select(Regulator)).all()
                     if REGION_OF.get(r.jurisdiction, "International") == region}
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

    # region -> allowed regulator set
    allowed: Optional[set] = set(regulator_ids) if regulator_ids else None
    if region:
        in_region = {r.regulator_id for r in session.scalars(select(Regulator)).all()
                     if REGION_OF.get(r.jurisdiction, "International") == region}
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

    collecting = sum(1 for r in rows if r["web"] + r["pdf"] > 0)
    headline = (f"Tracking {collecting} of {tot['regulators']} regulators · "
                f"{tot['documents']:,} documents · "
                f"{tot['new']:,} new in the last {days} day"
                f"{'s' if days != 1 else ''} · "
                + ("all sources healthy" if not attention
                   else f"{len(attention)} need attention"))

    return {"headline": headline, "days": days,
            "priority_days": priority_days,
            "totals": {"regulators_tracking": collecting,
                       "regulators_total": tot["regulators"],
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
