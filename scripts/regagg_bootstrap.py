#!/usr/bin/env python3
"""
One-command bootstrap on a fresh clone: put the shipped data in place so the
server + reg_* tools work immediately with the full collected corpus.

    python scripts/regagg_bootstrap.py

- imports the sanitized seed (data/seed/regagg_seed.sql.gz — reg_* corpus
  tables only; no users, no api keys) into data/sajha.db if the reg tables
  aren't populated yet (never overwrites collected data)
- the server creates its own auth tables + default admin on first boot;
  mint a fresh API key from the admin UI for your agent
- sanity-checks the corpus + markdown projection shipped in the repo
"""
from __future__ import annotations

import gzip
import sqlite3
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SEED = REPO / "data" / "seed" / "regagg_seed.sql.gz"
LIVE = REPO / "data" / "sajha.db"


def main() -> int:
    db = sqlite3.connect(LIVE)
    have = db.execute("select count(*) from sqlite_master where type='table' "
                      "and name='reg_documents'").fetchone()[0]
    docs = db.execute("select count(*) from reg_documents").fetchone()[0] if have else 0
    if docs:
        print(f"reg tables already populated ({docs:,} documents) — leaving them alone")
    elif not SEED.exists():
        print(f"ERROR: seed missing at {SEED}")
        return 1
    else:
        db.executescript(gzip.open(SEED, "rt", encoding="utf-8").read())
        db.commit()
        print(f"imported seed into {LIVE}")

    docs, = db.execute("select count(*) from reg_documents").fetchone()
    regs, = db.execute("select count(*) from reg_regulators").fetchone()
    news, = db.execute(
        "select count(*) from reg_regulators where category='news'").fetchone()
    md = sum(1 for _ in (REPO / "data" / "markdown").rglob("*.md"))
    corpus = sum(1 for _ in (REPO / "data" / "web_aggregator").rglob("content.md"))
    print(f"ready: {docs:,} documents | {regs} sources ({regs - news} regulators "
          f"+ {news} news) | {corpus:,} corpus files | {md:,} markdown files")
    print("start the server:  python run_server.py --port 3005")
    print("dashboard:         http://localhost:3005/api/regagg/ui")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
