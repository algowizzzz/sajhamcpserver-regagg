"""
Epic 5 — enrichment: classification, taxonomy-constrained tags, date extraction,
cross-reference edges (incl. supersedes -> status flip), pending edges, and the
enrichment_pending fallback on invalid LLM output.
"""

from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path

from sajha.regagg.enrichment import (
    Enricher, LLMBackend, MockLLM, load_taxonomy,
)
from sajha.regagg.models import Document, DocumentEdge, DocumentTag, PendingEdge
from sajha.regagg.versioning import CorpusVersioning, IngestInput

REPO = Path(__file__).resolve().parents[2]
TAXONOMY = str(REPO / "config" / "regulators" / "_taxonomy.yaml")
NOW = datetime(2026, 7, 15, 6, 0, tzinfo=timezone.utc)


def _ingest(session, storage, *, doc_type, ref, content, tags=None):
    v = CorpusVersioning(session, storage)
    inp = IngestInput(regulator_id="osfi", doc_type=doc_type, title=f"{ref} title",
                      content_md=content, source_url=f"https://osfi/{ref}",
                      reference_number=ref, tags=tags or [])
    return v.ingest(inp, run_id="r", now=NOW)


def test_enrich_classifies_tags_dates_and_supersedes(session, storage, seed_regulator):
    seed_regulator("osfi", "CA", "sitemap_diff")
    tax = load_taxonomy(TAXONOMY)

    # older doc B-10 (will be superseded)
    _ingest(session, storage, doc_type="guidance", ref="B-10", content="# B-10\nold guidance")
    # new doc B-13 supersedes B-10, cyber topic, dated
    content = ("# B-13 Technology and Cyber Risk\n"
               "TYPE:guidance STATUS:final PUBLISHED:2026-07-15 EFFECTIVE:2027-01-01 "
               "REF:supersedes:B-10 cyber capital text")
    _ingest(session, storage, doc_type="announcement", ref="B-13", content=content,
            tags=["canada", "prudential", "banking"])

    enr = Enricher(session, storage, MockLLM(), tax)
    b13 = session.get(Document, {"regulator_id": "osfi", "doc_id": "b-13"})
    res = enr.enrich_document(b13, default_tags=["canada", "prudential", "banking"])

    # classification corrected announcement -> guidance
    assert b13.doc_type == "guidance" and b13.status == "final"
    # taxonomy-constrained topic tags + config tags + status tag
    assert {"cyber_risk", "capital", "canada", "final"}.issubset(set(res.tags))
    # dates extracted, never guessed
    assert b13.published_date == date(2026, 7, 15)
    assert b13.effective_date == date(2027, 1, 1)
    # supersedes edge created and target flipped
    assert res.edges == 1
    edge = session.query(DocumentEdge).one()
    assert edge.edge_type == "supersedes" and edge.to_doc == "b-10"
    b10 = session.get(Document, {"regulator_id": "osfi", "doc_id": "b-10"})
    assert b10.status == "superseded"
    # config-sourced tag recorded with source='config'
    canada_tag = session.query(DocumentTag).filter_by(doc_id="b-13", tag="canada").one()
    assert canada_tag.source == "config"


def test_unresolved_reference_goes_to_pending_edges(session, storage, seed_regulator):
    seed_regulator("osfi", "CA", "sitemap_diff")
    tax = load_taxonomy(TAXONOMY)
    _ingest(session, storage, doc_type="guidance", ref="B-20",
            content="# B-20\nREF:references:NONEXISTENT-99 liquidity")
    enr = Enricher(session, storage, MockLLM(), tax)
    doc = session.get(Document, {"regulator_id": "osfi", "doc_id": "b-20"})
    res = enr.enrich_document(doc)
    assert res.pending == 1 and res.edges == 0
    pe = session.query(PendingEdge).one()
    assert pe.edge_type == "references" and "NONEXISTENT-99" in pe.raw_reference


def test_invalid_llm_output_marks_enrichment_pending(session, storage, seed_regulator):
    seed_regulator("osfi", "CA", "sitemap_diff")
    tax = load_taxonomy(TAXONOMY)
    _ingest(session, storage, doc_type="guidance", ref="B-30", content="# B-30\ntext")

    class BadLLM(LLMBackend):
        def classify(self, content, hint):
            return {"topic_tags": "not-a-list"}  # invalid -> ValidationError
        def summarize(self, content):
            return {"summary_md": "x"}
        def extract_refs(self, content):
            return {"references": []}

    enr = Enricher(session, storage, BadLLM(), tax)
    doc = session.get(Document, {"regulator_id": "osfi", "doc_id": "b-30"})
    res = enr.enrich_document(doc)
    assert res.enrichment_pending
    assert session.query(DocumentTag).filter_by(doc_id="b-30", tag="enrichment_pending").count() == 1
