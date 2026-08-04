# Regulatory Intelligence Aggregator — Delivery Roadmap

**Cadence:** 10 sprints × 2 weeks ≈ 5 months (Phase 1 build: sprints 1–6 ≈ 3
months; Phase 2 cloud/scale: sprints 7–10 ≈ 2 months).
**Team:** Backend Engineer (100%), Full-stack Engineer (100%), AI Engineer
(100%), Business Analyst (~25%), Project Manager (~25%).
**Velocity assumption:** 1 SP ≈ 0.9 dev-day → ~33 dev SP + 2 BA SP per sprint.
Plan runs 30–36 SP per sprint; PM effort is tracked but not pointed.

## Phase 1 — Build the aggregator (Sprints 1–6)
| Sprint | Goal | Epics | SP |
|---|---|---|---|
| 1 | Foundation: config-driven skeleton, corpus schema, verification harness — "regulator = config" proven | E1, E4 | 31 |
| 2 | Trust core: crash-safe versioning + archive (chaos-tested) and all three collection engines | E2, E3 | 36 |
| 3 | Live pipeline: end-to-end ingestion, orchestration with humane statuses, first regulators collecting | E3, E5, E4 | 36 |
| 4 | Visibility & intelligence: dashboard core, knowledge graph, completeness proofs, all 30 onboarded | E7, E6, E4 | 36 |
| 5 | Completion & control: changes/diff/explorer UI, manual override lane, 12 MCP tools, tool-surface security | E7, E5, E8 | 33 |
| 6 | Agentic integration & operational close-out: markdown projection, agent connectivity/skills/eval, pollers, backups, successor KB | E9, E5 | 30 |

## Phase 2 — Cloud migration & scale to 5,000 users (Sprints 7–10)
Target: integrate into the **existing AWS production platform** (MCP server,
agent, PostgreSQL, S3) rather than standing up a parallel stack.

| Sprint | Goal | Epics | SP |
|---|---|---|---|
| 7 | Cloud foundation & data migration: IaC baseline, PostgreSQL/RDS schema + data migration, S3 corpus cutover, secrets management, containerised workers | E11 | 31 |
| 8 | Cloud runtime & read-path scale: cloud-scheduled ingestion, backup/DR with PITR, eliminate per-row object reads, delegate search to the platform index, caching, horizontal read tier, cost model | E11, E12 | 33 |
| 9 | Platform integration & security: register reg_* tools on the production MCP server, SSO + RBAC, per-tenant keys and quotas, queue-based parallel ingestion, CI/CD | E13, E12 | 31 |
| 10 | Performance proof & cutover: load/soak to 5,000 users, tuning, observability and alerting, security review, production cutover and hypercare | E12, E13 | 36 |

### Why 5,000 users is mostly a read-side problem
Collection load is **fixed** — 30 regulators and a roughly constant daily delta
regardless of how many people use the system. What scales with users is the
read path: dashboard queries, MCP tool calls and agent retrieval. Phase 2
therefore concentrates on making reads cheap and horizontal (remove per-row
object-store reads, cache hot endpoints, pool connections, scale stateless
replicas) and proving it under load, rather than re-architecting collection.

## Scope boundaries
LLM enrichment execution, chatbot UX and the agent platform itself are owned
outside this team; stories cover the interfaces, registration and evaluation
handoffs. Backlog (E10) holds post-MVP enhancements that are not scheduled.

## Key assumptions & risks carried in the plan
- **Resourcing:** Sprints 7–10 assume AWS/platform capability — either the
  Backend Engineer skills up or a Platform Engineer joins. If neither, Phase 2
  slips; flag at sprint 6 planning.
- **Platform dependencies:** shared PostgreSQL, S3, MCP server and SSO are
  provided by the existing production application; cross-team coordination is
  a standing PM item from sprint 7.
- Regulator sites drift or block (mitigated: verification harness, sanctioned
  fallback chains, official-channel escalation — never evasion).
- Large regulator sites need depth-slicing (daily caps) to stay within the run
  window.
- Formal UAT capacity is limited to BA at 25% (mitigated by continuous product
  owner review).

Files: `sprint_plan.csv` (all stories), `epics.csv`, `capacity.csv`,
`Regulatory_Aggregator_Roadmap.xlsx` (Roadmap + Epics + Capacity sheets).
