#!/usr/bin/env python3
"""
Intraday news poll — cheap, safe to run every couple of hours.

The daily pass re-enriches the whole corpus; doing that six times a day would
be wasteful. This entry point collects the news lane only and skips the
full-corpus sweep, so a poll is a few dozen feed fetches plus writes for
genuinely new stories. Frequent polls also make the per-source story cap a
PER-POLL cap, which is what stops a busy news day scrolling past the collector.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sajha.regagg.config_loader import load_all      # noqa: E402


def news_ids() -> list:
    configs = load_all(REPO / "config" / "regulators")
    return sorted(k for k, c in configs.items() if getattr(c, "category", "") == "news")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rps", default="2.0")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    ids = news_ids()
    if not ids:
        print("no news sources configured")
        return 0
    cmd = [sys.executable, str(REPO / "scripts" / "regagg_ingest_live.py"),
           "--only", ",".join(ids), "--rps", str(args.rps)]
    print(f"news poll: {len(ids)} wires")
    if args.dry_run:
        print(" ".join(cmd))
        return 0
    rc = subprocess.call(cmd, cwd=str(REPO))

    # Announce what arrived without rewriting anyone's morning page.
    try:
        from sqlalchemy.orm import sessionmaker
        from sajha.core.config import get_settings
        from sajha.db.engine import get_engine, init_db
        from sajha.regagg import myday as _m
        init_db(get_settings())
        session = sessionmaker(bind=get_engine(), expire_on_commit=False)()
        for upd in _m.refresh_intraday(session):
            print(f"  update: {upd['persona_id']} — {upd['note']}")
    except Exception as e:  # noqa: BLE001 — collection succeeded either way
        print(f"  (intraday update skipped: {e})")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
