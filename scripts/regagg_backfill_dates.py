#!/usr/bin/env python3
"""Backfill publication dates for documents collected without one.

    ./.venv/bin/python scripts/regagg_backfill_dates.py            # dry run
    ./.venv/bin/python scripts/regagg_backfill_dates.py --apply
    ./.venv/bin/python scripts/regagg_backfill_dates.py --apply --only osfi

Dry run by default: a bulk write over 5,000 documents should be inspected
before it happens, and the report tells you what it *would* do per source.

Only documents with no date are touched. A date already collected from the
source is better evidence than anything recovered here and is never overwritten.
Every recovered date is tagged `date:url` or `date:text` so a later reader can
tell an inferred date from a published one.

Expect roughly a quarter to be recoverable. The rest do not carry a date
anywhere we hold, and are left alone — see sajha/regagg/date_recovery.py.
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sajha.regagg import date_recovery as _dr      # noqa: E402
from sajha.regagg.models import Document, DocumentTag  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write (default: dry run)")
    ap.add_argument("--only", help="comma-separated source ids")
    ap.add_argument("--limit", type=int, default=0, help="stop after N documents")
    args = ap.parse_args()

    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import sessionmaker

    import sajha.db.models  # noqa: F401  (registers the shared Base)
    from sajha.core.storage import LocalStorageBackend
    from sajha.regagg.corpus_storage import CorpusStorage

    engine = create_engine(f"sqlite:///{REPO/'data'/'sajha.db'}",
                           connect_args={"timeout": 60})
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    storage = CorpusStorage(LocalStorageBackend(str(REPO)))

    q = select(Document).where(Document.published_date.is_(None))
    if args.only:
        q = q.where(Document.regulator_id.in_(args.only.split(",")))
    docs = list(session.scalars(q).all())
    if args.limit:
        docs = docs[:args.limit]

    print(f"[dates] {len(docs)} document(s) with no publication date"
          f"{' — DRY RUN' if not args.apply else ''}")

    by_source: Counter = Counter()
    how: Counter = Counter()
    changed = 0
    for i, d in enumerate(docs, 1):
        text = ""
        try:
            text = storage.read_content(d.s3_prefix) or ""
        except Exception:  # noqa: BLE001 — an unreadable body is not a failure
            text = ""
        got, source = _dr.recover(url=d.source_url or "", text=text[:8000])
        how[source] += 1
        if not got:
            continue
        by_source[d.regulator_id] += 1
        changed += 1
        if args.apply:
            d.published_date = got
            session.merge(DocumentTag(regulator_id=d.regulator_id, doc_id=d.doc_id,
                                      tag=f"date:{source}", source="rule"))
            if changed % 200 == 0:
                session.commit()
                print(f"  … {changed} written")
        if i % 1000 == 0:
            print(f"  scanned {i}/{len(docs)}")

    if args.apply:
        session.commit()

    print(f"\n[dates] recovered {changed} of {len(docs)} "
          f"({100 * changed / max(len(docs), 1):.0f}%)")
    print(f"        from url: {how['url']}   from text: {how['text']}   "
          f"no date anywhere: {how['none']}")
    if by_source:
        print("        top sources:")
        for rid, n in by_source.most_common(10):
            print(f"          {rid:<20} {n}")
    if not args.apply:
        print("\n        dry run — nothing written. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
