"""
The corpus as a queryable surface: list it, read it, search it.

Everything the assistant can reach lives in ``data/markdown`` — the same files
the UI renders, so an answer can always be traced to a document a person can
open. The index is built lazily from those files and their frontmatter, and is
invalidated by mtime, so a poll that adds stories is picked up without a
restart.

Search comes in three flavours because they fail differently:

    keyword     exact terms — "SA-CCR", a company name, a rule number
    bm25        ranked relevance over the whole corpus, robust to phrasing
    similar     documents that look like a given one (TF-IDF cosine)

No embedding service is required for any of them: an on-prem install should
not need a second network dependency to answer "what changed at OSFI".
"""

from __future__ import annotations

import math
import os
import re
import threading
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

MARKDOWN_ROOT = Path("data/markdown")
_TOKEN = re.compile(r"[a-z0-9][a-z0-9'&.-]*")
STOP = {
    "the", "and", "for", "with", "that", "this", "from", "have", "has", "was",
    "were", "are", "will", "would", "been", "its", "it's", "their", "they",
    "not", "but", "you", "your", "our", "all", "can", "may", "more", "than",
    "into", "after", "over", "said", "says", "new", "one", "two", "about",
}


def tokenize(text: str) -> List[str]:
    return [t for t in _TOKEN.findall((text or "").lower())
            if len(t) > 2 and t not in STOP]


def _parse_frontmatter(raw: str) -> Tuple[Dict[str, str], str]:
    """Split the YAML frontmatter our projection writes from the body."""
    if not raw.startswith("---"):
        return {}, raw
    end = raw.find("\n---", 3)
    if end == -1:
        return {}, raw
    meta: Dict[str, str] = {}
    for line in raw[3:end].splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"')
    return meta, raw[end + 4:].lstrip("\n")


class CorpusIndex:
    """Lazily built, mtime-invalidated view over the markdown corpus."""

    def __init__(self, root: Optional[Path] = None):
        self.root = Path(root or os.getenv("REGAGG_MARKDOWN_ROOT", MARKDOWN_ROOT))
        self._lock = threading.Lock()
        self._docs: List[dict] = []
        self._df: Counter = Counter()
        self._postings: Dict[str, List[Tuple[int, int]]] = {}
        self._built_at: float = 0.0
        self._signature: Tuple[int, float] = (0, 0.0)

    # ── building ────────────────────────────────────────────────────────────

    def _current_signature(self) -> Tuple[int, float]:
        """Cheap staleness probe: file count + newest mtime."""
        n, newest = 0, 0.0
        if not self.root.exists():
            return (0, 0.0)
        for p in self.root.rglob("*.md"):
            n += 1
            try:
                newest = max(newest, p.stat().st_mtime)
            except OSError:
                continue
        return (n, newest)

    def ensure(self) -> None:
        sig = self._current_signature()
        with self._lock:
            if self._docs and sig == self._signature:
                return
            docs: List[dict] = []
            for path in sorted(self.root.rglob("*.md")):
                try:
                    raw = path.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                meta, body = _parse_frontmatter(raw)
                rel = path.relative_to(self.root)
                parts = rel.parts
                docs.append({
                    "path": str(rel),
                    "stage": parts[0] if parts else "",          # web | policy
                    "source": meta.get("regulator") or (parts[1] if len(parts) > 1 else ""),
                    "doc_type": meta.get("doc_type") or (parts[2] if len(parts) > 2 else ""),
                    "doc_id": path.stem,
                    "title": meta.get("title") or path.stem,
                    "published": meta.get("published") or "",
                    "source_url": meta.get("source_url") or "",
                    "status": meta.get("status") or "",
                    "version": meta.get("version") or "",
                    "body": body,
                    "mtime": path.stat().st_mtime,
                })
            postings: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
            df: Counter = Counter()
            for i, d in enumerate(docs):
                counts = Counter(tokenize(f"{d['title']} {d['body'][:8000]}"))
                d["length"] = sum(counts.values()) or 1
                for term, c in counts.items():
                    postings[term].append((i, c))
                    df[term] += 1
            self._docs, self._postings, self._df = docs, dict(postings), df
            self._signature, self._built_at = sig, datetime.now(timezone.utc).timestamp()

    # ── listing ─────────────────────────────────────────────────────────────

    def sources(self, lane: Optional[str] = None,
                lane_of=None) -> List[dict]:
        """Every source in the corpus with counts and date span."""
        self.ensure()
        agg: Dict[str, dict] = {}
        for d in self._docs:
            s = agg.setdefault(d["source"], {
                "source": d["source"], "documents": 0, "stages": set(),
                "doc_types": set(), "first": "", "last": ""})
            s["documents"] += 1
            s["stages"].add(d["stage"])
            if d["doc_type"]:
                s["doc_types"].add(d["doc_type"])
            pub = d["published"]
            if pub:
                s["first"] = min(s["first"] or pub, pub)
                s["last"] = max(s["last"], pub)
        out = []
        for s in agg.values():
            lane_name = lane_of(s["source"]) if lane_of else None
            if lane and lane_name and lane_name != lane:
                continue
            out.append({**s, "lane": lane_name,
                        "stages": sorted(s["stages"]),
                        "doc_types": sorted(s["doc_types"])})
        return sorted(out, key=lambda s: -s["documents"])

    def filter(self, source: Optional[Iterable[str]] = None,
               doc_type: Optional[Iterable[str]] = None,
               stage: Optional[str] = None,
               date_from: Optional[str] = None, date_to: Optional[str] = None,
               title_contains: Optional[str] = None) -> List[dict]:
        self.ensure()
        srcs = {s.lower() for s in source} if source else None
        types = {t.lower() for t in doc_type} if doc_type else None
        needle = (title_contains or "").lower()
        out = []
        for d in self._docs:
            if srcs and d["source"].lower() not in srcs:
                continue
            if types and d["doc_type"].lower() not in types:
                continue
            if stage and d["stage"] != stage:
                continue
            if date_from and (d["published"] or "9999") < date_from:
                continue
            if date_to and (d["published"] or "0000") > date_to:
                continue
            if needle and needle not in d["title"].lower():
                continue
            out.append(d)
        return out

    def get(self, doc_id: Optional[str] = None,
            path: Optional[str] = None) -> Optional[dict]:
        self.ensure()
        for d in self._docs:
            if (path and d["path"] == path) or (doc_id and d["doc_id"] == doc_id):
                return d
        return None

    # ── search ──────────────────────────────────────────────────────────────

    def keyword(self, query: str, limit: int = 20, **filters) -> List[dict]:
        """Exact term matching — what you want for a rule number or a ticker."""
        pool = self.filter(**filters)
        terms = [t for t in tokenize(query)] or [(query or "").lower()]
        hits = []
        for d in pool:
            hay = f"{d['title']} {d['body']}".lower()
            n = sum(hay.count(t) for t in terms)
            if n:
                hits.append((n, d))
        hits.sort(key=lambda x: -x[0])
        return [_summarise(d, score=n, why=f"{n} keyword hit{'s' if n > 1 else ''}")
                for n, d in hits[:limit]]

    def bm25(self, query: str, limit: int = 20, k1: float = 1.5, b: float = 0.75,
             **filters) -> List[dict]:
        """Okapi BM25 over the corpus, with the same filters as listing."""
        self.ensure()
        pool = self.filter(**filters)
        allowed = {d["path"] for d in pool} if filters else None
        terms = tokenize(query)
        if not terms or not self._docs:
            return []
        N = len(self._docs)
        avgdl = sum(d["length"] for d in self._docs) / max(N, 1)
        scores: Dict[int, float] = defaultdict(float)
        for term in terms:
            postings = self._postings.get(term)
            if not postings:
                continue
            idf = math.log(1 + (N - self._df[term] + 0.5) / (self._df[term] + 0.5))
            for i, tf in postings:
                dl = self._docs[i]["length"]
                scores[i] += idf * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * dl / avgdl))
        ranked = sorted(scores.items(), key=lambda kv: -kv[1])
        out = []
        for i, s in ranked:
            d = self._docs[i]
            if allowed is not None and d["path"] not in allowed:
                continue
            out.append(_summarise(d, score=round(s, 3), why="bm25 relevance"))
            if len(out) >= limit:
                break
        return out

    def similar(self, doc_id: Optional[str] = None, text: Optional[str] = None,
                limit: int = 10, **filters) -> List[dict]:
        """Documents that read like this one (TF-IDF cosine, no embeddings)."""
        self.ensure()
        if doc_id and not text:
            seed = self.get(doc_id=doc_id)
            if not seed:
                return []
            text = f"{seed['title']} {seed['body'][:4000]}"
        qcounts = Counter(tokenize(text or ""))
        if not qcounts:
            return []
        N = len(self._docs)
        qvec = {t: (1 + math.log(c)) * math.log(1 + N / (1 + self._df.get(t, 0)))
                for t, c in qcounts.items()}
        qnorm = math.sqrt(sum(v * v for v in qvec.values())) or 1.0
        pool = self.filter(**filters)
        allowed = {d["path"] for d in pool} if filters else None
        scores: Dict[int, float] = defaultdict(float)
        for term, qw in qvec.items():
            for i, tf in self._postings.get(term, ()):
                idf = math.log(1 + N / (1 + self._df[term]))
                scores[i] += qw * (1 + math.log(tf)) * idf
        out = []
        for i, s in sorted(scores.items(), key=lambda kv: -kv[1]):
            d = self._docs[i]
            if doc_id and d["doc_id"] == doc_id:
                continue
            if allowed is not None and d["path"] not in allowed:
                continue
            denom = qnorm * math.sqrt(d["length"]) or 1.0
            out.append(_summarise(d, score=round(s / denom, 4), why="similar wording"))
            if len(out) >= limit:
                break
        return out

    def stats(self) -> dict:
        self.ensure()
        by_stage: Counter = Counter(d["stage"] for d in self._docs)
        by_type: Counter = Counter(d["doc_type"] for d in self._docs if d["doc_type"])
        by_day: Counter = Counter(d["published"] for d in self._docs if d["published"])
        return {"documents": len(self._docs), "sources": len({d["source"] for d in self._docs}),
                "by_stage": dict(by_stage), "by_doc_type": dict(by_type),
                "days_covered": len(by_day),
                "recent_days": sorted(by_day.items(), reverse=True)[:14],
                "root": str(self.root), "terms_indexed": len(self._postings)}


def _summarise(d: dict, score: float = 0.0, why: str = "", body_chars: int = 320) -> dict:
    text = re.sub(r"\s+", " ", d["body"]).strip()
    return {"doc_id": d["doc_id"], "path": d["path"], "title": d["title"],
            "source": d["source"], "doc_type": d["doc_type"], "stage": d["stage"],
            "published": d["published"], "source_url": d["source_url"],
            "excerpt": text[:body_chars], "score": score, "why": why}


_INDEX: Optional[CorpusIndex] = None


def get_index() -> CorpusIndex:
    global _INDEX
    if _INDEX is None:
        _INDEX = CorpusIndex()
    return _INDEX
