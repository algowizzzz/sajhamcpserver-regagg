#!/usr/bin/env python3
"""
Generate config/tools/reg_*.json from the reg_tools classes (single source of
truth for the schemas). Re-run whenever the tool input schemas change.

    python scripts/regagg_gen_tool_configs.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sajha.tools.impl.reg_tools import (  # noqa: E402
    RegGraphTool, RegReadTool, RegSearchTool, RegTagsTool, RegWhatsNewTool,
)

TOOLS = [
    ("reg_search", RegSearchTool,
     "Search the regulatory corpus (BM25 + filters) across ~30 regulators; "
     "filter by jurisdiction, regulator, doc_type, tags, date, status."),
    ("reg_read", RegReadTool,
     "Read a regulatory document: summary (default), full markdown, metadata, "
     "or a historical archived version."),
    ("reg_tags", RegTagsTool,
     "Browse the controlled tag taxonomy with document counts and category."),
    ("reg_whats_new", RegWhatsNewTool,
     "List documents ingested in the last N days grouped by regulator; "
     "optionally only those with a comment deadline within N days."),
    ("reg_graph", RegGraphTool,
     "Traverse the cross-reference graph (implements/supersedes/interprets/"
     "references/consults_on) around a document, depth<=3, cycle-safe."),
]

OUT = REPO / "config" / "tools"


def main() -> int:
    for name, cls, desc in TOOLS:
        tool = cls(config={"name": name})
        cfg = {
            "name": name,
            "implementation": f"sajha.tools.impl.reg_tools.{cls.__name__}",
            "description": desc,
            "version": "0.1.0",
            "enabled": True,
            "inputSchema": tool.get_input_schema(),
            "outputSchema": tool.get_output_schema(),
            "metadata": {
                "author": "regagg",
                "category": "Regulatory Intelligence",
                "tags": ["regulatory", "compliance", "aggregator"],
                "cacheTTL": 300,
                "readOnly": True,
            },
        }
        path = OUT / f"{name}.json"
        path.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
