#!/usr/bin/env python3
"""
Record per-regulator source fixtures (TRD §9.2): fetch each regulator's
sources ONCE and store the raw bytes under tests/fixtures/{regulator_id}/ so
the connector suite runs against real recorded payloads with no network.

    python scripts/regagg_record_fixtures.py            # all 30
    python scripts/regagg_record_fixtures.py --only osfi,frb
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

import requests

from sajha.regagg.config_loader import load_all
from sajha.regagg.pipeline import build_api_url

UA = "BMO-RegIntel/1.0 (+regintel-ops@example.com)"
OUT = REPO / "tests" / "fixtures"


def fetch(url: str) -> bytes | None:
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=20, allow_redirects=True)
        return r.content if r.status_code == 200 else None
    except Exception:  # noqa: BLE001
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    args = ap.parse_args()
    configs = load_all(REPO / "config" / "regulators")
    if args.only:
        want = set(args.only.split(","))
        configs = {k: v for k, v in configs.items() if k in want}

    recorded = 0
    for cfg in configs.values():
        d = OUT / cfg.id
        d.mkdir(parents=True, exist_ok=True)
        got = []
        s = cfg.sources
        if s.sitemap and (b := fetch(s.sitemap.url)):
            (d / "sitemap.xml").write_bytes(b[:2_000_000])   # cap: fixtures stay small
            got.append("sitemap")
        for i, lp in enumerate(s.listing_pages):
            if (b := fetch(lp.url)):
                (d / f"listing_{i}.html").write_bytes(b[:1_000_000])
                got.append(f"listing_{i}")
        for i, f in enumerate(s.feeds):
            if (b := fetch(f.url)):
                (d / f"feed_{i}.xml").write_bytes(b[:1_000_000])
                got.append(f"feed_{i}")
        if s.api and (b := fetch(build_api_url(cfg))):
            import json as _json
            try:                       # only record if it's actually JSON
                _json.loads(b.decode("utf-8"))
                (d / "api.json").write_bytes(b[:1_000_000])
                got.append("api")
            except Exception:  # noqa: BLE001 — data-series APIs return HTML at base
                pass
        print(f"  {cfg.id:9s} recorded: {', '.join(got) or 'NOTHING (all sources failed)'}")
        recorded += bool(got)
    print(f"\n{recorded}/{len(configs)} regulators have recorded fixtures under tests/fixtures/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
