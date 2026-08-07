#!/usr/bin/env python3
"""
Morning generation: build every persona's page before the desk arrives.

Runs at 05:30 so My Day is cached and identical for everyone who opens it —
one truth per day. Generating here (rather than on first view) also means a
slow or failed model call is an operations problem at 05:30, not a user's
blank page at 07:30.

Exit code is non-zero if any persona failed, so cron/monitoring notices.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sqlalchemy import select                          # noqa: E402
from sqlalchemy.orm import sessionmaker                # noqa: E402

from sajha.core.config import get_settings             # noqa: E402
from sajha.db.engine import get_engine, init_db        # noqa: E402
from sajha.regagg import myday as M                    # noqa: E402
from sajha.regagg.models import Persona                # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--day", help="logical date (default: today)")
    ap.add_argument("--force", action="store_true", help="rebuild cached pages")
    args = ap.parse_args()

    init_db(get_settings())
    session = sessionmaker(bind=get_engine(), expire_on_commit=False)()
    personas = session.scalars(select(Persona)).all()
    if not personas:
        print("no personas yet — nothing to generate")
        return 0

    now = datetime.now(timezone.utc)
    ok = failed = 0
    for p in personas:
        try:
            out = M.build_my_day(session, p, day=args.day, force=args.force, now=now)
            led = out["ledger"]
            print(f"  {p.persona_id} {p.name[:28]:28s} {out['generator']:>10s} "
                  f"shown={led['shown']:<3d} matched={led['matched']:<3d} "
                  f"quiet={led['quiet_entities']}")
            ok += 1
        except Exception as e:  # noqa: BLE001 — one bad persona must not stop the rest
            print(f"  {p.persona_id} {p.name[:28]:28s} FAILED {e}")
            failed += 1
    print(f"generated {ok} page(s), {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
