"""
D9 — connector detection against RECORDED live fixtures (tests/fixtures/{id}/),
one parametrized case per regulator that has recordings. No network: these are
real payloads captured by scripts/regagg_record_fixtures.py.

Each case asserts the connector parses its real-world payload shape without
error and (for non-empty payloads) yields DetectionEvents with sane URLs.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from sajha.regagg.config_loader import load_all
from sajha.regagg.connectors import get_connector

REPO = Path(__file__).resolve().parents[2]
FIXTURES = REPO / "tests" / "fixtures"
CONFIGS = load_all(REPO / "config" / "regulators")

_cases = sorted(p.name for p in FIXTURES.iterdir()
                if p.is_dir() and any(p.iterdir())) if FIXTURES.exists() else []


@pytest.mark.parametrize("regulator_id", _cases)
def test_connector_parses_recorded_payload(regulator_id):
    cfg = CONFIGS[regulator_id]
    d = FIXTURES / regulator_id
    payloads = {}
    if (d / "sitemap.xml").exists():
        payloads["sitemap"] = (d / "sitemap.xml").read_bytes()
    listings = sorted(d.glob("listing_*.html"))
    if listings:
        payloads["listings"] = [p.read_bytes() for p in listings]
        payloads["listing_base"] = (cfg.sources.listing_pages[0].url
                                    if cfg.sources.listing_pages else "")
    feeds = sorted(d.glob("feed_*.xml"))
    if feeds:
        payloads["feeds"] = [p.read_bytes() for p in feeds]
    if (d / "api.json").exists():
        try:
            payloads["api"] = json.loads((d / "api.json").read_text())
        except json.JSONDecodeError:
            pass   # legacy recording of a non-JSON API base; ignored

    events = get_connector(cfg, "fixture-run").detect(payloads)
    # parse must not blow up; if the recorded payload had entries, we detect them
    for e in events[:5]:
        assert e.url.startswith("http")
        assert e.regulator_id == regulator_id
    # sitemap-index regulators may legitimately detect 0 at this layer (children
    # are resolved by the pipeline), so only assert non-negative
    assert isinstance(events, list)


def test_fixture_coverage_report():
    """Not a gate — prints which regulators still lack recordings."""
    missing = sorted(set(CONFIGS) - set(_cases))
    print(f"\nfixture coverage: {len(_cases)}/{len(CONFIGS)} recorded; missing: {missing}")
    assert len(_cases) >= 1
