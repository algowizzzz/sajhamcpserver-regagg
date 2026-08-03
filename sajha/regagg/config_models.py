"""
Regulator configuration models (pydantic v2).

One YAML file per regulator under ``config/regulators/{id}.yaml`` deserializes
into a :class:`RegulatorConfig`. "Regulator is config, not code": adding
regulator #31 is a new YAML file, never a code change.

The models are strict (``extra='forbid'``) so a typo in a config is caught at
load time rather than silently ignored — this is the Foundation gate
("all 30 configs parse").
"""

from __future__ import annotations

from datetime import date
from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

# ── Controlled vocabularies (mirror 04_DATA_SCHEMA + 06_SOURCE_MAP) ──────────

ConnectorType = Literal["api", "rss", "sitemap_diff"]
FetchMethod = Literal["html_to_md", "pdf_to_md", "playwright", "tavily"]

# Controlled doc-type set (04_DATA_SCHEMA §4). doc_type_rules must map into this.
DOC_TYPES = frozenset({
    "final_rule", "consultation", "guidance", "announcement",
    "enforcement", "speech", "report",
})


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


# ── Source references ───────────────────────────────────────────────────────

class SourceRef(_Strict):
    """A single candidate URL (sitemap, listing page, or feed).

    ``verified`` is flipped to True only by scripts/verify_sources — never by
    hand. Until then the source is untrusted (invariant #4).
    """
    url: str
    verified: bool = False
    checked_at: Optional[str] = None


class ApiSource(_Strict):
    """An API-backed source (e.g. Federal Register, BoC Valet)."""
    provider: str
    base: str
    agencies: Optional[List[str]] = None
    verified: bool = False
    checked_at: Optional[str] = None


class Sources(_Strict):
    """Per-regulator source bundle. Which fields are populated depends on the
    connector (validated in :meth:`RegulatorConfig._check_connector_sources`)."""
    sitemap: Optional[SourceRef] = None
    listing_pages: List[SourceRef] = Field(default_factory=list)
    feeds: List[SourceRef] = Field(default_factory=list)
    api: Optional[ApiSource] = None

    def all_refs(self) -> List[SourceRef]:
        refs: List[SourceRef] = []
        if self.sitemap:
            refs.append(self.sitemap)
        refs.extend(self.listing_pages)
        refs.extend(self.feeds)
        return refs


class DocTypeRule(_Strict):
    """URL/query pattern → doc_type mapping. First matching rule wins;
    fallback order is LLM classification → 'announcement' (see US-2.2)."""
    pattern: str
    doc_type: str

    @model_validator(mode="after")
    def _check_doc_type(self) -> "DocTypeRule":
        if self.doc_type not in DOC_TYPES:
            raise ValueError(
                f"doc_type '{self.doc_type}' not in controlled set {sorted(DOC_TYPES)}"
            )
        return self


# ── Regulator config ────────────────────────────────────────────────────────

class RegulatorConfig(_Strict):
    """One regulator = one config entry. Shape matches config/regulators/*.yaml."""

    id: str
    name: str
    jurisdiction: str
    active: bool = True
    connector: ConnectorType
    sources: Sources
    fetch: FetchMethod = "html_to_md"
    rate_limit_rps: float = 0.5
    schedule: str = "daily_morning"
    include_patterns: List[str] = Field(default_factory=list)
    exclude_patterns: List[str] = Field(default_factory=list)
    default_tags: List[str] = Field(default_factory=list)
    doc_type_rules: List[DocTypeRule] = Field(default_factory=list)
    staleness_alert_days: int = 14
    backfill_cutoff: Optional[date] = None
    notes: Optional[str] = None
    meta_source: bool = False        # e.g. Federal Register: dedup vs agency copies
    harvest_pdfs: bool = True        # extract same-domain PDF links from ingested HTML

    @model_validator(mode="after")
    def _check_connector_sources(self) -> "RegulatorConfig":
        """Each connector requires the matching source shape to be present."""
        s = self.sources
        if self.connector == "api":
            if s.api is None:
                raise ValueError("connector 'api' requires sources.api")
        elif self.connector == "rss":
            if not s.feeds:
                raise ValueError("connector 'rss' requires sources.feeds (>=1)")
        elif self.connector == "sitemap_diff":
            if s.sitemap is None and not s.listing_pages:
                raise ValueError(
                    "connector 'sitemap_diff' requires sources.sitemap or sources.listing_pages"
                )
        if self.rate_limit_rps <= 0:
            raise ValueError("rate_limit_rps must be > 0")
        return self

    # Convenience -------------------------------------------------------------

    @property
    def is_fully_verified(self) -> bool:
        """True only when every candidate source has been verified. Onboarding
        gate (Epic 5) requires >=1 verified primary source per regulator."""
        refs = self.sources.all_refs()
        api_ok = self.sources.api.verified if self.sources.api else True
        return bool(refs or self.sources.api) and all(r.verified for r in refs) and api_ok

    @property
    def verified_source_count(self) -> int:
        n = sum(1 for r in self.sources.all_refs() if r.verified)
        if self.sources.api and self.sources.api.verified:
            n += 1
        return n

    @property
    def total_source_count(self) -> int:
        n = len(self.sources.all_refs())
        if self.sources.api:
            n += 1
        return n
