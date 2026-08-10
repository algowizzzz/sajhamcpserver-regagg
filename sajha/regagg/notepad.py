"""A working notepad for the digital worker — findings that outlive the window.

The context window is not the constraint people assume it is (this install's
model accepted a 400,000-token prompt). The constraint is that a *conversation*
accumulates: read forty documents in full and the transcript, not any single
document, is what overflows. Summarising as you go is the answer, and an agent
cannot summarise as it goes without somewhere to put the summary.

So: sections of markdown the worker writes to while it reads, and reads back
when it composes. Three properties make it useful rather than decorative.

**It survives the turn.** A qualitative pass over a rulebook is not one
question. Notes are keyed by owner and notepad name and persist on disk, so
"carry on with the crypto review" picks up where it stopped.

**The index is cheap.** Every step the worker is shown the section names and
their sizes — tens of characters — not the contents. It reads a section only
when it needs it. A notepad that re-entered the prompt in full each step would
be the very problem it exists to solve.

**Appending is the default.** A worker that overwrites its own notes halfway
through a long read loses exactly the work this is meant to protect, so
`replace` has to be asked for by name.

Stored as plain markdown under `data/notepads/<owner>/<name>.md` — readable,
diffable, and greppable without the app. Names are slugged, never joined raw:
a notepad name arrives from a model, and a model can be talked into `../`.
"""

from __future__ import annotations

import re
import threading
from contextvars import ContextVar
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

# A section heading the worker did not name. Anonymous notes still have to land
# somewhere findable rather than being concatenated into one wall.
DEFAULT_SECTION = "notes"

MAX_SECTION_CHARS = 200_000        # a section, not a corpus
MAX_NOTEPAD_CHARS = 2_000_000

_SLUG = re.compile(r"[^a-z0-9._-]+")
_lock = threading.RLock()

# Who the current request is writing as. The tools are called by name with only
# the model's arguments, so ownership cannot come from the argument list — a
# model must not be able to name someone else's notepad.
_owner: ContextVar[str] = ContextVar("notepad_owner", default="shared")


def set_owner(owner: Optional[str]) -> None:
    _owner.set(slug(owner or "shared") or "shared")


def get_owner() -> str:
    return _owner.get()


def slug(text: str) -> str:
    """A filename component that cannot escape its directory."""
    s = _SLUG.sub("-", (text or "").strip().lower()).strip("-._")
    s = s.replace("..", "-")
    return s[:80]


def root() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "notepads"


def _path(name: str, owner: Optional[str] = None) -> Path:
    n = slug(name) or "scratch"
    o = slug(owner or get_owner()) or "shared"
    d = root() / o
    d.mkdir(parents=True, exist_ok=True)
    p = (d / f"{n}.md").resolve()
    # belt and braces: the slug should make this impossible, so if it ever
    # fires the slug is broken and silence would be the wrong answer
    if d.resolve() not in p.parents:
        raise ValueError(f"refusing to write outside the notepad directory: {name}")
    return p


# ── sections ────────────────────────────────────────────────────────────────

def _parse(text: str) -> Dict[str, str]:
    """Split a notepad into its `## section` bodies, order preserved."""
    out: Dict[str, str] = {}
    current = None
    buf: List[str] = []
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            if current is not None:
                out[current] = "\n".join(buf).strip()
            current = m.group(1).strip()
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        out[current] = "\n".join(buf).strip()
    return out


def _render(sections: Dict[str, str]) -> str:
    return "\n\n".join(f"## {k}\n{v}".rstrip() for k, v in sections.items()) + "\n"


def _demote(note: str) -> str:
    """Push `#`/`##` headings inside a note down to `###`.

    Section structure belongs to the notepad, not to note text. A model writing
    a tidy `## OSFI guideline` at the top of its note was splitting the file on
    the next read: the section it had named came back EMPTY and the content sat
    under a phantom heading. Notes looked lost the moment they were read back.
    """
    return re.sub(r"^(#{1,2})(?=\s)", "###", note, flags=re.M)


def read_raw(name: str = "scratch", owner: Optional[str] = None) -> str:
    p = _path(name, owner)
    try:
        return p.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


# ── the two operations ──────────────────────────────────────────────────────

def write(note: str, section: str = DEFAULT_SECTION, mode: str = "append",
          name: str = "scratch", owner: Optional[str] = None) -> dict:
    """Add to (or replace) one section. Returns the index, never the contents."""
    note = _demote((note or "").strip())
    if not note:
        return {"ok": False, "error": "nothing to write"}
    section = (section or DEFAULT_SECTION).strip()[:120] or DEFAULT_SECTION
    if mode not in ("append", "replace"):
        return {"ok": False,
                "error": f"mode must be 'append' or 'replace', not {mode!r}"}

    with _lock:
        p = _path(name, owner)
        sections = _parse(read_raw(name, owner))
        prior = sections.get(section, "")
        if mode == "replace" or not prior:
            body = note
        else:
            stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
            body = f"{prior}\n\n_{stamp}Z_\n{note}"
        if len(body) > MAX_SECTION_CHARS:
            return {"ok": False, "error": f"section '{section}' would exceed "
                                          f"{MAX_SECTION_CHARS:,} characters; "
                                          f"summarise it with mode='replace'"}
        sections[section] = body
        text = _render(sections)
        if len(text) > MAX_NOTEPAD_CHARS:
            return {"ok": False, "error": "notepad is full; consolidate a section "
                                          "with mode='replace'"}
        p.write_text(text, encoding="utf-8")

    return {"ok": True, "notepad": slug(name) or "scratch", "section": section,
            "mode": mode, "section_chars": len(sections[section]),
            "index": index(name, owner)}


def read(section: Optional[str] = None, name: str = "scratch",
         owner: Optional[str] = None, max_chars: int = 40000,
         offset: int = 0) -> dict:
    """One section, or — with no section — the index alone.

    Returning the whole notepad by default would put every note back in the
    prompt on every call, which is the cost this is here to avoid.
    """
    sections = _parse(read_raw(name, owner))
    npd = slug(name) or "scratch"
    if not sections:
        return {"ok": True, "notepad": npd, "sections": [], "empty": True,
                "hint": "Nothing written yet. Use notepad_write as you read."}
    if section is None:
        return {"ok": True, "notepad": npd, "index": index(name, owner),
                "hint": "Pass section= to read one. Contents are omitted here on "
                        "purpose so the index stays cheap."}
    key = next((k for k in sections if k.lower() == section.strip().lower()), None)
    if key is None:
        return {"ok": False, "notepad": npd, "error": f"no section {section!r}",
                "sections": list(sections)}
    body = sections[key]
    off = max(0, int(offset))
    window = body[off:off + max(1, int(max_chars))]
    end = off + len(window)
    return {"ok": True, "notepad": npd, "section": key,
            "total_chars": len(body), "offset": off, "chars_returned": len(window),
            "truncated": end < len(body),
            "next_offset": end if end < len(body) else None,
            "content": window}


def index(name: str = "scratch", owner: Optional[str] = None) -> List[dict]:
    """Section names and sizes — what the worker is shown every step."""
    return [{"section": k, "chars": len(v), "first_line": (v.splitlines() or [""])[0][:90]}
            for k, v in _parse(read_raw(name, owner)).items()]


def summary_line(name: str = "scratch", owner: Optional[str] = None) -> str:
    """One line for the system prompt. Empty string when there is nothing."""
    ix = index(name, owner)
    if not ix:
        return ""
    bits = ", ".join(f"{s['section']} ({s['chars']:,}c)" for s in ix[:12])
    return f"Your notepad '{slug(name) or 'scratch'}' holds: {bits}."


def clear(name: str = "scratch", owner: Optional[str] = None) -> dict:
    with _lock:
        p = _path(name, owner)
        existed = p.exists()
        if existed:
            p.unlink()
    return {"ok": True, "cleared": existed, "notepad": slug(name) or "scratch"}
