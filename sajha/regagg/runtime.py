"""
Runtime context providers — how the regagg feature obtains a DB session,
storage, and loaded configs at request time.

Kept behind overridable providers so:
  * the running SAJHA app wires real ones at startup (``wire_from_app``), and
  * tests inject a SQLite session + local storage (``set_providers``).

MCP tools and the admin API call ``get_session`` / ``get_storage`` / ``get_configs``
per request; they never hold state between calls (invariant #2).
"""

from __future__ import annotations

import contextvars
import threading

from typing import Callable, Dict, Optional

from sajha.regagg.config_models import RegulatorConfig
from sajha.regagg.corpus_storage import CorpusStorage

_session_provider: Optional[Callable] = None
_storage_provider: Optional[Callable[[], CorpusStorage]] = None
_configs_provider: Optional[Callable[[], Dict[str, RegulatorConfig]]] = None
_taxonomy: Optional[dict] = None
_rerun_trigger: Optional[Callable] = None


def set_providers(session=None, storage=None, configs=None, taxonomy=None,
                  rerun_trigger=None) -> None:
    global _session_provider, _storage_provider, _configs_provider, _taxonomy, _rerun_trigger
    if session is not None:
        _session_provider = session
    if storage is not None:
        _storage_provider = storage
    if configs is not None:
        _configs_provider = configs
    if taxonomy is not None:
        _taxonomy = taxonomy
    if rerun_trigger is not None:
        _rerun_trigger = rerun_trigger


def get_rerun_trigger() -> Callable:
    """Return the rerun enqueuer. Default spawns the ingest runner as a detached
    subprocess so UI Run buttons genuinely execute (Saad's external scheduler
    can override via set_providers(rerun_trigger=...))."""
    if _rerun_trigger is not None:
        return _rerun_trigger
    return spawn_ingest


def spawn_ingest(scope="all", logical_date=None, ids=None, operator=None,
                 max_docs=None, include=None, wait=False) -> dict:
    """Launch scripts/regagg_ingest_live.py. One coarse guard: refuse if an
    ingest process is already running (SQLite has a single writer).

    `wait=True` blocks until the batch finishes and reports its exit code —
    that is how `runqueue` knows when to read the outcomes back and move on to
    the next batch. Callers that just want it started leave it False.
    """
    import subprocess, sys
    from pathlib import Path
    repo = Path(__file__).resolve().parents[2]
    script = repo / "scripts" / "regagg_ingest_live.py"

    # refuse a second concurrent fleet — check for an existing runner
    probe = subprocess.run(["pgrep", "-f", "regagg_ingest_live"],
                           capture_output=True, text=True)
    if probe.stdout.strip():
        return {"started": False, "reason": "an ingest run is already active",
                "active_pids": probe.stdout.split()}

    cmd = [sys.executable, str(script), "--rps", "3", "--timeout", "10",
           "--operator", operator or "ui"]
    if scope == "ids" and ids:
        cmd += ["--only", ",".join(ids)]
    if max_docs:
        cmd += ["--max-docs", str(max_docs)]
    if include:
        cmd += ["--include", include]
    log = repo / "logs" / "regagg_ui_run.log"
    log.parent.mkdir(exist_ok=True)
    with open(log, "ab") as fh:
        proc = subprocess.Popen(cmd, stdout=fh, stderr=fh,
                                start_new_session=True, cwd=str(repo))
    out = {"started": True, "pid": proc.pid, "scope": scope, "ids": ids,
           "log": str(log)}
    if wait:
        out["returncode"] = proc.wait()
    return out


def reconcile_report(session, storage) -> dict:
    from sajha.regagg import orchestrator
    return orchestrator.reconcile(session, storage)


def get_session():
    if _session_provider is None:
        raise RuntimeError("regagg runtime not wired: call runtime.set_providers(...) "
                           "or runtime.wire_from_app() at startup")
    return _session_provider()


def get_storage() -> CorpusStorage:
    if _storage_provider is not None:
        return _storage_provider()
    from sajha.core.storage import get_storage as _s
    return CorpusStorage(_s())


def get_configs() -> Dict[str, RegulatorConfig]:
    if _configs_provider is not None:
        return _configs_provider()
    from sajha.regagg.config_loader import load_all
    return load_all()


def get_taxonomy() -> dict:
    global _taxonomy
    if _taxonomy is None:
        from sajha.regagg.enrichment import load_taxonomy
        _taxonomy = load_taxonomy("config/regulators/_taxonomy.yaml")
    return _taxonomy


_SESSION_REGISTRY = None

# Sessions are scoped to the REQUEST, not the thread. Thread-scoping pinned one
# pooled connection per worker thread forever; FastAPI's threadpool is far
# larger than the QueuePool (5+10), so a busy server exhausted it and every
# later request blocked for 30s (found by the Playwright suite).
#
# A ContextVar is the right key because Starlette copies the request's context
# into the threadpool when it runs a sync endpoint — so the middleware and the
# handler agree on the scope, and remove() frees the connection the handler
# actually used. Falls back to the thread id outside a request (CLI, jobs).
_REQUEST_SCOPE: "contextvars.ContextVar[object]" = contextvars.ContextVar(
    "regagg_session_scope", default=None)


def _scope_key():
    return _REQUEST_SCOPE.get() or threading.get_ident()


def begin_request_scope() -> None:
    """Give this request its own session scope (call at request start)."""
    _REQUEST_SCOPE.set(object())


def release_session() -> None:
    """Return this request's session and its connection to the pool."""
    if _SESSION_REGISTRY is not None:
        try:
            _SESSION_REGISTRY.remove()
        except Exception:  # noqa: BLE001 — never fail a response on cleanup
            pass


def wire_from_app() -> None:  # pragma: no cover - exercised in the running server
    """Wire providers to the live SAJHA app (call once at startup).

    Sessions are THREAD-SCOPED (scoped_session): each request-handler thread
    reuses one session instead of leaking a new pooled connection per API call
    — a fresh session per call exhausted the QueuePool (5+10) within minutes
    under the dashboard's 5s polling."""
    from sqlalchemy.orm import scoped_session, sessionmaker
    from sajha.db.engine import get_engine
    from sajha.core.storage import get_storage as _s
    from sajha.regagg.config_loader import load_all
    SessionLocal = scoped_session(
        sessionmaker(bind=get_engine(), expire_on_commit=False, autoflush=False),
        scopefunc=_scope_key)
    global _SESSION_REGISTRY
    _SESSION_REGISTRY = SessionLocal
    set_providers(session=SessionLocal,
                  storage=lambda: CorpusStorage(_s()),
                  configs=load_all)
