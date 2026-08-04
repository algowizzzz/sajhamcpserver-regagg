#!/usr/bin/env python3
"""
Daily delta poll — THE entrypoint for the external scheduler.

    ./.venv/bin/python scripts/regagg_daily_poll.py            # normal daily run
    ./.venv/bin/python scripts/regagg_daily_poll.py --deep     # weekly deep run

Cron examples:
    0 6 * * *  cd /path/to/sajhamcpserver && ./.venv/bin/python scripts/regagg_daily_poll.py >> logs/regagg_daily.log 2>&1
    0 2 * * 6  cd /path/to/sajhamcpserver && ./.venv/bin/python scripts/regagg_daily_poll.py --deep >> logs/regagg_daily.log 2>&1

What a daily run does (delta semantics, all idempotent):
  1. Fleet ingest, every active regulator:
       * RSS regs: feeds only carry recent items -> naturally delta
       * sitemap regs: lastmod fast-path skips known-unchanged URLs;
         changed content archives the prior version (US-3.x)
       * daily cap per giant (fincen/osfi/csa/iais/fintrac) so slow sites
         extend depth a slice per day instead of blocking the fleet
       * fincen gets a long timeout (slow .gov host)
  2. Resolve pending cross-reference edges against the grown corpus.
  3. Reconcile storage/DB invariants (crash repair, staging cleanup).
  4. Print a one-line delta summary (also visible on /api/regagg/ui — Runs tab).

--deep raises the giant caps (weekly depth accrual). Every run is safe to
re-execute; unchanged content is never duplicated.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

GIANTS = "fincen,osfi,csa,iais,fintrac"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--deep", action="store_true", help="weekly deep run (bigger giant caps)")
    ap.add_argument("--rps", type=float, default=2.0)
    args = ap.parse_args()

    started = datetime.now(timezone.utc)
    giant_cap = 3000 if args.deep else 500

    # 1 — fleet ingest (reuse the hardened live runner; giants last + capped)
    cmd = [sys.executable, str(REPO / "scripts" / "regagg_ingest_live.py"),
           "--skip", "amf_qc",                       # bot-blocked, escalated
           "--giants", GIANTS, "--giant-cap", str(giant_cap),
           "--rps", str(args.rps), "--timeout", "25" if args.deep else "15"]
    print(f"[daily-poll] fleet ingest starting (deep={args.deep}, giant_cap={giant_cap})",
          flush=True)
    rc = subprocess.call(cmd)
    if rc != 0:
        print(f"[daily-poll] WARNING: ingest exited rc={rc} (partial results are kept)")

    # 2 + 3 — pending-edge resolution + reconciliation
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    import sajha.db.models  # noqa: F401
    from sajha.core.storage import LocalStorageBackend
    from sajha.regagg import rules
    from sajha.regagg.corpus_storage import CorpusStorage
    from sajha.regagg.orchestrator import reconcile

    engine = create_engine(f"sqlite:///{REPO/'data'/'sajha.db'}",
                           connect_args={"timeout": 60})
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    storage = CorpusStorage(LocalStorageBackend(str(REPO)))
    resolved = rules.resolve_pending(session)
    rec = reconcile(session, storage)
    # nightly self-heal of the agent-stack markdown projection (write-through
    # covers normal ingests; this catches anything missed)
    from sajha.regagg import projection
    proj = projection.resync(session, storage)
    print(f"[daily-poll] markdown projection: {proj['projected']} files current "
          f"({proj['skipped_no_content']} without content)")

    # 4 — delta summary for the log line
    c = engine.connect()
    today = started.date().isoformat()
    new_docs, archived, errors = c.execute(text(
        "select coalesce(sum(ingested),0), coalesce(sum(archived),0), "
        "coalesce(sum(errors),0) from reg_runs where logical_date=:d"), {"d": today}).one()
    total = c.execute(text("select count(*) from reg_documents")).scalar()
    mins = (datetime.now(timezone.utc) - started).total_seconds() / 60
    print(f"[daily-poll] DONE {today}: +{new_docs} new · {archived} revisions archived · "
          f"{errors} errors · {resolved} edges resolved · corpus {total} · "
          f"integrity {'OK' if rec['ok'] else 'VIOLATIONS: ' + str(rec['invariant_violations'])} · "
          f"{mins:.0f} min", flush=True)
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
