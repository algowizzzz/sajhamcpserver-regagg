"""Tavily financial-news search, for one named company at a time.

Deliberately NOT built on ``sajha.tools.impl.tavily_tool_refactored``. That tool
also has a demo mode, but an unlabelled one: with no key it returns invented
results through the same shape as real ones, and nothing downstream can tell
the difference. A fabricated headline against a real counterparty is worse than
an empty table, because nothing about it looks wrong.

There is a stand-in here — the table has to be buildable before the key exists —
but it is labelled at every level that can carry a label: the hit says ``demo``,
the stored row says ``mode='demo'``, and the page shows a banner that cannot be
dismissed. Set TAVILY_API_KEY and all of it switches off; nothing else changes.

Cost is the other reason this module is thin and explicit. Every real call is a
billed credit, a persona can hold hundreds of names, and a sweep that quietly
re-searched everything on each page load would be an expensive mistake nobody
noticed until the invoice. Callers pass a budget and are told what they spent.
"""

from __future__ import annotations

import datetime as _dt
import os
from dataclasses import dataclass
from typing import Dict, List, Optional

ENDPOINT = "https://api.tavily.com/search"
TIMEOUT = 20
MAX_RESULTS = 3


class NotConfigured(RuntimeError):
    """No API key. Not an outage — a setup step that has not happened."""


@dataclass
class Hit:
    title: str
    url: str
    snippet: str
    source: str = ""
    published: str = ""
    score: float = 0.0
    demo: bool = False          # invented, and every layer above must say so

    def as_dict(self) -> dict:
        return {"title": self.title, "url": self.url, "snippet": self.snippet,
                "source": self.source, "published": self.published,
                "score": self.score, "demo": self.demo}


def api_key() -> Optional[str]:
    return (os.getenv("TAVILY_API_KEY") or os.getenv("tavily_api_key") or "").strip() or None


def configured() -> bool:
    return api_key() is not None


def _host(url: str) -> str:
    try:
        from urllib.parse import urlparse
        return (urlparse(url).netloc or "").replace("www.", "")
    except Exception:  # noqa: BLE001
        return ""


class TavilyNews:
    """One search per company name, with the spend made visible."""

    def __init__(self, key: Optional[str] = None, *, depth: str = "basic",
                 days: int = 7, session=None):
        self.key = key or api_key()
        self.depth = depth if depth in ("basic", "advanced") else "basic"
        self.days = max(1, min(int(days or 7), 30))
        self.searches = 0
        self.errors = 0
        self._session = session

    @property
    def credits(self) -> int:
        """Tavily bills advanced search at roughly twice basic."""
        return self.searches * (2 if self.depth == "advanced" else 1)

    def _post(self, payload: dict) -> dict:
        if self._session is not None:            # injected in tests
            return self._session.post(ENDPOINT, json=payload, timeout=TIMEOUT).json()
        import requests
        r = requests.post(ENDPOINT, json=payload, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()

    def search(self, name: str, *, extra: str = "") -> List[Hit]:
        """Financial news for one entity. Raises NotConfigured without a key."""
        if not self.key:
            raise NotConfigured(
                "TAVILY_API_KEY is not set on this install, so entity news "
                "cannot be fetched. The table is left empty rather than filled "
                "with placeholder results.")
        query = f'"{name}" {extra}'.strip() if extra else f'"{name}"'
        payload = {"api_key": self.key, "query": query, "topic": "news",
                   "search_depth": self.depth, "days": self.days,
                   "max_results": MAX_RESULTS, "include_answer": False,
                   "include_raw_content": False, "include_images": False}
        self.searches += 1
        try:
            data = self._post(payload) or {}
        except Exception as e:  # noqa: BLE001 — one dead name must not kill a sweep
            self.errors += 1
            raise RuntimeError(str(e)[:200]) from e

        hits: List[Hit] = []
        for r in (data.get("results") or [])[:MAX_RESULTS]:
            url = str(r.get("url") or "")
            hits.append(Hit(
                title=str(r.get("title") or "").strip(),
                url=url,
                snippet=str(r.get("content") or "").strip(),
                source=_host(url),
                published=str(r.get("published_date") or "")[:10],
                score=float(r.get("score") or 0.0),
            ))
        return hits


class DemoNews:
    """Stand-in results so the table can be built and reviewed without a key.

    Everything it returns is invented. That is fine for building the page and
    dangerous the moment it is mistaken for real, so it is marked at every
    level that can carry a mark: each hit says ``demo``, the row records
    ``mode='demo'``, and the page shows a banner it cannot dismiss. Setting
    TAVILY_API_KEY switches all of that off and nothing else changes.

    Output is deterministic per (name, day): reloading the page shows the same
    invented story rather than a new one each time, which would make the demo
    feel broken and hide real caching bugs.
    """

    TEMPLATES = [
        ("{name} reports Q{q} results, net income up {pc}% year on year",
         "The company said quarterly net income rose {pc}% on stronger fee income, "
         "with management repeating full-year guidance.", "earnings"),
        ("{name} prices ${amt}m senior notes due 20{yr}",
         "Proceeds are earmarked for refinancing near-term maturities. Books were "
         "reported multiple times covered.", "funding"),
        ("Ratings agency revises {name} outlook to {outlook}",
         "The agency cited leverage trending {dir} its downgrade threshold, while "
         "affirming the long-term issuer rating.", "rating"),
        ("{name} draws regulatory scrutiny over disclosure practices",
         "A supervisor has asked for additional information following a review of "
         "the group's periodic filings. No penalty has been proposed.", "regulatory"),
        ("{name} to acquire minority stake in regional peer",
         "The transaction is expected to close next quarter subject to approval and "
         "is not expected to affect the acquirer's capital position.", "deal"),
        ("{name} names new chief financial officer",
         "The appointment follows the previous officer's move to another firm. The "
         "company said its financial strategy is unchanged.", "governance"),
    ]
    SOURCES = ["reuters.com", "bloomberg.com", "ft.com", "wsj.com",
               "americanbanker.com", "spglobal.com"]

    def __init__(self, *, day: str = "", coverage: float = 0.45, **_kw):
        self.day = day
        self.coverage = coverage
        self.searches = 0
        self.errors = 0

    @property
    def credits(self) -> int:
        return 0        # nothing was billed, and the UI should say zero

    def _rng(self, name: str):
        import hashlib
        import random
        seed = hashlib.sha256(f"{name}|{self.day}".encode()).hexdigest()[:12]
        return random.Random(int(seed, 16))

    def search(self, name: str, *, extra: str = "") -> List[Hit]:
        self.searches += 1
        rng = self._rng(name)
        # Most names are not in the news on a given day. A demo where every row
        # has a story would misrepresent what the real table looks like.
        if rng.random() > self.coverage:
            return []
        title_t, body_t, kind = rng.choice(self.TEMPLATES)
        vals = {"name": name, "q": rng.randint(1, 4), "pc": rng.randint(3, 42),
                "amt": rng.choice([250, 300, 400, 500, 750, 1000]),
                "yr": rng.randint(28, 36),
                "outlook": rng.choice(["negative", "stable", "positive"]),
                "dir": rng.choice(["toward", "away from"])}
        src = rng.choice(self.SOURCES)
        when = self.day or _dt.date.today().isoformat()
        return [Hit(title=title_t.format(**vals),
                    url=f"https://{src}/demo/{kind}/{abs(hash(name)) % 10**7}",
                    snippet=body_t.format(**vals),
                    source=src, published=when, score=round(rng.uniform(.5, .95), 2),
                    demo=True)]


def client_for(day: str = "", *, depth: str = "basic", days: int = 7):
    """The real client when a key is present, the marked stand-in when not."""
    return TavilyNews(depth=depth, days=days) if configured() else DemoNews(day=day)


def estimate(entities: int, *, depth: str = "basic") -> dict:
    """What a sweep will cost before anyone starts it.

    Shown in the UI next to the button. A person about to spend money should
    see the number before the click, not after it.
    """
    per = 2 if depth == "advanced" else 1
    credits = entities * per
    return {"entities": entities, "depth": depth, "credits": credits,
            "note": f"{credits} Tavily credit(s) — one search per name"}
