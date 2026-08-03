# Enabling a Chatbot on the Regulatory Corpus

The corpus (5,500+ documents, 29 regulators, versioned, fully sourced) is served
through 5 stateless MCP tools. This guide is everything the chatbot team needs.

## 1. Connection

| | |
|---|---|
| MCP endpoint (HTTP) | `http://localhost:3002/mcp` (SSE: `/mcp/sse`, WS: `/mcp/ws`) |
| Auth header | `X-API-Key: sja_regintel_132a1b83ec357f0f1f2d998c614c436c` |
| Scope | `reg_*` tools ONLY (allowlist enforced server-side; anything else → JSON-RPC -32001) |

## 2. The five tools and when the agent should use them

| Tool | Use when the user asks… | Key params |
|---|---|---|
| `reg_search` | "what does X say about…", any topical question | `query`, filters: `regulator_id[]`, `jurisdiction[]`, `doc_type[]`, `tags[]`, `date_from/to`, `status[]` |
| `reg_read` | to actually read a hit | `doc_id`, `regulator_id`, `mode`: `summary` → `full` → `meta`; `version_ts` for historical versions |
| `reg_whats_new` | "what changed this week/month" | `days`, `jurisdiction[]`, `doc_type[]`, `deadlines_within` |
| `reg_graph` | "what implements/supersedes/relates to X" | `doc_id`, `edge_types[]`, `depth` ≤3, `direction` |
| `reg_tags` | to discover the controlled vocabulary before filtering | `prefix` |

## 3. The agent pattern (put this in the system prompt)

```
You answer questions about financial regulation using ONLY the regulatory
corpus tools. Follow this pattern:

1. NARROW FIRST: call reg_search with the user's topic plus any filters you
   can infer (regulator, jurisdiction, doc_type, dates). Prefer filtered
   searches over broad ones.
2. READ CHEAP, THEN DEEP: for promising hits call reg_read mode=summary;
   only fetch mode=full when the summary is insufficient or the user needs
   exact wording.
3. RELATE: when the user asks about impact/lineage, call reg_graph on the
   document to find what it implements, supersedes, or references.
4. FRESHNESS: for "what's new/changed" questions use reg_whats_new, not search.

CITATION RULE (non-negotiable): every factual claim must cite
  [Regulator · Reference/Title · Published date · source_url]
taken from the tool output's meta. If the corpus has no answer, say so —
never fill gaps from general knowledge without labeling it as such.

STATUS AWARENESS: check the document's `status`. If it is `superseded`,
say so and offer the successor (reg_graph, edge_type=supersedes, direction=in).
VERSION AWARENESS: if version_n > 1, the prior text is retrievable
(mode=version) — offer diffs when the user asks what changed.
```

## 4. Worked examples

**"What are OSFI's expectations on third-party cyber incidents?"**
`reg_search(query="third-party cyber incident reporting", regulator_id=["osfi"])`
→ `reg_read(doc_id="b-13", regulator_id="osfi", mode="summary")` → answer + cite B-13, 2026-07-15, URL.

**"What changed in EU capital rules this month?"**
`reg_whats_new(days=30, jurisdiction=["eu"], doc_type=["final_rule","guidance"])` → group by regulator, cite each.

**"Does anything implement BCBS 239 in Canada?"**
`reg_search(query="BCBS 239", jurisdiction=["canada"])` + `reg_graph(doc_id=…, edge_types=["implements"])`.

## 5. Honest limitations to encode in the bot
- Topic tags are rule-based until the LLM enrichment layer runs — prefer
  full-text `query` over `tags` filters for recall.
- Summaries are not yet LLM-generated; `mode=summary` may be empty → fall back
  to `mode=full` (first N chars) and say the summary is pending.
- AMF Québec has no data (bot-blocked, escalated). MAS is thin (JS-heavy site).
- Depth on the largest sites (OSC 29k URLs, FinCEN) accrues via daily runs —
  absence of a document ≠ non-existence; the coverage % per regulator is at
  `/api/regagg/tree`.

## 6. Evaluation checklist before go-live (spec FR-7)
- [ ] 20-question eval set spanning ≥8 regulators; every answer carries
      regulator + date + working source_url
- [ ] Superseded-document question → bot flags status and cites successor
- [ ] "What changed last week" → matches the UI Changes tab for the same window
- [ ] Out-of-corpus question → bot declines rather than hallucinating
- [ ] Latency: p95 search < 1s on the current corpus
