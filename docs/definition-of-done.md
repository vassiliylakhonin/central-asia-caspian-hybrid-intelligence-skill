# Definition of done

The two hard bars this repo aims to clear, their binary criteria, and what does not count as progress.

Referenced from `AGENTS.md`. Current status per criterion is in [`STATUS.md`](../STATUS.md).

The repo tracks maturity on two axes. **Continuous invariants** (C1–C4) must hold at every commit and can regress. **Bars** are sequential and one-way: Bar 1 is the threshold for being a credible artifact, Bar 2 for being an agent-validated specialist resource, and Bar 3 for having demonstrated that the vertical changes the substance of an answer at all. Practitioner review is valuable for buying-side trust, but it is not the hard gate when the downstream consumer is an agent integrator. [`STATUS.md`](../STATUS.md) must always state honestly which bar has been cleared, which has not, and which invariants currently hold. **Do not pretend a bar is cleared if it is not, and do not let a cleared bar mask a failing invariant.**

## Continuous invariants (C1–C4)

The bars are sequential and one-way: once cleared, a bar stays cleared, because it records that a body of work was done. That is the right shape for content maturity and the wrong shape for whether the repo currently works. Executable surfaces regress silently — a dependency releases a new major version, a path moves, an entry point stops importing — and nothing in a sequential bar catches it.

The invariants below are the other axis. They are **not** bars. They must hold at every commit, they can go from met to not-met, and `STATUS.md` records their current state honestly, including regressions. A cleared bar never entitles the repo to a failing invariant.

- **C1 — Declared executables run on a clean install.** Every entry point this repo documents — the MCP server, `scripts/validate.py`, the test command, any documented install line — starts from a fresh environment built only from the declared dependencies. Dependency constraints must match the import paths the code actually uses: an unbounded `>=` pin against a library that has renamed the symbol being imported does not satisfy this criterion, even while an older pinned environment still happens to work locally.
- **C2 — The package installs as a namespaced package.** A `[build-system]` block is declared, and no module is installed at the top level of `site-packages`. Modules ship under a distinct package name, and tests import them the way a consumer would — through the installed name, not by loading a file path. A test that reaches a module by file path proves the module's logic and proves nothing about whether the shipped artifact can reach it.
- **C3 — No tool returns a fabricated finding.** Every declared-but-unimplemented tool returns an explicit non-finding carrying `result_is_not_a_finding` and `human_review_required`. The structured decision schema must remain incapable of expressing an approval, a block, or an enforcement action. This invariant is enforced by test, not by prose, because it is the one failure mode an agent consumer cannot detect for itself.
- **C4 — Documentation references resolve.** Every path, runtime variant, example and companion file named in `README.md`, `AGENTS.md`, `SKILL.md` or `STATUS.md` exists. A status claim whose evidence link is broken is an unsupported status claim.

Invariant failures are not roadmap items. They are defects, and they take precedence over new bar work.

## Bar 1 — Early but credible (the minimum bar)

A senior AI or agent engineering reviewer should understand that this repo is not a generic regional prompt. It should read as an early but credible vertical specialist skill for Central Asia + Caspian strategic-risk agents, with evidence discipline, mechanism-first reasoning, examples, source guidance and clear limitations. Specifically:

- **B1.1** README follows the section structure in [`repo-conventions.md`](repo-conventions.md) "README priorities".
- **B1.2** All four canonical evidence modes are demonstrated by at least one example each.
- **B1.3** All preferred examples in [`repo-conventions.md`](repo-conventions.md) "Examples" exist or are explicitly deferred with a reason.
- **B1.4** `evals/` has a review checklist, a starter rubric and a failure-modes file with honest labels (no benchmark claim).
- **B1.5** Validation script passes on every commit to `main`.

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

## Bar 3 — Demonstrated specialist lift (the bar this repo has not attempted)

Bar 2 asked whether loading this skill changes the **structure** of an agent's output. It does, and that is recorded. But a structural rubric will show a large delta for any well-formed skill file, because it measures whether sections appeared — not whether the Central Asia + Caspian reading got better. Every Bar 2 writeup says so explicitly, and that honesty is exactly what leaves the central claim of a *vertical specialist* repo untested.

That claim is: **this vertical changes the substance of the answer, beyond what the horizontal method (`global-think-tank-analyst`) produces on its own.** Bar 3 measures it. Nothing before Bar 3 does.

Bar 3 is not a harder version of Bar 2. It is the first bar whose outcome is not known in advance, and the first that can be cleared by a negative result.

- **B3.1 — Substantive rubric, pre-registered.** A rubric of at least eight items, each a checkable substantive claim: a named transmission channel, a named authoritative source or regulator, a named plausible false positive, a named verification artifact a reviewer would actually pull. Committed *before* any Bar 3 output is scored, with the commit hash recorded in each case file. Reusing the Bar 2 structural rubric does not satisfy this criterion; nor does a rubric whose items can be satisfied by formatting.
- **B3.2 — Three-condition protocol.** Each case runs the same question, model, model version and date under three conditions: **(A)** no skill loaded, **(B)** the horizontal method only, **(C)** the horizontal method plus this vertical. Prompts recorded verbatim. Condition B is the one that matters; A exists only to show the rubric can discriminate at all.
- **B3.3 — Case coverage.** At least five cases under `evals/specialist-lift/`, spanning at least three distinct archetypes from [`risk-archetypes.md`](risk-archetypes.md).
- **B3.4 — Blind, different-family judge.** Outputs are presented in randomized order with condition labels stripped, and scored by a model from a different vendor family than the one that generated them. Author scoring may accompany a judge score; it may never substitute for one. The self-preference bias noted in B2.7 is stronger here, because the author knows which condition is meant to win.
- **B3.5 — Lift reported for every case, including null and negative results.** Bar 3 requires the C-over-B delta to be **measured and published per case**, not to be positive. Dropping or re-running a case after seeing its score fails this criterion outright, and is the single most likely way this bar gets quietly faked.
- **B3.6 — At least one negative control.** A question inside the region's geography where regional mechanism should *not* change the substance, and where condition C correctly adds nothing beyond B. Without this, the measurement cannot distinguish "the vertical adds signal" from "the vertical always adds words".
- **B3.7 — Re-runnable harness.** A script in-repo regenerates the case set. Each case file carries the exact prompts, model identifiers and dates needed for a third party to re-run it. A manual procedure described in prose does not satisfy this.
- **B3.8 — Scope statement on every case.** Small N; not a labelled dataset; measures substantive coverage against a rubric the author wrote; not factual accuracy; not compliance, sanctions, AML or screening validation; not practitioner validation.

### Bar 3 can be cleared by a null result

This is deliberate and it is the point of the bar.

If measured lift is consistently at or near zero across the case set, **Bar 3 is cleared** — the question was asked properly and answered honestly — and the correct follow-on is to fold this repo's regional content into the horizontal method and retire it as a separate skill. That is a successful outcome, not a failure.

A vertical that cannot demonstrate lift is not a failed repo. An *unmeasured* vertical is. Bar 3 exists so that "should this repo exist separately?" becomes a question with evidence behind it instead of a question no one asks.

### Bar 3 anti-criteria

Beyond the repo-wide anti-criteria below, these specifically do not count as progress toward Bar 3:

- Publishing only the cases with positive lift, or removing a case after seeing its score.
- Editing the rubric after reading outputs. If the rubric is wrong, re-pre-register it and re-run the whole set.
- Presenting the Bar 2 structural rubric, or any rubric satisfiable by formatting, as substantive.
- Treating a same-family or unblinded judge as the load-bearing evidence.
- Crediting condition C for being longer, more hedged, or better formatted than B.
- Declaring lift because the outputs "read better" or "feel more expert".
- Presenting Bar 3 as factual accuracy, compliance usefulness, or practitioner validation. It is none of those.
- Adding more examples, archetypes or source-backed memos *instead of* running the measurement. Bar 1 and Bar 2 are cleared; more of their currency does not buy Bar 3.

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
