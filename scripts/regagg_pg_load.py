#!/usr/bin/env python3
"""
Copy the regagg tables from a SQLite database into PostgreSQL.

The on-prem migration path: collect on a laptop or a pilot box (SQLite), then
move the corpus into the production database without re-crawling every source.
Idempotent per row (upsert by primary key) and safe to re-run.

    SAJHA_DB_TYPE=postgresql SAJHA_DB_NAME=regagg ... \
        python scripts/regagg_pg_load.py --from data/sajha.db
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sqlalchemy import inspect, text                      # noqa: E402
from sqlalchemy.dialects.postgresql import insert as pg_insert   # noqa: E402

from sajha.core.config import get_settings                # noqa: E402
from sajha.db.engine import get_engine, init_db           # noqa: E402
import sajha.regagg.models as m                           # noqa: E402

JSON_HINT = ("config", "extraction", "spec", "dossier", "ledger", "meta",
             "shared_with", "watermark")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="src", default="data/sajha.db")
    ap.add_argument("--only", help="comma-separated table names")
    args = ap.parse_args()

    init_db(get_settings())
    engine = get_engine()
    if engine.dialect.name != "postgresql":
        print("target is not PostgreSQL — set SAJHA_DB_TYPE=postgresql")
        return 1

    src = sqlite3.connect(REPO / args.src)
    src.row_factory = sqlite3.Row
    have = set(inspect(engine).get_table_names())
    wanted = set((args.only or "").split(",")) if args.only else None

    total = 0
    for model in m.REGAGG_MODELS:
        table = model.__tablename__
        if table not in have or (wanted and table not in wanted):
            continue
        try:
            rows = src.execute(f"SELECT * FROM {table}").fetchall()
        except sqlite3.OperationalError:
            continue                     # table absent in the source
        if not rows:
            continue
        cols = {c.name for c in model.__table__.columns}
        pk = [c.name for c in model.__table__.primary_key]
        payload = []
        for r in rows:
            d = {k: r[k] for k in r.keys() if k in cols}
            for k, v in list(d.items()):
                # SQLite stores JSON columns as text; Postgres wants objects
                if isinstance(v, str) and (k in JSON_HINT or k.endswith("_json")):
                    try:
                        d[k] = json.loads(v)
                    except (TypeError, ValueError):
                        pass
            payload.append(d)
        with engine.begin() as conn:
            for chunk in (payload[i:i + 500] for i in range(0, len(payload), 500)):
                stmt = pg_insert(model.__table__).values(chunk)
                conn.execute(stmt.on_conflict_do_nothing(index_elements=pk))
        print(f"  {table:26s} {len(payload):>6,} rows")
        total += len(payload)
    print(f"loaded {total:,} rows into PostgreSQL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
