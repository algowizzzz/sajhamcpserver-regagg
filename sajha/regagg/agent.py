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
import logging
import re
from typing import Any, Callable, Dict, List, Optional, Tuple

MAX_STEPS = 20

# What one tool result may contribute, and what the whole run may.
#
# MAX_TOOL_CHARS was 6,000 — set when the corpus was news stories. Against a
# 104,000-character capital guideline it delivered 5% of the document, and the
# worker reported the other 95% to a user as "not contained in the corpus".
# The model is not the constraint: this install's provider accepted a
# 400,000-token prompt. What actually overflows is the accumulated transcript,
# so the limit belongs on the RUN, not on each call.
MAX_TOOL_CHARS = 60_000            # ~15k tokens: most documents in one call
TOOL_CHAR_BUDGET = 400_000         # ~100k tokens of tool output across the run

# Below this the worker is told to write up rather than keep reading, because
# an investigation that dies at the budget with nothing in the notepad has to
# start over.
BUDGET_WARN_AT = 80_000

# Room held back from the allowance so the harness can explain a cut without
# the explanation itself overrunning the budget.
_NOTE_RESERVE = 400

_EXHAUSTED = ("[READING BUDGET EXHAUSTED — this tool was not run. Answer now "
              "from what you have read and from your notepad, and say which "
              "document would settle anything still open.]")


def _truncation_note(cut: int, total: int) -> str:
    """Say who did the cutting. The model must not read this as missing data."""
    return (f"\n[TRUNCATED BY THE HARNESS: {cut:,} of {total:,} characters were "
            f"dropped from this result. A limit of the reader, NOT a gap in the "
            f"corpus. Re-read in smaller windows with corpus_read "
            f"offset/max_chars, and write findings to the notepad as you go.]")

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

READING A LONG DOCUMENT
- corpus_read returns a WINDOW, not always the whole file. Every result carries
  total_chars, pct_of_document and next_offset. Check them.
- If next_offset is not null you have not finished the document. Call
  corpus_read again with offset=next_offset and keep going until it is null.
  Detail that matters — tables, numeric thresholds, risk weights, annexes — is
  usually deep in the file, not in the opening paragraphs.
- NEVER say the corpus lacks something you did not read to the end of. "I read
  the first 12% and the tables were not in it" is a fact about your reading;
  "the corpus does not contain the tables" is a claim about the data, and it is
  the one thing you must not get wrong. Page to the end, or say plainly how far
  you read.

YOUR NOTEPAD
- notepad_write records a finding; notepad_read returns it later. Notes persist
  after this reply, so work can be resumed.
- Write as you read, not at the end. Reading forty documents and holding it all
  in your head is what runs you out of room — a note costs a fraction of the
  document it summarises.
- One section per topic or per document, and cite the doc_id in the note.
- notepad_read with no section returns just the index, which is cheap. Read a
  section only when you need it.
- Use it for anything qualitative and long: reading a rulebook end to end,
  comparing versions, building up a picture across many sources.

WHEN A TOOL PUSHES BACK
- A rejected argument names the parameters the tool does accept. Retry with one
  of those. Do not fetch everything and filter it by eye instead — that looks
  like it worked and quietly drops whatever you did not skim.
- Check that a result matches the filter you asked for. If you requested one
  source and other sources come back, the filter did not apply: say so in your
  answer and treat the result as unscoped.
- If you cannot scope a question with the tools you have, say that plainly.
  An unscoped result presented as a scoped one is the one failure the reader
  cannot detect for themselves.

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
    # the only two that write, and only ever the worker's own reasoning
    "notepad_write", "notepad_read",
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
    """Run a tool, but check the call against its contract first.

    The schema the model was handed is the same one validated here, so a
    parameter the tool does not implement comes back as a correctable error
    on the first call instead of being dropped in silence. The model can
    then retry with a filter that exists — or say the corpus cannot answer
    the question — rather than reasoning over a result it believes is
    narrower than it is.
    """
    from sajha.tools.tools_registry import ToolsRegistry
    tool = ToolsRegistry().get_tool(name)
    if tool is None:
        return {"error": f"unknown tool {name}"}
    arguments = arguments or {}
    try:
        tool.validate_arguments(arguments)
    except ValueError as e:
        # Log it too: a rejection only the model sees is a contract gap nobody
        # gets to fix. Repeated entries here name the filter a tool should grow.
        logging.getLogger(__name__).warning("tool contract: %s", e)
        return {"error": str(e), "arguments_rejected": True}
    return tool.execute(arguments)


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
           client=None, max_steps: int = MAX_STEPS,
           owner: Optional[str] = None, notepad: str = "scratch",
           budget: int = TOOL_CHAR_BUDGET) -> dict:
    """Run the loop. Returns the answer plus the route it took."""
    question = (question or "").strip()
    if not question:
        return {"ok": False, "answer": "Ask a question about the corpus.",
                "steps": [], "generator": "none"}

    # Bind the notepad to this request before any tool can touch it. Ownership
    # is never an argument the model supplies.
    from sajha.regagg import notepad as _notepad
    _notepad.set_owner(owner)

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

    # What is already in the notepad, as one line. The contents are not
    # injected — that would put every note back in the prompt on every step,
    # which is the cost the notepad exists to avoid.
    carried = _notepad.summary_line(notepad, owner)
    if carried:
        system += ("\n\nCARRIED OVER: " + carried +
                   " This is your own earlier work on this — read the relevant "
                   "section before repeating a search you have already done.")
    system += f"\n\nYour notepad for this work is named '{notepad}'."

    messages: List[dict] = [{"role": "system", "content": system},
                            {"role": "user", "content": question}]
    steps: List[dict] = []
    used_docs: List[str] = []

    spent = 0
    warned = False

    for step in range(max_steps):
        # Running out of budget mid-investigation and returning nothing wastes
        # everything gathered. Two steps out, ask for the answer it can already
        # support — a partial answer with citations beats an apology.
        remaining = max_steps - step
        left = budget - spent
        if remaining == 2 or (left <= BUDGET_WARN_AT and not warned):
            warned = True
            messages.append({"role": "user", "content":
                f"You are near the end of your budget ({remaining} tool calls and "
                f"{left:,} characters of reading left). Write anything you have "
                f"not yet recorded to the notepad now, then answer from what you "
                f"have, citing the doc_ids you opened. If some part is unresolved, "
                f"say what is missing and which document would settle it."})
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
            # Out of budget: do not run the tool at all. Running it to return
            # nothing but an apology spends time and the provider's tokens for
            # no reading, and the honest move is to go and write the answer.
            if budget - spent <= _NOTE_RESERVE:
                payload, cut, content = _EXHAUSTED, 0, 0
                steps.append({"tool": name, "arguments": args, "skipped": True,
                              "result_chars": len(payload), "content_chars": 0,
                              "dropped_chars": 0, "budget_left": 0})
                messages.append({"role": "tool", "tool_call_id": call.get("id"),
                                 "name": name, "content": payload})
                continue

            try:
                result = _run_tool(name, args)
            except Exception as e:  # noqa: BLE001 — a failed tool is a fact, not a crash
                result = {"error": str(e)[:200]}
            # Cut to whatever is smaller: this call's cap, or what is left of
            # the run. A silent cut is what made a 5%-read look like a complete
            # one, so when it happens the model is told, in the payload — and
            # room for saying so is reserved out of the allowance, or the
            # explanation would itself push the run over budget.
            encoded = json.dumps(result, default=str)
            allowed = max(0, min(MAX_TOOL_CHARS, budget - spent))
            if len(encoded) <= allowed:
                payload, cut = encoded, 0
            else:
                room = max(0, allowed - _NOTE_RESERVE)
                payload = encoded[:room]
                cut = len(encoded) - room
                payload += _truncation_note(cut, len(encoded))
            content = len(encoded) - cut          # corpus text, not bookkeeping
            spent += content
            steps.append({"tool": name, "arguments": args,
                          "result_chars": len(payload), "content_chars": content,
                          "dropped_chars": cut, "budget_left": max(0, budget - spent)})
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
