"""A short preview for a document, so a card can be read without opening it.

Two lanes, two different problems, and one rule that applies to both: when
nothing usable can be found, return nothing. A card with no preview is a card
with no preview; a card showing a postal address looks like the system does not
understand the document.

NEWS is a constraint, not a difficulty. Collected news is headline + the
publisher's own feed summary + a link, and nothing else — the article body is
never stored, deliberately, because reproducing it is the publisher's right and
not ours. So the preview here is the summary the publisher themselves put in
the feed, and there is no deeper text to fall back to.

REGULATORY is the opposite: tens of thousands of characters, of which the first
few hundred are almost always furniture. Real openings from the corpus:

    255 Albert Street Ottawa, Canada K1A 0H2 www.osfi-bsif.gc.ca
    Unclassified / Non classifié
    Terrorist Financing Assessment 2018 ... 2 TABLE OF CONTENTS Introduction ....
    PRESS RELEASE 7 April 2026

Enumerating that junk is a losing game — every regulator has its own. Instead
each candidate paragraph is scored for how much it reads like prose, and the
first one that passes wins. A rule that asks "is this a sentence?" survives a
new regulator; a list of known letterheads does not.
"""

from __future__ import annotations

import re
from typing import List, Optional

MAX_CHARS = 260
MIN_WORDS = 8

# Labelled fields regulators use for exactly this purpose. When a document says
# what it is about, believe it rather than guessing from the first paragraph.
_LABELLED = re.compile(
    r"^\s*(?:subject|objective|objectif|purpose|summary|overview|re)\s*[:–-]\s*(.+)",
    re.IGNORECASE)

_URL = re.compile(r"(https?://|www\.)\S+", re.IGNORECASE)
_LINK_ONLY = re.compile(r"^\s*\[[^\]]*\]\([^)]*\)\s*$")
_HEADING = re.compile(r"^\s{0,3}#{1,6}\s+")
_QUOTE = re.compile(r"^\s*>")
_TOC = re.compile(r"\.{4,}\s*\d+\s*$")          # "Introduction ......... 3"
_POSTCODE = re.compile(r"\b[A-Z]\d[A-Z]\s?\d[A-Z]\d\b|\b\d{5}(?:-\d{4})?\b")
_CLASSIFICATION = re.compile(
    r"^\s*(unclassified|restricted|confidential|internal|public|for information)\b",
    re.IGNORECASE)
_PAGE_NO = re.compile(r"^\s*(?:page\s*)?\d{1,4}\s*$", re.IGNORECASE)
MIN_SENTENCE_WORDS = 6
_CONTENTS = re.compile(r"^\s*(?:table of )?contents\b|\bcontents\b\s*\d", re.IGNORECASE)
# Generic across every publisher, so a short list is safe here — unlike
# letterheads, these phrases are not regulator-specific.
_BOILERPLATE = re.compile(
    r"\b(?:un)?subscribe\b|\bfor more information or to\b"
    r"|members of the media|media (?:inquiries|enquiries)"
    r"|signaler un probl|report a problem|terms of use|privacy policy"
    r"|all rights reserved|cookies? (?:policy|settings)"
    r"|accessible via the .{0,30}website here",
    re.IGNORECASE)


def _has_sentence(p: str) -> bool:
    """Does this contain a real sentence — several words, then a full stop?

    Written as a scan rather than a regex on purpose. The obvious pattern for
    "six words then a stop" nests two quantifiers, which backtracks
    catastrophically on long paragraphs that never match — and regulatory
    documents supply plenty of those. A linear pass cannot hang a page render.
    """
    words = 0
    for token in p.split():
        words += 1
        if token[-1:] in ".!?" and words >= MIN_SENTENCE_WORDS:
            return True
        if token[-1:] in ".!?":
            words = 0        # a short fragment ended; start counting again
    return False


def _strip_frontmatter(md: str) -> str:
    if not md.startswith("---"):
        return md
    end = md.find("\n---", 3)
    return md if end == -1 else md[end + 4:]


def _paragraphs(md: str) -> List[str]:
    """Blank-line separated blocks, with markdown furniture flattened."""
    text = _strip_frontmatter(md or "")
    text = re.sub(r"^\s*\|.*\|\s*$", "", text, flags=re.MULTILINE)   # table rows
    out = []
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block:
            continue
        lines = [l for l in block.splitlines()
                 if not _HEADING.match(l) and not _LINK_ONLY.match(l)
                 and not _QUOTE.match(l)]
        joined = re.sub(r"\s+", " ", " ".join(lines)).strip()
        joined = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", joined)      # keep link text
        joined = re.sub(r"[*_`]{1,3}", "", joined)
        if joined:
            out.append(joined)
    return out


def _is_furniture(p: str, title: str = "") -> bool:
    """Reject what is printed on the page rather than written in the document."""
    if _CLASSIFICATION.match(p) or _PAGE_NO.match(p) or _TOC.search(p):
        return True
    if _POSTCODE.search(p) and len(p) < 200:      # address blocks are short
        return True
    letters = sum(c.isalpha() for c in p)
    if not letters or letters / len(p) < 0.55:    # dot leaders, figures, tables
        return True
    if p.isupper() and len(p) < 90:               # PRESS RELEASE, banner lines
        return True
    if title and p.strip().lower().startswith(title.strip().lower()[:40]) \
            and len(p) < len(title) + 60:
        return True                               # the title printed again
    if _CONTENTS.search(p[:60]) or _BOILERPLATE.search(p):
        return True
    words = p.split()
    if len(words) < MIN_WORDS:
        return True
    # Numbered fragments strung together: "Introduction 2 Phishing 5 Insider 8".
    numeric = sum(1 for w in words if w.strip(".,()").isdigit())
    if numeric / len(words) > 0.15:
        return True
    # Prose is mostly lowercase words; headings and mastheads are not. Checked
    # without a punctuation escape hatch, because a heading run like
    # "INNOVATION HOURS PROGRAM ... I. EXECUTIVE SUMMARY" contains a full stop
    # and slipped through when one was allowed.
    lower = sum(1 for w in words if w[:1].islower())
    if lower / len(words) < 0.30:
        return True
    return False


def _clean(p: str, max_chars: int) -> str:
    p = _URL.sub("", p).strip(" -–—·|")
    p = re.sub(r"\s{2,}", " ", p)
    if len(p) <= max_chars:
        return p.strip()
    cut = p[:max_chars]
    # prefer a sentence boundary, then a word boundary — never mid-word
    end = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
    if end > max_chars * 0.5:
        return cut[:end + 1].strip()
    sp = cut.rfind(" ")
    return (cut[:sp] if sp > 0 else cut).rstrip(" ,;:") + "…"


def from_markdown(md: str, *, title: str = "", lane: str = "regulatory",
                  max_chars: int = MAX_CHARS) -> str:
    """The first thing in this document a person would actually want to read."""
    paras = _paragraphs(md)
    if not paras:
        return ""

    if lane == "news":
        # The body IS the publisher's summary; the only furniture is the title
        # repeated as a heading, already stripped above.
        for p in paras:
            if not _is_furniture(p, title):
                return _clean(p, max_chars)
        # A one-line summary can be shorter than MIN_WORDS and still be the
        # whole of what the publisher gave us — take it rather than show blank.
        for p in paras:
            if len(p.split()) >= 4 and not _CLASSIFICATION.match(p):
                return _clean(p, max_chars)
        return ""

    # Regulatory: a labelled field beats a guess, but only in the opening pages
    # where such labels are meaningful.
    for p in paras[:12]:
        m = _LABELLED.match(p)
        if m:
            val = m.group(1).strip()
            # "Subject: Interest Rate Risk Management Category: ..." — keep the
            # subject, drop the metadata train that follows it
            val = re.split(r"\s+(?:Category|No|Date|Effective|Audience)\s*:", val)[0]
            if len(val.split()) >= 3:
                return _clean(val, max_chars)

    # Prose, and it has to contain a sentence. Requiring one costs a preview on
    # a handful of genuinely list-shaped documents and buys never printing a
    # contents page as though it were a summary.
    for p in paras:
        if not _is_furniture(p, title) and _has_sentence(p):
            return _clean(p, max_chars)
    return ""


def for_prefix(storage, prefix: Optional[str], *, title: str = "",
               lane: str = "regulatory", max_chars: int = MAX_CHARS) -> str:
    """Read a stored document and summarise it, tolerating anything.

    A preview is a nicety; failing to produce one must never take a page down,
    so every failure path returns an empty string. Only the first 40k characters
    are read — the opening is all this looks at, and some policy PDFs run to
    nearly two megabytes.
    """
    if storage is None or not prefix:
        return ""
    try:
        raw = storage.read_content(prefix) or ""
    except Exception:  # noqa: BLE001
        return ""
    return from_markdown(raw[:40000], title=title or "", lane=lane,
                         max_chars=max_chars)


def for_document(storage, doc, *, lane: str = "regulatory",
                 max_chars: int = MAX_CHARS) -> str:
    return for_prefix(storage, getattr(doc, "s3_prefix", None),
                      title=getattr(doc, "title", "") or "", lane=lane,
                      max_chars=max_chars)
