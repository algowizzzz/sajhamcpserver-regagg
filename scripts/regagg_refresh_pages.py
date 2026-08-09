#!/usr/bin/env python3
"""Rebuild cached My Day pages so they pick up dossier changes.

    ./.venv/bin/python scripts/regagg_refresh_pages.py            # dry run
    ./.venv/bin/python scripts/regagg_refresh_pages.py --apply

A page is cached per persona per day and is deliberately read-only, so a change
to what the dossier carries — card previews, a new field — does not appear on
pages already built. They would fix themselves tomorrow; this fixes them now.

Only pages missing the field are rebuilt, so it is cheap to re-run and it does
not disturb a page someone may already have read unless that page is stale.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--all", action="store_true",
                    help="rebuild every cached page, not only those missing previews")
    args = ap.parse_args()

    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import sessionmaker

    import sajha.db.models  # noqa: F401
    from sajha.core.storage import LocalStorageBackend
    from sajha.regagg import myday as _m, runtime
    from sajha.regagg.corpus_storage import CorpusStorage
    from sajha.regagg.models import PageSpec, Persona

    engine = create_engine(f"sqlite:///{REPO/'data'/'sajha.db'}",
                           connect_args={"timeout": 60})
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    storage = CorpusStorage(LocalStorageBackend(str(REPO)))
    runtime.set_providers(session=lambda: session, storage=lambda: storage)

    pages = list(session.scalars(select(PageSpec)).all())
    todo = []
    for pg in pages:
        items = (pg.dossier or {}).get("items") or []
        has = any(i.get("preview") for i in items)
        if args.all or (items and not has):
            todo.append(pg)

    print(f"[pages] {len(todo)} of {len(pages)} cached page(s) to rebuild"
          f"{'' if args.apply else ' — DRY RUN'}")
    done = 0
    for pg in todo:
        persona = session.get(Persona, pg.persona_id)
        if persona is None:
            continue
        print(f"  {persona.name[:34]:<35} {pg.day}")
        if args.apply:
            _m.build_my_day(session, persona, day=pg.day, force=True)
            done += 1

    if args.apply:
        print(f"\n[pages] rebuilt {done}")
    else:
        print("\n        dry run — nothing written. Re-run with --apply.")
    runtime.set_providers(session=lambda: None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
