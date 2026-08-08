"""Columns the desk defines, filled by a model, checked by code.

A credit desk does not want the columns we imagined; it wants the ones its own
process runs on — event severity, rating direction, whether the name is on
watch. So the persona declares them, in YAML or JSON, and the sweep fills them.

The safety property is narrow and important: **a declared column with declared
values can only ever hold one of those values, or "unknown".** The model
proposes; this module disposes. That is what makes a generated column safe to
sort, filter and count on — and what stops "Major" quietly becoming "major
event (probable)" halfway down a 500-row table, which would break every filter
built on it without looking broken.

    columns:
      - name: event
        label: Event size
        values: [major, minor, none]
        describe: major if it could move the credit; none if the story is routine
      - name: rating_impact
        label: Rating impact
        values: [negative, neutral, positive, unclear]
      - name: note
        label: Analyst note
        type: text
        max_chars: 120
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

MAX_COLUMNS = 12
MAX_VALUES = 12
MAX_TEXT = 300
UNKNOWN = "unknown"

_SLUG = re.compile(r"^[a-z][a-z0-9_]{0,31}$")

# Columns the sweep always produces; a persona may not redefine them.
RESERVED = {"entity", "title", "snippet", "url", "source", "published", "status"}


@dataclass(frozen=True)
class Column:
    name: str
    label: str
    kind: str = "enum"                       # enum | text
    values: List[str] = field(default_factory=list)
    describe: str = ""
    max_chars: int = 120

    def coerce(self, raw: Any) -> str:
        """Force a model's answer into this column, or admit it does not fit.

        Case and surrounding punctuation are forgiven because they carry no
        meaning; anything else is not. A near-miss is still a miss: silently
        mapping "major event" onto "major" would make the column look reliable
        while quietly deciding what the model meant.
        """
        if raw is None:
            return UNKNOWN
        text = str(raw).strip()
        if not text:
            return UNKNOWN
        if self.kind == "text":
            return text[:min(self.max_chars, MAX_TEXT)]
        low = text.lower().strip(" .,:;\"'")
        for v in self.values:
            if low == v.lower():
                return v
        return UNKNOWN


def _norm_values(raw) -> List[str]:
    if raw is None:
        return []
    if isinstance(raw, str):
        raw = re.split(r"[,\n|]+", raw)
    out, seen = [], set()
    for v in raw:
        s = str(v).strip()
        if s and s.lower() not in seen:
            seen.add(s.lower())
            out.append(s)
    return out[:MAX_VALUES]


def parse(spec: Any) -> tuple[List[Column], List[str]]:
    """Read a column schema from YAML text, JSON text, or an already-parsed
    structure. Returns the columns plus the problems worth telling the author
    about — a schema that half-loads should say which half."""
    problems: List[str] = []
    if not spec:
        return [], problems

    data = spec
    if isinstance(spec, str):
        text = spec.strip()
        if not text:
            return [], problems
        try:
            data = json.loads(text)
        except ValueError:
            try:
                import yaml
                data = yaml.safe_load(text)
            except Exception as e:  # noqa: BLE001
                return [], [f"could not parse as JSON or YAML: {str(e)[:120]}"]

    if isinstance(data, dict):
        data = data.get("columns", data.get("table", []))
    if not isinstance(data, list):
        return [], ["expected a list of columns, or a mapping with a 'columns' key"]

    cols: List[Column] = []
    seen = set()
    for i, raw in enumerate(data):
        if len(cols) >= MAX_COLUMNS:
            problems.append(f"only the first {MAX_COLUMNS} columns are used")
            break
        if isinstance(raw, str):
            raw = {"name": raw}
        if not isinstance(raw, dict):
            problems.append(f"column {i + 1} is not a mapping")
            continue
        name = str(raw.get("name") or raw.get("id") or "").strip().lower()
        name = re.sub(r"[\s-]+", "_", name)
        if not _SLUG.match(name):
            problems.append(f"column {i + 1}: '{name or raw}' is not a usable name "
                            "(lower case letters, digits and underscore)")
            continue
        if name in RESERVED:
            problems.append(f"'{name}' is produced by the sweep and cannot be redefined")
            continue
        if name in seen:
            problems.append(f"'{name}' appears twice")
            continue
        seen.add(name)
        values = _norm_values(raw.get("values") or raw.get("options"))
        kind = str(raw.get("type") or ("enum" if values else "text")).lower()
        if kind not in ("enum", "text"):
            problems.append(f"'{name}': unknown type '{kind}', treated as text")
            kind = "text"
        if kind == "enum" and not values:
            problems.append(f"'{name}': an enum column needs values, treated as text")
            kind = "text"
        try:
            max_chars = int(raw.get("max_chars") or 120)
        except (TypeError, ValueError):
            max_chars = 120
        cols.append(Column(
            name=name,
            label=str(raw.get("label") or name.replace("_", " ")).strip()[:40],
            kind=kind, values=values,
            describe=str(raw.get("describe") or raw.get("description") or "").strip()[:200],
            max_chars=max(20, min(max_chars, MAX_TEXT)),
        ))
    return cols, problems


def prompt_fragment(cols: List[Column]) -> str:
    """How the columns are described to the model — the same text every time,
    generated from the schema so the two cannot drift apart."""
    lines = []
    for c in cols:
        bit = f'- "{c.name}"'
        if c.kind == "enum":
            bit += ": one of " + ", ".join(f'"{v}"' for v in c.values)
            bit += f', or "{UNKNOWN}" if the snippet does not say'
        else:
            bit += f": free text, at most {c.max_chars} characters, or empty"
        if c.describe:
            bit += f" — {c.describe}"
        lines.append(bit)
    return "\n".join(lines)


def coerce_row(cols: List[Column], raw: Dict[str, Any]) -> Dict[str, str]:
    """Every declared column gets a value; nothing undeclared gets through."""
    raw = raw if isinstance(raw, dict) else {}
    return {c.name: c.coerce(raw.get(c.name)) for c in cols}


def to_dicts(cols: List[Column]) -> List[dict]:
    return [{"name": c.name, "label": c.label, "kind": c.kind,
             "values": c.values, "describe": c.describe} for c in cols]


DEFAULT_SPEC = """# Columns for the entity table. Edit freely.
columns:
  - name: event
    label: Event
    values: [major, minor, none]
    describe: major if it could move the credit on its own; none if routine
  - name: rating_impact
    label: Rating impact
    values: [negative, neutral, positive, unclear]
  - name: action
    label: Action
    values: [review now, monitor, no action]
"""
