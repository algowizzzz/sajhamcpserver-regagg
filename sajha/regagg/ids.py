"""
Deterministic identifiers & hashing for the corpus.

Everything here is a pure function of its inputs — no clocks except where a
timestamp is explicitly requested — so ingestion is reproducible and testable.
"""

from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from typing import Optional

VERSION_TS_FORMAT = "%Y-%m-%dT%H-%M-%SZ"  # UTC basic, filesystem-safe


def content_hash(markdown: str) -> str:
    """sha256 of normalized markdown, prefixed. Stable change-detection key."""
    h = hashlib.sha256(markdown.encode("utf-8")).hexdigest()
    return f"sha256:{h}"


def short_hash(text: str, n: int = 16) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:n]


_SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify_ref(reference_number: str) -> str:
    """Turn a regulator reference (e.g. 'Guideline B-13') into a stable id token."""
    s = _SLUG_RE.sub("-", reference_number.strip().lower()).strip("-")
    return s or ""


def assign_doc_id(reference_number: Optional[str], content_hash_value: str) -> str:
    """doc_id = regulator's own reference number when available, else first 16 hex
    of the content hash (US-2.2)."""
    if reference_number:
        slug = slugify_ref(reference_number)
        if slug:
            return slug
    digest = content_hash_value.split(":", 1)[-1]
    return digest[:16]


def stable_doc_id(reference_number: Optional[str], url: str,
                  existing: Optional[str] = None) -> str:
    """Identity of a *document*, stable across content changes (so a revision
    becomes version N+1 of the same doc, not a new doc).

    Priority: regulator's reference number -> the doc_id already mapped to this
    URL in seen_urls -> a hash of the URL. NB: unlike the handover's US-2.2
    literal wording we do NOT fall back to the *content* hash — that changes on
    every edit and would break versioning. The URL is the stable key; content
    hash remains the change-detection signal.
    """
    if reference_number:
        slug = slugify_ref(reference_number)
        if slug:
            return slug
    if existing:
        return existing
    return short_hash(url)


def now_version_ts(dt: Optional[datetime] = None) -> str:
    """Version timestamp for archive folder names. Pass dt for determinism."""
    dt = dt or datetime.now(timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).strftime(VERSION_TS_FORMAT)


def make_run_id(logical_date: str, regulator_id: str, short: str) -> str:
    """runs.run_id = {date}_{regulator}_{short}."""
    return f"{logical_date}_{regulator_id}_{short}"


def published_year(published_date, ingested: Optional[datetime] = None) -> int:
    """Year bucket for storage layout: published year, fallback ingestion year."""
    if published_date is not None:
        return published_date.year
    return (ingested or datetime.now(timezone.utc)).year
