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
        failed        — the run produced nothing despite trying, or >20% of
                        detected URLs errored (systemic problem worth a red row)
        success       — docs landed; scattered per-URL errors (dead links on
                        the regulator's side, throttling) stay visible as an
                        error count, not a false alarm
        success_empty — nothing new and nothing wrong
        """
        error_rate = self.errors / max(self.detected, 1)
        if self.errors and (self.ingested == 0 or error_rate > 0.20):
            self.status = "failed"
        elif self.ingested == 0:
            self.status = "success_empty"
        else:
            self.status = "success"
        return self

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
