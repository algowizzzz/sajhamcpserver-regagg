#!/usr/bin/env python3
"""
Idempotent schema migration for the regagg product tables.

Safe to run repeatedly and on every deploy: creates any missing table and adds
any missing column. Works on SQLite (dev) and PostgreSQL (on-prem), because the
models declare JSONFlex — JSONB on Postgres, JSON elsewhere.

    python scripts/regagg_migrate.py
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sqlalchemy import inspect, text                      # noqa: E402

from sajha.db.base import Base                            # noqa: E402
from sajha.db.engine import get_engine, init_db           # noqa: E402
import sajha.regagg.models as m                           # noqa: E402

# columns added after the first release: (table, column, DDL type)
ADDED_COLUMNS = [
    ("reg_documents", "extraction", {"postgresql": "JSONB", "default": "TEXT"}),
    ("reg_documents", "materiality_score", {"default": "INTEGER NOT NULL DEFAULT 0"}),
    ("reg_documents", "materiality_band",
     {"default": "VARCHAR(16) NOT NULL DEFAULT 'Informational'"}),
    ("reg_documents", "materiality_reason", {"default": "TEXT"}),
    ("reg_regulators", "category",
     {"default": "VARCHAR(16) NOT NULL DEFAULT 'regulatory'"}),
]


def main() -> int:
    from sajha.core.config import get_settings
    init_db(get_settings())        # honours db.type/db.path (SAJHA_* env)
    engine = get_engine()
    dialect = engine.dialect.name
    Base.metadata.create_all(engine, tables=[x.__table__ for x in m.REGAGG_MODELS])
    print(f"tables ensured ({dialect})")

    insp = inspect(engine)
    existing_tables = set(insp.get_table_names())
    added = 0
    with engine.begin() as conn:
        for table, column, types in ADDED_COLUMNS:
            if table not in existing_tables:
                continue
            cols = {c["name"] for c in insp.get_columns(table)}
            if column in cols:
                continue
            ddl = types.get(dialect, types["default"])
            conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {ddl}"))
            print(f"  + {table}.{column} {ddl}")
            added += 1
    print(f"migration complete: {added} column(s) added")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
