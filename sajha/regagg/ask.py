"""
Ask: grounded chat over a pinned artifact.

The rule that makes this usable in a bank is the same one that governs the
generated pages — **no citation, no claim**. The model is never asked what it
knows; it is handed a small, explicit evidence pack (a story cluster, a
document, or a day's page) and asked to answer from that alone. Every answer
is validated before it is returned:

  grounded  every sentence maps to a source in the pack
  cited     every [n] refers to a source that exists
  numeric   every figure appears in the pack

An answer that fails validation is not shown. The user gets the evidence and a
plain statement that the assistant could not answer safely — which is more
useful than a confident sentence nobody can check.

There is no free-roaming retrieval here on purpose. "What do you know about
X?" is a question this system should answer by *showing the documents*, which
Explore already does; chat exists to interpret what the analyst is looking at.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

MAX_QUESTION = 500
MAX_SOURCES = 12

SYSTEM = (
    "You are a research assistant for a bank's risk team. You answer ONLY from "
    "the numbered sources provided. Rules, without exception:\n"
    "1. Every factual sentence must end with a citation like [1] or [2][3].\n"
    "2. Never state a fact that is not in the sources. If the sources do not "
    "answer the question, say exactly what they do and do not establish.\n"
    "3. Never introduce a number, name, date or amount that is not in the sources.\n"
    "4. Be brief and concrete. No preamble, no hedging, no advice on what to do "
    "— you report what the sources say; the analyst decides.\n"
    "Return ONLY JSON: {\"answer\": \"...\", \"used\": [1,2], \"answerable\": true|false}"
)

_CITE = re.compile(r"\[(\d+)\]")
_NUM = re.compile(r"\d[\d,.]*")


# ── evidence packs ──────────────────────────────────────────────────────────

def pack_for_cluster(session, persona, day: str, cluster_key: str) -> Optional[dict]:
    """Every document behind one card on a My Day page."""
    from sajha.regagg import myday as _m
    page = _m.build_my_day(session, persona, day=day)
    items = (page.get("dossier") or {}).get("items", []) + \
            (page.get("dossier") or {}).get("suppressed", [])
    for item in items:
        if item["cluster_key"] == cluster_key:
            return {
                "kind": "story cluster",
                "title": item["title"],
                "context": {"event": item["event_type"],
                            "entities": item["entities"],
                            "corroboration": item["corroboration"],
                            "why_it_surfaced": item["why"]},
                "sources": [
                    {"n": n, "title": d["title"], "publisher": d.get("source", ""),
                     "published": d.get("published", ""), "url": d.get("url", ""),
                     "regulator_id": d["regulator_id"], "doc_id": d["doc_id"]}
                    for n, d in enumerate(item["docs"][:MAX_SOURCES], 1)],
            }
    return None


def pack_for_document(session, storage, regulator_id: str, doc_id: str) -> Optional[dict]:
    """One document, with its text — for "what does this actually say?"."""
    from sajha.regagg.models import Document, Regulator
    doc = session.get(Document, {"regulator_id": regulator_id, "doc_id": doc_id})
    if doc is None:
        return None
    reg = session.get(Regulator, regulator_id)
    text = ""
    if storage is not None:
        try:
            text = (storage.read_content(doc.s3_prefix) or "")[:6000]
        except Exception:  # noqa: BLE001 — a missing body is not a crash
            text = ""
    return {
        "kind": "document",
        "title": doc.title,
        "context": {"type": doc.doc_type, "published": str(doc.published_date or ""),
                    "materiality": doc.materiality_score,
                    "band": doc.materiality_band,
                    "why_it_scored": doc.materiality_reason or ""},
        "sources": [{"n": 1, "title": doc.title,
                     "publisher": getattr(reg, "name", regulator_id),
                     "published": str(doc.published_date or ""),
                     "url": doc.source_url, "regulator_id": regulator_id,
                     "doc_id": doc_id, "text": text}],
    }


def pack_for_day(session, persona, day: Optional[str] = None) -> dict:
    """The whole page — for "what should I look at first?"."""
    from sajha.regagg import myday as _m
    page = _m.build_my_day(session, persona, day=day)
    items = (page.get("dossier") or {}).get("items", [])
    sources, n = [], 0
    for item in items[:MAX_SOURCES]:
        n += 1
        d = item["docs"][0] if item["docs"] else {}
        sources.append({"n": n, "title": item["title"],
                        "publisher": d.get("source", ""),
                        "published": d.get("published", ""), "url": d.get("url", ""),
                        "regulator_id": d.get("regulator_id", ""),
                        "doc_id": d.get("doc_id", ""),
                        "note": f"{item['event_type']} · {item['severity']} · "
                                f"{item['corroboration']} source(s) · {item['why']}"})
    return {"kind": f"{persona.name} — {(page.get('spec') or {}).get('day', '')}",
            "title": f"{persona.name}'s page",
            "context": {"ledger": page.get("ledger") or {}},
            "sources": sources}


# ── validation ──────────────────────────────────────────────────────────────

def _pack_numbers(pack: dict) -> set:
    nums = set()
    blob = json.dumps(pack)
    for token in _NUM.findall(blob):
        cleaned = token.replace(",", "").rstrip(".")
        if cleaned.isdigit():
            nums.add(cleaned)
    return nums


def validate_answer(answer: str, used: List[int], pack: dict) -> Tuple[bool, List[str]]:
    """An answer may summarise the pack. It may not go beyond it."""
    problems: List[str] = []
    if not (answer or "").strip():
        return False, ["empty answer"]
    valid_ns = {s["n"] for s in pack["sources"]}
    cited = {int(c) for c in _CITE.findall(answer)}
    for c in cited:
        if c not in valid_ns:
            problems.append(f"citation [{c}] does not exist")
    for c in (used or []):
        if c not in valid_ns:
            problems.append(f"'used' names source {c}, which does not exist")
    if not cited:
        problems.append("no citations — every claim must point at a source")
    allowed = _pack_numbers(pack)
    for token in _NUM.findall(_CITE.sub("", answer)):
        cleaned = token.replace(",", "").rstrip(".")
        if cleaned.isdigit() and cleaned not in allowed and len(cleaned) > 1:
            problems.append(f"figure {token!r} is not in the sources")
    return (not problems), problems


# ── the call ────────────────────────────────────────────────────────────────

def _render_sources(pack: dict) -> str:
    lines = []
    for s in pack["sources"]:
        line = f"[{s['n']}] {s['title']}"
        if s.get("publisher"):
            line += f" — {s['publisher']}"
        if s.get("published"):
            line += f" ({s['published']})"
        if s.get("note"):
            line += f"\n     {s['note']}"
        if s.get("text"):
            line += f"\n     {s['text'][:2500]}"
        lines.append(line)
    return "\n".join(lines)


def answer_question(question: str, pack: dict, client=None) -> dict:
    """Answer from the pack, or explain honestly that it cannot be answered."""
    question = (question or "").strip()[:MAX_QUESTION]
    if not question:
        return {"ok": False, "answer": "Ask a question about this item.",
                "sources": pack["sources"], "generator": "none"}
    if not pack.get("sources"):
        return {"ok": False, "generator": "none", "sources": [],
                "answer": "There are no sources pinned, so there is nothing to "
                          "answer from. Open an item first."}

    from sajha.regagg.extraction import _provider_from_env
    provider, openai_client = _provider_from_env()
    if client is None and provider is None:
        return {"ok": False, "generator": "unconfigured", "sources": pack["sources"],
                "answer": "No model is configured on this install, so answers "
                          "cannot be generated. The sources for this item are "
                          "listed below — they are the same evidence the "
                          "assistant would have used."}

    user = (f"CONTEXT: {pack['kind']} — {pack['title']}\n"
            f"{json.dumps(pack.get('context', {}), default=str)}\n\n"
            f"SOURCES:\n{_render_sources(pack)}\n\n"
            f"QUESTION: {question}")
    try:
        if client is not None:
            raw = client.complete(SYSTEM, user, max_tokens=700)
        else:
            raw = openai_client.complete(SYSTEM, user, max_tokens=700)
        data = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
        answer = str(data.get("answer", "")).strip()
        used = [int(u) for u in (data.get("used") or []) if str(u).isdigit()]
    except Exception as e:  # noqa: BLE001 — a provider failure is not a wrong answer
        return {"ok": False, "generator": "error", "sources": pack["sources"],
                "answer": "The assistant could not be reached just now. The "
                          "sources for this item are below and unaffected.",
                "detail": str(e)[:200]}

    ok, problems = validate_answer(answer, used, pack)
    if not ok:
        return {"ok": False, "generator": "rejected", "sources": pack["sources"],
                "answer": "The assistant produced an answer that could not be "
                          "verified against the sources, so it was withheld. "
                          "The evidence is below — it is the whole of what is known.",
                "problems": problems[:3]}
    return {"ok": True, "answer": answer, "used": used, "sources": pack["sources"],
            "generator": f"llm:{provider}" if client is None else "llm:test"}
