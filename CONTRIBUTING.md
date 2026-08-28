# Contributing

This repo is a vertical specialist skill in the Agenda Intelligence portfolio (see [AGENTS.md](AGENTS.md) for positioning and the relationship to Global Think Tank Analyst, the Gulf + Middle East sibling vertical, and Agenda Intelligence MD).

## First 15 minutes

If you've just landed in this repo and want to understand it before editing, do these in order. Each step is real-time-boxed at ~5 minutes.

**1. Read these three files, in order:**

1. [`README.md`](README.md) — what this is (Central Asia + Caspian vertical specialist), the four-repo stack, and where you draw the line versus the sibling Gulf + Middle East skill (no Iran sanctions, no GCC banking, no maritime chokepoint content here).
2. [`AGENTS.md`](AGENTS.md) — canonical project rules: identity, scope, evidence rules, retrieved-content trust, and currency triggers. It points to [`docs/analysis-contract.md`](docs/analysis-contract.md) (provenance tags, calibration, response modes, input-claim accounting), [`docs/definition-of-done.md`](docs/definition-of-done.md), and [`docs/repo-conventions.md`](docs/repo-conventions.md).
3. [`STATUS.md`](STATUS.md) — honest current state per Bar 1 / Bar 2 criterion. This is where you find out what's actually shipped vs what's claimed.

**2. Get the validator running locally:**

```bash
git clone https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill
cd central-asia-caspian-hybrid-intelligence-skill
python3 scripts/validate.py
```

Requirements: Python 3.8+. No additional packages — the validator uses the standard library. Expected final output: `PASS: repository validation complete`. CI runs the same command on every push.

**3. Read one concrete artifact end-to-end:**

- For the agent-eval validation pattern that closes Bar 2: skim [`evals/agent-eval/README.md`](evals/agent-eval/README.md) and one case file.

**Unfamiliar with a term in `AGENTS.md`?** See the [portfolio glossary](https://github.com/vassiliylakhonin/agenda-intelligence-md/blob/main/docs/glossary.md) — single source of truth across the four repos for evidence modes, uncertainty labels (`Verified`/`Plausible`/`Judgment`/`Unknown`), Axis A/B provenance tags, table-cell discipline, three-value response logic, and the maturity-framework asymmetry (this repo and the Gulf+ME sibling use Bar 1/2; `global-think-tank-analyst` uses the Maturity framework from `VALIDATION_PLAN.md`; `agenda-intelligence-md` uses `ROADMAP.md` version targets — do not transplant terminology between them).

**When something is unclear**, the lookup order is: this repo's [`AGENTS.md`](AGENTS.md) → portfolio canon ([agenda-intelligence-md/AGENTS.md](https://github.com/vassiliylakhonin/agenda-intelligence-md/blob/main/AGENTS.md), [global-think-tank-analyst/AGENTS.md](https://github.com/vassiliylakhonin/global-think-tank-analyst/blob/main/AGENTS.md)) → open an issue using the template under [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/).

---

## Before opening a PR

1. **Open an issue first** with context, the change you intend, and the evidence behind it.
2. **Keep edits tightly scoped** and evidence-driven. Prefer small, additive changes over rewrites.
3. **For prompt or skill updates, include before/after examples.**
4. **Run the validator locally** — see below. PRs that break CI on `main` will be rejected.
5. **Open a PR** with concise rationale and risk notes.

## Required artifacts for a vertical specialist skill

This repo and its sibling [Gulf + Middle East](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill) follow the same minimum file set. Keep the topology aligned.

**Root files (required, file-presence checked by `.github/workflows/validate.yml`):**
- `README.md` — public positioning per [`docs/repo-conventions.md`](docs/repo-conventions.md) "README priorities"
- `AGENTS.md` — canonical project contract (identity, scope, evidence rules, Definition of Done)
- `CLAUDE.md` — Claude Code working rules (inherits AGENTS.md)
- `SKILL.md` — complete canonical runtime-neutral skill contract
- `STATUS.md` — honest Bar 1 / Bar 2 status
- `CONTRIBUTING.md` — this file
- `LICENSE`
- `SECURITY.md`
- `llms.txt` — orientation for LLMs and agent indexers
- `.gitignore`

**Directories (required):**
- `skills/central-asia-caspian/SKILL.md` — regular Claude Code composition adapter that attaches the root contract first and the Claude overlay second
- `runtimes/{claude,codex,openclaw}/SKILL.md` — additive runtime overlays loaded after the root contract
- `examples/` — flagship memos; every non-`README.md` file must declare an `Evidence mode:`
- `evals/` — must contain `checklist.md`, `failure-modes.md`, `starter-rubric.md`; `evals/agent-eval/` holds Bar 2 cases
- `docs/` — including `source-guide.md`, `currency-watch.md`, `cold-start-interview.md`, `regional-logic.md`, `risk-archetypes.md`
- `templates/` — at minimum `practice-profile.md`
- `scripts/` — at minimum `validate.py`
- `.github/workflows/validate.yml`

**Optional artifacts (present in this repo, not currently required by validator):**
- `CONTEXT.md` — keeps the regional / portfolio vocabulary distinct across the four-repo stack (vertical specialist vs Agenda Intelligence MD vs Global Think Tank Analyst vs regional lens). Update if a term is reused or repositioned.

**Sibling-repo deltas (intentional):**
- The Gulf + Middle East skill carries `signals/` and `taxonomy.json` (with a `render-readme.py` helper) for its archetype taxonomy and signal feed. CA-Caspian does not currently publish signals; if added, mirror the four-file consistency pattern.

`scripts/validate.py` is the authoritative list. Run it after any structural change.

## Local validation

CI runs `scripts/validate.py` on every push. Run it locally before opening a PR:

```bash
python3 scripts/validate.py
```

Expected final output: `PASS: repository validation complete`.

The validator enforces packaging, structural, link, and honesty invariants. Common reasons it fails:

- **Required root files missing.** `AGENTS.md`, `README.md`, `STATUS.md` must all be present.
- **README forbidden claims.** Phrases like `guarantees compliance`, `guarantees accuracy`, `detects sanctions evasion`, `fully autonomous`, `trusted by`, `used by` are blocked.
- **README disclosure missing.** README must contain the line: `no production-usage, adoption or benchmark numbers are claimed`.
- **Companion repo links missing.** README must link to [Gulf + Middle East](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill), [Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst), and [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md).
- **STATUS.md must state Bar 2 status honestly.** The current evidence requires the exact phrase `**Bar 2 — cleared for agent integration.**`; do not change it without updating the evidence in `STATUS.md`.
- **Packaged skill composition drift.** `skills/central-asia-caspian/SKILL.md` must be a regular file whose `name` matches its directory and whose description matches the root contract. It must attach `${CLAUDE_PLUGIN_ROOT}/SKILL.md` once, then `${CLAUDE_PLUGIN_ROOT}/runtimes/claude/SKILL.md` once, without copying their sections. Both plugin manifests must stay synchronized.
- **Example evidence-mode count is stale.** Every file in `examples/*.md` (except `README.md`) must declare an `Evidence mode:` of `reasoning-only`, `illustrative source packet`, `live-source-backed`, or `user-provided sources`. The README's mode-count summary line and STATUS.md's source-anchored ratio must match the actual count. If you add or change an example, update both.
- **Live-source-backed and user-provided sources examples** must include a `Retrieval date: YYYY-MM-DD`.
- **The root `SKILL.md`** must contain every common analytical section and required safety phrase defined in `REQUIRED_CANONICAL_SECTIONS` and `REQUIRED_CANONICAL_BODY_PHRASES`.
- **Runtime overlays** must load `../../SKILL.md` first, contain only their allowlisted platform sections, keep a description of at least 120 characters, avoid determinative language, and have balanced fenced code blocks. Copying a common root section into an overlay fails validation.

Read [`scripts/validate.py`](scripts/validate.py) directly for the authoritative list of constraints — the validator is the source of truth.

## Content rules

When editing docs, examples, or skill instructions:

- Separate facts, assessments, assumptions, scenarios, and unknowns.
- Preserve evidence-mode labels and uncertainty language.
- Do not fabricate citations, dates, policy changes, sanctions details, incidents, or metrics.
- Do not add hype or unsupported claims.
- Keep the project credible, conservative, and decision-useful.

The full content contract for this repo lives in [AGENTS.md](AGENTS.md). [CLAUDE.md](CLAUDE.md) inherits from it for Claude Code sessions.

**Where a new rule goes.** `AGENTS.md` is the contract and stays short; task-specific detail lives in `docs/` and is reached from it by a pointer — see AGENTS.md "Where a new rule goes". Adding a section to `AGENTS.md` when it belongs in `docs/analysis-contract.md`, `docs/definition-of-done.md`, or `docs/repo-conventions.md` is the drift this layout exists to prevent. Bar status belongs in `STATUS.md` only; a second copy goes stale and then contradicts the first.

## Project boundaries

This repo is a domain skill, not an infrastructure product. Do not add or imply:

- MCP server functionality
- CLI tooling
- schemas or validators beyond `scripts/validate.py`
- runtime infrastructure
- live intelligence collection
- factuality verification guarantees
- legal, sanctions, investment, or security advice
- claims of operational monitoring maturity

Product linting, schemas, and runtime tooling belong in the [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) repo. This repo may keep dependency-free CI validators for its own documentation and handoff examples. Cross-region maritime and Gulf-specific content belongs in [Gulf + Middle East Hybrid Intelligence Skill](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill).

## PR checklist

- [ ] `python3 scripts/validate.py` passes locally, including package, handoff, and link checks
- [ ] If an example was added or renamed: README.md examples list, `examples/README.md`, and the README mode-count summary line are all updated in the same PR
- [ ] Behavior or positioning change noted in commit message or PR description
- [ ] No claims of external verification, validation, MCP, CLI, or CI checks unless truly implemented in this repo
- [ ] No exaggerated language ("revolutionary", "production-grade", "guarantees correctness", "fully autonomous")

## Contact

Author: Vassiliy Lakhonin · [github.com/vassiliylakhonin](https://github.com/vassiliylakhonin)

For questions about positioning, the broader Agenda Intelligence portfolio, or potential review collaboration, open an issue on this repository.
