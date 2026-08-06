"""
Financial-news lane (category: news, fetch: feed_summary).

The copyright constraint IS the design: a news document is built entirely from
the publisher's own feed (headline + summary + link) and the pipeline must
never fetch the article page. These tests prove that with a fetcher that
explodes on contact, plus the per-source daily cap and the UI grouping.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest

from sajha.regagg.config_loader import load_all, load_one
from sajha.regagg.models import Document, Regulator
from sajha.regagg.pipeline import run_regulator

REPO = Path(__file__).resolve().parents[2]
CONFIGS = REPO / "config" / "regulators"
NOW = datetime(2026, 8, 5, 6, 0, tzinfo=timezone.utc)


class ExplodingFetcher:
    """Any article fetch is a copyright/ToS violation in the news lane."""

    def fetch(self, url, method=None):  # pragma: no cover - failure path
        raise AssertionError(f"news lane must never fetch article pages: {url}")


def _feed(n, with_summary=True):
    items = "".join(
        f"<item><title>Story {i}</title>"
        f"<link>https://news.example.com/story-{i}</link>"
        + (f"<description>&lt;p&gt;Summary of story {i}.&lt;/p&gt;</description>"
           if with_summary else "")
        + "<pubDate>Tue, 04 Aug 2026 09:00:00 GMT</pubDate></item>"
        for i in range(n))
    return f'<?xml version="1.0"?><rss version="2.0"><channel>{items}</channel></rss>'.encode()


def _news_cfg(feed_items=3, cap=50):
    """A minimal in-repo-shaped news config (bbc_business as the template)."""
    cfg = load_one(CONFIGS / "bbc_business.yaml")
    return cfg.model_copy(update={
        "max_docs_per_run": cap,
        "backfill_cutoff": None,   # fixture dates are synthetic
        "sources": cfg.sources.model_copy(update={
            "feeds": [cfg.sources.feeds[0].model_copy(
                update={"url": "https://news.example.com/rss"})]}),
    }), (lambda url: _feed(feed_items))


def _seed_news(session, rid="bbc_business"):
    session.add(Regulator(regulator_id=rid, name=rid, jurisdiction="UK",
                          connector="rss", config={}, category="news"))
    session.commit()


def test_all_news_configs_parse_with_news_contract():
    """Every category:news config must be feed_summary + capped + news_story."""
    news = {k: v for k, v in load_all(CONFIGS).items() if v.category == "news"}
    assert len(news) == 20
    for cfg in news.values():
        assert cfg.fetch == "feed_summary"
        assert cfg.max_docs_per_run == 50
        assert all(r.doc_type == "news_story" for r in cfg.doc_type_rules)


def test_feed_summary_never_fetches_articles(session, storage):
    _seed_news(session)
    cfg, opener = _news_cfg(feed_items=3)
    m = run_regulator(session, storage, cfg, opener, ExplodingFetcher(),
                      run_id="2026-08-05_bbc_business_t1",
                      logical_date="2026-08-05", now=NOW)
    assert (m.ingested, m.errors) == (3, 0) and m.status == "success"
    docs = session.query(Document).all()
    assert all(d.doc_type == "news_story" for d in docs)
    # content = headline + publisher summary + attribution, nothing scraped
    text = storage.read_content(docs[0].s3_prefix)
    assert "Summary of story" in text and "Read the full story at the source" in text
    assert "<p>" not in text  # summary HTML is stripped to plain text


def test_config_cap_limits_daily_stories(session, storage):
    """max_docs_per_run applies when the caller passes no explicit cap."""
    _seed_news(session)
    cfg, opener = _news_cfg(feed_items=12, cap=5)
    m = run_regulator(session, storage, cfg, opener, ExplodingFetcher(),
                      run_id="2026-08-05_bbc_business_t2",
                      logical_date="2026-08-05", now=NOW)
    assert m.ingested == 5 == session.query(Document).count()


def test_news_sources_group_under_financial_news(session):
    from sajha.regagg.queries_ui import REGION_ORDER, coverage_tree
    _seed_news(session)
    session.add(Regulator(regulator_id="osfi", name="OSFI", jurisdiction="CA",
                          connector="sitemap_diff", config={}))  # default: regulatory
    session.commit()
    assert "Financial News" in REGION_ORDER
    tree = coverage_tree(session)
    by_region = {r["region"]: r for r in tree["regions"]}
    news_ids = [i["regulator_id"] for i in by_region["Financial News"]["institutions"]]
    assert news_ids == ["bbc_business"]
    assert "osfi" in [i["regulator_id"] for i in by_region["Canada"]["institutions"]]


def test_news_dashboard_ranks_credit_events_first(session, storage):
    """A creditor-protection story must outrank a generic markets story."""
    from sajha.regagg.queries_ui import news_dashboard
    _seed_news(session)
    cfg, _ = _news_cfg()
    feed = (
        '<?xml version="1.0"?><rss version="2.0"><channel>'
        '<item><title>Stocks rally as shares climb</title>'
        '<link>https://news.example.com/markets-1</link>'
        '<pubDate>Tue, 04 Aug 2026 09:00:00 GMT</pubDate></item>'
        '<item><title>Retailer files for bankruptcy, creditor protection sought</title>'
        '<link>https://news.example.com/credit-1</link>'
        '<pubDate>Tue, 04 Aug 2026 10:00:00 GMT</pubDate></item>'
        '</channel></rss>').encode()
    run_regulator(session, storage, cfg, lambda url: feed, ExplodingFetcher(),
                  run_id="2026-08-05_bbc_business_t3",
                  logical_date="2026-08-05", now=NOW)
    d = news_dashboard(session, storage=storage)
    assert len(d["stories"]) == 2 and d["days"]
    assert d["stories"][0]["topic"] == "credit"          # bankruptcy outranks
    assert d["stories"][1]["topic"] == "markets"
    assert d["stories"][0]["rank"] > d["stories"][1]["rank"]
    assert "credit" in d["stories"][0]["why"] or "signal" in d["stories"][0]["why"]
