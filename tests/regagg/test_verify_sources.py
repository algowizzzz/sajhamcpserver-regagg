"""
Epic 9 — source verification harness (offline). Exercises reachability,
content-type, parseability, and freshness checks with an injected opener.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from sajha.regagg.config_loader import load_one
from sajha.regagg.verify_sources import (
    FAIL, PASS, WARN, check_source, render_report_md, verify_config,
)

REPO = Path(__file__).resolve().parents[2]
CONFIGS = REPO / "config" / "regulators"
NOW = datetime(2026, 7, 15, tzinfo=timezone.utc)

GOOD_SITEMAP = (b'<?xml version="1.0"?><urlset '
                b'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                b'<url><loc>https://x/a</loc><lastmod>2026-07-01</lastmod></url>'
                b'<url><loc>https://x/b</loc><lastmod>2026-07-10</lastmod></url></urlset>')
STALE_SITEMAP = (b'<?xml version="1.0"?><urlset '
                 b'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                 b'<url><loc>https://x/a</loc><lastmod>2020-01-01</lastmod></url></urlset>')
GOOD_FEED = (b'<?xml version="1.0"?><rss version="2.0"><channel>'
             b'<item><title>t</title><link>https://x/1</link>'
             b'<pubDate>Wed, 01 Jul 2026 00:00:00 GMT</pubDate></item></channel></rss>')
LISTING_OK = b"<html>" + b"".join(f'<a href="/{i}">l</a>'.encode() for i in range(6)) + b"</html>"
LISTING_THIN = b'<html><a href="/1">only one</a></html>'
GOOD_API = b'{"results":[{"document_number":"2026-1"}]}'


def _opener(mapping):
    def _o(url):
        if url not in mapping:
            raise ConnectionError("unreachable")
        code, ctype, body = mapping[url]
        return code, ctype, body
    return _o


def test_check_sitemap_pass():
    op = _opener({"u": (200, "application/xml", GOOD_SITEMAP)})
    c = check_source("u", "sitemap", op, now=NOW)
    assert c.status == PASS and c.item_count == 2


def test_check_sitemap_stale_warns():
    op = _opener({"u": (200, "text/xml", STALE_SITEMAP)})
    c = check_source("u", "sitemap", op, now=NOW)
    assert c.status == WARN and "stale" in c.reason


def test_check_wrong_content_type_fails():
    op = _opener({"u": (200, "text/html", GOOD_SITEMAP)})
    c = check_source("u", "sitemap", op, now=NOW)
    assert c.status == FAIL and "content-type" in c.reason


def test_check_unreachable_and_404():
    assert check_source("missing", "feed", _opener({}), now=NOW).status == FAIL
    op = _opener({"u": (404, "application/xml", GOOD_FEED)})
    assert check_source("u", "feed", op, now=NOW).status == FAIL


def test_check_feed_and_api_and_listing():
    assert check_source("f", "feed", _opener({"f": (200, "application/rss+xml", GOOD_FEED)}),
                        now=NOW).status == PASS
    assert check_source("a", "api", _opener({"a": (200, "application/json", GOOD_API)}),
                        now=NOW).status == PASS
    assert check_source("l", "listing", _opener({"l": (200, "text/html", LISTING_OK)}),
                        now=NOW).status == PASS
    assert check_source("l", "listing", _opener({"l": (200, "text/html", LISTING_THIN)}),
                        now=NOW).status == FAIL


def test_verify_config_over_real_osfi_config():
    cfg = load_one(CONFIGS / "osfi.yaml")   # sitemap + 2 listings
    op = _opener({
        cfg.sources.sitemap.url: (200, "application/xml", GOOD_SITEMAP),
        cfg.sources.listing_pages[0].url: (200, "text/html", LISTING_OK),
        cfg.sources.listing_pages[1].url: (200, "text/html", LISTING_THIN),
    })
    rep = verify_config(cfg, op, now=NOW)
    assert rep.has_verified_primary          # sitemap + one listing passed
    assert rep.passed == 2 and len(rep.checks) == 3
    md = render_report_md([rep])
    assert "osfi" in md and "verified primary source" in md
