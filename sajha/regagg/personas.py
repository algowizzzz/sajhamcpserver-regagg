"""
Persona storage and retrieval.

A persona is configuration, never code: one JSON document (scope, salience,
presentation) plus an indexed entity list. Saving bumps a version and snapshots
the config, so "why did I see this on Aug 6?" stays answerable after edits.

The layout is DERIVED from the shape of the scope, not chosen by the user:
many entities -> exception-first, rule families dominant -> change-first,
otherwise narrative-first.
"""

from __future__ import annotations

import csv
import io
import re
import secrets
from typing import Dict, List, Optional, Tuple

from sqlalchemy import delete, func, select

from sajha.regagg.models import Persona, PersonaEntity, PersonaVersion

LANES = ("news", "regulatory")

DEFAULT_CONFIG = {
    "scope": {"sectors": [], "topics": [], "classes": [], "rule_families": [],
              "regions": []},
    "salience": {"topic_weights": {}, "serious_threshold": 50,
                 "min_corroboration": 1, "min_materiality": 15},
    "presentation": {"layout": "auto", "depth": "summaries", "max_items": 20},
}

# how many entities before a persona is a "book" rather than a "beat"
BOOK_THRESHOLD = 50


def _merge(base: dict, override: Optional[dict]) -> dict:
    out = {k: (dict(v) if isinstance(v, dict) else list(v) if isinstance(v, list) else v)
           for k, v in base.items()}
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = {**out[k], **v}
        else:
            out[k] = v
    return out


def derive_layout(config: dict, entity_count: int) -> str:
    """The persona's shape picks its layout — the user never does."""
    forced = (config.get("presentation") or {}).get("layout", "auto")
    if forced and forced != "auto":
        return forced
    if entity_count >= BOOK_THRESHOLD:
        return "exception_first"
    if (config.get("scope") or {}).get("rule_families"):
        return "change_first"
    return "narrative_first"


def parse_entities(raw: str, kind: str = "obligor") -> List[dict]:
    """Accept pasted CSV or one-name-per-line. First column is the name;
    an optional second column is the sector. Blank lines and a header row
    ('name', 'entity', …) are ignored."""
    rows: List[dict] = []
    seen = set()
    text = (raw or "").strip()
    if not text:
        return rows
    reader = csv.reader(io.StringIO(text))
    for i, cols in enumerate(reader):
        if not cols:
            continue
        name = (cols[0] or "").strip().strip('"')
        if not name:
            continue
        if i == 0 and name.lower() in {"name", "entity", "obligor", "issuer", "counterparty"}:
            continue
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        meta = {}
        if len(cols) > 1 and cols[1].strip():
            meta["sector"] = cols[1].strip()
        rows.append({"canonical": name[:255], "kind": kind, "meta": meta})
    return rows


def save_persona(session, *, owner_id: str, name: str, lane: str,
                 config: Optional[dict] = None, entities: Optional[List[dict]] = None,
                 persona_id: Optional[str] = None,
                 shared_with: Optional[List[str]] = None) -> Persona:
    """Create or update. Every save snapshots a version."""
    if lane not in LANES:
        raise ValueError(f"lane must be one of {LANES}")
    merged = _merge(DEFAULT_CONFIG, config)

    p = session.get(Persona, persona_id) if persona_id else None
    if p is None:
        p = Persona(persona_id=persona_id or f"p-{secrets.token_hex(5)}",
                    owner_id=owner_id, name=name[:160], lane=lane,
                    config=merged, version_n=1,
                    shared_with=list(shared_with or []))
        session.add(p)
    else:
        p.name, p.lane, p.config = name[:160], lane, merged
        p.version_n = (p.version_n or 1) + 1
        if shared_with is not None:
            p.shared_with = list(shared_with)
    session.flush()

    if entities is not None:
        session.execute(delete(PersonaEntity).where(
            PersonaEntity.persona_id == p.persona_id))
        for e in entities:
            session.add(PersonaEntity(persona_id=p.persona_id,
                                      canonical=e["canonical"],
                                      kind=e.get("kind", "obligor"),
                                      meta=e.get("meta", {})))
    count = session.scalar(select(func.count()).select_from(PersonaEntity)
                           .where(PersonaEntity.persona_id == p.persona_id)) or 0
    session.merge(PersonaVersion(persona_id=p.persona_id, version_n=p.version_n,
                                 config=merged, entity_count=count))
    session.commit()
    return p


def entity_count(session, persona_id: str) -> int:
    return session.scalar(select(func.count()).select_from(PersonaEntity)
                          .where(PersonaEntity.persona_id == persona_id)) or 0


def entity_names(session, persona_id: str) -> List[str]:
    return [c for (c,) in session.execute(
        select(PersonaEntity.canonical).where(
            PersonaEntity.persona_id == persona_id)).all()]


def persona_dict(session, p: Persona) -> dict:
    n = entity_count(session, p.persona_id)
    return {"persona_id": p.persona_id, "owner_id": p.owner_id, "name": p.name,
            "lane": p.lane, "config": p.config, "version_n": p.version_n,
            "shared_with": p.shared_with or [], "entity_count": n,
            "layout": derive_layout(p.config or {}, n),
            "updated_at": str(p.updated_at or "")}


def list_personas(session, user_id: str, lane: Optional[str] = None) -> List[dict]:
    """Personas you own, plus ones shared with you (view-only)."""
    stmt = select(Persona)
    if lane:
        stmt = stmt.where(Persona.lane == lane)
    out = []
    for p in session.scalars(stmt).all():
        shared = p.shared_with or []
        if p.owner_id == user_id or user_id in shared:
            d = persona_dict(session, p)
            d["can_edit"] = p.owner_id == user_id
            out.append(d)
    return sorted(out, key=lambda d: (not d["can_edit"], d["name"].lower()))


def get_persona(session, persona_id: str, user_id: str) -> Tuple[Optional[Persona], Optional[str]]:
    p = session.get(Persona, persona_id)
    if p is None:
        return None, "Persona not found."
    if p.owner_id != user_id and user_id not in (p.shared_with or []):
        return None, "You do not have access to that persona."
    return p, None
