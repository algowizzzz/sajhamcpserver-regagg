"""
Regulatory Intelligence Aggregator (regagg)
===========================================

Embedded SAJHA feature: an on-prem pipeline that tracks ~30 financial
regulators worldwide, keeps a normalized, versioned document corpus up to
date daily, enriches each document (tags/summary/graph edges), and exposes
the corpus to the chatbot through stateless MCP retrieval tools.

Deployment decisions (2026-08-02):
  * Topology  : embedded in this repo — reuses the SAJHA tool registry,
                storage backend, web-crawler primitives, cache / circuit
                breaker, and LLM layer. No parallel service.
  * Scheduler : Prefect (daily fan-out, retries, rerun API).
  * Datastore : PostgreSQL — corpus tables live on the shared SQLAlchemy
                Base (namespaced `reg_*`) alongside the core schema.

Architectural invariants (from the handover; violating any fails review):
  1. Regulator is config, not code.
  2. Tools/connectors are stateless; all state in Postgres + object storage.
  3. Archive is append-only; nothing is ever deleted.
  4. No source URL is trusted until scripts/verify_sources passes it.

Source of truth for the design: the handover doc set (00_INDEX .. 06_SOURCE_MAP).
"""

__all__ = ["config_models", "config_loader", "models"]

__version__ = "0.1.0"  # Epic 1 — Foundation
