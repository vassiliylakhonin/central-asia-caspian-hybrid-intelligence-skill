# STATUS.md

Honest status against the Definition of Done in [`AGENTS.md`](AGENTS.md). Update this file truthfully whenever a criterion is met or no longer met. Do not advance status without verifiable evidence.

## What the invariants and the bars mean

Maturity is tracked on two axes.

**Continuous invariants (C1–C4)** must hold at every commit and *can regress*. They cover whether the repo currently works, not how much work has been done. A cleared bar never entitles the repo to a failing invariant, and an invariant failure takes precedence over new bar work.

**Bars** are sequential and one-way. Full criteria live in [`docs/definition-of-done.md`](docs/definition-of-done.md); the short version:

- **Bar 1 — Early but credible.** Structural minimum for a vertical specialist skill: README follows the section structure in [`docs/repo-conventions.md`](docs/repo-conventions.md) "README priorities", all four evidence modes (`live-source-backed`, `user-provided sources`, `illustrative source packet`, `reasoning-only`) demonstrated, all preferred examples present, an `evals/` triad (checklist + rubric + failure-modes) with honest labels, validation passing, no exaggerated claims.
- **Bar 2 — Agent-validated specialist resource.** The agent-integration bar: source-anchored majority of flagship examples, at least three agent-eval delta cases, evidence-mode mapping exercised through Agenda Intelligence MD's `analyze` tool, platform differentiation (or honest consolidation) across runtime variants, source freshness discipline, and explicit structural-only honesty on every agent-eval. B2.8 (practitioner review) is optional and audience-gated.
- **Bar 3 — Demonstrated specialist lift.** The bar that tests the repo's actual claim: that this vertical changes the *substance* of an answer beyond the horizontal method alone. Bar 2 measured structure, and a structural rubric rewards any well-formed skill file. Bar 3 measures substance under a pre-registered rubric, a three-condition protocol (no skill / horizontal only / horizontal + vertical), and a blind different-family judge. **Bar 3 can be cleared by a null result** — if the vertical demonstrably adds nothing, the honest outcome is to fold its content into the horizontal method and retire the separate repo.

Each criterion is binary: met with verifiable evidence, or not. Anti-criteria in `AGENTS.md` and `docs/definition-of-done.md` list moves that do *not* count as progress.

**Update (2026-08-30):** Added the continuous-invariant axis (C1-C4) and Bar 3 (demonstrated specialist lift). No previously recorded bar status was changed — cleared bars stay cleared, and rewriting them retroactively would break the audit trail this file exists to keep. Two invariants are recorded as **not met** on first assessment (C1, C2); both are verified defects in the executable surface, not new criteria applied to old work. Bar 3 is recorded as **not attempted**.

**Last updated:** 2026-08-24 (the root skill carries the complete runtime-neutral contract. A structural smoke test verified root-plus-overlay loading in Claude and Codex and direct GitHub installation and discovery in OpenClaw; OpenClaw model behavior was not tested. The four existing `analyze` agent-eval delta cases remain compatibility evidence for the older strategic-intelligence runtime.)

Current Agenda composition: this repo produces regional reasoning and an optional claim/source packet; Agenda Intelligence MD lints packet completeness before human review. The linter does not assess factual truth. Existing `analyze` / MCP evals remain valid for their recorded compatibility workflow, but they do not validate the current evidence-packet linter.

## Continuous invariants

Checked at every commit. These can regress; two currently do.

| Invariant | Status | Evidence |
|---|---|---|
| C1 Declared executables run on a clean install | ❌ **not met** | `scripts/validate.py` and the `unittest` suite pass. The **MCP server does not start on a clean install.** `pyproject.toml` declares `mcp>=1.2.0` with no upper bound; `src/mcp_server.py` imports `from mcp.server.fastmcp import FastMCP`. A fresh environment resolves to mcp 2.x, where `FastMCP` was renamed to `MCPServer`, and the import raises `ModuleNotFoundError`. An older locally-pinned environment still works, which is why this went unnoticed. Fix: choose one `mcp` major version across the whole portfolio and pin it — the horizontal repo currently targets 2.x while both verticals target 1.x, so an environment holding both breaks one of them. |
| C2 Package installs as a namespaced package | ❌ **not met** | `pyproject.toml` declares no `[build-system]` block and no package configuration. The built wheel installs `mcp_server` and `mcp_contract` as **top-level modules** in `site-packages` — a name adjacent to the official SDK's — and `src/mcp_server.py` does a bare `from mcp_contract import ...` that resolves only when the working directory is `src/`. `tests/test_mcp_contract.py` reaches the module through `importlib.util.spec_from_file_location`, so it proves the contract's logic and proves nothing about whether the shipped artifact can import it. |
| C3 No tool returns a fabricated finding | ✅ met | Every declared tool in `src/mcp_server.py` returns `not_implemented` with `result_is_not_a_finding` and `human_review_required`. `tests/test_mcp_contract.py::test_structured_contract_cannot_approve_or_enforce` asserts that `schemas/compliance-decision.schema.json` cannot express `approve`, `block` or `freeze_funds`, and that `human_review_required` is `const: true`. Enforced by test, not by prose. |
| C4 Documentation references resolve | ✅ met | `scripts/validate.py` checks tracked Markdown links and own-site links on every commit; currently passing. |

C1 and C2 are defects, not roadmap items. They rank ahead of any Bar 3 work.

## Bar 1 — Early but credible

| Criterion | Status | Notes |
|---|---|---|
| B1.1 README follows the "README priorities" structure | ✅ met | See `README.md`. |
| B1.2 All four evidence modes demonstrated | ✅ met | `reasoning-only`, `illustrative source packet`, `live-source-backed`, `user-provided sources` each have at least one example. |
| B1.3 All preferred examples exist or are deferred with reason | ✅ met | All six AGENTS.md preferred examples exist. |
| B1.4 `evals/` has checklist + starter rubric + failure-modes with honest labels | ✅ met | No benchmark claim made. `evals/skill-improvement/` adds validation-gated skill-edit cases, also explicitly non-benchmark. |
| B1.5 Validation passes on every commit to `main` | ✅ met | `python3 scripts/validate.py` runs in CI and pre-commit. |
| B1.6 Honesty constraints observed everywhere | ✅ met | No fabricated citations. |
**Bar 1 — cleared.**

## Bar 2 — Agent-validated specialist resource

| Criterion | Status | What is missing |
|---|---|---|
| B2.1 Source-anchored majority (≥50% of flagship examples) | ✅ met (at threshold, no margin) | 8 of 16 flagship examples are source-anchored (6 `live-source-backed`, 2 `user-provided sources`) — 50%. Wave 8 added an `illustrative source packet` source-conflict-surfacing demonstrator (KZ→RU CHPL-circumvention volume estimates), which is not source-anchored; the ratio dropped from 53% to exactly the 50% threshold. To restore margin, the next added example should be `live-source-backed` or `user-provided sources`. |
| B2.2 Agent-eval delta documented (≥3 cases) | ✅ met | Four completed cases exist: `2026-05-20-correspondent-exposure.md`, `2026-05-20-customs-mirror-statistics-anomaly.md`, `2026-05-20-caspian-corridor-chokepoint.md`, and `2026-06-30-sdn-premise-stop.md` (false-premise hard stop, independent blind Haiku 4.5 judge, 3/7 → 7/7). |
| B2.3 Evidence-mode mapping exercised through `analyze` | ✅ met | `2026-05-20-customs-mirror-statistics-anomaly.md` maps upstream `live-source-backed` specialist material to Agenda Intelligence `analyze` as `mixed`, not `live_source_backed`. |
| B2.4 Platform differentiation or consolidation across `runtimes/{codex,claude,openclaw}` | ✅ met | Common behavior is consolidated in the root `SKILL.md`. Claude adds `Claude Tool-Use Awareness`; Codex adds `Codex Agentic-Loop Awareness`; OpenClaw inherits the root behavior and adds only direct GitHub installation guidance. A [structural smoke test](evals/2026-08-24-runtime-loading-smoke.md) verified Claude and Codex loading plus OpenClaw installation and discovery; OpenClaw model behavior remains `Not tested`. The validator rejects duplicated common sections and non-allowlisted overlay sections. |
| B2.5 Honest real-use evidence or explicit "no real-use evidence" disclosure | ✅ met via negative disclosure | README states no production-usage, adoption or benchmark numbers are claimed; this STATUS file states no positive real-use record exists yet. |
| B2.6 Source freshness discipline | ✅ met | Retrieval dates stated on `live-source-backed` examples; documented re-verification horizons per claim type in [docs/source-guide.md](docs/source-guide.md), including stale-source handling rules. Same-day re-verification required for sanctions / AML / export-controls operational decisions regardless of horizon. |
| B2.7 Agent-eval honesty discipline | ✅ met | All four completed agent-evals state structural-only limitations and avoid factual-verification, model-quality, aggregate-benchmark and practitioner-validation claims. The 2026-06-30 case was scored by two independent blind judges — Haiku 4.5 (same-vendor) and GPT-5 (cross-vendor) — which reproduced the delta cell-for-cell (3/7 → 7/7); it still discloses author-written Condition B and that two judges are not a labelled dataset, per the self-preference-bias rule in `AGENTS.md` B2.7. |
| B2.8 Practitioner review (optional, audience-gated) | optional / not required for Bar 2 | No `validated-cases/` directory yet. Add only if the downstream audience includes practitioner buying-side trust, not as the hard agent-integration gate. |

**Bar 2 — cleared for agent integration.**

## Open path to Bar 2

What would need to happen, in honest order:

1. ~~Decide on platform differentiation vs consolidation for `runtimes/` variants (closes B2.4).~~ Done — Wave 4.
2. ~~Add more source-anchored memos to push the ratio over half (closes B2.1).~~ Done — Wave 6 raised ratio to 54% (7 of 13); B2.1 met.
3. ~~Add two more agent-eval delta cases under `evals/agent-eval/` using the Agenda Intelligence methodology (closes B2.2).~~ Done — `customs-mirror-statistics-anomaly` and `caspian-corridor-chokepoint`.
4. ~~Make the customs / mirror-statistics agent-eval source-backed through the product shell, mapping specialist source-backed material to `user_provided` or `mixed` (closes B2.3).~~ Done — mapped to `mixed`.
5. ~~Keep each agent-eval explicitly structural-only: no factual verification, no model-quality comparison, no aggregate benchmark claim (closes B2.7 as the set grows).~~ Done for the four current compatibility cases.
6. If real agent-integrator use happens, record it publicly with permission (strengthens B2.5 positively); if not, leave the negative disclosure as it stands.
7. If the audience expands to practitioner buying-side trust, add practitioner reviews under `validated-cases/`; do not treat them as required for agent-first Bar 2.

None of these steps should be faked. Bar 2 is now cleared as a hard agent-integration bar, not as practitioner validation. Most repos in this space conflate a polished prompt with evidence that it improves agent output structure.

## Bar 3 — Demonstrated specialist lift

**Not attempted.** No criterion is met. This is the honest state, not a deferral: Bar 2 was cleared in May–August 2026 and no measurement of substantive lift has been run since.

Recorded plainly because it is the load-bearing gap in this repo. The Bar 2 agent-eval deltas are large (3/7 → 7/7 and comparable margins on the other cases), and every one of those writeups states that the rubric is structural. A structural rubric shows a large delta for any well-formed skill file. **There is currently no evidence that the Central Asia + Caspian content adds anything over the horizontal method (`global-think-tank-analyst`) on its own.** That is the claim the repo is named for.

| Criterion | Status | What is missing |
|---|---|---|
| B3.1 Substantive rubric, pre-registered (≥8 checkable substantive items) | ❌ not met | No substantive rubric exists. `evals/starter-rubric.md` and the Bar 2 agent-eval rubric are structural. |
| B3.2 Three-condition protocol documented (no skill / horizontal only / horizontal + vertical) | ❌ not met | Bar 2 cases are two-condition (with / without the product shell) and do not isolate the vertical from the horizontal method. |
| B3.3 ≥5 cases under `evals/specialist-lift/`, ≥3 distinct archetypes | ❌ not met | Directory does not exist. |
| B3.4 Blind, different-family judge | ❌ not met | One Bar 2 case (`2026-06-30-sdn-premise-stop.md`) used two blind judges including a cross-vendor one — the right method, applied to a structural rubric. Reusable here. |
| B3.5 Lift reported per case, including null and negative | ❌ not met | Nothing measured yet. |
| B3.6 ≥1 negative control (region should not change the substance) | ❌ not met | No negative control exists anywhere in `evals/`. |
| B3.7 Re-runnable harness | ❌ not met | Bar 2 cases are manual writeups; no script regenerates them. |
| B3.8 Scope statement on every Bar 3 case | ❌ not met | No cases yet. |

### Open path to Bar 3

In honest order. Steps 1 and 2 are defects and come first.

1. Fix C1 — unify the `mcp` major version across the portfolio and correct the import.
2. Fix C2 — add `[build-system]`, ship a namespaced package, and make the test import the installed name.
3. Write the substantive rubric from `docs/risk-archetypes.md` and commit it **before** generating anything (B3.1). This is the step that decides whether Bar 3 means anything; it is also the step only the author can do, because it requires the regional knowledge the repo claims to encode.
4. Build the harness and run five cases plus one negative control under the three-condition protocol (B3.2, B3.3, B3.6, B3.7).
5. Score blind with a different-family judge and publish every result, including nulls (B3.4, B3.5, B3.8).
6. Act on the answer. Positive lift: this repo is justified as a separate skill and the rubric becomes the maintenance target. Null lift: fold the regional content into the horizontal method and retire this repo. Both outcomes clear Bar 3.

Do not add more examples, archetypes or source-backed memos in place of steps 3-5. Bar 1 and Bar 2 are cleared; more of their currency does not buy Bar 3.

## What this status is not

- Not a roadmap commitment with dates.
- Not an admission of failure — Bar 1 is a genuine accomplishment for an early-stage specialist skill.
- Not a marketing document. If a future contributor finds it inconvenient, that is the point.
