"""
Deterministic (no-LLM) enrichment: reference-number extraction and rule-based
cross-reference edges. Pure regex + corpus lookups — runs inline at ingestion
for every document, independent of any model.

Two jobs:
  1. ``extract_reference_number(title)`` — the regulator's own identifier for
     THIS document (drives stable doc_ids and inventory reconciliation).
  2. ``extract_citations(content)`` — identifiers this document MENTIONS,
     with an edge-type guess (``supersedes`` when the mention sits near
     replace/supersede language, else ``references``).

Patterns cover the regulators in scope; adding one is a table entry, not code.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Optional, Tuple

from sqlalchemy import select

from sajha.regagg import ids
from sajha.regagg.models import Document, DocumentEdge, PendingEdge

# ── reference-number grammars (regulator-agnostic superset) ──────────────────
# (label, compiled regex). Order matters: more specific first.
REF_PATTERNS: List[Tuple[str, re.Pattern]] = [
    ("osfi_guideline", re.compile(r"\bGuideline\s+([A-E]-\d{1,2})\b", re.I)),
    ("osfi_car",       re.compile(r"\bCAR(?:\s+Guideline)?[,\s]+Chapter\s+(\d{1,2})\b", re.I)),
    ("osfi_lar",       re.compile(r"\bLAR(?:\s+Guideline)?[,\s]+Chapter\s+(\d{1,2})\b", re.I)),
    ("frb_sr",         re.compile(r"\bSR\s?(\d{2}-\d{1,3})\b")),
    ("occ_bulletin",   re.compile(r"\bBulletin\s+(\d{4}-\d{1,3})\b", re.I)),
    ("fdic_fil",       re.compile(r"\bFIL-?(\d{1,3}-\d{4})\b", re.I)),
    ("csa_ni",         re.compile(r"\b(?:National Instrument|NI)\s+(\d{2}-\d{3})\b", re.I)),
    ("apra_aps",       re.compile(r"\b((?:APS|CPS|SPS|HPS)\s?\d{3})\b")),
    ("uk_pscp",        re.compile(r"\b((?:PS|CP|SS|FG|DP)\s?\d{1,2}/\d{2})\b")),
    ("eu_rts",         re.compile(r"\b((?:RTS|ITS)\s+\d{4}/\d{1,4})\b", re.I)),
    ("bcbs",           re.compile(r"\b(BCBS\s?\d{1,3})\b", re.I)),
    ("fedreg_doc",     re.compile(r"\b(\d{4}-\d{4,6})\b(?=[^%]*Federal Register)", re.I)),
    ("sec_release",    re.compile(r"\bRelease\s+No\.?\s+(3[34]-\d{4,6})\b", re.I)),
    ("bare_guideline", re.compile(r"^([A-E]-\d{1,2})\b")),   # titles like "B-13 — ..."
]

# words that flip a nearby citation from `references` to `supersedes`
_SUPERSEDE_NEAR = re.compile(
    r"(supersed\w+|replac\w+|rescind\w+|withdraw\w+|repeal\w+)", re.I)
_NEAR_WINDOW = 120  # chars around the match to scan for supersede language


@dataclass
class Citation:
    reference: str
    edge_type: str          # supersedes | references
    context: str


def extract_reference_number(title: str) -> Optional[str]:
    """Regulator's identifier for this document, from its title. None if absent."""
    if not title:
        return None
    for label, pat in REF_PATTERNS:
        m = pat.search(title)
        if m:
            ref = m.group(1)
            if label == "osfi_car":
                return f"CAR-Ch{ref}"
            if label == "osfi_lar":
                return f"LAR-Ch{ref}"
            if label == "frb_sr":
                return f"SR {ref}"
            return ref
    return None


def extract_citations(content: str, own_ref: Optional[str] = None,
                      max_citations: int = 25) -> List[Citation]:
    """Identifiers mentioned in the body, with a supersedes/references guess.
    The document's own reference is excluded."""
    out: List[Citation] = []
    seen = set()
    own_slug = ids.slugify_ref(own_ref) if own_ref else None
    for label, pat in REF_PATTERNS:
        if label in ("fedreg_doc",):        # too noisy for citation mining
            continue
        for m in pat.finditer(content or ""):
            ref = m.group(1)
            if label == "osfi_car":
                ref = f"CAR-Ch{ref}"
            elif label == "osfi_lar":
                ref = f"LAR-Ch{ref}"
            elif label == "frb_sr":
                ref = f"SR {ref}"
            slug = ids.slugify_ref(ref)
            if not slug or slug in seen or slug == own_slug:
                continue
            seen.add(slug)
            # supersede language precedes its object ("supersedes Guideline B-10"),
            # so scan backwards only, and never across a sentence boundary.
            lo = max(0, m.start() - _NEAR_WINDOW)
            before = content[lo:m.start()]
            dot = max(before.rfind("."), before.rfind("\n"))
            if dot >= 0:
                before = before[dot + 1:]
            et = "supersedes" if _SUPERSEDE_NEAR.search(before) else "references"
            ctx = content[max(0, m.start() - 60):m.end() + 60]
            out.append(Citation(reference=ref, edge_type=et, context=ctx.strip()[:200]))
            if len(out) >= max_citations:
                return out
    return out


def apply_rules(session, doc: Document, content: str) -> dict:
    """Inline deterministic pass for one document. Returns a small report.

    * fills ``reference_number`` when the title yields one and none is set,
    * writes edges to corpus docs matched by reference slug,
    * unresolved citations -> reg_pending_edges,
    * a ``supersedes`` edge flips the target's status (spec US-4.3.3).
    """
    report = {"reference_number": None, "edges": 0, "pending": 0}

    ref = extract_reference_number(doc.title or "")
    if ref and not doc.reference_number:
        doc.reference_number = ref
        report["reference_number"] = ref

    for cit in extract_citations(content or "", own_ref=doc.reference_number):
        slug = ids.slugify_ref(cit.reference)
        target = session.scalars(select(Document).where(Document.doc_id == slug)).first()
        if target is None:
            target = session.scalars(select(Document).where(
                Document.reference_number == cit.reference)).first()
        if target is not None and not (target.regulator_id == doc.regulator_id
                                       and target.doc_id == doc.doc_id):
            exists = session.scalars(select(DocumentEdge).where(
                DocumentEdge.from_regulator == doc.regulator_id,
                DocumentEdge.from_doc == doc.doc_id,
                DocumentEdge.to_regulator == target.regulator_id,
                DocumentEdge.to_doc == target.doc_id,
                DocumentEdge.edge_type == cit.edge_type)).first()
            if not exists:
                session.add(DocumentEdge(
                    from_regulator=doc.regulator_id, from_doc=doc.doc_id,
                    to_regulator=target.regulator_id, to_doc=target.doc_id,
                    edge_type=cit.edge_type, confidence=0.8))   # rule-based confidence
                report["edges"] += 1
                if cit.edge_type == "supersedes" and target.status != "superseded":
                    target.status = "superseded"
        else:
            dup = session.scalars(select(PendingEdge).where(
                PendingEdge.from_regulator == doc.regulator_id,
                PendingEdge.from_doc == doc.doc_id,
                PendingEdge.raw_reference == cit.reference)).first()
            if not dup:
                session.add(PendingEdge(
                    from_regulator=doc.regulator_id, from_doc=doc.doc_id,
                    raw_reference=cit.reference, edge_type=cit.edge_type))
                report["pending"] += 1
    return report


def resolve_pending(session) -> int:
    """Nightly-style resolver: retry pending edges against the grown corpus."""
    resolved = 0
    for pe in session.scalars(select(PendingEdge)).all():
        slug = ids.slugify_ref(pe.raw_reference)
        target = session.scalars(select(Document).where(Document.doc_id == slug)).first() \
            or session.scalars(select(Document).where(
                Document.reference_number == pe.raw_reference)).first()
        if target is None:
            pe.attempts += 1
            continue
        exists = session.scalars(select(DocumentEdge).where(
            DocumentEdge.from_regulator == pe.from_regulator,
            DocumentEdge.from_doc == pe.from_doc,
            DocumentEdge.to_regulator == target.regulator_id,
            DocumentEdge.to_doc == target.doc_id,
            DocumentEdge.edge_type == pe.edge_type)).first()
        if not exists:
            session.add(DocumentEdge(
                from_regulator=pe.from_regulator, from_doc=pe.from_doc,
                to_regulator=target.regulator_id, to_doc=target.doc_id,
                edge_type=pe.edge_type, confidence=0.8))
            resolved += 1
        session.delete(pe)
    session.commit()
    return resolved
