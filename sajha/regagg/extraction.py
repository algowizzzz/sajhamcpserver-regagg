"""
Ingest-time understanding: read each document once, for everyone.

Two backends behind one interface:

  DeterministicExtractor  always available, no key, no cost. Event typing by
                          phrase rules; entity spotting by n-gram lookup
                          against the union of all watchlists.
  LLMExtractor            used when ANTHROPIC_API_KEY is set. Resolves oblique
                          references ("the Montreal meal-kit maker") that no
                          keyword list can catch, and types events by meaning.

Whichever runs, the OUTPUT SHAPE IS IDENTICAL and is stored on the document, so
the persona join downstream never knows or cares which produced it. The
extraction records which backend and model version wrote it — an extraction you
cannot attribute is an extraction you cannot defend.
"""

from __future__ import annotations

import json
import os
import re
from typing import Dict, Iterable, List, Optional

# ── event vocabulary ────────────────────────────────────────────────────────
# Ordered by credit impact: the first rule that matches wins, so "creditor
# protection" beats a passing mention of "shares".

EVENT_RULES = [
    ("credit_event", "creditor_protection",
     ["creditor protection", "chapter 11", "chapter 7", "ccaa", "administration",
      "receivership", "insolven", "bankrupt", "liquidation", "wind-up"]),
    ("credit_event", "default",
     ["defaults on", "missed payment", "missed a payment", "payment default",
      "fails to pay", "debt restructuring", "restructure its debt", "distressed exchange"]),
    ("credit_event", "downgrade",
     ["downgrade", "cut to junk", "junk status", "negative outlook", "credit watch",
      "rating cut", "cuts rating"]),
    ("credit_event", "upgrade", ["upgrade", "raises rating", "positive outlook"]),
    ("ccr_signal", "counterparty_stress",
     ["hedge fund", "leveraged", "margin call", "collateral call", "clearing member",
      "prime broker", "counterparty risk", "fund meltdown", "fund collapse"]),
    ("rates", "policy",
     ["rate hike", "rate cut", "interest rate", "policy rate", "rate decision",
      "monetary policy", "inflation", "federal reserve", "central bank",
      "bank of canada", "bond yield", "yield curve"]),
    ("guidance", "outlook",
     ["cuts guidance", "lowers guidance", "raises guidance", "profit warning",
      "outlook", "forecast", "warns on"]),
    ("deal", "m_and_a",
     ["acquisition", "acquires", "merger", "takeover", "buyout", "to buy",
      "stake in", "ipo", "spin-off", "divest"]),
    ("regulatory", "enforcement",
     ["fine", "penalty", "sanction", "enforcement action", "consent order",
      "settlement with", "charged with", "probe", "investigation"]),
    ("operations", "disruption",
     ["strike", "work stoppage", "outage", "recall", "shutdown", "layoff",
      "job cuts", "closes plant"]),
]

# words that make a headline materially heavier regardless of type
SEVERITY_TERMS = ["granted", "court", "filed", "collapse", "halt", "emergency",
                  "unprecedented", "record", "surge", "plunge", "slump", "crisis"]

_WORD = re.compile(r"[A-Za-z0-9&.'-]+")
MAX_NGRAM = 5


def normalize_name(name: str) -> str:
    """Fold a company name to its comparable core: case, punctuation and the
    corporate suffixes that differ between how a watchlist and a newsroom
    write the same company."""
    s = (name or "").lower().strip()
    s = re.sub(r"[^\w\s&-]", " ", s)
    s = re.sub(r"\b(inc|corp|corporation|co|ltd|limited|llc|lp|plc|sa|nv|ag|"
               r"group|holdings|holding|company|the)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


class EntityIndex:
    """N-gram lookup over every watchlist name in the system.

    Scanning 6,000 names against each headline is 3.6M substring tests a day;
    tokenising the headline and looking up its n-grams is a few hundred dict
    hits. Cost is a function of the TEXT, not of how many names are watched —
    which is why a 6,000-name book costs the same as a 10-name one.
    """

    def __init__(self, names: Iterable[str] = ()):
        self._by_norm: Dict[str, str] = {}
        for n in names:
            self.add(n)

    def add(self, name: str) -> None:
        norm = normalize_name(name)
        if norm and len(norm) > 2:          # 1-2 char "names" match everything
            self._by_norm.setdefault(norm, name)

    def __len__(self) -> int:
        return len(self._by_norm)

    def find(self, text: str) -> List[dict]:
        """Every watchlist name appearing in the text, longest match first."""
        tokens = _WORD.findall((text or "").lower())
        if not tokens or not self._by_norm:
            return []
        hits: Dict[str, dict] = {}
        for size in range(min(MAX_NGRAM, len(tokens)), 0, -1):
            for i in range(len(tokens) - size + 1):
                gram = normalize_name(" ".join(tokens[i:i + size]))
                canonical = self._by_norm.get(gram)
                if canonical and canonical not in hits:
                    hits[canonical] = {"canonical": canonical,
                                       "as_written": " ".join(tokens[i:i + size]),
                                       "confidence": "high" if size > 1 else "medium"}
        return list(hits.values())


def classify_event(text: str) -> tuple:
    low = (text or "").lower()
    for etype, subtype, phrases in EVENT_RULES:
        for p in phrases:
            if p in low:
                return etype, subtype, p
    return "general", None, None


def severity_signals(text: str) -> List[str]:
    low = (text or "").lower()
    return [t for t in SEVERITY_TERMS if t in low]


class DeterministicExtractor:
    """No key, no cost, no network — and reproducible forever."""

    backend = "deterministic"
    version = "1"

    def __init__(self, index: Optional[EntityIndex] = None):
        self.index = index or EntityIndex()

    def extract(self, title: str, summary: str = "") -> dict:
        text = f"{title or ''} {summary or ''}".strip()
        etype, subtype, matched = classify_event(text)
        return {
            "entities": self.index.find(text),
            "event_type": etype, "event_subtype": subtype,
            "severity_signals": severity_signals(text),
            "matched_phrase": matched,
            "backend": self.backend, "version": self.version,
        }


class LLMExtractor:
    """Reads the headline the way an analyst would. Falls back, never fails.

    The deterministic result is computed first and returned whenever the model
    is unavailable, errors, or answers with something that does not fit the
    schema — the pipeline must never stall on a provider.
    """

    backend = "llm"

    PROMPT = (
        "You extract structured facts from a financial news headline for a bank's "
        "credit risk team. Return ONLY JSON with keys: entities (list of "
        '{"canonical": company name as normally written, "as_written": the exact '
        'phrase in the text, "confidence": high|medium}), event_type (one of '
        "credit_event, ccr_signal, rates, guidance, deal, regulatory, operations, "
        "general), event_subtype (short snake_case or null), severity_signals "
        "(list of short phrases). Name only companies that are the SUBJECT of the "
        "story. If none, return an empty list. No commentary."
    )

    def __init__(self, index: Optional[EntityIndex] = None, model: Optional[str] = None,
                 client=None):
        self.fallback = DeterministicExtractor(index)
        self.model = model or os.getenv("REGAGG_EXTRACT_MODEL", "claude-haiku-4-5-20251001")
        self._client = client
        self.version = self.model

    def _get_client(self):
        if self._client is None:
            import anthropic          # imported lazily: optional dependency
            self._client = anthropic.Anthropic()
        return self._client

    def extract(self, title: str, summary: str = "") -> dict:
        base = self.fallback.extract(title, summary)
        text = f"{title or ''}\n{summary or ''}".strip()
        if not text:
            return base
        try:
            resp = self._get_client().messages.create(
                model=self.model, max_tokens=400, system=self.PROMPT,
                messages=[{"role": "user", "content": text}])
            raw = "".join(getattr(b, "text", "") for b in resp.content)
            data = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
        except Exception:  # noqa: BLE001 — provider down must not stop ingestion
            base["llm_error"] = True
            return base

        ents = []
        for e in (data.get("entities") or []):
            if isinstance(e, dict) and e.get("canonical"):
                ents.append({"canonical": str(e["canonical"])[:255],
                             "as_written": str(e.get("as_written", ""))[:255],
                             "confidence": e.get("confidence", "medium")})
        return {
            "entities": ents or base["entities"],
            "event_type": data.get("event_type") or base["event_type"],
            "event_subtype": data.get("event_subtype") or base["event_subtype"],
            "severity_signals": data.get("severity_signals") or base["severity_signals"],
            "matched_phrase": base.get("matched_phrase"),
            "backend": self.backend, "version": self.version,
        }


def get_extractor(index: Optional[EntityIndex] = None):
    """LLM when a key is configured, deterministic otherwise — same shape."""
    if os.getenv("ANTHROPIC_API_KEY"):
        return LLMExtractor(index)
    return DeterministicExtractor(index)


def build_index_from_watchlists(session) -> EntityIndex:
    """Every name any persona watches, in one index (extraction is shared)."""
    from sqlalchemy import select
    from sajha.regagg.models import PersonaEntity
    names = [c for (c,) in session.execute(select(PersonaEntity.canonical)).all()]
    return EntityIndex(names)
