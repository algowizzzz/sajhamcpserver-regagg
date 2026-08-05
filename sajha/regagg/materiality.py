"""
Materiality scoring — not every change deserves equal attention.

A new capital rule from our primary prudential regulator and a press release
about office closures are both "changes"; only one should reach an analyst's
morning queue at the top. This module scores each document 0-100 and bands it
Critical → Informational.

Design constraints (deliberate):
  * DETERMINISTIC — same inputs always produce the same score. No model call,
    no drift, reproducible in an audit.
  * EXPLAINABLE — every score carries a reason string naming the factors that
    produced it ("final_rule +40; home regulator +25; capital +15; new +10").
    A bank cannot act on an unexplained ranking.
  * CONFIG-DRIVEN — weights live in config/regulators/_materiality.yaml so the
    business tunes priorities without a code change or redeploy.

When the owner's LLM enrichment lands, it improves the INPUTS (better topic
tags, better doc_type) and the same scoring rules get sharper automatically.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional, Sequence

import yaml

CONFIG_PATH = "config/regulators/_materiality.yaml"


@lru_cache(maxsize=4)
def load_config(path: str = CONFIG_PATH) -> dict:
    p = Path(path)
    if not p.is_absolute():
        p = Path.cwd() / p
    return yaml.safe_load(p.read_text(encoding="utf-8"))


@dataclass
class Materiality:
    score: int
    band: str
    reasons: List[str] = field(default_factory=list)

    @property
    def reason(self) -> str:
        return "; ".join(self.reasons)


def _tier_of(regulator_id: str, cfg: dict) -> Optional[str]:
    for tier, ids in (cfg.get("regulator_tiers") or {}).items():
        if regulator_id in ids:
            return tier
    return None


def _matched_topics(tags: Sequence[str], text: str, cfg: dict) -> Dict[str, str]:
    """topic -> group, from enrichment tags first then keyword fallback."""
    groups: Dict[str, str] = {}
    for group, topics in (cfg.get("topic_groups") or {}).items():
        for t in topics:
            groups[t] = group
    found: Dict[str, str] = {}
    for tag in tags or []:
        if tag in groups:
            found[tag] = groups[tag]
    if not found:  # keyword fallback for the rule-based (no-LLM) corpus
        low = (text or "")[:4000].lower()
        for topic, kws in (cfg.get("topic_keywords") or {}).items():
            if topic in groups and any(k in low for k in kws):
                found[topic] = groups[topic]
    return found


def score(
    *,
    regulator_id: str,
    doc_type: str,
    title: str = "",
    text: str = "",
    tags: Optional[Sequence[str]] = None,
    change_kind: str = "new",              # new | revised | superseded | deadline
    comment_deadline: Optional[date] = None,
    lines_changed: int = 0,
    today: Optional[date] = None,
    cfg: Optional[dict] = None,
) -> Materiality:
    """Score one document/change. Pure function — safe to call anywhere."""
    cfg = cfg or load_config()
    today = today or date.today()
    total = 0
    reasons: List[str] = []

    # 1+2 — document type scaled by how much this regulator matters to us
    base = (cfg.get("doc_type_base") or {}).get(doc_type, 5)
    tier = _tier_of(regulator_id, cfg)
    mult = (cfg.get("regulator_tier") or {}).get(tier, 1.0) if tier else 1.0
    weighted = int(round(base * mult))
    total += weighted
    if tier and mult != 1.0:
        reasons.append(f"{doc_type} x{mult} ({tier.replace('_', ' ')}) = {weighted}")
    else:
        reasons.append(f"{doc_type} +{weighted}")

    # 3 — risk domains touched (highest-weight group only, to avoid stacking
    #     five near-synonymous tags into a false Critical)
    topics = _matched_topics(list(tags or []), f"{title}\n{text}", cfg)
    if topics:
        weights = cfg.get("topic_weights") or {}
        best_group = max({g for g in topics.values()},
                         key=lambda g: weights.get(g, 0))
        w = weights.get(best_group, 0)
        total += w
        named = sorted(t for t, g in topics.items() if g == best_group)[:3]
        reasons.append(f"{', '.join(named)} +{w}")

    # 4 — what happened
    ck = (cfg.get("change_kind") or {}).get(change_kind, 0)
    if ck:
        total += ck
        reasons.append(f"{change_kind} +{ck}")

    # 5 — deadline clock
    if comment_deadline:
        days = (comment_deadline - today).days
        prox = cfg.get("deadline_proximity") or {}
        if 0 <= days <= 30:
            w = prox.get("within_days_30", 0)
            total += w
            reasons.append(f"comment deadline in {days}d +{w}")
        elif 30 < days <= 60:
            w = prox.get("within_days_60", 0)
            total += w
            reasons.append(f"comment deadline in {days}d +{w}")

    # 6 — how much actually changed
    if change_kind == "revised" and lines_changed:
        mag = cfg.get("revision_magnitude") or {}
        if lines_changed >= 200:
            w = mag.get("lines_changed_200", 0)
            total += w
            reasons.append(f"{lines_changed} lines changed +{w}")
        elif lines_changed >= 50:
            w = mag.get("lines_changed_50", 0)
            total += w
            reasons.append(f"{lines_changed} lines changed +{w}")

    total = max(0, min(100, total))
    return Materiality(score=total, band=band_for(total, cfg), reasons=reasons)


def band_for(value: int, cfg: Optional[dict] = None) -> str:
    cfg = cfg or load_config()
    for name, floor in sorted((cfg.get("bands") or {}).items(),
                              key=lambda kv: -kv[1]):
        if value >= floor:
            return name
    return "Informational"


BAND_ORDER = ["Critical", "High", "Medium", "Low", "Informational"]


def score_document(doc, text: str = "", tags: Optional[Sequence[str]] = None,
                   change_kind: Optional[str] = None,
                   lines_changed: int = 0, cfg: Optional[dict] = None) -> Materiality:
    """Convenience wrapper for a reg_documents row."""
    if change_kind is None:
        change_kind = ("superseded" if doc.status == "superseded"
                       else "revised" if (doc.version_n or 1) > 1 else "new")
    return score(regulator_id=doc.regulator_id, doc_type=doc.doc_type,
                 title=doc.title or "", text=text, tags=tags,
                 change_kind=change_kind, comment_deadline=doc.comment_deadline,
                 lines_changed=lines_changed, cfg=cfg)
