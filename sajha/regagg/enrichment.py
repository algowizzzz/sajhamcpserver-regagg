"""
Enrichment pipeline (FR-3 / Feature 4): classify -> summarize -> graph extract.

Each pass returns strict JSON validated by a pydantic schema (1 retry, then the
document is tagged ``enrichment_pending`` and queued for review). Topic tags are
constrained to the controlled taxonomy. A ``supersedes`` edge flips the target
document's status to ``superseded`` (US-4.3).

The LLM backend is abstracted (``LLMBackend``): ``MockLLM`` is deterministic for
tests; ``AnthropicBackend`` (documented) wires the repo's sajha/ai layer in prod.
Reference resolution uses exact (regulator, reference_number) match first, then a
normalized-title match (pg_trgm on Postgres; a portable fallback here), else
``reg_pending_edges`` for later resolution as the corpus grows.
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Dict, List, Optional

import yaml
from pydantic import BaseModel, ValidationError
from sqlalchemy import select

from sajha.regagg.config_models import DOC_TYPES
from sajha.regagg.models import (
    Document, DocumentEdge, DocumentTag, PendingEdge,
)

EDGE_TYPES = ("implements", "supersedes", "interprets", "references", "consults_on")
STATUS_VALUES = ("proposed", "final", "superseded", "withdrawn")


# ── output schemas (strict) ─────────────────────────────────────────────────

class Classification(BaseModel):
    doc_type: str
    topic_tags: List[str] = []
    status: str = "final"


class SummaryOut(BaseModel):
    summary_md: str
    published_date: Optional[str] = None
    effective_date: Optional[str] = None
    comment_deadline: Optional[str] = None


class RefOut(BaseModel):
    raw: str
    edge_type: str
    target_reference: Optional[str] = None
    target_title: Optional[str] = None


class GraphOut(BaseModel):
    references: List[RefOut] = []


# ── LLM backends ────────────────────────────────────────────────────────────

class LLMBackend(ABC):
    @abstractmethod
    def classify(self, content: str, hint: Optional[str]) -> dict: ...
    @abstractmethod
    def summarize(self, content: str) -> dict: ...
    @abstractmethod
    def extract_refs(self, content: str) -> dict: ...


class MockLLM(LLMBackend):
    """Deterministic backend for tests/offline. Reads lightweight markers in the
    content so tests can assert exact behaviour:
        TYPE:<doc_type>            -> classification doc_type
        STATUS:<status>            -> classification status
        keywords cyber/capital/aml/liquidity -> topic tags
        REF:<edge_type>:<reference> -> a cross-reference edge
    """
    KEYWORD_TAGS = {
        "cyber": "cyber_risk", "capital": "capital", "aml": "aml_cft",
        "liquidity": "liquidity", "climate": "climate_risk", "crypto": "crypto_assets",
    }

    def classify(self, content: str, hint: Optional[str]) -> dict:
        m = re.search(r"TYPE:(\w+)", content)
        doc_type = m.group(1) if m else (hint or "announcement")
        s = re.search(r"STATUS:(\w+)", content)
        status = s.group(1) if s else "final"
        tags = sorted({tag for kw, tag in self.KEYWORD_TAGS.items()
                       if kw in content.lower()})
        return {"doc_type": doc_type, "topic_tags": tags, "status": status}

    def summarize(self, content: str) -> dict:
        first = content.strip().splitlines()[0] if content.strip() else ""
        out = {"summary_md": f"Summary: {first[:280]}"}
        for field_name, marker in (("published_date", "PUBLISHED:"),
                                   ("effective_date", "EFFECTIVE:"),
                                   ("comment_deadline", "DEADLINE:")):
            mm = re.search(rf"{marker}(\d{{4}}-\d{{2}}-\d{{2}})", content)
            if mm:
                out[field_name] = mm.group(1)
        return out

    def extract_refs(self, content: str) -> dict:
        refs = [{"raw": f"{et}:{ref}", "edge_type": et, "target_reference": ref}
                for et, ref in re.findall(r"REF:(\w+):([\w\-]+)", content)]
        return {"references": refs}


class AnthropicBackend(LLMBackend):  # pragma: no cover - needs credentials/network
    """Production backend via the repo's sajha/ai layer. Not exercised in tests.

    Each method builds a strict-JSON prompt (taxonomy injected for classify) and
    calls the configured model, returning parsed JSON for schema validation.
    """
    def __init__(self, ai_client=None, taxonomy: Optional[dict] = None):
        self.ai = ai_client
        self.taxonomy = taxonomy or {}

    def _complete_json(self, prompt: str) -> dict:
        import json
        # sajha/ai exposes a chat/completion surface; kept generic here.
        text = self.ai.complete(prompt, response_format="json")  # type: ignore[attr-defined]
        return json.loads(text)

    def classify(self, content: str, hint):
        allowed = self.taxonomy.get("tags", {}).get("topic", [])
        return self._complete_json(
            f"Classify this regulatory document. doc_type in {sorted(DOC_TYPES)}, "
            f"topic tags ONLY from {allowed}. Return JSON "
            f'{{"doc_type","topic_tags","status"}}.\n\n{content[:8000]}')

    def summarize(self, content: str):
        return self._complete_json(
            "Summarize (<=300 words, plain language: what changed, who's affected, "
            'key dates) and extract dates. Return JSON {"summary_md","published_date",'
            '"effective_date","comment_deadline"}.\n\n' + content[:16000])

    def extract_refs(self, content: str):
        return self._complete_json(
            "Extract references to other regulations. Return JSON "
            '{"references":[{"raw","edge_type","target_reference","target_title"}]} '
            f"edge_type in {list(EDGE_TYPES)}.\n\n" + content[:16000])


# ── enricher ────────────────────────────────────────────────────────────────

@dataclass
class EnrichResult:
    doc_id: str
    tags: List[str] = field(default_factory=list)
    status: str = "final"
    edges: int = 0
    pending: int = 0
    enrichment_pending: bool = False
    error: Optional[str] = None


def load_taxonomy(path: str) -> dict:
    return yaml.safe_load(open(path, encoding="utf-8"))


class Enricher:
    def __init__(self, session, storage, llm: LLMBackend, taxonomy: dict):
        self.s = session
        self.st = storage
        self.llm = llm
        self.tax = taxonomy
        self.valid_topics = set(taxonomy.get("tags", {}).get("topic", []))

    def enrich_document(self, doc: Document, default_tags: Optional[List[str]] = None) -> EnrichResult:
        res = EnrichResult(doc_id=doc.doc_id, status=doc.status)
        content = self.st.read_content(doc.s3_prefix) or ""

        # 1 — classify
        cls = self._call(lambda: Classification.model_validate(
            self.llm.classify(content, doc.doc_type)))
        if cls is None:
            return self._mark_pending(doc, res, "classify")
        if cls.doc_type in DOC_TYPES:
            doc.doc_type = cls.doc_type
        if cls.status in STATUS_VALUES:
            doc.status = cls.status
            res.status = cls.status

        # 2 — summarize (+ dates)
        summ = self._call(lambda: SummaryOut.model_validate(self.llm.summarize(content)))
        if summ is None:
            return self._mark_pending(doc, res, "summarize")
        self.st.backend.write_text(f"{doc.s3_prefix}/summary.md", summ.summary_md)
        self._apply_dates(doc, summ)

        # 3 — graph
        graph = self._call(lambda: GraphOut.model_validate(self.llm.extract_refs(content)))
        if graph is None:
            return self._mark_pending(doc, res, "graph")

        # tags = jurisdiction (from config default_tags) + topics (taxonomy-filtered) + status
        tags = set(default_tags or [])
        tags.update(t for t in cls.topic_tags if t in self.valid_topics)
        tags.add(cls.status)
        self._write_tags(doc, tags, default_tags or [])
        res.tags = sorted(tags)

        # edges
        for ref in graph.references:
            if ref.edge_type not in EDGE_TYPES:
                continue
            target = self._resolve(ref)
            if target is not None:
                self._add_edge(doc, target, ref.edge_type, confidence=0.9)
                res.edges += 1
                if ref.edge_type == "supersedes":
                    self._mark_superseded(target)
            else:
                self.s.add(PendingEdge(from_regulator=doc.regulator_id, from_doc=doc.doc_id,
                                       raw_reference=ref.raw, edge_type=ref.edge_type))
                res.pending += 1

        self.s.commit()
        return res

    # ── helpers ─────────────────────────────────────────────────────────────

    def _call(self, fn, retries: int = 1):
        """Call an LLM pass; on invalid JSON retry once, else return None."""
        for attempt in range(retries + 1):
            try:
                return fn()
            except (ValidationError, ValueError, KeyError):
                if attempt >= retries:
                    return None
        return None

    def _mark_pending(self, doc: Document, res: EnrichResult, stage: str) -> EnrichResult:
        self.s.merge(DocumentTag(regulator_id=doc.regulator_id, doc_id=doc.doc_id,
                                 tag="enrichment_pending", source="rule"))
        self.s.commit()
        res.enrichment_pending = True
        res.error = f"{stage} failed schema validation"
        return res

    def _apply_dates(self, doc: Document, summ: SummaryOut) -> None:
        for attr, val in (("published_date", summ.published_date),
                          ("effective_date", summ.effective_date),
                          ("comment_deadline", summ.comment_deadline)):
            if val:
                try:
                    setattr(doc, attr, date.fromisoformat(val))
                except ValueError:
                    pass  # never guess a date

    def _write_tags(self, doc: Document, tags: set, default_tags: List[str]) -> None:
        for tag in tags:
            src = "config" if tag in default_tags else "llm"
            self.s.merge(DocumentTag(regulator_id=doc.regulator_id, doc_id=doc.doc_id,
                                     tag=tag, source=src))

    def _resolve(self, ref: RefOut) -> Optional[Document]:
        if ref.target_reference:
            from sajha.regagg import ids
            slug = ids.slugify_ref(ref.target_reference)
            hit = self.s.scalars(select(Document).where(Document.doc_id == slug)).first()
            if hit:
                return hit
            hit = self.s.scalars(select(Document).where(
                Document.reference_number == ref.target_reference)).first()
            if hit:
                return hit
        if ref.target_title:
            norm = ref.target_title.strip().lower()
            for d in self.s.scalars(select(Document)).all():
                if norm and norm in (d.title or "").lower():
                    return d
        return None

    def _add_edge(self, src: Document, dst: Document, edge_type: str, confidence: float):
        existing = self.s.scalars(select(DocumentEdge).where(
            DocumentEdge.from_regulator == src.regulator_id, DocumentEdge.from_doc == src.doc_id,
            DocumentEdge.to_regulator == dst.regulator_id, DocumentEdge.to_doc == dst.doc_id,
            DocumentEdge.edge_type == edge_type)).first()
        if existing:
            return
        self.s.add(DocumentEdge(
            from_regulator=src.regulator_id, from_doc=src.doc_id,
            to_regulator=dst.regulator_id, to_doc=dst.doc_id,
            edge_type=edge_type, confidence=confidence))

    def _mark_superseded(self, target: Document) -> None:
        target.status = "superseded"
        self.s.merge(DocumentTag(regulator_id=target.regulator_id, doc_id=target.doc_id,
                                 tag="superseded", source="rule"))
