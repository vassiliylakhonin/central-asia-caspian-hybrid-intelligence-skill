# Companion patterns

This document describes **structural patterns** for using this skill alongside the other two repos in the portfolio:

- **Agenda Intelligence MD** — for validation, schema, evidence-audit and scoring of outputs.
- **Global Think Tank Analyst** — for broader strategic-risk memo workflows that may invoke this skill as a specialist sub-step.

These are illustrative patterns, not implemented integrations. They do **not** describe a current API of either companion repo. For actual interfaces, schemas and tooling, consult those repos directly.

## Pattern 1 — Validating outputs against Agenda Intelligence MD

### Intent

Treat memos produced with this skill as artifacts that can be passed to the Agenda Intelligence MD layer for validation, evidence audit and scoring — keeping reasoning here and validation there, without duplicating either.

### Structural pattern

1. **Produce a memo** with this skill in any of the four canonical evidence modes (`live-source-backed`, `user-provided sources`, `illustrative source packet`, `reasoning-only`). The memo states evidence mode at the top, uses `Verified` / `Plausible` / `Judgment` / `Unknown` labels where useful, and ends with a limitation note.
2. **Hand the memo to the Agenda Intelligence MD validation layer** — schemas, evidence audit, scoring, CLI / MCP / CI tooling where implemented.
3. **Read the validator's findings** — structure compliance, missing required sections, evidence-label coverage, forbidden determinative language, source-handling discipline, factuality flags where Agenda Intelligence MD supports them.
4. **Iterate the memo** in this skill based on validator findings; do not re-implement validation here.

### Boundary

- This skill produces analytical artifacts. It does not validate them.
- Agenda Intelligence MD validates structure, evidence discipline and scoring. It does not generate specialist regional reasoning.
- Do not duplicate Agenda Intelligence MD logic inside this repo. If a check belongs to validation, it belongs to that repo.

### What to expect when wiring this up

- Treat schema and CLI signatures as belonging to Agenda Intelligence MD. Read its README and source for current contracts.
- If Agenda Intelligence MD exposes an MCP server, this skill remains MCP-agnostic — the integration is at the workflow level (memo → validator → revision loop), not at the skill level.
- Validator output should drive memo revision in this skill, not be reproduced inside it.

## Pattern 2 — Invoking this skill from Global Think Tank Analyst

### Intent

Use Global Think Tank Analyst for broad strategic-risk memo workflows; delegate the Central Asia / Caspian-specific reasoning to this skill, then re-integrate.

### Structural pattern

1. **Start in Global Think Tank Analyst** for the broader workflow — scenario design, red-team mode, multi-region policy memo, or general strategic-risk framing.
2. **Identify a Central Asia / Caspian-specific sub-question** that meets the inclusion criteria in `docs/regional-logic.md` (mechanism, exposure, leverage or decision actually depend on the region).
3. **Delegate the sub-question to this skill**, supplying:
   - geography (KZ, UZ, AZ, TM, KG, TJ, Caspian as relevant)
   - audience and role (bank, fintech, investor, operator, energy team, analyst)
   - time horizon
   - sector
   - objective and depth
   - evidence mode (reuse the parent workflow's evidence mode where possible)
4. **Receive a specialist memo** with mechanism-first reasoning, exposure map, trigger points, role-based implications, confidence footer and limitation note.
5. **Re-integrate the specialist memo** back into the Global Think Tank Analyst workflow as one input among others; do not replace the broader memo with the specialist memo.

### Boundary

- Global Think Tank Analyst owns the broader memo workflow, scenario and red-team modes, and general policy-risk framing.
- This skill owns the Central Asia / Caspian-specific mechanism and risk-transmission logic.
- Do not turn this skill into a generic strategic-memo tool. Do not turn Global Think Tank Analyst into a regional specialist.

### What to expect when wiring this up

- The handoff is at the prompt / workflow level. Pass the sub-question, scope and evidence mode; receive a structured memo.
- Evidence mode should match across the parent workflow and the specialist sub-step. If the parent is `live-source-backed`, the specialist memo should be too — not `reasoning-only`.
- Cross-link memos rather than concatenate them. Preserve provenance of which step produced which content.

## Combined pattern — specialist memo, validated, embedded

A workflow that uses both companion patterns:

1. Global Think Tank Analyst frames the broader question.
2. This skill produces the Central Asia / Caspian specialist sub-memo.
3. Agenda Intelligence MD validates and scores the specialist sub-memo (and optionally the parent memo) against schemas, evidence rules and forbidden-claim lists.
4. Findings drive revisions in the originating layer:
   - structural / evidence findings → the layer that produced the memo (this skill or Global Think Tank Analyst).
   - factual findings → source retrieval and re-grounding, not invention.
5. The validated specialist memo is embedded in the broader strategic memo with provenance preserved.

This pattern keeps each repo doing what it is good at and avoids duplicate logic.

## Honest limits of this document

- The interfaces (CLI, MCP, schemas, scoring rubrics) of Agenda Intelligence MD and Global Think Tank Analyst are owned by those repos; consult them directly.
- These patterns describe **how to think about the integration**, not a turnkey wiring.
- This document does not assert that any specific integration is currently implemented end-to-end.
