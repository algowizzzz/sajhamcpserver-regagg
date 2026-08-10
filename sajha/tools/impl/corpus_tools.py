"""
MCP tools over the markdown corpus — the toolset a digital worker reasons with.

Deliberately a PLETHORA rather than a workflow. The worker is not told how to
answer "what changed at OSFI"; it is given the moves — list what exists, read
one or many documents, search three different ways, look up a company, ask what
changed since a date — and left to compose them. A tool that forces one path
would cap the assistant at whatever path we imagined.

Everything reads ``data/markdown``: the same files the UI renders, so any answer
can be traced to a document the person can open. All are read-only and stateless.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from sajha.tools.base_mcp_tool import BaseMCPTool


def _lane_of_source(source: str) -> Optional[str]:
    """news | regulatory, taken from the regulator table (never hard-coded)."""
    try:
        from sajha.regagg import runtime
        from sajha.regagg.models import Regulator
        reg = runtime.get_session().get(Regulator, source)
        return getattr(reg, "category", None) if reg is not None else None
    except Exception:  # noqa: BLE001 — the corpus is usable without the DB
        return None


class _CorpusTool(BaseMCPTool):
    def _index(self):
        from sajha.regagg.corpus_index import get_index
        return get_index()

    def get_input_schema(self) -> Dict:
        """Serve the schema from the tool's JSON config — one definition, not two."""
        cfg = getattr(self, "config", None) or {}
        return cfg.get("inputSchema") or {"type": "object", "properties": {}}

    def get_output_schema(self) -> Dict:
        return {"type": "object"}

    @staticmethod
    def _filters(a: Dict[str, Any]) -> Dict[str, Any]:
        out: Dict[str, Any] = {}
        if a.get("source"):
            out["source"] = a["source"] if isinstance(a["source"], list) else [a["source"]]
        if a.get("doc_type"):
            out["doc_type"] = (a["doc_type"] if isinstance(a["doc_type"], list)
                               else [a["doc_type"]])
        for k in ("stage", "date_from", "date_to", "title_contains"):
            if a.get(k):
                out[k] = a[k]
        return out


class CorpusListSourcesTool(_CorpusTool):
    """What exists at all — the map before the territory."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        lane = arguments.get("lane")
        srcs = self._index().sources(lane=lane, lane_of=_lane_of_source)
        return {"sources": srcs, "count": len(srcs),
                "note": "lane is 'regulatory' or 'news'; use source ids with the "
                        "other corpus tools"}


class CorpusListFilesTool(_CorpusTool):
    """Directory listing with filters — what documents do we hold?"""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        limit = int(arguments.get("limit", 50))
        offset = int(arguments.get("offset", 0))
        docs = self._index().filter(**self._filters(arguments))
        docs.sort(key=lambda d: (d.get("published") or "", d["title"]), reverse=True)
        page = docs[offset:offset + limit]
        return {"total": len(docs), "offset": offset, "returned": len(page),
                "files": [{"doc_id": d["doc_id"], "path": d["path"],
                           "title": d["title"], "source": d["source"],
                           "doc_type": d["doc_type"], "stage": d["stage"],
                           "published": d["published"],
                           "source_url": d["source_url"]} for d in page]}


class CorpusReadTool(_CorpusTool):
    """Read one document, whole or head."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        doc = self._index().get(doc_id=arguments.get("doc_id"),
                                path=arguments.get("path"))
        if doc is None:
            return {"found": False,
                    "error": "No such document. Use corpus_list_files or a search "
                             "tool to get a doc_id."}
        body = doc["body"]
        total = len(body)
        chars = max(1, int(arguments.get("max_chars", 40000)))
        offset = max(0, int(arguments.get("offset", 0)))
        window = body[offset:offset + chars]
        end = offset + len(window)
        more = end < total
        out = {"found": True, "doc_id": doc["doc_id"], "path": doc["path"],
               "title": doc["title"], "source": doc["source"],
               "doc_type": doc["doc_type"], "published": doc["published"],
               "source_url": doc["source_url"], "status": doc["status"],
               "version": doc["version"],
               # The reader has to be able to tell "the corpus lacks this" from
               # "I have not read that far yet". A bare `truncated: true` was
               # reported to a user as a gap in the corpus.
               "total_chars": total, "offset": offset, "chars_returned": len(window),
               "pct_of_document": round(end / total * 100, 1) if total else 100.0,
               "truncated": more,
               "next_offset": end if more else None,
               "markdown": window}
        if more:
            out["note"] = (f"You have read to character {end:,} of {total:,} "
                           f"({out['pct_of_document']}%). Call corpus_read again "
                           f"with offset={end} for the next part. Do NOT describe "
                           f"the unread part as missing from the corpus.")
        return out


class CorpusReadManyTool(_CorpusTool):
    """Read several documents in one call — comparison without ten round trips."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        ids: List[str] = arguments.get("doc_ids") or []
        per = max(1, int(arguments.get("max_chars_each", 12000)))
        ix, out, partial = self._index(), [], []
        for did in ids[:20]:
            doc = ix.get(doc_id=did)
            if doc is None:
                out.append({"doc_id": did, "found": False})
                continue
            body, total = doc["body"], len(doc["body"])
            row = {"doc_id": did, "found": True, "title": doc["title"],
                   "source": doc["source"], "published": doc["published"],
                   "source_url": doc["source_url"],
                   "total_chars": total, "chars_returned": min(per, total),
                   "truncated": total > per,
                   "markdown": body[:per]}
            if row["truncated"]:
                # This tool exists for comparison. A long document compared on
                # its first 12k is a comparison of introductions, so name the
                # ones that need a full read rather than letting it pass.
                row["next_offset"] = per
                partial.append(did)
            out.append(row)
        res = {"requested": len(ids), "returned": len(out), "documents": out}
        if partial:
            res["note"] = ("Only the opening of these documents was returned: "
                           + ", ".join(partial)
                           + ". Use corpus_read with offset to read one in full "
                             "before drawing a conclusion about its contents.")
        return res


class CorpusKeywordSearchTool(_CorpusTool):
    """Exact terms — a rule number, a ticker, a company written one way."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        res = self._index().keyword(arguments.get("query", ""),
                                    limit=int(arguments.get("limit", 20)),
                                    **self._filters(arguments))
        return {"query": arguments.get("query", ""), "matches": len(res),
                "results": res}


class CorpusBM25SearchTool(_CorpusTool):
    """Ranked relevance over the whole corpus — robust to how it was phrased."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        res = self._index().bm25(arguments.get("query", ""),
                                 limit=int(arguments.get("limit", 20)),
                                 **self._filters(arguments))
        return {"query": arguments.get("query", ""), "matches": len(res),
                "results": res}


class CorpusSimilarTool(_CorpusTool):
    """Documents that read like this one, or like a passage of text."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        res = self._index().similar(doc_id=arguments.get("doc_id"),
                                    text=arguments.get("text"),
                                    limit=int(arguments.get("limit", 10)),
                                    **self._filters(arguments))
        return {"matches": len(res), "results": res}


class CorpusChangesTool(_CorpusTool):
    """What entered or changed since a date — the 'what's new' question."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        since = arguments.get("since")
        lane = arguments.get("lane")
        limit = int(arguments.get("limit", 40))
        # A source filter has to bite here. Silently returning every source when
        # one was asked for reads as "nothing changed at OSFI" — a wrong answer
        # dressed as an empty one.
        wanted = arguments.get("source")
        wanted = ({s.lower() for s in wanted} if isinstance(wanted, list)
                  else {wanted.lower()} if wanted else None)
        try:
            from sajha.regagg import queries_ui, runtime
            session = runtime.get_session()
            days = int(arguments.get("days", 7))
            data = queries_ui.changes(session, days=days,
                                      category=lane, min_band=arguments.get("min_band"))
            items = data.get("changes", [])
            if wanted:
                items = [c for c in items
                         if str(c.get("regulator_id", "")).lower() in wanted]
            items = items[:limit]
            return {"days": days, "lane": lane,
                    "source": sorted(wanted) if wanted else None,
                    "count": len(items),
                    "counts": None if wanted else data.get("counts"),
                    "changes": items,
                    "note": "kind 'new' means first collected (which on a first "
                            "crawl includes older documents); 'revised' means the "
                            "text changed and a diff exists"}
        except Exception:  # noqa: BLE001 — fall back to the files themselves
            docs = self._index().filter(date_from=since,
                                        **self._filters(arguments))
            docs.sort(key=lambda d: d.get("published") or "", reverse=True)
            return {"since": since, "count": len(docs),
                    "files": [{"doc_id": d["doc_id"], "title": d["title"],
                               "source": d["source"], "published": d["published"]}
                              for d in docs[:limit]]}


class CorpusEntityLookupTool(_CorpusTool):
    """Find every document that names a company, however it was written.

    Uses the same matcher the desks use, so "Goodfood" finds "Goodfood Market
    Corp." and an ambiguous match is reported as such rather than asserted.
    """

    def execute(self, arguments: Dict[str, Any]) -> Any:
        name = (arguments.get("name") or "").strip()
        if not name:
            return {"error": "name is required"}
        limit = int(arguments.get("limit", 25))
        confirmed, possible = [], []
        try:
            from sajha.regagg.matching import WatchlistMatcher
            matcher = WatchlistMatcher([name])
        except Exception:  # noqa: BLE001
            matcher = None

        from sajha.regagg import runtime
        from sajha.regagg.models import Document
        try:
            session = runtime.get_session()
            docs = session.query(Document).all()
        except Exception:  # noqa: BLE001
            docs = []
        for d in docs:
            ex = getattr(d, "extraction", None) or {}
            for ent in (ex.get("entities") or []):
                written = ent.get("canonical") or ""
                if matcher is None:
                    hit, conf = (name if name.lower() in written.lower() else None), "confirmed"
                else:
                    hit, conf, _reason = matcher.match(written)
                if not hit:
                    continue
                row = {"doc_id": d.doc_id, "source": d.regulator_id,
                       "title": d.title, "published": str(d.published_date or ""),
                       "written_as": written, "event_type": ex.get("event_type"),
                       "url": d.source_url}
                (confirmed if conf == "confirmed" else possible).append(row)
                break
        # the corpus text is the backstop when nothing was extracted
        text_hits = self._index().keyword(name, limit=limit)
        return {"name": name, "confirmed": confirmed[:limit],
                "possible": possible[:limit], "mentions_in_text": text_hits,
                "note": "'possible' means the name is ambiguous (e.g. a one-word "
                        "watchlist name inside a longer company name) — verify "
                        "before relying on it"}


class CorpusStatsTool(_CorpusTool):
    """Shape of the corpus: how much, from where, over what period."""

    def execute(self, arguments: Dict[str, Any]) -> Any:
        return self._index().stats()
