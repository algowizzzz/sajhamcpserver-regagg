"""
Distillation: a day's corpus -> the handful of items THIS persona must see.

Entirely deterministic. Selection is where a miss hurts most, so selection is
the part that must be provable: run it twice on the same day and it returns the
same items, forever. The LLM (if any) only narrates what this module chose.

Every run emits a coverage ledger — matched / shown / quiet / suppressed —
whose counts must reconcile. Silence is reported as a number, never implied.
"""

from __future__ import annotations

import re
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List, Optional

from sqlalchemy import func, or_, select

from sajha.regagg.extraction import EntityIndex, classify_event, normalize_name
from sajha.regagg.matching import WatchlistMatcher
from sajha.regagg.models import (Document, DocumentVersion, Persona,
                                 PersonaEntity, Regulator)

# Topic weights a persona inherits unless it overrides them (credit lens).
DEFAULT_WEIGHTS = {"credit_event": 60, "ccr_signal": 50, "regulatory": 40,
                   "rates": 35, "guidance": 25, "deal": 20, "operations": 18,
                   "general": 5}
# a persona may phrase its weights in business terms; map them onto event types
WEIGHT_ALIASES = {"credit": "credit_event", "ccr": "ccr_signal",
                  "counterparty": "ccr_signal", "rules": "regulatory"}

HOME_MARKET_BONUS = {"CA": 6, "US": 3}
SERIOUS_DEFAULT = 50
# how much a topic-only match is discounted against a named-entity match
TOPIC_ONLY_DAMPENER = 0.55


def _weights(persona_config: dict) -> Dict[str, int]:
    out = dict(DEFAULT_WEIGHTS)
    for k, v in ((persona_config.get("salience") or {}).get("topic_weights") or {}).items():
        try:
            out[WEIGHT_ALIASES.get(str(k).lower(), str(k).lower())] = int(v)
        except (TypeError, ValueError):
            continue
    return out


def _cluster_key(title: str, entities: List[str] = (), event_type: str = "") -> str:
    """Same event from several wires -> one item.

    Keyed on WHO and WHAT rather than wording: two wires describing the same
    company's creditor protection use different headlines ("Meal kit company
    Goodfood…" vs "Montreal's Goodfood…"), so a word-overlap key left them as
    separate items and the corroboration count — the thing that separates a
    real event from chatter — always read 1. When no watched entity is named,
    fall back to the headline's significant words.
    """
    if entities:
        return f"{'|'.join(sorted(normalize_name(e) for e in entities))}::{event_type}"
    words = [w for w in re.findall(r"[a-z0-9]+", (title or "").lower())
             if len(w) > 3][:12]
    return " ".join(sorted(set(words))[:8])


def _extraction_of(doc) -> dict:
    """Read the stored extraction, computing a cheap one if ingestion predates
    the extraction stage (so an upgraded install still works on old rows)."""
    ex = getattr(doc, "extraction", None)
    if isinstance(ex, dict) and ex.get("event_type"):
        return ex
    etype, subtype, matched = classify_event(doc.title or "")
    return {"entities": [], "event_type": etype, "event_subtype": subtype,
            "severity_signals": [], "matched_phrase": matched,
            "backend": "on_read", "version": "0"}


def _attach_previews(items: List[dict], regs: dict) -> None:
    """Give each card the opening of its own top document.

    Only the cards that will be shown, and only their first document — the
    dossier is cached on the page, so previewing all six documents of twenty
    clusters would multiply the stored page for text nobody sees.

    The lane comes from the source's category, not the persona's: a preview of
    a news story is the publisher's feed summary and may never be the article
    body, and that rule follows the document rather than the reader.
    """
    from sajha.regagg import excerpt as _x
    try:
        from sajha.regagg import runtime
        storage = runtime.get_storage()
    except Exception:  # noqa: BLE001 — previews are never worth an outage
        return
    for item in items:
        docs = item.get("docs") or []
        if not docs:
            continue
        top = docs[0]
        lane = getattr(regs.get(top.get("regulator_id")), "category", "regulatory")
        text = _x.for_prefix(storage, top.get("s3_prefix"),
                             title=top.get("title") or item.get("title") or "",
                             lane=lane)
        if text:
            item["preview"] = text
            item["preview_source"] = top.get("source") or top.get("regulator_id")
            item["preview_kind"] = ("publisher summary" if lane == "news"
                                    else "document opening")


def build_dossier(session, persona: Persona, day: Optional[str] = None,
                  lookback_days: int = 1, now: Optional[datetime] = None,
                  max_items: Optional[int] = None) -> dict:
    """Everything the composer is allowed to talk about, and the ledger."""
    now = now or datetime.now(timezone.utc)
    day = day or now.date().isoformat()
    cfg = persona.config or {}
    scope = cfg.get("scope") or {}
    salience = cfg.get("salience") or {}
    weights = _weights(cfg)
    serious_at = int(salience.get("serious_threshold") or SERIOUS_DEFAULT)
    min_corroboration = int(salience.get("min_corroboration") or 1)
    cap = int(max_items or (cfg.get("presentation") or {}).get("max_items") or 20)

    watch_names = [c for (c,) in session.execute(
        select(PersonaEntity.canonical).where(
            PersonaEntity.persona_id == persona.persona_id)).all()]
    index = EntityIndex(watch_names)
    matcher = WatchlistMatcher(watch_names)
    total_watched = len(watch_names)

    regs = {r.regulator_id: r for r in session.scalars(select(Regulator)).all()}
    lane_ids = [rid for rid, r in regs.items()
                if getattr(r, "category", "regulatory") == ("news" if persona.lane == "news"
                                                            else "regulatory")]

    # the day's arrivals in this lane
    day_col = func.coalesce(Document.published_date, func.date(Document.ingested_at))
    since = (datetime.fromisoformat(day) - timedelta(days=lookback_days - 1)).date()
    docs = session.scalars(
        select(Document).where(Document.regulator_id.in_(lane_ids or [""]),
                               day_col >= since.isoformat(),
                               day_col <= day)).all()

    families = [f.lower() for f in (scope.get("rule_families") or [])]
    classes = [c.lower() for c in (scope.get("classes") or [])]
    topics_wanted = {str(t).lower() for t in (scope.get("topics") or [])}

    scanned = len(docs)
    clusters: Dict[str, dict] = {}
    for d in docs:
        ex = _extraction_of(d)
        text = f"{d.title or ''}"
        hits = ex.get("entities") or index.find(text)
        matched_names, possible_names = [], []
        for h in hits:
            written = h.get("canonical", "")
            hit, confidence, reason = matcher.match(written)
            if not hit:
                continue
            record = {**h, "canonical": hit, "extracted_as": written,
                      "match_confidence": confidence, "match_reason": reason}
            # An ambiguous name is neither dropped nor asserted: it is shown
            # as "possible mention — verify", which is the only honest answer
            # when the text cannot settle it.
            (matched_names if confidence == "confirmed" else possible_names).append(record)
        fam_hit = [f for f in families if f.replace("-", " ") in text.lower()
                   or f in (d.reference_number or "").lower()]
        class_hit = [c for c in classes if c in text.lower()]
        etype = ex.get("event_type", "general")

        # is this item in scope at all?
        in_scope = bool(matched_names or possible_names or fam_hit or class_hit)
        if not in_scope and topics_wanted and etype in topics_wanted:
            in_scope = True
        if not in_scope and persona.lane == "regulatory" and families == []:
            in_scope = d.materiality_band in ("Critical", "High")
        if not in_scope:
            continue

        key = _cluster_key(d.title,
                           [h["canonical"] for h in matched_names],
                           etype) or d.doc_id
        c = clusters.setdefault(key, {
            "cluster_key": key, "title": d.title, "docs": [], "sources": set(),
            "entities": {}, "event_type": etype,
            "event_subtype": ex.get("event_subtype"),
            "severity_signals": list(ex.get("severity_signals") or []),
            "rule_families": [], "classes": [], "materiality": 0, "possible": {},
            "regulator_id": d.regulator_id, "jurisdiction":
                getattr(regs.get(d.regulator_id), "jurisdiction", ""),
            "first_seen": str(d.ingested_at or ""), "day": day,
        })
        c["docs"].append({"regulator_id": d.regulator_id, "doc_id": d.doc_id,
                          "title": d.title, "url": d.source_url,
                          "source": getattr(regs.get(d.regulator_id), "name", d.regulator_id),
                          "published": str(d.published_date or ""),
                          # carried so a preview can be read later without a
                          # second pass over the documents table
                          "s3_prefix": d.s3_prefix})
        c["sources"].add(d.regulator_id)
        for h in matched_names:
            c["entities"][h["canonical"]] = h
        for h in possible_names:
            if h["canonical"] not in c["entities"]:
                c["possible"][h["canonical"]] = h
        c["rule_families"] = sorted(set(c["rule_families"]) | set(fam_hit))
        c["classes"] = sorted(set(c["classes"]) | set(class_hit))
        c["materiality"] = max(c["materiality"], d.materiality_score or 0)
        if etype != "general" and c["event_type"] == "general":
            c["event_type"], c["event_subtype"] = etype, ex.get("event_subtype")

    # score every cluster
    items: List[dict] = []
    for c in clusters.values():
        corroboration = len(c["sources"])
        base = weights.get(c["event_type"], DEFAULT_WEIGHTS["general"])
        # A story that merely belongs to a topic you follow is CONTEXT; a story
        # that names something you are responsible for is an EXCEPTION. Without
        # this, a desk that follows "rates" saw every rates story marked
        # serious — and a page where everything is serious says nothing.
        # Context can still escalate on its own merits (several wires carrying
        # it, or high materiality), which is exactly when it deserves to.
        specific = bool(c["entities"] or c["rule_families"] or c["classes"])
        if not specific:
            base = int(base * TOPIC_ONLY_DAMPENER)
        bonus = HOME_MARKET_BONUS.get(c["jurisdiction"], 0)
        sev = 3 * len(c["severity_signals"])
        corr = 8 * (corroboration - 1)
        rule = 25 if c["rule_families"] else 0
        score = base + bonus + sev + corr + rule + int(0.2 * c["materiality"])
        why = [f"{c['event_type'].replace('_', ' ')} +{base}"
               + ("" if specific else " (topic match, not your names)")]
        if c["entities"]:
            why.append(f"{len(c['entities'])} watched name"
                       f"{'s' if len(c['entities']) > 1 else ''}")
        if c["possible"]:
            why.append(f"{len(c['possible'])} possible mention"
                       f"{'s' if len(c['possible']) > 1 else ''} — verify")
        if c["rule_families"]:
            why.append(f"watched rule ({', '.join(c['rule_families'])}) +{rule}")
        if corroboration > 1:
            why.append(f"{corroboration} sources +{corr}")
        if bonus:
            why.append(f"{c['jurisdiction']} market +{bonus}")
        items.append({
            "cluster_key": c["cluster_key"], "title": c["title"],
            "event_type": c["event_type"], "event_subtype": c["event_subtype"],
            "entities": sorted(c["entities"].keys()),
            "possible_entities": [
                {"name": k, "written": v.get("extracted_as"),
                 "reason": v.get("match_reason")}
                for k, v in sorted(c["possible"].items())],
            "rule_families": c["rule_families"], "classes": c["classes"],
            "corroboration": corroboration, "sources": sorted(c["sources"]),
            "materiality": c["materiality"], "score": score,
            "severity": "serious" if score >= serious_at else "watch",
            "why": "; ".join(why), "docs": c["docs"][:6], "day": c["day"],
        })

    items.sort(key=lambda i: (-i["score"], i["title"] or ""))
    matched_total = len(items)
    below_floor = [i for i in items if i["corroboration"] < min_corroboration]
    keep = [i for i in items if i["corroboration"] >= min_corroboration]
    shown, overflow = keep[:cap], keep[cap:]

    _attach_previews(shown, regs)

    touched = {n for i in shown for n in i["entities"]}
    flagged = {p["name"] for i in shown for p in i.get("possible_entities", [])}
    ledger = {
        "scanned_documents": scanned,
        "watchlist_size": total_watched,
        "matched": matched_total,
        "shown": len(shown),
        "suppressed_below_floor": len(below_floor),
        "suppressed_overflow": len(overflow),
        "quiet_entities": max(total_watched - len(touched), 0),
        "entities_with_events": len(touched),
        "entities_possible": len(flagged - touched),
        "serious": sum(1 for i in shown if i["severity"] == "serious"),
        "watch": sum(1 for i in shown if i["severity"] == "watch"),
    }
    # conservation: nothing may vanish without appearing in a counter
    assert ledger["matched"] == (ledger["shown"] + ledger["suppressed_below_floor"]
                                 + ledger["suppressed_overflow"]), ledger

    return {
        "persona_id": persona.persona_id, "persona_name": persona.name,
        "persona_version": persona.version_n, "lane": persona.lane,
        "day": day, "items": shown, "suppressed": below_floor + overflow,
        "ledger": ledger,
        "rule_families_watched": scope.get("rule_families") or [],
        "generated_from": {"documents": scanned, "clusters": len(clusters)},
    }
