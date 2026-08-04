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

from fastapi import APIRouter, Header, HTTPException, UploadFile
from fastapi import File as FileField, Form as FormField
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlalchemy import select

from sajha.regagg import queries, runtime
from sajha.regagg.models import Document, DocumentTag, Regulator, Run


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
    def corpus(region: Optional[str] = None, regulators: Optional[str] = None,
               kind: Optional[str] = None, doc_type: Optional[str] = None,
               status: Optional[str] = None, q: Optional[str] = None,
               date_from: Optional[str] = None, date_to: Optional[str] = None,
               limit: int = 50, offset: int = 0):
        from sajha.regagg import queries_ui
        return queries_ui.corpus_browse(
            runtime.get_session(), runtime.get_storage(), region=region,
            regulator_ids=regulators.split(",") if regulators else None,
            kind=kind, doc_type=doc_type, status=status, q=q,
            date_from=date_from, date_to=date_to,
            limit=min(limit, 200), offset=max(offset, 0))

    @router.get("/changes")
    def changes(days: int = 7, region: Optional[str] = None,
                regulators: Optional[str] = None, source_kind: Optional[str] = None,
                kinds: Optional[str] = None, date_from: Optional[str] = None,
                date_to: Optional[str] = None):
        from sajha.regagg import queries_ui
        return queries_ui.changes(
            runtime.get_session(), days=days, region=region,
            regulator_ids=regulators.split(",") if regulators else None,
            source_kind=source_kind,
            kinds=kinds.split(",") if kinds else None,
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

    @router.get("/runs-overview")   # NB: not /runs/{run_id} — avoids path capture
    def runs_over():
        from sajha.regagg import queries_ui
        return queries_ui.runs_overview(runtime.get_session())

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
