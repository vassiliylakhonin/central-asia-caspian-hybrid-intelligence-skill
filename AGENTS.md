# AGENTS.md

## Project identity

Central Asia + Caspian Hybrid Intelligence Skill is a vertical specialist skill for AI agents working on Central Asia, the Caspian region, sanctions, AML, banking, logistics, corridors, energy, infrastructure and geopolitical risk.

Use this positioning:

> Central Asia & Caspian specialist skill for AI agents working on sanctions, AML, corridors, banking, logistics, energy and geopolitical risk.

This repo is a domain skill, not an infrastructure product.

## Relationship to the broader stack

Agenda Intelligence MD:
- validation
- schemas
- evidence audit
- scoring
- CLI / MCP / CI tooling where implemented

Global Think Tank Analyst:
- broad strategic-risk memo workflows
- general policy-risk analysis
- scenario and red-team memo modes

Central Asia + Caspian Hybrid Intelligence Skill:
- specialist regional/corridor-risk reasoning
- domain-specific risk transmission logic
- sanctions / AML / banking / logistics / energy / corridor analysis patterns

Do not duplicate Agenda Intelligence MD inside this repo.
Do not turn this repo into a CLI, MCP server, screening engine, or validation platform unless explicitly requested.

## Scope

Core scope:
- Central Asia
- Caspian region when material
- sanctions and AML exposure
- routing and transshipment risk
- correspondent banking and payment rails
- beneficial ownership opacity
- logistics chokepoints
- energy and infrastructure corridors
- Russia / China / EU / Middle East connectivity when material
- state capacity and political economy
- strategic competition and leverage

Expand geography only when it changes the mechanism, risk exposure, leverage, or decision. Do not expand geography for decoration.

## Evidence rules

Every example must state its evidence mode:
- live-source-backed
- user-provided sources
- illustrative source packet
- reasoning-only

Do not fabricate:
- citations
- sanctions designations
- legal conclusions
- compliance conclusions
- company facts
- ownership structures
- enforcement actions
- dates
- statistics
- prices
- regulatory changes

If facts are not verified, say so.

Use labels where helpful:
- Verified
- Plausible
- Judgment
- Unknown

## Safety and limitation rules

This repo must not claim to provide:
- legal advice
- compliance advice
- sanctions screening
- AML transaction monitoring
- investment advice
- factual verification by itself
- live source retrieval by itself
- guaranteed correctness
- production-grade risk controls

Avoid exaggerated claims:
- revolutionary
- best-in-class
- fully autonomous
- guarantees compliance
- solves hallucinations
- detects sanctions evasion

Use careful language:
- helps structure analysis
- supports analyst-style reasoning
- requires source-backed verification for factual claims
- does not replace professional review

## Analytical style

Prefer mechanism-first reasoning.

Good output should include:
- bottom line
- scope and evidence mode
- primary driver
- risk transmission mechanism
- exposure map
- actor incentives and leverage
- role-based implications
- trigger points
- unknowns
- confidence
- what would change the judgment
- limitation note

Avoid:
- generic geopolitical essays
- alarmism without transmission channel
- fake precision
- overconfident forecasting
- unsupported legal/compliance conclusions
- vague “monitor closely” recommendations

## README priorities

README should make value clear in 30 seconds.

Recommended structure:
1. One-line positioning
2. Problem
3. What it does
4. What it is not
5. Relationship to Agenda Intelligence MD and Global Think Tank Analyst
6. Quick usage
7. Before / after
8. Flagship example
9. Skill files
10. Source guide
11. Risk archetypes
12. Review checklist
13. Limitations
14. Roadmap

## Examples

Examples should be concrete and role-relevant.

Preferred examples:
- fintech sanctions/routing exposure
- bank correspondent/counterparty exposure
- Caspian corridor logistics chokepoint
- energy/infrastructure corridor risk
- beneficial ownership opacity
- trade finance or dual-use goods routing

Every example must include evidence mode and limitation note.

## Evaluation docs

Use honest labels:
- review checklist
- starter rubric
- failure modes

Do not call it a benchmark unless benchmark cases and results actually exist.

## Validation

If validation scripts exist, run them before finalizing changes.

Prefer additive improvements.
Do not introduce heavy dependencies unless necessary.

## Definition of done

The repo aims to clear two bars in sequence. Bar 1 is the threshold for being a credible artifact. Bar 2 is the threshold for being an externally validated specialist resource. The repo's `STATUS.md` (or this section if `STATUS.md` does not yet exist) must always state honestly which bar has been cleared and which has not. **Do not pretend a bar is cleared if it is not.**

### Bar 1 — Early but credible (the minimum bar)

A senior AI or agent engineering reviewer should understand that this repo is not a generic regional prompt. It should read as an early but credible vertical specialist skill for Central Asia + Caspian strategic-risk agents, with evidence discipline, mechanism-first reasoning, examples, source guidance and clear limitations. Specifically:

- **B1.1** README follows the 14-section structure in "README priorities".
- **B1.2** All four canonical evidence modes are demonstrated by at least one example each.
- **B1.3** All preferred examples in "Examples" exist or are explicitly deferred with a reason.
- **B1.4** `evals/` has a review checklist, a starter rubric and a failure-modes file with honest labels (no benchmark claim).
- **B1.5** Validation script passes on every commit to `main`.
- **B1.6** Honesty constraints in "Safety and limitation rules" are observed everywhere.

### Bar 2 — Externally validated specialist resource (the harder bar)

The criteria below close the weaknesses that Bar 1 alone cannot close (single-author scoring, structural-reasoning-heavy examples, no external review, undifferentiated skill files, no real-use evidence). Each criterion is binary: either met with verifiable evidence, or not.

- **B2.1 — Source-anchored majority.** At least half of the flagship examples in `examples/` are `live-source-backed` or `user-provided sources` (not `reasoning-only` or `illustrative source packet`). Source-backed examples must cite primary URLs (regulators, IFIs, FATF/EAG, central banks, court records) for legal-grade claims, with secondary reporting clearly tiered.
- **B2.2 — External review.** At least one reviewer outside the author has reviewed at least one example and one application of the starter rubric, and either (a) their findings have been incorporated, or (b) the response is explicitly addressed and recorded. The reviewer must be identifiable (name, role or verifiable public attribution); anonymous or fabricated reviewers do not count.
- **B2.3 — Validated cases (not a benchmark).** At least three memos produced with the skill have been reviewed by a domain practitioner (compliance, AML, sanctions, banking, corridor logistics, energy, or regional risk) and labeled as either "useful in their workflow" or "useful with the specified revisions". Stored in a `validated-cases/` directory with practitioner attribution where they consent, anonymized otherwise. **This is not a benchmark and must not be called one.** No aggregated scores; no claims of "X% accuracy".
- **B2.4 — Platform differentiation or consolidation.** Each variant in `skills/{codex,claude,openclaw}/SKILL.md` either (a) has at least one platform-specific feature that meaningfully changes output (e.g. Claude tool-use awareness, Codex agentic-loop awareness, OpenClaw-specific contract), or (b) is consolidated. Three near-identical files presented as three skills do not meet this criterion.
- **B2.5 — Honest real-use evidence.** Either (a) the repo links to at least one public, attributable real-use record (a memo, a workflow, a published reference, with permission), or (b) the README and `STATUS.md` explicitly state that no real-use evidence exists yet. No implicit suggestion of adoption that has not occurred.
- **B2.6 — Source freshness discipline.** `live-source-backed` examples carry a retrieval date, and the repo has a documented practice (in `docs/source-guide.md` or a `STATUS.md` note) for re-verifying or marking stale any source older than a stated horizon. Examples beyond the horizon are either refreshed or labeled stale.
- **B2.7 — Independent rubric application.** At least one application of `evals/starter-rubric.md` to a memo has been performed by someone other than the author, with their scorecard added to `evals/scoring-example.md` (or a sibling file) under their attribution.

### Anti-criteria (things that do **not** count as progress toward done)

- Adding more `reasoning-only` examples once Bar 1 is cleared. Source-anchored ratio is the binding constraint.
- Adding worked scorecards by the same author to imply external validation.
- Renaming a starter rubric a "benchmark", "scoring framework" or "evaluation suite" without the underlying validated cases.
- Adding adoption-style language ("used by", "trusted by", "production-grade") without B2.5 evidence.
- Adding more topics, badges or boilerplate without a corresponding substance change.
- Moving repo metadata (description, topics, homepage) in ways that imply a status the repo has not earned.

### Honest current status

At the time of writing this Definition of Done:

- **Bar 1 — cleared.** All B1.1–B1.6 criteria observable in the current tree.
- **Bar 2 — not cleared.** B2.1 partially (2 of 9 flagship examples are source-anchored — short of half). B2.2, B2.3, B2.5 and B2.7 are entirely open (single-author state). B2.4 is not yet decided (current variants are near-identical). B2.6 is partially in place (retrieval dates exist; no documented re-verification horizon).

Future contributors must update this status truthfully as criteria are met, and must not advance the status without verifiable evidence.
