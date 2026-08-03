"""
Epic 4 — orchestration: daily fan-out, failure isolation, rerun idempotency,
reconcile. Offline via injected openers.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from sajha.regagg import orchestrator
from sajha.regagg.config_loader import load_one
from sajha.regagg.fetch import Fetcher, fixture_opener
from sajha.regagg.models import Run

REPO = Path(__file__).resolve().parents[2]
CONFIGS = REPO / "config" / "regulators"
NOW = datetime(2026, 7, 10, 6, 0, tzinfo=timezone.utc)

OSFI = "https://www.osfi-bsif.gc.ca"
G_B13 = f"{OSFI}/en/guidance/guideline-b-13"


def _sitemap(entries):
    body = "".join(f"<url><loc>{u}</loc><lastmod>{lm}</lastmod></url>" for u, lm in entries)
    return (f'<?xml version="1.0"?><urlset '
            f'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>').encode()


def _doc(title, body):
    return (f"<html><head><title>{title}</title></head><body><main>"
            f"<h1>{title}</h1><p>{body}</p></main></body></html>".encode(), "text/html")


def test_daily_fanout_isolates_one_regulator_failure(session, storage, seed_regulator):
    osfi = load_one(CONFIGS / "osfi.yaml")
    boc = load_one(CONFIGS / "boc.yaml")   # rss
    seed_regulator("osfi", "CA", "sitemap_diff")
    seed_regulator("boc", "CA", "rss")
    configs = {"osfi": osfi, "boc": boc}

    osfi_src = {f"{OSFI}/sitemap.xml": _sitemap([(G_B13, "2026-07-01")]),
                f"{OSFI}/en/guidance": b"<html></html>",
                f"{OSFI}/en/news": b"<html></html>"}
    osfi_fetch = Fetcher(fixture_opener({G_B13: _doc("B-13", "text")}))

    def opener_for(cfg):
        if cfg.id == "osfi":
            return lambda url: osfi_src[url]
        # boc: feeds missing -> source opener raises -> that run fails, osfi unaffected
        def _boom(url):
            raise ConnectionError(f"boc feed unreachable: {url}")
        return _boom

    def fetcher_for(cfg):
        return osfi_fetch if cfg.id == "osfi" else Fetcher(fixture_opener({}))

    manifests = orchestrator.run_daily(
        session, storage, configs, opener_for, fetcher_for,
        logical_date="2026-07-10", now=NOW)

    by_id = {m.regulator_id: m for m in manifests}
    assert by_id["osfi"].status == "success" and by_id["osfi"].ingested == 1
    assert by_id["boc"].status == "failed" and by_id["boc"].errors >= 1
    # both runs recorded regardless of outcome
    assert session.query(Run).count() == 2


def test_rerun_subset_is_idempotent(session, storage, seed_regulator):
    osfi = load_one(CONFIGS / "osfi.yaml")
    seed_regulator("osfi", "CA", "sitemap_diff")
    configs = {"osfi": osfi}
    src = {f"{OSFI}/sitemap.xml": _sitemap([(G_B13, "2026-07-01")]),
           f"{OSFI}/en/guidance": b"<html></html>", f"{OSFI}/en/news": b"<html></html>"}
    opener_for = lambda cfg: (lambda url: src[url])          # noqa: E731
    fetcher_for = lambda cfg: Fetcher(fixture_opener({G_B13: _doc("B-13", "text")}))  # noqa: E731

    orchestrator.run_daily(session, storage, configs, opener_for, fetcher_for,
                           "2026-07-10", now=NOW)
    m = orchestrator.rerun(session, storage, configs, opener_for, fetcher_for,
                           "2026-07-10", scope="ids", regulator_ids=["osfi"],
                           operator="alice", now=NOW)
    assert m[0].trigger == "rerun" and m[0].ingested == 0   # nothing changed
    rec = orchestrator.reconcile(session, storage)
    assert rec["ok"] and rec["invariant_violations"] == []
    # rerun logged the operator
    reruns = [r for r in session.query(Run).all() if r.trigger == "rerun"]
    assert reruns and reruns[0].operator == "alice"
