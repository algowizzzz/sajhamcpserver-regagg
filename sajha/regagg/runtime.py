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
    """Return the rerun enqueuer. Default records intent only — production wires
    this to the Prefect sidecar (flows_prefect) which actually runs the flow."""
    if _rerun_trigger is not None:
        return _rerun_trigger

    def _default(scope, logical_date, ids, operator):
        return {"enqueued": ids or "all", "note": "recorded; wire Prefect to execute"}
    return _default


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


def wire_from_app() -> None:  # pragma: no cover - exercised in the running server
    """Wire providers to the live SAJHA app (call once at startup)."""
    from sajha.db.engine import get_db_session
    from sajha.core.storage import get_storage as _s
    from sajha.regagg.config_loader import load_all
    set_providers(session=get_db_session,
                  storage=lambda: CorpusStorage(_s()),
                  configs=load_all)
