"""
Scheduling & orchestration core (FR-4 / US-5.x), scheduler-agnostic.

``run_daily`` fans out one independent run per active regulator; one regulator's
failure never blocks or fails the others. ``rerun`` re-runs all / a subset / one
for a chosen logical date (idempotent — unchanged docs are skipped). ``reconcile``
repairs versioning invariants and reports integrity.

These are plain functions so they're unit-testable with no scheduler. The Prefect
sidecar (flows_prefect.py) is a thin wrapper that calls them; APScheduler or cron
could call them equally.

Network IO is injected via ``opener_for(config) -> source_opener`` and
``fetcher_for(config) -> Fetcher`` so the orchestrator runs offline in tests.
"""

from __future__ import annotations

import logging
from typing import Callable, Dict, List, Optional

from sajha.regagg import ids
from sajha.regagg.config_models import RegulatorConfig
from sajha.regagg.corpus_storage import CorpusStorage
from sajha.regagg.events import RunManifest
from sajha.regagg.fetch import Fetcher
from sajha.regagg.pipeline import run_regulator
from sajha.regagg.versioning import CorpusVersioning

logger = logging.getLogger(__name__)

OpenerFor = Callable[[RegulatorConfig], Callable[[str], bytes]]
FetcherFor = Callable[[RegulatorConfig], Fetcher]


def _run_id(logical_date: str, regulator_id: str, trigger: str, salt: str = "") -> str:
    short = ids.short_hash(f"{logical_date}|{regulator_id}|{trigger}|{salt}", 4)
    return ids.make_run_id(logical_date, regulator_id, short)


def run_daily(
    session,
    storage: CorpusStorage,
    configs: Dict[str, RegulatorConfig],
    opener_for: OpenerFor,
    fetcher_for: FetcherFor,
    logical_date: str,
    regulator_ids: Optional[List[str]] = None,
    trigger: str = "schedule",
    operator: Optional[str] = None,
    now=None,
) -> List[RunManifest]:
    """Fan out one run per selected active regulator. Failures are isolated."""
    selected = _select(configs, regulator_ids, only_active=(trigger == "schedule"))
    manifests: List[RunManifest] = []
    for cfg in selected:
        run_id = _run_id(logical_date, cfg.id, trigger)
        try:
            m = run_regulator(
                session, storage, cfg,
                source_opener=opener_for(cfg), fetcher=fetcher_for(cfg),
                run_id=run_id, logical_date=logical_date, trigger=trigger,
                operator=operator, now=now)
        except Exception as e:  # noqa: BLE001 — isolate a hard regulator failure
            logger.exception("regulator %s failed", cfg.id)
            m = RunManifest(run_id=run_id, regulator_id=cfg.id,
                            logical_date=logical_date, trigger=trigger, errors=1)
            m.error_list.append({"stage": "fatal", "error": str(e)})
            m.finalize()
        manifests.append(m)
    return manifests


def rerun(
    session,
    storage: CorpusStorage,
    configs: Dict[str, RegulatorConfig],
    opener_for: OpenerFor,
    fetcher_for: FetcherFor,
    logical_date: str,
    scope: str = "all",                 # 'all' | list of ids passed via regulator_ids
    regulator_ids: Optional[List[str]] = None,
    operator: Optional[str] = None,
    now=None,
) -> List[RunManifest]:
    ids_arg = None if scope == "all" else (regulator_ids or [])
    return run_daily(session, storage, configs, opener_for, fetcher_for,
                     logical_date, regulator_ids=ids_arg, trigger="rerun",
                     operator=operator, now=now)


def reconcile(session, storage: CorpusStorage,
              regulator_id: Optional[str] = None) -> Dict:
    """Run the versioning reconcile + invariant check across the corpus (US-3.3)."""
    v = CorpusVersioning(session, storage)
    report = v.reconcile(regulator_id=regulator_id)
    report["invariant_violations"] = v.check_invariants(regulator_id=regulator_id)
    report["ok"] = not report["invariant_violations"]
    return report


def _select(configs: Dict[str, RegulatorConfig],
            regulator_ids: Optional[List[str]], only_active: bool) -> List[RegulatorConfig]:
    if regulator_ids is not None:
        chosen = [configs[i] for i in regulator_ids if i in configs]
    else:
        chosen = list(configs.values())
    if only_active:
        chosen = [c for c in chosen if c.active]
    return chosen
