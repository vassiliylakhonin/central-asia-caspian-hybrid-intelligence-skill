# Companion patterns

This document describes **structural patterns** for using this skill alongside the other two repos in the portfolio:

- **Agenda Intelligence MD** — primarily for deterministic evidence-packet checks before human review; older memo validation and scoring remain compatibility surfaces.
- **Global Think Tank Analyst** — for broader strategic-risk memo workflows that may invoke this skill as a specialist sub-step.

These are illustrative patterns, not implemented integrations. They do **not** describe a current API of either companion repo. For actual interfaces, schemas and tooling, consult those repos directly.

## Pattern 1 — Handing a claim/source packet to Agenda Intelligence MD

### Intent

Keep the regional reasoning in this repo, then pass externally checkable claims and supplied source text to the Agenda Intelligence MD linter without serializing the full memo or its judgments.

### Structural pattern

1. **Produce a memo** with this skill in any canonical evidence mode. Keep facts, assessments, assumptions, scenarios, and unknowns distinct.
2. **Select externally checkable claims** — factual and quantitative statements, not scenarios or analyst judgments.
3. **Build the packet** — stable `claim_id`, declared `source_ids`, optional verbatim `quotes`, and caller-supplied `sources[]` text. Follow [`docs/evidence-packet-handoff.md`](evidence-packet-handoff.md).
4. **Run the linter** — `agenda-intelligence check evidence-packet.json --strict`.
5. **Revise the originating memo or packet** based on missing references, quote mismatches, weak lexical support, unmatched numbers, and reviewer actions.

### Boundary

- This skill produces analytical artifacts and the handoff packet. It does not lint them.
- Agenda Intelligence MD reports packet completeness. It does not generate specialist regional reasoning or establish factual truth.
- Do not duplicate Agenda Intelligence MD logic inside this repo. The local script validates only the repository's synthetic handoff fixture and documentation invariants.

### What to expect when wiring this up

- Treat the packet schema and CLI signature as belonging to Agenda Intelligence MD. Read its README and source for the current contract.
- Older `analyze`, memo-schema, scoring, and MCP paths are compatibility workflows. Use them only when a caller explicitly depends on those interfaces.
- Linter output should drive memo or packet revision in this skill, not be reproduced inside it.

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
3. Externally checkable claims and supplied source text are extracted into an evidence packet.
4. Agenda Intelligence MD lints the packet before human review.
5. Findings drive revisions in the originating layer. The linter does not produce factual findings; source-quality or truth questions require separate retrieval and human review.
6. The reviewed specialist memo is embedded in the broader strategic memo with provenance preserved.

This pattern keeps each repo doing what it is good at and avoids duplicate logic.

## Honest limits of this document

- The interfaces (CLI, MCP, schemas, scoring rubrics) of Agenda Intelligence MD and Global Think Tank Analyst are owned by those repos; consult them directly.
- These patterns describe **how to think about the integration**, not a turnkey wiring.
- This document does not assert that any specific integration is currently implemented end-to-end.
