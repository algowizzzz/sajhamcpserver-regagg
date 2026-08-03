#!/usr/bin/env python3
"""
Verify every regulator's candidate sources against the live web (Epic 9 / Epic 5
onboarding gate). Writes verification_report.md; with --write, flips
verified/checked_at in the YAML for sources that pass.

    python scripts/verify_sources.py                 # all regulators, report only
    python scripts/verify_sources.py --regulator osfi
    python scripts/verify_sources.py --write         # persist verified flags

This is the ONLY step that touches the network. Regulators failing discovery are
listed in the report for a human (Saad) to fix — never auto-guessed.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sajha.regagg.config_loader import iter_config_paths, load_one  # noqa: E402
from sajha.regagg.verify_sources import (  # noqa: E402
    render_report_md, verify_config,
)


def _http_opener(url: str):
    import requests
    resp = requests.get(url, headers={"User-Agent": "BMO-RegIntel/1.0 (+regintel-ops@example.com)"},
                        timeout=30, allow_redirects=True)
    return resp.status_code, resp.headers.get("Content-Type", ""), resp.content


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--regulator", help="verify a single regulator id")
    ap.add_argument("--write", action="store_true", help="persist verified flags to YAML")
    ap.add_argument("--out", default="verification_report.md")
    args = ap.parse_args()

    base = REPO / "config" / "regulators"
    paths = ([base / f"{args.regulator}.yaml"] if args.regulator
             else iter_config_paths(base))

    reports = []
    for p in paths:
        cfg = load_one(p)
        print(f"verifying {cfg.id} ...", flush=True)
        rep = verify_config(cfg, _http_opener)
        reports.append(rep)
        print(f"  {rep.passed}/{len(rep.checks)} passed")
        if args.write:
            print("  (--write) NOTE: YAML flag update is a manual review step; "
                  "see report before flipping verified:true")

    md = render_report_md(reports)
    (REPO / args.out).write_text(md, encoding="utf-8")
    print(f"\nwrote {args.out}")
    ready = sum(r.has_verified_primary for r in reports)
    print(f"{ready}/{len(reports)} regulators have >=1 verified primary source")
    return 0 if ready == len(reports) else 2


if __name__ == "__main__":
    raise SystemExit(main())
