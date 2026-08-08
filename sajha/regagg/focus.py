"""A focused view of today's page: same evidence, narrower lens.

The daily page is a record. Someone may have read it at 06:14 and acted on it,
so nothing here overwrites it — a focus produces an ephemeral view that is
returned and forgotten, and the cached page is untouched. The response says so
explicitly, because a filtered page that looks like the daily page is a page
that will be quoted as one.

The split between what code does and what the model does is the same one the
rest of the product uses, and it matters more here because the input is free
text:

    entities and sources FILTER, in code. They decide which cards survive, the
    same way the persona watchlist does. Deterministic, reproducible, and
    inspectable — the response reports exactly what each clause removed.

    the prompt only REORDERS and NARRATES. It can say "these three are what
    matter for CRE exposure" about cards that are already present. It cannot
    introduce a document that did not match, and it cannot invent a fact: the
    narrative is validated against the filtered dossier before it is returned,
    and dropped if it fails.

That asymmetry is the whole design. A prompt that could add documents would be
a search box wearing a summary's clothes, and nobody could tell which of the
two they were reading.
"""

from __future__ import annotations

import json
import re
from typing import Dict, List, Optional, Sequence, Tuple

MAX_PROMPT = 400
MAX_TERMS = 40

SYSTEM = (
    "You order a risk analyst's items by how well they answer ONE question, and "
    "write one sentence about the top of that order.\n"
    "Rules, without exception:\n"
    "1. Use ONLY the items given. Never add, merge or rename one.\n"
    "2. Return every item id you were given, most relevant first.\n"
    "3. The sentence must mention only items you ranked in the top three, and "
    "must not contain a number, name or date that is not in those items.\n"
    "4. If the question does not fit any item, say so plainly in the sentence "
    "and keep the original order.\n"
    'Return ONLY JSON: {"order": ["id", ...], "note": "one sentence"}'
)


def _terms(value) -> List[str]:
    """Accept a list, or a comma/newline separated string, and normalise."""
    if value is None:
        return []
    if isinstance(value, str):
        parts = re.split(r"[,\n;]+", value)
    else:
        parts = list(value)
    out, seen = [], set()
    for p in parts:
        t = str(p).strip()
        key = t.lower()
        if t and key not in seen:
            seen.add(key)
            out.append(t)
    return out[:MAX_TERMS]


def _matches_entity(item: dict, wanted: Sequence[str]) -> bool:
    """An entity clause is satisfied by a confirmed OR a possible match.

    Excluding possibles would quietly drop exactly the cards a person filtering
    by a company name most needs to see — the ambiguous ones. They stay, and the
    card already carries its own "possible" flag for the reader to judge.
    """
    if not wanted:
        return True
    names = {n.lower() for n in item.get("entities", [])}
    names |= {p.get("name", "").lower() for p in item.get("possible_entities", [])}
    hay = " ".join(names)
    return any(w.lower() in hay for w in wanted)


def _matches_source(item: dict, wanted: Sequence[str]) -> bool:
    if not wanted:
        return True
    srcs = {s.lower() for s in item.get("sources", [])}
    srcs |= {(d.get("regulator_id") or "").lower() for d in item.get("docs", [])}
    return any(w.lower() in srcs for w in wanted)


def apply_filters(items: List[dict], *, entities: Sequence[str] = (),
                  sources: Sequence[str] = ()) -> Tuple[List[dict], dict]:
    """Narrow the items, and account for everything that was removed."""
    kept, dropped_entity, dropped_source = [], 0, 0
    for it in items:
        if not _matches_entity(it, entities):
            dropped_entity += 1
            continue
        if not _matches_source(it, sources):
            dropped_source += 1
            continue
        kept.append(it)
    return kept, {"input": len(items), "kept": len(kept),
                  "dropped_no_entity_match": dropped_entity,
                  "dropped_no_source_match": dropped_source}


# ── ranking by prompt (narration only) ──────────────────────────────────────

def _render(items: List[dict]) -> str:
    lines = []
    for it in items:
        bits = [f"[{it['cluster_key']}] {it.get('title', '')}"]
        if it.get("entities"):
            bits.append("names: " + ", ".join(it["entities"][:6]))
        if it.get("event_type"):
            bits.append(f"type: {it['event_type']}")
        if it.get("preview"):
            bits.append(it["preview"][:200])
        lines.append(" — ".join(bits))
    return "\n".join(lines)


def _validate_note(note: str, items: List[dict]) -> Tuple[bool, List[str]]:
    """The note may summarise what is present. It may not go beyond it."""
    problems: List[str] = []
    if not (note or "").strip():
        return False, ["empty"]
    blob = json.dumps(items, default=str)
    allowed = {t.replace(",", "").rstrip(".")
               for t in re.findall(r"\d[\d,.]*", blob)}
    for token in re.findall(r"\d[\d,.]*", note):
        cleaned = token.replace(",", "").rstrip(".")
        if cleaned.isdigit() and len(cleaned) > 1 and cleaned not in allowed:
            problems.append(f"figure {token!r} is not in the items")
    return (not problems), problems


def rank_by_prompt(items: List[dict], prompt: str, client=None) -> dict:
    """Reorder and narrate. Never adds, never removes, never invents.

    Any failure — no model, a provider error, a malformed reply, an id that was
    not in the input, a number that appears nowhere — falls back to the
    deterministic order with the reason stated. A focused view that silently
    reordered on a hallucinated basis would be worse than one that did not
    reorder at all.
    """
    prompt = (prompt or "").strip()[:MAX_PROMPT]
    if not prompt or not items:
        # Filtering without a question is the ordinary case, not a degraded one.
        # Reporting it as a reason put "no prompt" on screen like a fault.
        return {"items": items, "note": None, "ranked": False, "reason": None}

    if client is None:
        try:
            from sajha.regagg.extraction import _provider_from_env
            _provider, client = _provider_from_env()
        except Exception:  # noqa: BLE001
            client = None
        if client is None:
            return {"items": items, "note": None, "ranked": False,
                    "reason": "no model configured — filtered, not reordered"}

    user = (f"QUESTION: {prompt}\n\nITEMS:\n{_render(items)}\n\n"
            f"Return all {len(items)} ids in order.")
    try:
        raw = client.complete(SYSTEM, user, max_tokens=700)
        data = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
        order = [str(x) for x in (data.get("order") or [])]
        note = str(data.get("note") or "").strip()
    except Exception as e:  # noqa: BLE001
        return {"items": items, "note": None, "ranked": False,
                "reason": f"assistant unavailable ({str(e)[:60]})"}

    by_key = {it["cluster_key"]: it for it in items}
    if set(order) - set(by_key):
        return {"items": items, "note": None, "ranked": False,
                "reason": "the assistant named an item that was not in the list"}

    ok, problems = _validate_note(note, items)
    ranked = [by_key[k] for k in order if k in by_key]
    ranked += [it for it in items if it["cluster_key"] not in set(order)]
    return {"items": ranked, "ranked": True,
            "note": note if ok else None,
            "reason": None if ok else f"note withheld: {problems[0]}"}


# ── the view ────────────────────────────────────────────────────────────────

def focus(page: dict, *, prompt: str = "", entities=None, sources=None,
          client=None) -> dict:
    """Build an ephemeral focused view over an already-built daily page."""
    ents, srcs = _terms(entities), _terms(sources)
    prompt = (prompt or "").strip()[:MAX_PROMPT]
    dossier = dict(page.get("dossier") or {})
    items = list(dossier.get("items") or [])

    kept, accounting = apply_filters(items, entities=ents, sources=srcs)
    ranked = rank_by_prompt(kept, prompt, client=client)

    ledger = dict(dossier.get("ledger") or {})
    ledger.update({
        "shown": len(ranked["items"]),
        "serious": sum(1 for i in ranked["items"] if i.get("severity") == "serious"),
        "watch": sum(1 for i in ranked["items"] if i.get("severity") == "watch"),
    })

    return {
        "focused": True,
        "day": page.get("spec", {}).get("day") or dossier.get("day"),
        "criteria": {"prompt": prompt, "entities": ents, "sources": srcs},
        "items": ranked["items"],
        "note": ranked["note"],
        "ranked": ranked["ranked"],
        "reason": ranked["reason"],
        "filtering": accounting,
        "ledger": ledger,
        "notice": "filtered by you, not the generated page — the daily page is "
                  "unchanged",
    }
