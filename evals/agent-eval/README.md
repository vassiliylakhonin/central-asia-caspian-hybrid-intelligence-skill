# Agent-Eval Delta Cases

This directory records structural with/without evaluations for agent integration. These cases test how output shape changes when Agenda Intelligence routes a question through the Central Asia + Caspian specialist: provenance, uncertainty, evidence mode, watch-next indicators, role-based actions, and regional mechanism depth.

Agent-eval delta is not factual verification, not a model-quality comparison, not practitioner validation, and not an aggregate benchmark.

## Completed Cases

- [`2026-05-20-correspondent-exposure.md`](2026-05-20-correspondent-exposure.md) — regional banking / correspondent exposure / sanctions-sector routing in `reasoning_only` mode.
- [`2026-05-20-customs-mirror-statistics-anomaly.md`](2026-05-20-customs-mirror-statistics-anomaly.md) — source-backed customs / mirror-statistics anomaly case exercising `mixed` evidence-mode mapping through Agenda Intelligence `analyze`.
- [`2026-05-20-caspian-corridor-chokepoint.md`](2026-05-20-caspian-corridor-chokepoint.md) — corridor / logistics / energy chokepoint case testing regional mechanics beyond sanctions analysis.
- [`2026-06-30-sdn-premise-stop.md`](2026-06-30-sdn-premise-stop.md) — false-premise hard stop: an asserted-but-unverified OFAC SDN listing; tests stop-and-request vs analyzing an unconfirmed designation. Scored blind by two independent judges — Haiku 4.5 and cross-vendor GPT-5 — with identical results (3/7 → 7/7).

## Rule-level canon evals

These test a single AGENTS.md rule (both conditions carry the canon; only the rule under test differs). They do **not** count toward B2.2.

- [`2026-07-10-input-claim-accounting-kz-routing.md`](2026-07-10-input-claim-accounting-kz-routing.md) — input-claim accounting rule, KZ routing packet: delta 0 on a labeled 8-claim illustrative packet; baseline canon already accounts for every claim; blind same-vendor judge.

## Planned Cases

Planned files do not count toward B2.2 until both conditions, scoring, observations, and limitations are completed.

No planned files are active at this time.

## Completion Rules

A completed agent-eval must include:

- the exact or reproducible user question;
- model name and date;
- evidence mode;
- Condition A output: same model and question without Agenda Intelligence product shell / MCP specialist routing;
- Condition B output: same model and question with Agenda Intelligence routing to the relevant modules;
- structural scoring for both conditions;
- delta observations;
- limitations stating that the eval is structural only.

Source-backed specialist work passed through Agenda Intelligence `analyze` must use the product-shell evidence modes `user_provided` or `mixed`, not `live_source_backed`.
