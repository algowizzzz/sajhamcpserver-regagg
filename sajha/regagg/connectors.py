"""
Connector engines (FR-1). Three stateless detectors, selected by config:

    connector: sitemap_diff  -> SitemapDiffConnector
    connector: rss           -> RssConnector
    connector: api           -> ApiConnector

Each ``detect(payloads)`` is a pure function of its already-fetched source
payloads (sitemap XML / feed bytes / API JSON) — network IO happens in the
pipeline, so connectors are trivially testable against recorded fixtures.
Adding regulator #31 is a new YAML config, never a new connector class.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from datetime import date, datetime
from typing import Dict, List, Optional
from urllib.parse import urljoin, urlparse

import feedparser
from bs4 import BeautifulSoup

from sajha.regagg.config_models import RegulatorConfig
from sajha.regagg.events import DetectionEvent


# ── shared helpers ──────────────────────────────────────────────────────────

def match_doc_type(text: str, config: RegulatorConfig) -> Optional[str]:
    """First doc_type_rule whose pattern is found in `text` (URL or query)."""
    for rule in config.doc_type_rules:
        if re.search(rule.pattern, text):
            return rule.doc_type
    return None


def passes_filters(url: str, config: RegulatorConfig) -> bool:
    for pat in config.exclude_patterns:
        if re.search(pat, url):
            return False
    if config.include_patterns:
        return any(re.search(pat, url) for pat in config.include_patterns)
    return True


def _parse_date(value) -> Optional[date]:
    if not value:
        return None
    if isinstance(value, date):
        return value
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return datetime.strptime(str(value)[:len(fmt) + 5], fmt).date()
        except (ValueError, TypeError):
            continue
    try:
        return datetime(*value[:3]).date()  # feedparser struct_time
    except Exception:  # noqa: BLE001
        return None


class BaseConnector:
    connector_type = "base"

    def __init__(self, config: RegulatorConfig, run_id: str,
                 seen: Optional[Dict[str, str]] = None):
        self.config = config
        self.run_id = run_id
        self.seen = seen or {}   # url -> last_modified/hash signal (for fast-path skip)

    def detect(self, payloads: Dict) -> List[DetectionEvent]:  # pragma: no cover
        raise NotImplementedError


# ── sitemap / listing differ ────────────────────────────────────────────────

class SitemapDiffConnector(BaseConnector):
    connector_type = "sitemap_diff"

    def detect(self, payloads: Dict) -> List[DetectionEvent]:
        urls: Dict[str, Optional[str]] = {}  # url -> lastmod

        sitemap = payloads.get("sitemap")
        if sitemap:
            for url, lastmod in self._parse_sitemap(sitemap):
                urls.setdefault(url, lastmod)

        for html in payloads.get("listings", []) or []:
            base = payloads.get("listing_base", "")
            for url in self._extract_links(html, base):
                urls.setdefault(url, None)

        events: List[DetectionEvent] = []
        for url, lastmod in urls.items():
            if not passes_filters(url, self.config):
                continue
            seen_sig = self.seen.get(url)
            is_known = url in self.seen
            # lastmod fast-path: skip a known URL whose lastmod hasn't advanced.
            if is_known and lastmod and seen_sig and lastmod <= seen_sig:
                continue
            events.append(DetectionEvent(
                regulator_id=self.config.id, url=url, run_id=self.run_id,
                published_date=_parse_date(lastmod),
                doc_type_hint=match_doc_type(url, self.config),
                source="sitemap_diff", is_update=is_known))
        return events

    @staticmethod
    def _parse_sitemap(data: bytes) -> List[tuple]:
        """Parse sitemap.xml (and sitemap-index recursion is handled by the
        pipeline supplying child sitemaps). Returns [(loc, lastmod)]."""
        out = []
        try:
            root = ET.fromstring(data)
        except ET.ParseError:
            return out
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        for url_el in root.findall(".//sm:url", ns) or root.findall(".//url"):
            loc = url_el.findtext("sm:loc", namespaces=ns) or url_el.findtext("loc")
            lastmod = url_el.findtext("sm:lastmod", namespaces=ns) or url_el.findtext("lastmod")
            if loc:
                out.append((loc.strip(), (lastmod or "").strip() or None))
        return out

    @staticmethod
    def _extract_links(html: bytes | str, base_url: str) -> List[str]:
        soup = BeautifulSoup(html if isinstance(html, str) else html.decode("utf-8", "replace"),
                             "html.parser")
        host = urlparse(base_url).netloc
        links = []
        for a in soup.find_all("a", href=True):
            full = urljoin(base_url, a["href"])
            if urlparse(full).netloc == host or not host:
                links.append(full.split("#")[0])
        return links


# ── RSS / Atom ──────────────────────────────────────────────────────────────

class RssConnector(BaseConnector):
    connector_type = "rss"

    def detect(self, payloads: Dict) -> List[DetectionEvent]:
        events: List[DetectionEvent] = []
        seen_ids = set()
        for feed_bytes in payloads.get("feeds", []) or []:
            parsed = feedparser.parse(feed_bytes)
            for entry in parsed.entries:
                link = entry.get("link")
                if not link:
                    continue
                guid = entry.get("id") or link
                if guid in seen_ids:
                    continue
                seen_ids.add(guid)
                if not passes_filters(link, self.config):
                    continue
                pub = _parse_date(entry.get("published_parsed") or entry.get("published")
                                  or entry.get("updated"))
                events.append(DetectionEvent(
                    regulator_id=self.config.id, url=link, run_id=self.run_id,
                    title=entry.get("title"), published_date=pub,
                    doc_type_hint=match_doc_type(link, self.config),
                    source="rss", is_update=link in self.seen))
        return events


# ── API (provider adapters) ─────────────────────────────────────────────────

class ApiConnector(BaseConnector):
    connector_type = "api"

    def detect(self, payloads: Dict) -> List[DetectionEvent]:
        api = self.config.sources.api
        provider = api.provider if api else None
        data = payloads.get("api") or {}
        if provider == "federal_register":
            return self._federal_register(data)
        # boc_valet etc. are data-series APIs, not document sources -> no docs.
        return []

    def _federal_register(self, data: Dict) -> List[DetectionEvent]:
        events = []
        for rec in data.get("results", []):
            url = rec.get("html_url") or rec.get("pdf_url")
            if not url or not passes_filters(url, self.config):
                continue
            type_str = f"type={rec.get('type', '')}"
            events.append(DetectionEvent(
                regulator_id=self.config.id, url=url, run_id=self.run_id,
                title=rec.get("title"),
                published_date=_parse_date(rec.get("publication_date")),
                reference_number=rec.get("document_number"),
                doc_type_hint=match_doc_type(type_str, self.config),
                source="api:federal_register", is_update=url in self.seen))
        return events


# ── factory ─────────────────────────────────────────────────────────────────

_REGISTRY = {
    "sitemap_diff": SitemapDiffConnector,
    "rss": RssConnector,
    "api": ApiConnector,
}


def get_connector(config: RegulatorConfig, run_id: str,
                  seen: Optional[Dict[str, str]] = None) -> BaseConnector:
    cls = _REGISTRY.get(config.connector)
    if cls is None:
        raise ValueError(f"unknown connector '{config.connector}'")
    return cls(config, run_id, seen)
