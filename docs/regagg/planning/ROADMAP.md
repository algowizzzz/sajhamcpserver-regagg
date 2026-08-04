# Regulatory Intelligence Aggregator — 3-Month Delivery Roadmap

**Cadence:** 6 sprints × 2 weeks. **Team:** Backend Engineer (100%), Full-stack
Engineer (100%), AI Engineer (100%), Business Analyst (~25%), Project Manager
(~25%). **Velocity assumption:** 1 SP ≈ 0.9 dev-day → ~33 dev SP + 2 BA SP per
sprint (plan runs 30–36 SP/sprint; PM effort non-pointed).

## Sprint goals
| Sprint | Goal | Epics |
|---|---|---|
| 1 | Foundation: config-driven skeleton, corpus schema, verification harness — "regulator = config" proven | E1, E4 |
| 2 | Trust core: crash-safe versioning + archive (chaos-tested) and all three collection engines | E2, E3 |
| 3 | Live pipeline: end-to-end ingestion, orchestration with humane statuses, 18 regulators collecting | E3, E5, E4 |
| 4 | Visibility & intelligence: dashboard core (coverage/corpus/runs), knowledge graph, completeness proofs, all 30 onboarded | E7, E6, E4 |
| 5 | Completion & control: changes/diff/explorer UI, manual override lane, 12 MCP tools, security hardening of the tool surface | E7, E5, E8 |
| 6 | Agentic integration & operational close-out: markdown projection, agent connectivity + skills + eval, daily pollers, backups, successor KB | E9, E5, E10 |

## Scope boundaries (owned outside this team)
LLM enrichment execution, chatbot UX, enterprise scheduling infrastructure, and
production infrastructure (Postgres/TLS/secrets) integrate at defined
interfaces; stories cover the interfaces and handoffs, backlog covers the rest.

## Key risks carried in the plan
Regulator sites drift/block (mitigated: verification harness, fallback chains,
official-channel escalations) · giant sites need depth-slicing (daily caps) ·
formal UAT capacity limited to BA 25% (mitigated: continuous PO review).

Files: `sprint_plan.csv` (all stories), `epics.csv`, `capacity.csv`,
`Regulatory_Aggregator_Roadmap.xlsx` (Roadmap + Epics + Capacity sheets).
