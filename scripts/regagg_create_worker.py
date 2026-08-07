#!/usr/bin/env python3
"""
Create (or refresh) the riskGPT digital worker on the agent platform.

The worker is CONFIGURATION, not code: its tool list is read from this server's
tool registry, so enabling a new corpus tool offers it to the worker without a
edit here. The same record can be opened and toggled in the agent platform's
admin UI — this script just makes the setup reproducible.

    python scripts/regagg_create_worker.py \
        --workers ../agent_clean/agent_clean_repo/config/workers.json
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

WORKER_ID = "w-riskgpt"
DEFAULT_PATTERNS = ["corpus_*", "reg_*"]

SYSTEM_PROMPT = """You are riskGPT, the research assistant for a bank's credit and
market risk teams, working over a corpus of regulatory documents and financial
news that this platform has already collected.

WHAT YOU HAVE
- corpus_list_sources / corpus_list_files: what data exists, by source and date.
- corpus_read / corpus_read_many: the markdown of specific documents.
- corpus_search_bm25: ranked relevance when you know the topic, not the wording.
- corpus_search_keyword: exact terms — rule numbers, tickers, precise phrases.
- corpus_search_similar: widen from one good hit to the rest of the story.
- corpus_entity_lookup: a company by any spelling; ambiguous hits come back as
  'possible' and must be treated as unconfirmed.
- corpus_changes: what entered or was revised recently.
- The reg_* tools give the structured view: coverage, diffs, materiality bands.

HOW TO WORK
- Choose your own route; there is no fixed workflow. Several small, targeted
  calls beat one broad one.
- Read documents before concluding. A search snippet is a pointer, not evidence.
- Cite the doc_id of everything you used.
- If the corpus cannot answer, say so plainly and say what it does contain.
  Never fill a gap from memory or the open internet.
- You report what the corpus says. The analyst decides what to do about it.
"""


def discover_tools(patterns) -> list:
    """Every registered tool matching the patterns — the registry is the truth."""
    names = []
    for cfg in sorted((REPO / "config" / "tools").glob("*.json")):
        try:
            data = json.loads(cfg.read_text())
        except (OSError, ValueError):
            continue
        name = data.get("name") or cfg.stem
        if data.get("enabled", True) and any(fnmatch.fnmatch(name, p) for p in patterns):
            names.append(name)
    return sorted(names)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", required=True, help="path to workers.json")
    ap.add_argument("--patterns", default=",".join(DEFAULT_PATTERNS),
                    help="comma-separated tool name patterns")
    ap.add_argument("--name", default="riskGPT — financial web data aggregator")
    args = ap.parse_args()

    tools = discover_tools([p.strip() for p in args.patterns.split(",") if p.strip()])
    if not tools:
        print("no tools matched — is the tool registry populated?")
        return 1

    path = Path(args.workers)
    if not path.exists():
        print(f"workers file not found: {path}")
        return 1
    doc = json.loads(path.read_text())
    workers = doc.get("workers", [])

    worker = {
        "worker_id": WORKER_ID,
        "name": args.name,
        "description": ("Answers credit and market risk questions from the "
                        "collected regulatory and financial-news corpus."),
        "enabled": True,
        "system_prompt": SYSTEM_PROMPT,
        "enabled_tools": tools,
        "agent_mode": "react",
        "enable_memory": False,
        "created_by": "regagg",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "domain_data_path": "./data/workers/w-riskgpt/domain_data",
        "my_data_path": "./data/workers/w-riskgpt/my_data",
        "workflows_path": "./data/workers/w-riskgpt/workflows/verified",
    }
    existing = next((w for w in workers if w.get("worker_id") == WORKER_ID), None)
    if existing:
        existing.update(worker)
        action = "updated"
    else:
        workers.append(worker)
        action = "created"
    doc["workers"] = workers
    path.write_text(json.dumps(doc, indent=2) + "\n")

    print(f"{action} {WORKER_ID} with {len(tools)} tools")
    for t in tools:
        print(f"   {t}")
    print("\nPoint the agent platform at this server:")
    print("   SAJHA_BASE_URL=http://127.0.0.1:3005")
    print("   SAJHA_API_KEY=<a key whose allowlist covers these tools>")
    print("Tools can be toggled per worker in the agent platform's admin UI.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
