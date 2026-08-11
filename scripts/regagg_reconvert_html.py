#!/usr/bin/env python3
"""Re-convert stored raw.html into markdown, without touching the network.

`html_to_md` chose its container as `main or article or body` — the first
matching tag, whatever was in it. On OSC the first `<article>` is a search
widget containing the word "Search", so every OSC page converted to six
characters and was stored with an empty body. 10,560 documents, 100% of the
source; RBI the same. The corpus reported 19,761 documents while more than half
were titles with nothing underneath.

The pages themselves were fine — `raw.html` is 280 KB apiece and sitting right
there. So this re-runs the conversion over what we already hold: no refetching,
no politeness budget, nothing asked of the regulators a second time.

Writes `content.md` in the corpus store and the `data/markdown` projection, and
leaves the document row's hash alone — the *source* did not change, our reading
of it did, so this is not a new version.

    python scripts/regagg_reconvert_html.py                # dry run
    python scripts/regagg_reconvert_html.py --apply
    python scripts/regagg_reconvert_html.py --apply --only osc,rbi
    python scripts/regagg_reconvert_html.py --apply --all   # not just the empties
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write (default: dry run)")
    ap.add_argument("--only", help="comma-separated regulator ids")
    ap.add_argument("--all", action="store_true",
                    help="re-convert every document, not only the empty ones")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    import sqlite3

    from sajha.regagg.fetch import html_to_md

    db = REPO / "data" / "sajha.db"
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    q = "SELECT regulator_id, doc_id, doc_type, s3_prefix FROM reg_documents " \
        "WHERE s3_prefix IS NOT NULL"
    params: list = []
    if args.only:
        ids = args.only.split(",")
        q += f" AND regulator_id IN ({','.join('?' * len(ids))})"
        params = ids
    rows = list(con.execute(q, params))
    con.close()

    todo = []
    for rid, doc_id, doc_type, prefix in rows:
        raw = Path(prefix) / "raw.html"
        content = Path(prefix) / "content.md"
        if not raw.exists():
            continue
        try:
            if not args.all and content.exists() and content.stat().st_size > 0:
                continue
        except OSError:
            pass
        todo.append((rid, doc_id, doc_type, Path(prefix), raw, content))
    if args.limit:
        todo = todo[:args.limit]

    print(f"{len(todo):,} documents to re-convert"
          f"{'' if args.apply else '  (dry run — pass --apply to write)'}")

    fixed = still_empty = failed = 0
    gained = 0
    for i, (rid, doc_id, doc_type, prefix, raw, content) in enumerate(todo, 1):
        try:
            html = raw.read_text(encoding="utf-8", errors="replace")
            md, _title = html_to_md(html)
        except Exception as e:  # noqa: BLE001 — one bad page must not stop the pass
            failed += 1
            print(f"  ! {rid}/{doc_id}: {e}")
            continue
        if not md.strip():
            # Genuinely nothing to read. That is a finding about the page, not
            # a silent skip — it is counted and reported.
            still_empty += 1
            continue
        before = content.stat().st_size if content.exists() else 0
        gained += len(md) - before
        fixed += 1
        if args.apply:
            content.write_text(md, encoding="utf-8")
            _reproject(REPO, rid, doc_id, doc_type, md)
        if i % 500 == 0:
            print(f"  … {i:,}/{len(todo):,}")

    print(f"\nrecovered : {fixed:,} documents, {gained/1e6:.1f} MB of text")
    print(f"still empty: {still_empty:,}  (the page really has no prose)")
    print(f"failed     : {failed:,}")
    if not args.apply:
        print("\nnothing was written — re-run with --apply")
    return 0


def _reproject(repo: Path, rid: str, doc_id: str, doc_type: str, md: str) -> None:
    """Refresh the agent-consumable copy, preserving its frontmatter."""
    lane = "policy" if doc_type in ("guidance", "final_rule", "consultation") else "web"
    for path in (repo / "data" / "markdown").rglob(f"{doc_id}.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if text.startswith("---"):
            end = text.find("\n---", 3)
            front = text[:end + 4] if end != -1 else ""
        else:
            front = ""
        path.write_text(f"{front}\n{md}\n" if front else md, encoding="utf-8")
        return
    del lane  # projection path is discovered, not assumed


if __name__ == "__main__":
    raise SystemExit(main())
