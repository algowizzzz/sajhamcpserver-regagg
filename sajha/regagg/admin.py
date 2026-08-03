"""
Operator admin API (Feature 6 / Epic 7, TRD §8).

A FastAPI router mountable on the SAJHA app (``app.include_router(create_admin_router())``)
that exposes the coverage matrix, regulator drill-down, run manifests, rerun /
toggle controls, the enrichment review queue, and the integrity report. It reuses
the shared read layer (queries.py) and the runtime providers, and logs every
mutating action to the core ``audit_log`` with the operator identity.

UI note: the spec's HTMX/Jinja screens (05_ADMIN_UX_SPEC) render on top of these
JSON endpoints; the endpoints are the contract and are what we test here.
"""

from __future__ import annotations

from datetime import date, datetime, timezone
from typing import List, Optional

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from sqlalchemy import select

from sajha.regagg import queries, runtime
from sajha.regagg.models import Document, DocumentTag, Regulator, Run


class RerunRequest(BaseModel):
    scope: str = "all"                 # 'all' | 'ids'
    date: Optional[str] = None         # logical date (defaults to today)
    ids: Optional[List[str]] = None


def _audit(session, operator: str, action: str, rtype: str, rid: str, details: str = "") -> None:
    """Best-effort audit to the core audit_log (no-op if table absent in a test DB)."""
    try:
        from sajha.db.models import AuditLog
        session.add(AuditLog(user_id=operator, action=action,
                             resource_type=rtype, resource_id=rid, details=details))
        session.commit()
    except Exception:  # noqa: BLE001
        session.rollback()


def create_admin_router() -> APIRouter:
    router = APIRouter(prefix="/api/regagg", tags=["regagg-admin"])

    @router.get("/coverage")
    def coverage(days: int = 7):
        session = runtime.get_session()
        return queries.coverage(session, days=days)

    @router.get("/regulators/{regulator_id}")
    def regulator_detail(regulator_id: str):
        session = runtime.get_session()
        reg = session.get(Regulator, regulator_id)
        if reg is None:
            raise HTTPException(404, f"regulator '{regulator_id}' not found")
        latest = session.scalars(
            select(Document).where(Document.regulator_id == regulator_id)
            .order_by(Document.ingested_at.desc()).limit(50)).all()
        staleness = _staleness(session, reg)
        return {
            "regulator_id": reg.regulator_id, "name": reg.name,
            "jurisdiction": reg.jurisdiction, "connector": reg.connector,
            "active": reg.active, "staleness_alert_days": reg.staleness_alert_days,
            "staleness": staleness,
            "latest_documents": [
                {"doc_id": d.doc_id, "title": d.title, "doc_type": d.doc_type,
                 "version_n": d.version_n, "source_url": d.source_url,
                 "published_date": d.published_date.isoformat() if d.published_date else None}
                for d in latest],
        }

    @router.get("/regulators/{regulator_id}/runs")
    def regulator_runs(regulator_id: str, limit: int = 20):
        session = runtime.get_session()
        runs = session.scalars(
            select(Run).where(Run.regulator_id == regulator_id)
            .order_by(Run.started_at.desc()).limit(limit)).all()
        return {"runs": [_run_dict(r) for r in runs]}

    @router.get("/runs/{run_id}")
    def run_detail(run_id: str):
        session = runtime.get_session()
        run = session.get(Run, run_id)
        if run is None:
            raise HTTPException(404, f"run '{run_id}' not found")
        manifest = None
        if run.manifest_path:
            try:
                import json
                manifest = json.loads(runtime.get_storage().backend.read_text(run.manifest_path))
            except Exception:  # noqa: BLE001
                manifest = None
        return {"run": _run_dict(run), "manifest": manifest}

    @router.post("/rerun")
    def rerun(req: RerunRequest, x_operator: str = Header("anonymous")):
        if req.scope not in ("all", "ids"):
            raise HTTPException(400, "scope must be 'all' or 'ids'")
        logical_date = req.date or date.today().isoformat()
        ids = req.ids if req.scope == "ids" else None
        _audit(runtime.get_session(), x_operator, "regagg.rerun", "regulator",
               ",".join(ids) if ids else "all", f"date={logical_date}")
        trigger = runtime.get_rerun_trigger()
        result = trigger(scope=req.scope, logical_date=logical_date, ids=ids, operator=x_operator)
        return {"queued": result, "scope": req.scope, "date": logical_date, "operator": x_operator}

    @router.post("/regulators/{regulator_id}/toggle")
    def toggle(regulator_id: str, x_operator: str = Header("anonymous")):
        session = runtime.get_session()
        reg = session.get(Regulator, regulator_id)
        if reg is None:
            raise HTTPException(404, f"regulator '{regulator_id}' not found")
        reg.active = not reg.active
        reg.updated_at = datetime.now(timezone.utc)
        session.commit()
        _audit(session, x_operator, "regagg.toggle", "regulator", regulator_id,
               f"active={reg.active}")
        return {"regulator_id": regulator_id, "active": reg.active}

    @router.get("/review-queue")
    def review_queue():
        session = runtime.get_session()
        rows = session.scalars(select(DocumentTag).where(
            DocumentTag.tag == "enrichment_pending")).all()
        return {"pending": [{"regulator_id": r.regulator_id, "doc_id": r.doc_id} for r in rows],
                "count": len(rows)}

    @router.get("/integrity")
    def integrity():
        session = runtime.get_session()
        return runtime.reconcile_report(session, runtime.get_storage())

    return router


# ── helpers ─────────────────────────────────────────────────────────────────

def _run_dict(r: Run) -> dict:
    return {
        "run_id": r.run_id, "regulator_id": r.regulator_id,
        "logical_date": r.logical_date.isoformat(), "trigger": r.trigger,
        "status": r.status, "detected": r.detected, "fetched": r.fetched,
        "ingested": r.ingested, "archived": r.archived, "errors": r.errors,
        "operator": r.operator,
        "started_at": r.started_at.isoformat() if r.started_at else None,
        "finished_at": r.finished_at.isoformat() if r.finished_at else None,
    }


def _staleness(session, reg: Regulator) -> dict:
    latest = session.scalars(
        select(Document).where(Document.regulator_id == reg.regulator_id)
        .order_by(Document.ingested_at.desc()).limit(1)).first()
    if latest is None:
        return {"flagged": False, "days_since_last": None}
    ingested = latest.ingested_at
    if ingested.tzinfo is None:  # SQLite/Postgres may return naive UTC
        ingested = ingested.replace(tzinfo=timezone.utc)
    days = (datetime.now(timezone.utc) - ingested).days
    return {"flagged": days > reg.staleness_alert_days, "days_since_last": days}
