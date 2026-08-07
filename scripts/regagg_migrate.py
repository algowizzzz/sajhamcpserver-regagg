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

def _ddl_type(engine, column) -> str:
    """Render a model column's type for this dialect (JSONB on Postgres)."""
    from sqlalchemy.schema import CreateColumn
    ddl = str(CreateColumn(column).compile(engine)).strip()
    # "name TYPE NOT NULL DEFAULT x" -> everything after the name
    return ddl.split(" ", 1)[1] if " " in ddl else "TEXT"


def main() -> int:
    from sajha.core.config import get_settings
    init_db(get_settings())        # honours db.type/db.path (SAJHA_* env)
    engine = get_engine()
    dialect = engine.dialect.name
    Base.metadata.create_all(engine, tables=[x.__table__ for x in m.REGAGG_MODELS])
    print(f"tables ensured ({dialect})")

    # Model-driven, not a hand-maintained list: on PostgreSQL the reg_* tables
    # may have been created by the SQL DDL scripts, which drift from the models
    # as the product evolves. Compare the mapped columns against what the
    # database actually has and add whatever is missing — so an upgrade of an
    # existing on-prem install always converges on the model.
    insp = inspect(engine)
    existing = set(insp.get_table_names())
    added = 0
    with engine.begin() as conn:
        for model in m.REGAGG_MODELS:
            table = model.__tablename__
            if table not in existing:
                continue
            have = {c["name"] for c in insp.get_columns(table)}
            for column in model.__table__.columns:
                if column.name in have:
                    continue
                ddl = _ddl_type(engine, column)
                # a NOT NULL column cannot be added to a populated table
                # without a default; fall back to nullable and let the app fill
                if "NOT NULL" in ddl and "DEFAULT" not in ddl.upper():
                    ddl = ddl.replace("NOT NULL", "").strip()
                conn.execute(text(f'ALTER TABLE {table} ADD COLUMN {column.name} {ddl}'))
                print(f"  + {table}.{column.name} {ddl}")
                added += 1
    # GIN indexes are the reason JSONB was chosen: they make containment
    # queries ("which documents mention this obligor?") index lookups instead
    # of full scans. Postgres only — SQLite ignores the concept.
    indexes = 0
    if dialect == "postgresql":
        with engine.begin() as conn:
            for table, column in (("reg_documents", "extraction"),
                                  ("reg_personas", "config"),
                                  ("reg_page_specs", "dossier")):
                if table not in existing:
                    continue
                name = f"ix_{table}_{column}_gin"
                conn.execute(text(
                    f"CREATE INDEX IF NOT EXISTS {name} ON {table} USING GIN ({column})"))
                indexes += 1
        print(f"  GIN indexes ensured: {indexes}")
    print(f"migration complete: {added} column(s) added")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
