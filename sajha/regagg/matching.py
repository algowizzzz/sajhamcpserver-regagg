"""
Entity matching: does this company in the news correspond to a watched name?

This is the highest-stakes code in the product. A miss means a desk sees
nothing on the day its own obligor is in the news — the failure the whole
system exists to prevent. A false positive means someone chases the wrong
company, which is cheaper but still corrosive to trust.

Three levels, deliberately:

  CONFIRMED   the names agree after normalisation and alias expansion.
  POSSIBLE    they plausibly agree but the evidence is ambiguous — a one-word
              watch name against a longer company name ("Apple" vs "Apple
              Hospitality REIT"). Surfaced to the analyst as "possible mention,
              verify", never silently dropped and never silently asserted.
  NO MATCH    nothing links them.

The ambiguous middle is the important part. A heuristic that must choose
between missing and over-claiming will do both; making "I am not sure" a
first-class outcome is what keeps the product honest at scale.
"""

from __future__ import annotations

import re
from typing import Dict, Iterable, List, Optional, Set, Tuple

# Legal forms and decorations that differ between a watchlist and a newsroom.
LEGAL_SUFFIXES = {
    "inc", "incorporated", "corp", "corporation", "co", "company", "ltd",
    "limited", "llc", "llp", "lp", "plc", "sa", "nv", "ag", "gmbh", "spa",
    "pty", "bhd", "ab", "oyj", "as", "asa", "kk", "kgaa", "sas", "srl",
    "holdings", "holding", "group", "groupe", "partners", "trust",
}
# Descriptors that carry meaning in a name and must NOT be stripped, because
# dropping them is exactly how "Apple Inc." starts matching "Apple Hospitality".
STRUCTURE_WORDS = {"reit", "bank", "financial", "capital", "energy", "motors",
                   "motor", "airlines", "technologies", "platforms", "pharma",
                   "pharmaceuticals", "industries", "resources", "properties",
                   "hospitality", "health", "healthcare", "media", "systems"}
NOISE_WORDS = {"the", "and", "of"}

_TOKEN = re.compile(r"[a-z0-9]+")


def normalise(name: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace. Nothing removed."""
    return " ".join(_TOKEN.findall((name or "").lower()))


def _tokens(name: str) -> List[str]:
    return [t for t in normalise(name).split() if t not in NOISE_WORDS]


def core_tokens(name: str) -> List[str]:
    """The name without legal decoration — 'Goodfood Market Corp.' -> goodfood market."""
    toks = _tokens(name)
    while toks and toks[-1] in LEGAL_SUFFIXES:
        toks.pop()
    return toks or _tokens(name)


def acronym(name: str) -> Optional[str]:
    """AMD from Advanced Micro Devices.

    Three words minimum, three letters minimum. A two-word name yields
    two-letter acronyms like 'GM' for "Goodfood Market", which would then
    match General Motors — an initialism that short is a coincidence, not a
    name.
    """
    toks = core_tokens(name)
    if len(toks) < 3:
        return None
    letters = "".join(t[0] for t in toks)
    return letters if 3 <= len(letters) <= 5 else None


def generate_aliases(name: str) -> Set[str]:
    """Every spelling of this company that should count as the same company.

    Covers what actually differs in practice: legal suffixes, punctuation and
    spacing ('J.P. Morgan' / 'JP Morgan' / 'JPMorgan'), and the acronym for
    multi-word names ('Advanced Micro Devices' -> 'amd'). It deliberately does
    NOT generate the bare head word of a multi-word name — that is the
    ambiguous case, and guessing there is how 'Apple Inc.' matched 'Apple
    Hospitality REIT'.
    """
    out: Set[str] = set()
    full = normalise(name)
    if not full:
        return out
    core = " ".join(core_tokens(name))
    for variant in (full, core):
        if not variant:
            continue
        out.add(variant)
        out.add(variant.replace(" ", ""))          # jp morgan -> jpmorgan
    ac = acronym(name)
    if ac:
        out.add(ac)
    return {a for a in out if len(a) >= 2}


def _is_ambiguous_extension(short: List[str], long: List[str]) -> bool:
    """short is a prefix of long, but long adds a MEANINGFUL word.

    'apple' + 'hospitality' is a different company; 'meta' + 'platforms' is
    the same one. We cannot tell these apart from the strings alone, which is
    precisely why the answer is POSSIBLE rather than yes or no.
    """
    extra = long[len(short):]
    return any(w in STRUCTURE_WORDS or len(w) > 3 for w in extra)


class WatchlistMatcher:
    """Match extracted company names against one persona's watchlist."""

    def __init__(self, names: Iterable[str],
                 extra_aliases: Optional[Dict[str, Iterable[str]]] = None):
        self.by_alias: Dict[str, str] = {}
        self.cores: List[Tuple[List[str], str]] = []
        for name in names:
            for alias in generate_aliases(name):
                self.by_alias.setdefault(alias, name)
            for alias in (extra_aliases or {}).get(name, ()):        # user-taught
                for a in generate_aliases(alias):
                    self.by_alias.setdefault(a, name)
            self.cores.append((core_tokens(name), name))

        # Candidate indexes. Without these, every lookup scanned the whole
        # watchlist twice — fine for ten names, 12,000 comparisons per story
        # for a 6,000-name book, which made page builds take minutes.
        # Both rules below require agreement on the START of the name, so
        # bucketing by it is exact, not approximate.
        self._by_first: Dict[str, List[Tuple[List[str], str]]] = {}
        self._by_head: Dict[str, List[Tuple[str, str]]] = {}
        for ctoks, name in self.cores:
            if not ctoks:
                continue
            self._by_first.setdefault(ctoks[0], []).append((ctoks, name))
            squashed = "".join(ctoks)
            if len(squashed) >= 6:
                self._by_head.setdefault(squashed[:6], []).append((squashed, name))

        # token -> the watched names containing it, used only when the token is
        # distinctive enough to identify one company on its own
        self._distinctive: Dict[str, List[str]] = {}
        for ctoks, name in self.cores:
            for tok in ctoks:
                if len(tok) >= 5 and tok not in STRUCTURE_WORDS:
                    self._distinctive.setdefault(tok, [])
                    if name not in self._distinctive[tok]:
                        self._distinctive[tok].append(name)

    def __len__(self) -> int:
        return len(self.cores)

    def match(self, written: str) -> Tuple[Optional[str], str, str]:
        """Return (watched_name, confidence, reason).

        confidence is 'confirmed', 'possible' or 'none'.
        """
        if not written:
            return None, "none", "empty"
        norm = normalise(written)
        squashed = norm.replace(" ", "")
        for key in (norm, squashed, " ".join(core_tokens(written)),
                    "".join(core_tokens(written))):
            if key and key in self.by_alias:
                return self.by_alias[key], "confirmed", "name matches"
        ac = acronym(written)
        if ac and ac in self.by_alias:
            return self.by_alias[ac], "confirmed", f"acronym {ac.upper()}"

        wtoks = core_tokens(written)
        wsquashed = "".join(wtoks)

        # Spacing differences are not name differences: 'JP Morgan',
        # 'J.P. Morgan' and 'JPMorgan' are one company written three ways, and
        # token comparison cannot see that because the tokens themselves differ.
        # Only an EXACT match after removing spaces is a confirmation, though:
        # 'Citadel' is a prefix of 'Citadel Broadcasting' too, and those are
        # different companies. A leftover word makes it a question, not a fact.
        spacing_possible: Optional[Tuple[str, str]] = None
        if len(wsquashed) >= 6:
            for csquashed, name in self._by_head.get(wsquashed[:6], ()):
                if csquashed == wsquashed:
                    return name, "confirmed", "same name, spelled with different spacing"
                short, long = sorted((csquashed, wsquashed), key=len)
                if long.startswith(short):
                    spacing_possible = (name, f"'{written}' may be a short form of '{name}'")

        best: Optional[Tuple[str, str]] = None
        for ctoks, name in (self._by_first.get(wtoks[0], ()) if wtoks else ()):
            short, long = (ctoks, wtoks) if len(ctoks) <= len(wtoks) else (wtoks, ctoks)
            if long[:len(short)] != short:
                continue                       # not even a prefix — unrelated
            if not _is_ambiguous_extension(short, long):
                return name, "confirmed", "same name, different length"
            best = (name, f"'{written}' may be '{name}' — extra words in the name")
        if best:
            return best[0], "possible", best[1]
        if spacing_possible:
            return spacing_possible[0], "possible", spacing_possible[1]

        # A company is often written by its distinctive word alone — "Disney"
        # for The Walt Disney Company, "RioCan" for RioCan REIT. The word has
        # to actually distinguish: generic industry words are excluded, and a
        # word shared by several watched names distinguishes nothing.
        for token in wtoks:
            if len(token) < 5 or token in STRUCTURE_WORDS:
                continue
            owners = self._distinctive.get(token)
            if owners and len(owners) == 1:
                name = owners[0]
                return name, "possible", (
                    f"'{written}' shares the distinctive word '{token}' with '{name}'")
        return None, "none", "no watched name in this story"


def recall_report(cases: Iterable[Tuple[str, str, bool]],
                  matcher_for=None) -> dict:
    """Score the matcher against (watch_name, written_form, should_match) cases.

    'possible' counts as a catch, not a miss: the analyst sees it flagged for
    verification, which is the outcome we want for a genuinely ambiguous name.
    """
    tp = fn = fp = amb = 0
    misses, false_hits = [], []
    for watch, written, should in cases:
        m = (matcher_for or WatchlistMatcher)([watch])
        name, confidence, _reason = m.match(written)
        hit = name is not None
        if confidence == "possible":
            amb += 1
        if should and hit:
            tp += 1
        elif should and not hit:
            fn += 1
            misses.append((watch, written))
        elif not should and confidence == "confirmed":
            fp += 1
            false_hits.append((watch, written))
    total = tp + fn
    return {"recall": (tp / total) if total else 0.0, "matched": tp,
            "missed": fn, "false_positives": fp, "flagged_possible": amb,
            "misses": misses, "false_hits": false_hits}
