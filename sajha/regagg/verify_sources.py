"""
Source verification harness (06_SOURCE_MAP §3 / Epic 9).

"No source URL is trusted until verify_sources passes it" (invariant #4). For each
candidate URL in a regulator config this checks:

    reachability   -> HTTP 200 + expected content-type
    parseability   -> sitemap has >=1 <url>; feed has >=1 entry; listing has >=5
                      in-domain links; api returns schema-valid JSON
    freshness      -> newest item/lastmod within `freshness_warn_days` (else warn)

It returns a structured report and can flip ``verified``/``checked_at`` in the
YAML. Network IO is injected (``opener``) so the check logic is unit-tested
offline; the CLI (scripts/verify_sources.py) supplies a real HTTP opener.

Gate: a regulator is onboard-ready when it has >=1 verified primary source and a
passing sample ingest. Failures escalate to a report for a human (Saad).
"""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from typing import Callable, Dict, List, Optional, Tuple

import feedparser

from sajha.regagg.config_models import RegulatorConfig

# opener(url) -> (status_code, content_type, body_bytes)
Opener = Callable[[str], Tuple[int, str, bytes]]

PASS, WARN, FAIL = "pass", "warn", "fail"


@dataclass
class SourceCheck:
    url: str
    kind: str                       # sitemap | listing | feed | api
    status: str = FAIL
    reason: str = ""
    checked_at: Optional[str] = None
    item_count: int = 0


@dataclass
class RegulatorReport:
    regulator_id: str
    checks: List[SourceCheck] = field(default_factory=list)

    @property
    def passed(self) -> int:
        return sum(c.status == PASS for c in self.checks)

    @property
    def has_verified_primary(self) -> bool:
        return self.passed >= 1

    def to_dict(self) -> dict:
        return {"regulator_id": self.regulator_id,
                "passed": self.passed, "total": len(self.checks),
                "has_verified_primary": self.has_verified_primary,
                "checks": [vars(c) for c in self.checks]}


def _expected_ctype(kind: str) -> Tuple[str, ...]:
    return {
        "sitemap": ("xml",), "feed": ("xml", "rss", "atom"),
        "listing": ("html",), "api": ("json",),
    }[kind]


def check_source(url: str, kind: str, opener: Opener,
                 now: Optional[datetime] = None, freshness_days: int = 90) -> SourceCheck:
    now = now or datetime.now(timezone.utc)
    chk = SourceCheck(url=url, kind=kind, checked_at=now.isoformat())
    try:
        status_code, ctype, body = opener(url)
    except Exception as e:  # noqa: BLE001
        chk.status, chk.reason = FAIL, f"unreachable: {e}"
        return chk

    if status_code != 200:
        chk.status, chk.reason = FAIL, f"HTTP {status_code}"
        return chk
    if not any(x in (ctype or "").lower() for x in _expected_ctype(kind)):
        chk.status, chk.reason = FAIL, f"unexpected content-type '{ctype}'"
        return chk

    ok, count, newest, reason = _parse_and_count(kind, body)
    chk.item_count = count
    if not ok:
        chk.status, chk.reason = FAIL, reason
        return chk

    # freshness (only where a date is available)
    if newest is not None and (now.date() - newest) > timedelta(days=freshness_days):
        chk.status, chk.reason = WARN, f"stale: newest item {newest} > {freshness_days}d old"
        return chk
    chk.status, chk.reason = PASS, f"{count} items"
    return chk


def _parse_and_count(kind: str, body: bytes) -> Tuple[bool, int, Optional[date], str]:
    if kind in ("sitemap",):
        try:
            root = ET.fromstring(body)
        except ET.ParseError as e:
            return False, 0, None, f"xml parse error: {e}"
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        # a sitemap INDEX is valid: the pipeline recurses into child sitemaps
        if root.tag.split("}")[-1] == "sitemapindex":
            kids = root.findall(".//sm:sitemap", ns) or root.findall(".//sitemap")
            newest = _newest_lastmod(root, ns)
            return (len(kids) >= 1, len(kids), newest,
                    "empty sitemap index" if not kids else "")
        locs = root.findall(".//sm:url", ns) or root.findall(".//url")
        newest = _newest_lastmod(root, ns)
        return (len(locs) >= 1, len(locs), newest,
                "no <url> entries" if not locs else "")
    if kind == "feed":
        parsed = feedparser.parse(body)
        n = len(parsed.entries)
        newest = None
        dates = [e.get("published_parsed") or e.get("updated_parsed") for e in parsed.entries]
        dates = [d for d in dates if d]
        if dates:
            newest = max(date(d.tm_year, d.tm_mon, d.tm_mday) for d in dates)
        return (n >= 1, n, newest, "no feed entries" if n == 0 else "")
    if kind == "listing":
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(body, "html.parser")
        links = [a for a in soup.find_all("a", href=True)]
        return (len(links) >= 5, len(links), None,
                f"only {len(links)} links (<5)" if len(links) < 5 else "")
    if kind == "api":
        try:
            data = json.loads(body)
        except json.JSONDecodeError as e:
            return False, 0, None, f"invalid json: {e}"
        results = data.get("results", data if isinstance(data, list) else [])
        n = len(results) if isinstance(results, list) else 0
        return (n >= 1, n, None, "no results" if n == 0 else "")
    return False, 0, None, f"unknown kind {kind}"


def _newest_lastmod(root, ns) -> Optional[date]:
    lms = []
    for el in (root.findall(".//sm:lastmod", ns) or root.findall(".//lastmod")):
        try:
            lms.append(date.fromisoformat((el.text or "")[:10]))
        except ValueError:
            continue
    return max(lms) if lms else None


def verify_config(config: RegulatorConfig, opener: Opener,
                  now: Optional[datetime] = None, freshness_days: int = 90) -> RegulatorReport:
    report = RegulatorReport(regulator_id=config.id)
    s = config.sources
    if s.sitemap:
        report.checks.append(check_source(s.sitemap.url, "sitemap", opener, now, freshness_days))
    for lp in s.listing_pages:
        report.checks.append(check_source(lp.url, "listing", opener, now, freshness_days))
    for f in s.feeds:
        report.checks.append(check_source(f.url, "feed", opener, now, freshness_days))
    if s.api:
        from sajha.regagg.pipeline import build_api_url
        report.checks.append(check_source(build_api_url(config), "api", opener, now, freshness_days))
    return report


def render_report_md(reports: List[RegulatorReport]) -> str:
    lines = ["# Source Verification Report", ""]
    total_ok = sum(r.has_verified_primary for r in reports)
    lines.append(f"**{total_ok}/{len(reports)} regulators** have >=1 verified primary source.\n")
    for r in reports:
        flag = "✅" if r.has_verified_primary else "❌"
        lines.append(f"## {flag} {r.regulator_id} ({r.passed}/{len(r.checks)} passed)")
        for c in r.checks:
            mark = {"pass": "✓", "warn": "⚠", "fail": "✗"}[c.status]
            lines.append(f"- {mark} `{c.kind}` {c.url} — {c.reason}")
        lines.append("")
    return "\n".join(lines)
