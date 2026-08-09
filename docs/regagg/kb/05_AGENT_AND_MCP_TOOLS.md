# 05 — MCP Tools, the Digital Worker, and Grounding

## 22 tools, two families

Registered through SAJHA's config-driven discovery: a tool exists because
`config/tools/{name}.json` names an implementation class. **No config means the
tool is not registered**, whatever code is on disk. Regenerate `reg_*` configs
with `scripts/regagg_gen_tool_configs.py`.

### `corpus_*` — 10 tools over the markdown projection

The toolset the digital worker reasons with. Deliberately a plethora rather
than a workflow: the worker is given the *moves*, not a route.

| Tool | Answers |
|---|---|
| `corpus_list_sources` | what exists at all — the map before the territory |
| `corpus_list_files` | directory listing with filters |
| `corpus_read` | one document, whole or head |
| `corpus_read_many` | several at once, for comparison without round trips |
| `corpus_search_keyword` | exact terms — a rule number, a ticker |
| `corpus_search_bm25` | ranked relevance, robust to phrasing |
| `corpus_search_similar` | documents that read like this one (TF-IDF cosine) |
| `corpus_changes` | what entered or changed since a date |
| `corpus_entity_lookup` | every document naming a company, however written |
| `corpus_stats` | shape of the corpus |

No embedding service is required for any of them. An on-prem install should not
need a second network dependency to answer "what changed at OSFI".

### `reg_*` — 12 tools over the index plane

`reg_coverage · reg_browse · reg_changes · reg_diff · reg_inventory ·
reg_runs_status · reg_trigger_run · reg_search · reg_read · reg_tags ·
reg_whats_new · reg_graph`

`reg_trigger_run` is the only **mutating** tool. Disable its config or scope the
key if agents must be read-only.

## The tool contract is validated

`BaseMCPTool.validate_arguments()` rejects an argument the tool does not
implement, driven by the tool's own `inputSchema`:

```
corpus_changes does not accept source. It would have been ignored, so the
result would not have been filtered the way you asked. Accepted parameters:
days, lane, limit, min_band, since.
```

> This exists because `corpus_changes` once accepted a `source` filter and
> silently ignored it. Asked what changed at OSFI, the worker got fedreg and
> news back, noticed, and reconstructed the answer by hand — 20 tool calls with
> a caveat about the tool. **An ignored filter is worse than a missing one: the
> caller believes the result is scoped.** With the filter honoured and declared,
> the same question takes 8 calls.

Strictness comes from the schema, not from the base class: a schema declaring
`properties` is closed unless it sets `additionalProperties: true`. An empty
`properties: {}` means "takes no parameters" and rejects everything.

`agent._run_tool()` validates before executing and logs rejections — a
rejection only the model sees is a contract gap nobody gets to fix.

## The digital worker

`sajha/regagg/agent.py`. An agentic loop: `MAX_STEPS = 12`, tool schemas read
from the registry so adding a tool offers it without a code edit.

Registered in the agent platform as **`w-riskgpt`** with all 22 tools enabled,
created by `scripts/regagg_create_worker.py` (which discovers tools by
`fnmatch` on `["corpus_*", "reg_*"]` rather than hard-coding a list).

Three things keep it usable:

- **Page context is explicit.** In *active* mode the worker is told what the
  person is looking at; in *passive* it ignores the screen. The person chooses
  and the choice is visible.
- **A landing nudge.** Two steps from the budget it is asked to answer from
  what it has already read. Running out mid-investigation and returning nothing
  wastes everything gathered.
- **Narration is stripped.** "Let me check…" preambles are cut; the reader
  wants the finding, not the search.

### What it does with a real question

Measured against the live corpus:

| Question | Calls | Outcome |
|---|---|---|
| "what changed at OSFI recently" | 8 | DSB cut to 3.0%, open consultations with deadlines |
| "what is the latest news about SoftBank" | 5 | three stories, entity lookup then read |
| "I'm a credit risk analyst — what should I worry about?" | 25 | CRE as top risk, OSFI's open Credit Risk Management consultation |

It also reports its own gaps: *"the OSFI documents in this corpus do not carry
populated publication dates, so I could not run a clean 'what's new in the last
N days' query."* That is the corpus defect in `02_DATA_AND_SCHEMA.md`, found by
the worker rather than by us.

## Grounding — the rules every generated surface obeys

**No citation, no claim.** Enforced in code, not by prompt:

| Surface | Rule | On failure |
|---|---|---|
| `ask.py` | every sentence cites a source in the pack; no figure outside it | answer withheld, evidence shown |
| `agent.py` | cites the doc_ids it opened | — |
| `focus.rank_by_prompt` | may reorder and narrate; may not add, remove or invent | falls back to deterministic order, states why |
| `myday.validate_spec` | coverage, citations, numbers | falls back to the deterministic template |
| `entity_table.classify` | values coerced against the persona's declared set | value becomes `unknown` |
| `entity_table.summarise` | no figure absent from the rows | falls back to a count |

An order naming an unknown card voids the whole ranking rather than being
partially trusted. A note inventing a figure is withheld while the ordering
survives — they are separately verifiable, so they fail separately.

## Chat sources

The `/ask` response carries `sources[]`, resolved through the corpus index to
real titles, publishers and URLs. For agent answers the list is built from **the
doc_ids actually cited in the prose**, topped up from what the tools returned.

> Previously it was built from `documents` — every doc_id any tool returned,
> mostly search hits the model never opened — then truncated to twelve. On a
> live answer the model cited four documents and none of the four appeared in
> the twelve shown. The panel was displaying evidence the answer did not use.

The UI renders these as chips inside the answer bubble with superscript
citations matching them. An id that cannot be resolved degrades to a marker
that still opens the document, rather than being deleted — silently dropping it
would make a cited claim look uncited.

## Auth for tools

MCP `tools/call` requires `X-API-Key`; per-key allowlists are enforced at the
route. The worker key's `tool_access_list` must be stored as a JSON **string**:

```python
json.dumps(["reg_*", "corpus_*"])
```

Storing it as a list silently matches nothing, and the tools appear absent over
MCP while working fine in-process. That cost an afternoon.
