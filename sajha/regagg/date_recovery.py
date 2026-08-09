"""Recover a publication date for documents collected without one.

74% of the corpus has no `published_date`, which is why "what changed in the
last N days" quietly misses most of it and why the assistant says so unprompted.

Measured on a 400-document sample of the undated set, the date is recoverable
for roughly a quarter of them: ~5% carry it in the URL path, ~24% state it in
the opening of the text. **The rest genuinely do not have one anywhere we
hold**, and this module returns nothing for those rather than guessing — an
invented date is worse than a missing one, because a missing date excludes a
document from a time query while a wrong date puts it in the wrong week.

Confidence is recorded with the date, because these are not equal evidence:

    url     the publisher put it in the path — strong, and machine-written
    text    a date near the top of the document — good, but it may be the date
            of the thing described rather than the date of publication
    none    nothing found

Callers store the confidence so a later reader can tell a collected date from
an inferred one.
"""

from __future__ import annotations

import datetime as _dt
import re
from typing import Optional, Tuple

# Dates in a URL path: /2026/08/07/, /2026-08-07-, /26aug2026/
_URL_YMD = re.compile(r"/(20\d{2})[/\-_](\d{1,2})[/\-_](\d{1,2})(?=[/\-_.]|$)")
_URL_YM = re.compile(r"/(20\d{2})[/\-_](\d{1,2})(?=[/\-_.]|$)")

_MONTHS = {m.lower(): i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August",
     "September", "October", "November", "December"], 1)}
_MON_RE = "|".join(_MONTHS)

# "7 August 2026" / "August 7, 2026" / "2026-08-07"
_TEXT_DMY = re.compile(rf"\b(\d{{1,2}})\s+({_MON_RE})\s+(20\d{{2}})\b", re.I)
_TEXT_MDY = re.compile(rf"\b({_MON_RE})\s+(\d{{1,2}}),?\s+(20\d{{2}})\b", re.I)
_TEXT_ISO = re.compile(r"\b(20\d{2})-(\d{2})-(\d{2})\b")

# Lines that carry a date but not *this document's* publication date.
_NOT_PUBLICATION = re.compile(
    r"\b(effective|comes into force|in force|closes?|closing|deadline|"
    r"comment period|expires?|as at|as of|accessed|retrieved|"
    r"copyright|©|last (?:updated|modified|reviewed))\b", re.I)

SCAN_CHARS = 4000          # the opening only; a date on page 40 is not the date


def _safe(y: int, m: int, d: int) -> Optional[_dt.date]:
    try:
        val = _dt.date(y, m, d)
    except ValueError:
        return None
    # A publication date in the future, or before the web, is a parse error.
    if val > _dt.date.today() + _dt.timedelta(days=1) or val.year < 1995:
        return None
    return val


def from_url(url: str) -> Optional[_dt.date]:
    if not url:
        return None
    m = _URL_YMD.search(url)
    if m:
        return _safe(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = _URL_YM.search(url)
    if m:
        # a month with no day: the first is the only defensible choice, and
        # it is still better than nothing for a "last 30 days" query
        return _safe(int(m.group(1)), int(m.group(2)), 1)
    return None


def from_text(text: str, *, scan: int = SCAN_CHARS) -> Optional[_dt.date]:
    """The first date in the opening that is not obviously about something else."""
    if not text:
        return None
    head = text[:scan]
    for line in head.splitlines():
        line = line.strip()
        if not line or _NOT_PUBLICATION.search(line):
            continue        # "Effective 1 November 2026" is not when it was published
        for rx, order in ((_TEXT_DMY, "dmy"), (_TEXT_MDY, "mdy"), (_TEXT_ISO, "iso")):
            m = rx.search(line)
            if not m:
                continue
            if order == "dmy":
                got = _safe(int(m.group(3)), _MONTHS[m.group(2).lower()], int(m.group(1)))
            elif order == "mdy":
                got = _safe(int(m.group(3)), _MONTHS[m.group(1).lower()], int(m.group(2)))
            else:
                got = _safe(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            if got:
                return got
    return None


def recover(*, url: str = "", text: str = "") -> Tuple[Optional[_dt.date], str]:
    """Best available date and where it came from. Strongest evidence first."""
    got = from_url(url)
    if got:
        return got, "url"
    got = from_text(text)
    if got:
        return got, "text"
    return None, "none"
