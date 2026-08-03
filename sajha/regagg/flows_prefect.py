"""
Prefect sidecar (optional) — thin wrappers over orchestrator.py.

Prefect is an optional dependency; this module imports lazily so the package
still loads without it (the deterministic core in orchestrator.py is what tests
exercise). To run the sidecar:

    pip install prefect
    prefect server start                       # or Prefect Cloud
    python -m sajha.regagg.flows_prefect deploy # register the daily schedule

The daily deployment triggers ``regagg_daily_flow`` at the cron in
config/regulators/_settings.yaml (06:00), one task per active regulator, with
retries/backoff. The admin "Rerun" button calls ``trigger_rerun`` which creates
a Prefect run of ``regagg_rerun_flow``.

Real DB sessions and network openers are constructed inside the flow from the
running SAJHA app (get_session / get_storage / a requests-based opener). Here we
keep signatures minimal and delegate all logic to orchestrator.py.
"""

from __future__ import annotations

from typing import List, Optional


def _require_prefect():
    try:
        import prefect  # noqa: F401
        return prefect
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(
            "Prefect is not installed. `pip install prefect` to run the sidecar. "
            "The orchestration core (sajha.regagg.orchestrator) runs without it."
        ) from exc


def build_daily_flow():
    """Construct the Prefect @flow lazily (only when prefect is available)."""
    prefect = _require_prefect()
    from prefect import flow, task

    from sajha.regagg import orchestrator
    from sajha.regagg.runtime import (  # app-wired providers (see runtime.py)
        get_configs, get_fetcher_for, get_opener_for, get_session, get_storage,
    )

    @task(retries=3, retry_delay_seconds=30)
    def _run_one(regulator_id: str, logical_date: str, trigger: str):
        session, storage = get_session(), get_storage()
        configs = {regulator_id: get_configs()[regulator_id]}
        return orchestrator.run_daily(
            session, storage, configs, get_opener_for(), get_fetcher_for(),
            logical_date, regulator_ids=[regulator_id], trigger=trigger)[0].to_dict()

    @flow(name="regagg_daily")
    def regagg_daily_flow(logical_date: str, regulator_ids: Optional[List[str]] = None):
        configs = get_configs()
        ids_ = regulator_ids or [c.id for c in configs.values() if c.active]
        # fan out — Prefect runs these concurrently subject to the task runner
        futures = [_run_one.submit(rid, logical_date, "schedule") for rid in ids_]
        return [f.result() for f in futures]

    return regagg_daily_flow


if __name__ == "__main__":  # pragma: no cover
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "deploy":
        flow = build_daily_flow()
        # Cron comes from _settings.yaml schedule.daily_cron (06:00 daily).
        flow.serve(name="regagg-daily", cron="0 6 * * *")
    else:
        print("usage: python -m sajha.regagg.flows_prefect deploy")
