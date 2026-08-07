"""
The riskGPT digital worker: an agentic loop over the corpus toolset.

The assistant is given the MOVES, not a workflow — list what exists, read one or
many documents, three kinds of search, look up a company, ask what changed — and
decides for itself how to answer. "What changed at OSFI recently?" might be a
changes call; "what is SpaceX going through?" is more likely an entity lookup
followed by reads. Prescribing one path would cap it at the path we imagined.

Two things keep it honest:

  every claim cites a doc_id it actually opened, and the transcript of tool
  calls is returned alongside the answer, so a reviewer can see the route;

  page context is explicit. In ACTIVE mode the assistant is told what the person
  is looking at and starts there; in PASSIVE mode it ignores the screen and goes
  to the corpus. The person chooses, and the choice is visible.
"""

from __future__ import annotations

import json
import re
from typing import Any, Callable, Dict, List, Optional, Tuple

MAX_STEPS = 12
MAX_TOOL_CHARS = 6000

SYSTEM = """You are riskGPT, a research assistant for a bank's credit and market
risk teams. You answer from a corpus of regulatory documents and financial news
that has already been collected — never from memory or the open internet.

HOW TO WORK
- Decide your own route. You have listing, reading, and three kinds of search.
- Prefer several small, targeted calls over one broad one.
- corpus_search_bm25 for topics; corpus_search_keyword for exact terms, rule
  numbers or tickers; corpus_entity_lookup for a company by any spelling;
  corpus_changes for "what's new"; corpus_list_sources / corpus_list_files to
  see what exists; corpus_read / corpus_read_many to actually read documents.
- Read before you conclude. A search snippet is a pointer, not evidence.
- If the corpus does not answer the question, say exactly that, and say what it
  DOES contain on the subject. Never fill a gap with general knowledge.

HOW TO ANSWER
- Lead with the answer. Be specific and brief.
- NEVER narrate your process. Do not write "let me check", "I now have a
  picture", "let me compile" or any commentary about your own steps. The reader
  wants the finding, not the search.
- Start directly with the substance — a heading or the key sentence.
- Cite the doc_id of every document you used, inline, like [doc_id].
- Give dates and sources for facts. Say when something is a single-source claim.
- You report what the corpus says; the analyst decides what to do about it.
"""

# The tools the worker may use. Names only — the schemas come from the tool
# registry, so adding a tool to the registry offers it here without a code edit.
DEFAULT_TOOLSET = [
    "corpus_list_sources", "corpus_list_files", "corpus_read", "corpus_read_many",
    "corpus_search_keyword", "corpus_search_bm25", "corpus_search_similar",
    "corpus_changes", "corpus_entity_lookup", "corpus_stats",
]


def _tool_specs(names: List[str]) -> List[dict]:
    """Read the tool contracts from the registry — never restate them here."""
    specs: List[dict] = []
    try:
        from sajha.tools.tools_registry import ToolsRegistry
        registry = ToolsRegistry()
        for name in names:
            cfg = (registry.tool_configs or {}).get(name)
            if not cfg:
                continue
            specs.append({"type": "function", "function": {
                "name": name,
                "description": cfg.get("description", ""),
                "parameters": cfg.get("inputSchema") or {"type": "object",
                                                         "properties": {}}}})
    except Exception:  # noqa: BLE001
        pass
    return specs


def _run_tool(name: str, arguments: Dict[str, Any]) -> Any:
    from sajha.tools.tools_registry import ToolsRegistry
    tool = ToolsRegistry().get_tool(name)
    if tool is None:
        return {"error": f"unknown tool {name}"}
    return tool.execute(arguments or {})


def page_brief(page: Optional[dict]) -> str:
    """What the person is looking at, in one line the model can act on."""
    if not page:
        return ""
    bits = [f"They are on the '{page.get('label') or page.get('view')}' page"]
    if page.get("lane"):
        bits.append(f"in the {page['lane']} lane")
    if page.get("day"):
        bits.append(f"showing {page['day']}")
    return " ".join(bits) + "."


def answer(question: str, *, page: Optional[dict] = None,
           context_mode: str = "active", toolset: Optional[List[str]] = None,
           client=None, max_steps: int = MAX_STEPS) -> dict:
    """Run the loop. Returns the answer plus the route it took."""
    question = (question or "").strip()
    if not question:
        return {"ok": False, "answer": "Ask a question about the corpus.",
                "steps": [], "generator": "none"}

    if client is None:
        from sajha.regagg.extraction import _provider_from_env
        provider, client = _provider_from_env()
        if client is None or not hasattr(client, "chat"):
            return {"ok": False, "generator": "unconfigured", "steps": [],
                    "answer": "No model is configured on this install, so the "
                              "assistant cannot run. Set DEEPSEEK_API_KEY (or "
                              "point DEEPSEEK_BASE_URL at a local model) and it "
                              "will use the same corpus tools the app uses."}
    else:
        provider = "test"

    names = toolset or DEFAULT_TOOLSET
    specs = _tool_specs(names)
    system = SYSTEM
    if context_mode == "active" and page:
        system += ("\n\nCONTEXT: " + page_brief(page) +
                   " Start from what is on that page when it is relevant, then "
                   "widen to the rest of the corpus.")
    else:
        system += ("\n\nCONTEXT: Ignore what is on screen; answer from the whole "
                   "corpus.")

    messages: List[dict] = [{"role": "system", "content": system},
                            {"role": "user", "content": question}]
    steps: List[dict] = []
    used_docs: List[str] = []

    for step in range(max_steps):
        # Running out of budget mid-investigation and returning nothing wastes
        # everything gathered. Two steps out, ask for the answer it can already
        # support — a partial answer with citations beats an apology.
        remaining = max_steps - step
        if remaining == 2:
            messages.append({"role": "user", "content":
                "You are near the end of your tool budget. Answer now from what "
                "you have already read, citing the doc_ids you opened. If some "
                "part is unresolved, say what is missing."})
        try:
            msg = client.chat(messages, tools=specs)
        except Exception as e:  # noqa: BLE001
            return {"ok": False, "generator": "error", "steps": steps,
                    "answer": "The assistant could not be reached. The corpus "
                              "itself is unaffected — Explore has the documents.",
                    "detail": str(e)[:200]}

        calls = msg.get("tool_calls") or []
        if not calls:
            text = strip_narration(msg.get("content") or "")
            return {"ok": bool(text), "answer": text or "No answer produced.",
                    "steps": steps, "documents": used_docs[:40],
                    "generator": f"agent:{provider}"}

        messages.append({"role": "assistant", "content": msg.get("content") or "",
                         "tool_calls": calls})
        for call in calls:
            fn = (call.get("function") or {})
            name = fn.get("name", "")
            try:
                args = json.loads(fn.get("arguments") or "{}")
            except (TypeError, ValueError):
                args = {}
            try:
                result = _run_tool(name, args)
            except Exception as e:  # noqa: BLE001 — a failed tool is a fact, not a crash
                result = {"error": str(e)[:200]}
            payload = json.dumps(result, default=str)[:MAX_TOOL_CHARS]
            steps.append({"tool": name, "arguments": args,
                          "result_chars": len(payload)})
            for key in ("doc_id",):
                used_docs.extend(_collect(result, key))
            messages.append({"role": "tool", "tool_call_id": call.get("id"),
                             "name": name, "content": payload})

    return {"ok": False, "generator": f"agent:{provider}", "steps": steps,
            "answer": "I could not settle this within the step budget. The tool "
                      "calls above show how far I got — narrowing the question "
                      "usually resolves it.",
            "documents": used_docs[:40]}


_NARRATION = re.compile(
    r"^\s*(?:(?:okay|ok|alright|now|good)[,.]?\s*)?"
    r"(?:i (?:now )?have|i(?:'ll| will)|let me|based on (?:my|the) (?:search|research|tool)"
    r"|here(?:'s| is) what i (?:found|have)|i(?:'ve| have) (?:now )?(?:gathered|compiled|checked))"
    r"[^\n]*\n+", re.IGNORECASE)


def strip_narration(text: str) -> str:
    """Remove the model thinking out loud before the answer.

    Asking it not to narrate helps but does not eliminate it; the reader wants
    the finding, so any leading 'let me check…' paragraphs are cut until real
    content starts.
    """
    out = (text or "").lstrip()
    for _ in range(4):
        new = _NARRATION.sub("", out, count=1).lstrip()
        if new == out:
            break
        out = new
    return out


def _collect(obj: Any, key: str, out: Optional[List[str]] = None) -> List[str]:
    out = out if out is not None else []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key and isinstance(v, str):
                out.append(v)
            else:
                _collect(v, key, out)
    elif isinstance(obj, list):
        for v in obj:
            _collect(v, key, out)
    return out
