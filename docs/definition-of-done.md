# Definition of done

The two hard bars this repo aims to clear, their binary criteria, and what does not count as progress.

Referenced from `AGENTS.md`. Current status per criterion is in [`STATUS.md`](../STATUS.md).

The repo aims to clear two hard bars in sequence, with an optional practitioner-trust layer when the audience requires it. Bar 1 is the threshold for being a credible artifact. Bar 2 is the threshold for being an agent-validated specialist resource. Practitioner review is valuable for buying-side trust, but it is not the hard gate when the downstream consumer is an agent integrator. [`STATUS.md`](../STATUS.md) must always state honestly which bar has been cleared and which has not. **Do not pretend a bar is cleared if it is not.**

## Bar 1 — Early but credible (the minimum bar)

A senior AI or agent engineering reviewer should understand that this repo is not a generic regional prompt. It should read as an early but credible vertical specialist skill for Central Asia + Caspian strategic-risk agents, with evidence discipline, mechanism-first reasoning, examples, source guidance and clear limitations. Specifically:

- **B1.1** README follows the section structure in [`repo-conventions.md`](repo-conventions.md) "README priorities".
- **B1.2** All four canonical evidence modes are demonstrated by at least one example each.
- **B1.3** All preferred examples in [`repo-conventions.md`](repo-conventions.md) "Examples" exist or are explicitly deferred with a reason.
- **B1.4** `evals/` has a review checklist, a starter rubric and a failure-modes file with honest labels (no benchmark claim).
- **B1.5** Validation script passes on every commit to `main`.
- **B1.6** Honesty constraints in `AGENTS.md` "Safety and limitation rules" are observed everywhere.

## Bar 2 — Agent-validated specialist resource (the harder bar)

The criteria below record the historical agent-integration bar built against Agenda Intelligence MD's older `analyze` compatibility runtime. They are not tests of the current evidence-packet linter. Each criterion is binary: either met with verifiable evidence, or not.

- **B2.1 — Source-anchored majority.** At least half of the flagship examples in `examples/` are `live-source-backed` or `user-provided sources` (not `reasoning-only` or `illustrative source packet`). Source-backed examples must cite primary URLs (regulators, IFIs, FATF/EAG, central banks, court records) for legal-grade claims, with secondary reporting clearly tiered.
- **B2.2 — Compatibility agent-eval delta documented.** At least three agent-evals committed under `evals/agent-eval/` per the historical methodology at https://github.com/vassiliylakhonin/agenda-intelligence-md/blob/main/docs/agent-eval-methodology.md. Each case runs the same model on the same question with and without the older Agenda Intelligence MCP or `analyze` compatibility runtime loaded with this skill as the regional specialist, then scores both outputs against the structural rubric tied to `agenda-memo.schema.json`. Self-scored by the author is acceptable for this historical agent-integration bar; aggregate scores are not claimed. Cases must include the model, date, full prompts or enough prompt text to reproduce, both outputs or excerpts, and a delta + observations section.
- **B2.3 — Compatibility evidence-mode mapping exercised.** At least one historical agent-eval demonstrates how source-backed specialist work is passed into Agenda Intelligence MD's older `analyze` contract as `user_provided` or `mixed`, not as `live_source_backed`. This confirms that the specialist evidence vocabulary did not break that compatibility schema; it is separate from the primary evidence-packet handoff.
- **B2.4 — Platform differentiation or consolidation.** Each variant in `runtimes/{codex,claude,openclaw}/SKILL.md` either (a) has at least one platform-specific feature that meaningfully changes output (e.g. Claude tool-use awareness, Codex agentic-loop awareness, OpenClaw-specific contract), or (b) is consolidated. Three near-identical files presented as three skills do not meet this criterion.
- **B2.5 — Honest real-use evidence.** Either (a) the repo links to at least one public, attributable real-use record (a memo, a workflow, a published reference, with permission), or (b) the README and `STATUS.md` explicitly state that no real-use evidence exists yet. No implicit suggestion of adoption that has not occurred.
- **B2.6 — Source freshness discipline.** `live-source-backed` examples carry a retrieval date, and the repo has a documented practice (in `docs/source-guide.md` or a `STATUS.md` note) for re-verifying or marking stale any source older than a stated horizon. Examples beyond the horizon are either refreshed or labeled stale.
- **B2.7 — Agent-eval honesty discipline.** Agent-eval writeups explicitly state that deltas are structural, not factual verification, not model-quality comparisons, and not aggregate benchmarks. They must not claim accuracy, compliance usefulness, or practitioner validation. When a delta is self-scored (same author or same model family doing the scoring), the writeup must also note self-preference bias — a judge marks rubric criteria "satisfied" more readily for its own family, even on objective binary criteria — and prefer a different-family or ensemble judge where the claim is load-bearing. A self-scored delta is never presented as external validation.
- **B2.8 — Practitioner review (optional, audience-gated).** If the downstream audience includes domain practitioners (compliance, AML, sanctions desks, banking risk leadership), record practitioner review separately under `validated-cases/` with attribution where consented, anonymized otherwise. This is a trust layer, not a hard Bar 2 gate for agent-first validation.

## Anti-criteria (things that do **not** count as progress toward done)

- Adding more `reasoning-only` examples once Bar 1 is cleared. Source-anchored ratio is the binding constraint.
- Presenting self-scored agent-evals as external validation, factual verification, model-quality comparison, or aggregate benchmark evidence.
- Renaming a starter rubric a "benchmark", "scoring framework" or "evaluation suite" without the underlying validated cases.
- Adding adoption-style language ("used by", "trusted by", "production-grade") without B2.5 evidence.
- Treating optional practitioner review as a substitute for agent-eval delta when the stated audience is agent integrators.
- Adding more topics, badges or boilerplate without a corresponding substance change.
- Moving repo metadata (description, topics, homepage) in ways that imply a status the repo has not earned.

## Current status

Current per-criterion status lives in [`STATUS.md`](../STATUS.md) — it is the single source of truth and carries the evidence for each criterion. Do not restate bar status here; a second copy goes stale and then lies.

Future contributors must update `STATUS.md` truthfully as criteria are met, and must not advance the status without verifiable evidence.
