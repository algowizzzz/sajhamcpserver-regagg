"""
Read layer over the corpus — shared by the MCP tools (Epic 6) and the admin
panel (Epic 7). All functions are stateless and read-only.

Search here is a portable filter-then-rank fallback (SQL filters -> keyword
scoring over title + stored markdown). In production the ranking step delegates
to the existing SAJHA BM25 MCP tool over content.md (TRD §7); the filter stage
is identical. Keeping one module avoids drift between the chatbot and the admin
views.
"""

from __future__ import annotations

import re
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List, Optional

from sqlalchemy import select

from sajha.regagg.models import (
    Document, DocumentEdge, DocumentTag, Run,
)


# ── search ──────────────────────────────────────────────────────────────────

def reg_search(session, storage, query: str, *, jurisdiction=None, regulator_id=None,
               doc_type=None, tags=None, date_from=None, date_to=None, status=None,
               limit: int = 10) -> List[dict]:
    stmt = select(Document)
    if regulator_id:
        stmt = stmt.where(Document.regulator_id.in_(_aslist(regulator_id)))
    if doc_type:
        stmt = stmt.where(Document.doc_type.in_(_aslist(doc_type)))
    if status:
        stmt = stmt.where(Document.status.in_(_aslist(status)))
    if date_from:
        stmt = stmt.where(Document.published_date >= _asdate(date_from))
    if date_to:
        stmt = stmt.where(Document.published_date <= _asdate(date_to))
    candidates = list(session.scalars(stmt).all())

    if jurisdiction:
        juris = set(_aslist(jurisdiction))
        candidates = [d for d in candidates if _doc_jurisdiction(session, d) in juris]
    if tags:
        want = set(_aslist(tags))
        candidates = [d for d in candidates if want <= _doc_tags(session, d)]

    terms = [t for t in re.split(r"\W+", query.lower()) if t]
    scored = []
    for d in candidates:
        score, snippet = _score(d, terms, storage)
        if query and score == 0:
            continue
        scored.append((score, d, snippet))
    scored.sort(key=lambda x: (-x[0], str(x[1].published_date or "")), reverse=False)
    scored.sort(key=lambda x: x[0], reverse=True)

    out = []
    for score, d, snippet in scored[:limit]:
        out.append({
            "doc_id": d.doc_id, "regulator_id": d.regulator_id, "title": d.title,
            "doc_type": d.doc_type, "status": d.status,
            "published_date": d.published_date.isoformat() if d.published_date else None,
            "score": round(score, 3), "snippet": snippet, "source_url": d.source_url,
        })
    return out


def _score(doc: Document, terms: List[str], storage) -> tuple:
    if not terms:
        return 1.0, (doc.title or "")[:200]
    title = (doc.title or "").lower()
    content = ""
    if storage is not None:
        content = (storage.read_content(doc.s3_prefix) or "").lower()
    score = 0.0
    for t in terms:
        score += title.count(t) * 3.0 + content.count(t) * 1.0
    snippet = _make_snippet(content or title, terms) if score else ""
    return score, snippet


def _make_snippet(text: str, terms: List[str], width: int = 160) -> str:
    for t in terms:
        i = text.find(t)
        if i >= 0:
            start = max(0, i - width // 2)
            return ("…" if start else "") + text[start:start + width].strip() + "…"
    return text[:width]


# ── read ────────────────────────────────────────────────────────────────────

def reg_read(session, storage, doc_id: str, mode: str = "summary",
             regulator_id: Optional[str] = None, version_ts: Optional[str] = None) -> dict:
    doc = _find_doc(session, doc_id, regulator_id)
    if doc is None:
        return {"error": f"doc_id '{doc_id}' not found"}
    meta = storage.read_meta(doc.s3_prefix) or {}
    if mode == "meta":
        return {"meta": meta}
    if version_ts:
        # read a historical version from archive
        from sajha.regagg.models import DocumentVersion
        ver = session.scalars(select(DocumentVersion).where(
            DocumentVersion.regulator_id == doc.regulator_id,
            DocumentVersion.doc_id == doc.doc_id,
            DocumentVersion.version_ts == version_ts)).first()
        if ver is None or not ver.archive_prefix:
            return {"error": f"version {version_ts} not found"}
        return {"content": storage.read_content(ver.archive_prefix),
                "meta": storage.read_meta(ver.archive_prefix)}
    if mode == "full":
        return {"content": storage.read_content(doc.s3_prefix), "meta": meta}
    return {"content": storage.read_summary(doc.s3_prefix) or "", "meta": meta}


# ── tags ────────────────────────────────────────────────────────────────────

def reg_tags(session, prefix: Optional[str] = None, taxonomy: Optional[dict] = None) -> List[dict]:
    rows = session.execute(select(DocumentTag.tag)).all()
    counts: Dict[str, int] = defaultdict(int)
    for (tag,) in rows:
        if prefix and not tag.startswith(prefix):
            continue
        counts[tag] += 1
    cat = _tag_categories(taxonomy) if taxonomy else {}
    return sorted(({"tag": t, "count": c, "category": cat.get(t, "other")}
                   for t, c in counts.items()), key=lambda x: -x["count"])


# ── whats_new ───────────────────────────────────────────────────────────────

def reg_whats_new(session, days: int = 7, jurisdiction=None, doc_type=None,
                  deadlines_within: Optional[int] = None, now: Optional[datetime] = None) -> dict:
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)
    stmt = select(Document).where(Document.ingested_at >= cutoff)
    if doc_type:
        stmt = stmt.where(Document.doc_type.in_(_aslist(doc_type)))
    docs = list(session.scalars(stmt).all())
    if jurisdiction:
        juris = set(_aslist(jurisdiction))
        docs = [d for d in docs if _doc_jurisdiction(session, d) in juris]
    if deadlines_within is not None:
        horizon = (now + timedelta(days=deadlines_within)).date()
        docs = [d for d in docs if d.comment_deadline and now.date() <= d.comment_deadline <= horizon]

    grouped: Dict[str, list] = defaultdict(list)
    for d in docs:
        grouped[d.regulator_id].append({
            "doc_id": d.doc_id, "title": d.title, "doc_type": d.doc_type,
            "published_date": d.published_date.isoformat() if d.published_date else None,
            "comment_deadline": d.comment_deadline.isoformat() if d.comment_deadline else None,
        })
    return {"days": days, "count": len(docs), "by_regulator": dict(grouped)}


# ── graph traversal ─────────────────────────────────────────────────────────

def reg_graph(session, doc_id: str, edge_types=None, depth: int = 1,
              direction: str = "both", regulator_id: Optional[str] = None) -> dict:
    doc = _find_doc(session, doc_id, regulator_id)
    if doc is None:
        return {"error": f"doc_id '{doc_id}' not found", "nodes": [], "edges": []}
    depth = max(1, min(depth, 3))
    et = set(_aslist(edge_types)) if edge_types else None
    start = (doc.regulator_id, doc.doc_id)
    visited = {start}
    nodes = {start}
    edges = []
    frontier = [start]
    for _ in range(depth):
        nxt = []
        for reg, did in frontier:
            for e in _incident_edges(session, reg, did, direction, et):
                edge = {"from": f"{e.from_regulator}/{e.from_doc}",
                        "to": f"{e.to_regulator}/{e.to_doc}",
                        "type": e.edge_type, "confidence": e.confidence}
                edges.append(edge)
                for node in ((e.from_regulator, e.from_doc), (e.to_regulator, e.to_doc)):
                    nodes.add(node)
                    if node not in visited:
                        visited.add(node)
                        nxt.append(node)
        frontier = nxt
    # de-dup edges
    uniq = {(e["from"], e["to"], e["type"]): e for e in edges}
    return {"root": f"{start[0]}/{start[1]}",
            "nodes": [f"{r}/{d}" for r, d in sorted(nodes)],
            "edges": list(uniq.values())}


def _incident_edges(session, reg, did, direction, et):
    out = []
    if direction in ("out", "both"):
        out += session.scalars(select(DocumentEdge).where(
            DocumentEdge.from_regulator == reg, DocumentEdge.from_doc == did)).all()
    if direction in ("in", "both"):
        out += session.scalars(select(DocumentEdge).where(
            DocumentEdge.to_regulator == reg, DocumentEdge.to_doc == did)).all()
    if et:
        out = [e for e in out if e.edge_type in et]
    return out


# ── coverage matrix (admin) ─────────────────────────────────────────────────

def coverage(session, days: int = 7, now: Optional[datetime] = None) -> dict:
    now = now or datetime.now(timezone.utc)
    start = (now.date() - timedelta(days=days - 1))
    runs = session.scalars(select(Run).where(Run.logical_date >= start)).all()
    matrix: Dict[str, Dict[str, dict]] = defaultdict(dict)
    for r in runs:
        cell = matrix[r.regulator_id].get(r.logical_date.isoformat())
        # latest run wins for the cell (by started_at)
        if cell is None or (r.started_at and cell["_started"] and r.started_at >= cell["_started"]):
            matrix[r.regulator_id][r.logical_date.isoformat()] = {
                "status": r.status, "new": r.ingested or 0, "errors": r.errors or 0,
                "_started": r.started_at}
    # strip private field
    for reg in matrix:
        for day in matrix[reg]:
            matrix[reg][day].pop("_started", None)
    dates = [(start + timedelta(days=i)).isoformat() for i in range(days)]
    return {"days": dates, "matrix": {k: dict(v) for k, v in matrix.items()}}


# ── helpers ─────────────────────────────────────────────────────────────────

def _aslist(v):
    return v if isinstance(v, (list, tuple, set)) else [v]


def _asdate(v):
    return v if isinstance(v, date) else date.fromisoformat(str(v))


def _find_doc(session, doc_id: str, regulator_id: Optional[str]):
    if regulator_id:
        return session.get(Document, {"regulator_id": regulator_id, "doc_id": doc_id})
    return session.scalars(select(Document).where(Document.doc_id == doc_id)).first()


def _doc_tags(session, doc) -> set:
    return {t for (t,) in session.execute(select(DocumentTag.tag).where(
        DocumentTag.regulator_id == doc.regulator_id,
        DocumentTag.doc_id == doc.doc_id)).all()}


def _doc_jurisdiction(session, doc) -> Optional[str]:
    from sajha.regagg.models import Regulator
    reg = session.get(Regulator, doc.regulator_id)
    return reg.jurisdiction if reg else None


def _tag_categories(taxonomy: dict) -> Dict[str, str]:
    cat = {}
    for category, tags in (taxonomy.get("tags") or {}).items():
        for t in tags:
            cat[t] = category
    return cat
