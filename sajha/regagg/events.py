"""
Event contracts passed between pipeline stages (TRD §3).

Connectors emit :class:`DetectionEvent`s (change detection only); the fetch
stage turns each into an :class:`IngestEvent` (full content). Both are plain
dataclasses, JSON-serializable, and carry ``run_id`` for manifest attribution.
"""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class DetectionEvent:
    regulator_id: str
    url: str
    run_id: str
    title: Optional[str] = None
    published_date: Optional[date] = None
    doc_type_hint: Optional[str] = None
    reference_number: Optional[str] = None
    source: str = ""              # which feed/sitemap/api surfaced it
    is_update: bool = False       # url already seen, content hash changed
    fetch_url: Optional[str] = None  # fetch HERE when set (e.g. FedReg raw_text_url
                                     # — the sanctioned endpoint); `url` stays the
                                     # provenance/identity anchor
    fallback_text: Optional[str] = None  # API-supplied text (e.g. FedReg abstract)
                                         # used when page fetch is bot-blocked

    def to_dict(self) -> dict:
        d = dataclasses.asdict(self)
        if self.published_date:
            d["published_date"] = self.published_date.isoformat()
        return d


@dataclass
class IngestEvent:
    detection: DetectionEvent
    content_md: str
    content_hash: str
    raw: Optional[bytes] = None
    raw_ext: str = "html"
    final_url: str = ""
    fetch_method: str = "html_to_md"
    ocr: bool = False
    extracted_title: Optional[str] = None


@dataclass
class RunManifest:
    """Per-regulator run summary, mirrored to reg_runs + _state/run_manifests."""
    run_id: str
    regulator_id: str
    logical_date: str
    trigger: str = "schedule"
    detected: int = 0
    fetched: int = 0
    ingested: int = 0
    archived: int = 0
    deduped: int = 0          # meta-source entries skipped (agency copy canonical)
    errors: int = 0
    status: str = "running"
    error_list: list = field(default_factory=list)
    detected_urls: list = field(default_factory=list)
    duration_s: float = 0.0

    def finalize(self) -> "RunManifest":
        """Status semantics (humane, not brutal):

        failed        — systemically wrong: more than 20% of detected URLs
                        errored, or fetching failed outright (errors, and not
                        one document came back)
        success       — docs landed; scattered per-URL errors (dead links on
                        the regulator's side) stay visible as an error count,
                        not a red row
        success_empty — nothing new. Whether a couple of links were dead is a
                        detail; it is not a failed collection.

        The old rule made ANY error fatal whenever nothing was ingested, so a
        source that correctly found nothing new went red over two 404s in 889
        URLs (fintrac, 0.2%) and one unreachable PDF in 17 (hkma). "Nothing
        changed today" is the most common healthy outcome there is, and it was
        being reported as a fault the moment a regulator left a dead link up.
        """
        error_rate = self.errors / max(self.detected, 1)
        fetch_collapsed = self.errors > 0 and self.fetched == 0 and self.detected > 0
        if error_rate > 0.20 or fetch_collapsed:
            self.status = "failed"
        elif self.ingested == 0:
            self.status = "success_empty"
        else:
            self.status = "success"
        return self

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
