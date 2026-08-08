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

import os
from datetime import date, datetime, timezone
from typing import List, Optional

from fastapi import APIRouter, Header, HTTPException, Request, Response, UploadFile
from fastapi import File as FileField, Form as FormField
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlalchemy import func, select

from sajha.regagg import queries, runtime
from sajha.regagg.models import Document, DocumentTag, Regulator, Run


class SignupRequest(BaseModel):
    email: str
    password: str
    display_name: Optional[str] = None


class LoginRequest(BaseModel):
    email: str
    password: str


class PersonaRequest(BaseModel):
    name: str
    lane: str = "news"
    config: Optional[dict] = None
    entities_raw: Optional[str] = None      # pasted CSV / one name per line
    entity_kind: str = "obligor"
    persona_id: Optional[str] = None
    shared_with: Optional[List[str]] = None


class AskRequest(BaseModel):
    question: str
    context_kind: str = "day"          # day | cluster | document
    context_mode: str = "active"       # active reads the current page first
    page: Optional[dict] = None        # what the person is looking at
    mode: str = "agent"                # agent (corpus tools) | pinned (one artifact)
    persona_id: Optional[str] = None
    day: Optional[str] = None
    cluster_key: Optional[str] = None
    regulator_id: Optional[str] = None
    doc_id: Optional[str] = None


class ManualDocRequest(BaseModel):
    regulator_id: str
    url: str                            # source URL (provenance anchor, required)
    title: Optional[str] = None
    doc_type: Optional[str] = None
    reference_number: Optional[str] = None
    markdown: Optional[str] = None      # operator-supplied md; omitted -> fetch url
    published_date: Optional[str] = None


class RerunRequest(BaseModel):
    scope: str = "all"                 # 'all' | 'ids'
    date: Optional[str] = None         # logical date (defaults to today)
    ids: Optional[List[str]] = None
    max_docs: Optional[int] = None     # per-regulator cap for this run
    include: Optional[str] = None      # comma-separated URL regex (gap-fill scope)


class SweepRequest(BaseModel):
    """A billed run, so every knob that affects the bill is explicit."""
    persona_id: Optional[str] = None
    day: Optional[str] = None
    budget: int = 600                  # hard ceiling on searches for this sweep
    depth: str = "basic"               # advanced costs roughly double
    days: int = 7
    refresh: bool = False              # re-search names already cached today
    classify: bool = True


class FocusRequest(BaseModel):
    """A lens over today's page. Entities and sources filter; prompt narrates."""
    persona_id: Optional[str] = None
    day: Optional[str] = None
    prompt: Optional[str] = None
    entities: Optional[List[str]] = None
    sources: Optional[List[str]] = None


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

    # ── identity ────────────────────────────────────────────────────────────
    # Native signup/login for the on-prem product. The session is an
    # HMAC-signed httpOnly cookie; nothing sensitive is readable by JS.

    def _current_user(request: Request):
        from sajha.regagg import auth as _auth
        uid = _auth.read_session(request.cookies.get(_auth.SESSION_COOKIE))
        if not uid:
            return None
        from sajha.regagg.models import RegUser
        return runtime.get_session().get(RegUser, uid)

    def _require_user(request: Request):
        user = _current_user(request)
        if user is None:
            raise HTTPException(401, "Sign in to continue.")
        return user

    def _set_session(response: Response, user_id: str) -> None:
        from sajha.regagg import auth as _auth
        response.set_cookie(
            _auth.SESSION_COOKIE, _auth.issue_session(user_id),
            max_age=_auth.SESSION_TTL_SECONDS, httponly=True, samesite="lax",
            secure=bool(os.getenv("REGAGG_COOKIE_SECURE")))

    @router.post("/auth/signup")
    def signup(req: SignupRequest, response: Response):
        from sajha.regagg import auth as _auth
        session = runtime.get_session()
        # first account on a fresh install is the admin
        from sajha.regagg.models import RegUser as _U
        first = (session.scalar(select(func.count()).select_from(_U)) or 0) == 0
        user, err = _auth.create_user(session, req.email, req.password,
                                      req.display_name or "",
                                      role="admin" if first else "analyst")
        if err:
            return {"ok": False, "error": err}
        _set_session(response, user.user_id)
        _audit(session, user.user_id, "regagg.signup", "user", user.user_id, "")
        return {"ok": True, "user": _auth.user_public(user), "first_user": first}

    @router.post("/auth/login")
    def login(req: LoginRequest, response: Response):
        from sajha.regagg import auth as _auth
        session = runtime.get_session()
        user, err = _auth.authenticate(session, req.email, req.password)
        if err:
            return {"ok": False, "error": err}
        _set_session(response, user.user_id)
        return {"ok": True, "user": _auth.user_public(user)}

    @router.post("/auth/logout")
    def logout(response: Response):
        from sajha.regagg import auth as _auth
        response.delete_cookie(_auth.SESSION_COOKIE)
        return {"ok": True}

    @router.get("/auth/me")
    def me(request: Request):
        from sajha.regagg import auth as _auth
        user = _current_user(request)
        if user is None:
            return {"user": None}
        return {"user": _auth.user_public(user)}

    # ── my day (the generated page) ─────────────────────────────────────────

    @router.get("/myday")
    def myday(request: Request, persona_id: Optional[str] = None,
              day: Optional[str] = None, refresh: bool = False):
        """The persona's page for a day. Cached per persona per day: everyone
        who opens it sees the same page, and it is not rewritten under them."""
        from sajha.regagg import myday as _m, personas as _p
        user = _require_user(request)
        session = runtime.get_session()
        if persona_id:
            p, err = _p.get_persona(session, persona_id, user.user_id)
            if err:
                raise HTTPException(404, err)
        else:
            mine = _p.list_personas(session, user.user_id)
            if not mine:
                return {"persona": None,
                        "message": "Create a persona to get your daily page."}
            p, _ = _p.get_persona(session, mine[0]["persona_id"], user.user_id)
        out = _m.build_my_day(session, p, day=day, force=refresh)
        out["persona"] = _p.persona_dict(session, p)
        return out

    @router.post("/ask")
    def ask(req: AskRequest, request: Request):
        """Answer a question.

        Two modes, because two different questions get asked. With an artifact
        pinned, answer from THAT and nothing else. Otherwise run the digital
        worker over the corpus toolset and let it find its own way there.
        """
        from sajha.regagg import ask as _ask, personas as _p
        user = _require_user(request)
        session = runtime.get_session()

        if req.mode == "agent" and req.context_kind not in ("cluster", "document"):
            from sajha.regagg import agent as _agent
            out = _agent.answer(req.question, page=req.page,
                                context_mode=req.context_mode)
            out["context"] = {"kind": "corpus",
                              "title": (req.page or {}).get("label") or "the corpus"}
            out["sources"] = [{"n": i + 1, "title": d, "publisher": "",
                               "doc_id": d, "regulator_id": ""}
                              for i, d in enumerate((out.get("documents") or [])[:12])]
            return out

        persona = None
        if req.context_kind in ("day", "cluster"):
            pid = req.persona_id
            if not pid:
                mine = _p.list_personas(session, user.user_id)
                pid = mine[0]["persona_id"] if mine else None
            if not pid:
                raise HTTPException(400, "Create a persona first.")
            persona, err = _p.get_persona(session, pid, user.user_id)
            if err:
                raise HTTPException(404, err)

        if req.context_kind == "cluster":
            if not req.cluster_key:
                raise HTTPException(400, "cluster_key is required.")
            pack = _ask.pack_for_cluster(session, persona, req.day, req.cluster_key)
            if pack is None:
                raise HTTPException(404, "That item is not on the page for that day.")
        elif req.context_kind == "document":
            if not (req.regulator_id and req.doc_id):
                raise HTTPException(400, "regulator_id and doc_id are required.")
            pack = _ask.pack_for_document(session, runtime.get_storage(),
                                          req.regulator_id, req.doc_id)
            if pack is None:
                raise HTTPException(404, "Document not found.")
        else:
            pack = _ask.pack_for_day(session, persona, req.day)

        out = _ask.answer_question(req.question, pack)
        out["context"] = {"kind": pack["kind"], "title": pack["title"]}
        return out

    @router.get("/corpus/doc/{doc_id}")
    def corpus_doc(doc_id: str, request: Request):
        """Resolve a doc_id the assistant cited to something the UI can open."""
        _require_user(request)
        from sqlalchemy import select as _select
        session = runtime.get_session()
        doc = session.scalars(
            _select(Document).where(Document.doc_id == doc_id)).first()
        if doc is None:
            raise HTTPException(404, "No such document.")
        return {"doc_id": doc.doc_id, "regulator_id": doc.regulator_id,
                "title": doc.title, "source_url": doc.source_url}

    @router.get("/desks")
    def desks(request: Request, day: Optional[str] = None, days: int = 30):
        """Every persona you can see, side by side — the desk dashboard.

        A head of risk does not want nine pages; they want to know which desks
        have something today and which are quiet, then open the one that does.
        """
        from sajha.regagg import myday as _m, personas as _p
        from sajha.regagg.models import PageSpec as _PS
        user = _require_user(request)
        session = runtime.get_session()
        out, totals = [], {"serious": 0, "watch": 0, "quiet_desks": 0}
        for meta in _p.list_personas(session, user.user_id):
            p, err = _p.get_persona(session, meta["persona_id"], user.user_id)
            if err:
                continue
            page = _m.build_my_day(session, p, day=day)
            led = page.get("ledger") or {}
            items = (page.get("dossier") or {}).get("items", [])
            top = items[0] if items else None
            out.append({
                "persona_id": p.persona_id, "name": p.name, "lane": p.lane,
                "layout": (page.get("spec") or {}).get("layout"),
                "day": (page.get("spec") or {}).get("day"),
                "generator": page.get("generator"),
                "watchlist": led.get("watchlist_size", 0),
                "serious": led.get("serious", 0), "watch": led.get("watch", 0),
                "quiet": led.get("quiet_entities", 0),
                "scanned": led.get("scanned_documents", 0),
                "matched": led.get("matched", 0),
                "lede": next((s.get("text") for s in
                              (page.get("spec") or {}).get("sections", [])
                              if s.get("component") == "lede"), ""),
                "top": ({"title": top["title"], "event_type": top["event_type"],
                         "entities": top["entities"], "why": top["why"],
                         "corroboration": top["corroboration"],
                         "cluster_key": top["cluster_key"]} if top else None),
            })
            totals["serious"] += led.get("serious", 0)
            totals["watch"] += led.get("watch", 0)
            if not led.get("serious") and not led.get("watch"):
                totals["quiet_desks"] += 1
        out.sort(key=lambda d: (-d["serious"], -d["watch"], d["name"]))

        # the window the desks are drawn from — stated, never implied
        from sajha.regagg.models import Document as _D, Regulator as _R
        news_ids = [r.regulator_id for r in session.scalars(select(_R)).all()
                    if getattr(r, "category", "regulatory") == "news"]
        day_col = func.coalesce(_D.published_date, func.date(_D.ingested_at))
        rows = session.execute(
            select(day_col, func.count()).where(_D.regulator_id.in_(news_ids or [""]))
            .group_by(day_col).order_by(day_col.desc()).limit(days)).all()
        window = [{"day": str(d), "count": c} for d, c in reversed(rows) if d]
        return {"desks": out, "totals": totals, "window": window,
                "window_days": len(window), "requested_days": days}

    @router.get("/myday/item/{cluster_key}")
    def myday_item(cluster_key: str, request: Request,
                   persona_id: Optional[str] = None, day: Optional[str] = None):
        """The evidence behind one card — every document it was built from."""
        from sajha.regagg import myday as _m, personas as _p
        user = _require_user(request)
        session = runtime.get_session()
        mine = _p.list_personas(session, user.user_id)
        pid = persona_id or (mine[0]["persona_id"] if mine else None)
        if not pid:
            raise HTTPException(404, "No persona.")
        p, err = _p.get_persona(session, pid, user.user_id)
        if err:
            raise HTTPException(404, err)
        data = _m.build_my_day(session, p, day=day)
        for item in (data["dossier"]["items"]
                     + data["dossier"].get("suppressed", [])):
            if item["cluster_key"] == cluster_key:
                return item
        raise HTTPException(404, "Item not on that day's page.")

    # ── personas ────────────────────────────────────────────────────────────

    @router.get("/personas/starters")
    def persona_starters():
        """Starter shapes for a new user — the alternative is a blank form."""
        from sajha.regagg import personas as _p
        return {"starters": _p.STARTERS}

    @router.get("/personas")
    def personas_list(request: Request, lane: Optional[str] = None):
        from sajha.regagg import personas as _p
        user = _require_user(request)
        return {"personas": _p.list_personas(runtime.get_session(), user.user_id, lane)}

    @router.get("/personas/{persona_id}")
    def persona_get(persona_id: str, request: Request):
        from sajha.regagg import personas as _p
        user = _require_user(request)
        session = runtime.get_session()
        p, err = _p.get_persona(session, persona_id, user.user_id)
        if err:
            raise HTTPException(404, err)
        out = _p.persona_dict(session, p)
        out["entities_preview"] = _p.entity_names(session, persona_id)[:50]
        out["can_edit"] = p.owner_id == user.user_id
        return out

    @router.post("/personas")
    def persona_save(req: PersonaRequest, request: Request):
        from sajha.regagg import personas as _p
        user = _require_user(request)
        session = runtime.get_session()
        if req.persona_id:
            existing, err = _p.get_persona(session, req.persona_id, user.user_id)
            if err:
                raise HTTPException(404, err)
            if existing.owner_id != user.user_id:
                raise HTTPException(403, "Shared personas are view-only.")
        entities = (_p.parse_entities(req.entities_raw, req.entity_kind)
                    if req.entities_raw is not None else None)
        try:
            p = _p.save_persona(session, owner_id=user.user_id, name=req.name,
                                lane=req.lane, config=req.config, entities=entities,
                                persona_id=req.persona_id, shared_with=req.shared_with)
        except ValueError as e:
            raise HTTPException(400, str(e))
        _audit(session, user.user_id, "regagg.persona_save", "persona", p.persona_id,
               f"v{p.version_n}")
        return _p.persona_dict(session, p)

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
        result = trigger(scope=req.scope, logical_date=logical_date, ids=ids,
                         operator=x_operator, max_docs=req.max_docs, include=req.include)
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

    @router.get("/whats-new")
    def whats_new(days: int = 7):
        session = runtime.get_session()
        return queries.reg_whats_new(session, days=days)

    # ── v2 UI data endpoints ────────────────────────────────────────────────

    @router.get("/overview")
    def overview(days: int = 1, priority_days: int = 7):
        from sajha.regagg import queries_ui
        return queries_ui.overview(runtime.get_session(), days=days,
                                   priority_days=priority_days)

    @router.get("/tree")
    def tree(days: int = 7):
        from sajha.regagg import queries_ui
        return queries_ui.coverage_tree(runtime.get_session(), days=days)

    @router.get("/browse/{regulator_id}")
    def browse(regulator_id: str, kind: Optional[str] = None,
               doc_type: Optional[str] = None, status: Optional[str] = None,
               q: Optional[str] = None, limit: int = 50, offset: int = 0):
        from sajha.regagg import queries_ui
        return queries_ui.browse(runtime.get_session(), regulator_id, kind=kind,
                                 doc_type=doc_type, status=status, q=q,
                                 limit=min(limit, 200), offset=offset)

    @router.get("/corpus")
    def corpus(region: Optional[str] = None, category: Optional[str] = None,
               regulators: Optional[str] = None,
               kind: Optional[str] = None, doc_type: Optional[str] = None,
               status: Optional[str] = None, q: Optional[str] = None,
               band: Optional[str] = None,
               date_from: Optional[str] = None, date_to: Optional[str] = None,
               limit: int = 50, offset: int = 0):
        from sajha.regagg import queries_ui
        return queries_ui.corpus_browse(
            runtime.get_session(), runtime.get_storage(), region=region,
            category=category,
            regulator_ids=regulators.split(",") if regulators else None,
            kind=kind, doc_type=doc_type, status=status, q=q, band=band,
            date_from=date_from, date_to=date_to,
            limit=min(limit, 200), offset=max(offset, 0))

    @router.get("/changes")
    def changes(days: int = 7, region: Optional[str] = None,
                category: Optional[str] = None,
                regulators: Optional[str] = None, source_kind: Optional[str] = None,
                kinds: Optional[str] = None, min_band: Optional[str] = None,
                date_from: Optional[str] = None, date_to: Optional[str] = None):
        from sajha.regagg import queries_ui
        return queries_ui.changes(
            runtime.get_session(), days=days, region=region, category=category,
            regulator_ids=regulators.split(",") if regulators else None,
            source_kind=source_kind,
            kinds=kinds.split(",") if kinds else None, min_band=min_band,
            date_from=date_from, date_to=date_to)

    @router.get("/documents/{regulator_id}/{doc_id}/diff")
    def doc_diff(regulator_id: str, doc_id: str):
        from sajha.regagg import queries_ui
        return queries_ui.version_diff(runtime.get_session(), runtime.get_storage(),
                                       regulator_id, doc_id)

    @router.get("/documents/{regulator_id}/{doc_id}/content")
    def doc_content(regulator_id: str, doc_id: str, mode: str = "summary"):
        return queries.reg_read(runtime.get_session(), runtime.get_storage(),
                                doc_id, mode=mode, regulator_id=regulator_id)

    @router.get("/exec/summary")
    def exec_summary(days: int = 1):
        """Home page payload — every tile/chart on it comes from here."""
        from sajha.regagg import queries_ui
        return queries_ui.exec_summary(runtime.get_session(), days=days)

    @router.get("/exec/regulatory")
    def exec_regulatory():
        from sajha.regagg import queries_ui
        return queries_ui.exec_regulatory(runtime.get_session())

    @router.get("/exec/news")
    def exec_news():
        from sajha.regagg import queries_ui
        return queries_ui.exec_news(runtime.get_session(),
                                    storage=runtime.get_storage())

    @router.get("/news")
    def news(day: Optional[str] = None):
        """Financial-news dashboard: one day ranked for a credit analyst."""
        from sajha.regagg import queries_ui
        return queries_ui.news_dashboard(runtime.get_session(),
                                         storage=runtime.get_storage(), day=day)

    @router.get("/runs-trend")
    def runs_trend(days: int = 14, category: Optional[str] = None):
        """Day-over-day detected/fetched/ingested, plus who produced it."""
        from sajha.regagg import queries_ui
        return queries_ui.runs_trend(runtime.get_session(), days=days,
                                     category=category)

    @router.get("/runs-overview")   # NB: not /runs/{run_id} — avoids path capture
    def runs_over():
        from sajha.regagg import queries_ui
        return queries_ui.runs_overview(runtime.get_session())

    @router.post("/myday/focus")
    def myday_focus(req: FocusRequest, request: Request):
        """An ephemeral focused view. Never writes, never replaces the day's page.

        POST because it carries a free-text prompt, not because it changes
        anything — nothing here touches the cached PageSpec.
        """
        from sajha.regagg import focus as _f, myday as _m, personas as _p
        user = _require_user(request)
        session = runtime.get_session()
        if req.persona_id:
            p, err = _p.get_persona(session, req.persona_id, user.user_id)
            if err:
                raise HTTPException(404, err)
        else:
            mine = _p.list_personas(session, user.user_id)
            if not mine:
                raise HTTPException(404, "no persona")
            p = mine[0]
        page = _m.build_my_day(session, p, day=req.day)
        return _f.focus(page, prompt=req.prompt or "",
                        entities=req.entities, sources=req.sources)

    def _persona_or_404(session, user, persona_id):
        from sajha.regagg import personas as _p
        if persona_id:
            p, err = _p.get_persona(session, persona_id, user.user_id)
            if err:
                raise HTTPException(404, err)
            return p
        mine = _p.list_personas(session, user.user_id)
        if not mine:
            raise HTTPException(404, "no persona")
        return mine[0]

    @router.get("/entities/table")
    def entities_table(request: Request, persona_id: Optional[str] = None,
                       day: Optional[str] = None, status: Optional[str] = None,
                       q: str = "", summary: bool = False):
        """One row per watched entity. Reads cache only — never spends."""
        from sajha.regagg import entity_table as _et
        user = _require_user(request)
        session = runtime.get_session()
        p = _persona_or_404(session, user, persona_id)
        data = _et.table(session, p, day=day, status=status, q=q)
        data["persona"] = {"persona_id": p.persona_id, "name": p.name}
        if summary:
            data["headline"] = _et.summarise(data["rows"], total=data["total"])
        return data

    @router.post("/entities/sweep")
    def entities_sweep(req: SweepRequest, request: Request,
                       x_operator: str = Header("anonymous")):
        """Run the searches. Explicitly triggered because it costs money.

        Never called on page load: the table endpoint reads cache, this one
        spends. A sweep fills only the gaps unless refresh is asked for.
        """
        from sajha.regagg import entity_table as _et
        user = _require_user(request)
        session = runtime.get_session()
        p = _persona_or_404(session, user, req.persona_id)
        _audit(session, x_operator, "regagg.entity_sweep", "persona",
               p.persona_id, f"budget={req.budget} depth={req.depth}")
        out = _et.sweep(session, p, day=req.day,
                        budget=max(1, min(int(req.budget or 600), 2000)),
                        depth=req.depth or "basic", days=int(req.days or 7),
                        refresh=bool(req.refresh))
        # Classify whatever rows exist. Gating this on a live API key meant the
        # judged columns stayed empty in demo mode, hiding half the feature.
        if req.classify and out.get("entities"):
            out["classification"] = _et.classify(session, p, day=out["day"])
        return out

    @router.get("/collection/overview")
    def collection_overview(lane: Optional[str] = None, days: int = 7,
                            trend_days: int = 30):
        """Everything the Collection page shows, on one clock.

        Assembled server-side rather than as five fetches, because the panels
        make claims about the same instant — a today bar that says "not
        scheduled" beside a matrix that already rolled to tomorrow would be
        worse than either alone.
        """
        from sajha.regagg import collection
        return collection.overview(runtime.get_session(), lane=lane,
                                   days=max(1, min(days, 31)),
                                   trend_days=max(7, min(trend_days, 120)))

    @router.get("/health/overview")
    def health_overview():
        from sajha.regagg import health
        return health.overview(runtime.get_session())

    @router.get("/schedule")
    def schedule_declared():
        """The declared schedule. Read-only: editing it is a config change, so
        it goes through review like the rest of the collection contract."""
        from sajha.regagg import schedule as _s
        return _s.get_schedule().describe()

    @router.get("/inventory/{regulator_id}")
    def inventory(regulator_id: str):
        from sajha.regagg import queries_ui
        return queries_ui.inventory(runtime.get_session(), regulator_id)

    @router.post("/documents")
    def add_document_manual(req: ManualDocRequest, x_operator: str = Header("anonymous")):
        """Human interjection: add/update a document by URL, pasted markdown, or
        both. Same versioning/provenance path as automated ingestion."""
        session = runtime.get_session()
        from sajha.regagg import manual
        try:
            result = manual.add_document(
                session, runtime.get_storage(),
                regulator_id=req.regulator_id, url=req.url, operator=x_operator,
                title=req.title, doc_type=req.doc_type or "guidance",
                reference_number=req.reference_number, markdown=req.markdown,
                published_date=req.published_date)
        except Exception as e:  # noqa: BLE001
            raise HTTPException(400, f"manual ingest failed: {e}")
        _audit(session, x_operator, "regagg.manual_add", "document",
               f"{req.regulator_id}/{result['doc_id']}", req.url)
        return result

    @router.get("/integrity")
    def integrity():
        session = runtime.get_session()
        return runtime.reconcile_report(session, runtime.get_storage())

    @router.post("/documents/upload")
    async def upload_document(
        regulator_id: str = FormField(...), url: str = FormField(...),
        title: Optional[str] = FormField(None), doc_type: str = FormField("guidance"),
        reference_number: Optional[str] = FormField(None),
        published_date: Optional[str] = FormField(None),
        file: UploadFile = FileField(...),
        x_operator: str = Header("anonymous"),
    ):
        """Manual UPLOAD lane: operator supplies the artifact itself (PDF/HTML)
        for a given source URL. Same versioning/provenance path as everything."""
        data = await file.read()
        if len(data) > 50_000_000:
            raise HTTPException(413, "file too large (50MB cap)")
        session = runtime.get_session()
        from sajha.regagg import manual
        try:
            result = manual.add_document(
                session, runtime.get_storage(),
                regulator_id=regulator_id, url=url, operator=x_operator,
                title=title, doc_type=doc_type, reference_number=reference_number,
                published_date=published_date, file_bytes=data)
        except Exception as e:  # noqa: BLE001
            raise HTTPException(400, f"upload ingest failed: {e}")
        _audit(session, x_operator, "regagg.manual_upload", "document",
               f"{regulator_id}/{result['doc_id']}", f"{url} ({file.filename})")
        return result

    # ── corpus file explorer (read-only, jailed to the corpus root) ─────────

    def _fs_resolve(path: str):
        from pathlib import Path
        base = Path("data/web_aggregator").resolve()
        target = (base / path.lstrip("/")).resolve()
        if base != target and base not in target.parents:
            raise HTTPException(400, "path escapes corpus root")
        if not target.exists():
            raise HTTPException(404, f"not found: {path}")
        return base, target

    @router.get("/fs")
    def fs_list(path: str = ""):
        """List one level of the corpus tree (regulator/current/doc_type/…)."""
        base, target = _fs_resolve(path)
        if not target.is_dir():
            raise HTTPException(400, "not a directory")
        entries = []
        for child in sorted(target.iterdir(),
                            key=lambda p: (not p.is_dir(), p.name.lower())):
            if child.name.startswith("."):
                continue
            entries.append({
                "name": child.name,
                "dir": child.is_dir(),
                "size": child.stat().st_size if child.is_file() else None,
                "children": sum(1 for _ in child.iterdir()) if child.is_dir() else None,
            })
        return {"path": str(target.relative_to(base)) if target != base else "",
                "entries": entries}

    @router.get("/fs/file")
    def fs_file(path: str, download: bool = False):
        """Return a corpus file: text types inline (md/json/txt), binaries as
        a download (raw.pdf / raw.html originals)."""
        from fastapi.responses import FileResponse
        _, target = _fs_resolve(path)
        if not target.is_file():
            raise HTTPException(400, "not a file")
        if target.stat().st_size > 20_000_000:
            raise HTTPException(413, "file too large")
        if not download and target.suffix in (".md", ".json", ".txt"):
            return {"name": target.name, "size": target.stat().st_size,
                    "text": target.read_text(encoding="utf-8", errors="replace")[:500_000]}
        media = {".pdf": "application/pdf", ".html": "text/html"}.get(
            target.suffix, "application/octet-stream")
        return FileResponse(str(target), media_type=media, filename=target.name)

    @router.get("/ui", response_class=HTMLResponse)
    def ui():
        """v2 operator/analyst dashboard (file-based so it's editable without
        touching Python). Falls back to the embedded v1 page if missing."""
        from pathlib import Path
        f = Path(__file__).parent / "ui_dashboard.html"
        if f.exists():
            return f.read_text(encoding="utf-8")
        return DASHBOARD_HTML

    return router


# ── operator dashboard (05_ADMIN_UX_SPEC, served at /api/regagg/ui) ──────────

DASHBOARD_HTML = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Regulatory Intelligence — Coverage</title>
<style>
  :root{--bg:#f6f7f9;--card:#fff;--ink:#1a2230;--muted:#69707d;--line:#e5e8ee;
        --green:#1e9e63;--yellow:#d9a400;--red:#d1443b;--grey:#c3c8d2;--accent:#2b5bd7}
  @media (prefers-color-scheme:dark){:root{--bg:#0f1218;--card:#171b22;--ink:#e7ebf2;
        --muted:#98a0ad;--line:#262c36;--grey:#3a414d;--accent:#5b83f0}}
  *{box-sizing:border-box}body{margin:0;font:14px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;
        background:var(--bg);color:var(--ink)}
  header{padding:16px 22px;border-bottom:1px solid var(--line);display:flex;
        align-items:center;gap:16px;flex-wrap:wrap;background:var(--card)}
  h1{font-size:16px;margin:0;font-weight:650}
  .sub{color:var(--muted);font-size:12px}
  .spacer{flex:1}
  select,button{font:inherit;color:var(--ink);background:var(--card);
        border:1px solid var(--line);border-radius:8px;padding:6px 10px;cursor:pointer}
  .wrap{padding:18px 22px;max-width:1200px;margin:0 auto}
  .tiles{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:18px}
  .tile{background:var(--card);border:1px solid var(--line);border-radius:12px;
        padding:12px 16px;min-width:130px}
  .tile b{font-size:22px;font-weight:680;display:block}
  .tile span{color:var(--muted);font-size:12px}
  .card{background:var(--card);border:1px solid var(--line);border-radius:12px;
        padding:14px 16px;margin-bottom:18px;overflow-x:auto}
  .card h2{font-size:13px;margin:0 0 12px;color:var(--muted);text-transform:uppercase;
        letter-spacing:.04em}
  table{border-collapse:collapse;width:100%}
  th,td{padding:6px 8px;text-align:center;font-size:12px;white-space:nowrap}
  th.reg,td.reg{text-align:left;position:sticky;left:0;background:var(--card);
        font-weight:600;cursor:pointer}
  td.reg:hover{color:var(--accent)}
  .cell{width:26px;height:26px;border-radius:6px;display:inline-flex;align-items:center;
        justify-content:center;color:#fff;font-size:11px;font-weight:600}
  .g{background:var(--green)}.y{background:var(--yellow)}.r{background:var(--red)}
  .x{background:var(--grey);opacity:.5}
  .legend{display:flex;gap:14px;color:var(--muted);font-size:12px;margin-top:10px;flex-wrap:wrap}
  .legend i{width:12px;height:12px;border-radius:3px;display:inline-block;vertical-align:-1px;margin-right:5px}
  .jchip{font-size:10px;color:var(--muted);border:1px solid var(--line);border-radius:5px;
        padding:1px 5px;margin-left:6px}
  .doc{padding:8px 0;border-bottom:1px solid var(--line)}
  .doc a{color:var(--accent);text-decoration:none;font-weight:550}
  .doc .meta{color:var(--muted);font-size:12px}
  .pill{font-size:11px;border:1px solid var(--line);border-radius:20px;padding:1px 8px;color:var(--muted)}
  .ok{color:var(--green)}.bad{color:var(--red)}
</style></head>
<body>
<header>
  <div><h1>Regulatory Intelligence Aggregator</h1>
    <div class="sub">Operator coverage dashboard · <span id="dbtype">demo corpus</span></div></div>
  <div class="spacer"></div>
  <label class="sub">Window
    <select id="days"><option>7</option><option>14</option><option>30</option></select></label>
  <span id="integrity" class="pill">integrity …</span>
  <button onclick="load()">↻ Refresh</button>
</header>
<div class="wrap">
  <div class="tiles" id="tiles"></div>
  <div class="card"><h2>Coverage matrix (regulators × days)</h2>
    <div id="matrix">loading…</div>
    <div class="legend">
      <span><i class="g"></i>success · new docs</span>
      <span><i class="y"></i>success · 0 new</span>
      <span><i class="r"></i>failed</span>
      <span><i class="x"></i>not scheduled</span>
      <span class="sub">click a regulator to drill down</span></div></div>
  <div class="card" id="drill" style="display:none"></div>
  <div class="card"><h2>What's new (last 7 days)</h2><div id="new">loading…</div></div>
</div>
<script>
const API="/api/regagg";
async function j(u){const r=await fetch(API+u);return r.json();}
function cell(c){if(!c)return '<span class="cell x">·</span>';
  const k=c.status==="success"?"g":c.status==="success_empty"?"y":c.status==="failed"?"r":"x";
  const n=c.status==="failed"?("!"+(c.errors||0)):(c.new||0);
  return `<span class="cell ${k}" title="${c.status}">${n}</span>`;}
async function load(){
  const days=+document.getElementById("days").value;
  const cov=await j(`/coverage?days=${days}`);
  const regs=Object.keys(cov.matrix).sort();
  let head=`<table><tr><th class="reg">Regulator</th>`+
    cov.days.map(d=>`<th>${d.slice(5)}</th>`).join("")+`</tr>`;
  let totNew=0,fail=0,succ=0;
  for(const r of regs){
    head+=`<tr><td class="reg" onclick="drill('${r}')">${r}</td>`;
    for(const d of cov.days){const c=cov.matrix[r][d];
      if(c){if(c.status==="failed")fail++;else succ++;totNew+=c.new||0;}
      head+=`<td>${cell(c)}</td>`;}
    head+=`</tr>`;}
  head+=`</table>`;
  document.getElementById("matrix").innerHTML = regs.length?head:"<span class='sub'>no runs yet — trigger ingestion</span>";
  // tiles
  const rq=await j(`/review-queue`);
  document.getElementById("tiles").innerHTML=
    tile(regs.length,"regulators with runs")+tile(totNew,"new docs in window")+
    tile(succ,"successful cells")+tile(fail,"failed cells",fail?"bad":"")+
    tile(rq.count,"in review queue",rq.count?"bad":"ok");
  // integrity
  const ig=await j(`/integrity`);
  const el=document.getElementById("integrity");
  el.textContent=ig.ok?"✓ integrity clean":"✗ "+(ig.invariant_violations||[]).length+" violations";
  el.className="pill "+(ig.ok?"ok":"bad");
  // whats new
  const wn=await j(`/whats-new?days=7`);
  let h="";for(const [reg,docs] of Object.entries(wn.by_regulator||{})){
    for(const d of docs){h+=`<div class="doc"><a href="${'#'}">${d.title}</a>
      <span class="pill">${d.doc_type}</span>
      <div class="meta">${reg} · ${d.published_date||"no date"}</div></div>`;}}
  document.getElementById("new").innerHTML=h||"<span class='sub'>nothing in the last 7 days</span>";
}
function tile(n,l,cls=""){return `<div class="tile"><b class="${cls}">${n}</b><span>${l}</span></div>`;}
async function drill(id){
  const d=await j(`/regulators/${id}`);const el=document.getElementById("drill");
  el.style.display="block";
  let docs=(d.latest_documents||[]).map(x=>`<div class="doc">
    <a href="${x.source_url}" target="_blank" rel="noopener">${x.title}</a>
    <span class="pill">${x.doc_type}</span> ${x.version_n>1?`<span class="pill">v${x.version_n}</span>`:""}
    <div class="meta">${x.published_date||"no date"} · ${x.doc_id}</div></div>`).join("");
  const st=d.staleness||{};
  el.innerHTML=`<h2>${d.name} <span class="jchip">${d.jurisdiction}</span>
    <span class="jchip">${d.connector}</span>
    <span class="jchip">${d.active?"active":"inactive"}</span>
    ${st.flagged?`<span class="pill bad">stale ${st.days_since_last}d</span>`:""}</h2>
    ${docs||"<span class='sub'>no documents yet</span>"}`;
  el.scrollIntoView({behavior:"smooth",block:"nearest"});
}
document.getElementById("days").onchange=load;
load();
</script></body></html>"""


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
