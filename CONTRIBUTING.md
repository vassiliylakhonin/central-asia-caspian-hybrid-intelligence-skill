# Contributing

This repo is a vertical specialist skill in the Agenda Intelligence portfolio (see [AGENTS.md](AGENTS.md) for positioning and the relationship to Global Think Tank Analyst, the Gulf + Middle East sibling vertical, and Agenda Intelligence MD).

## First 15 minutes

If you've just landed in this repo and want to understand it before editing, do these in order. Each step is real-time-boxed at ~5 minutes.

**1. Read these three files, in order:**

1. [`README.md`](README.md) — what this is (Central Asia + Caspian vertical specialist), the four-repo stack, and where you draw the line versus the sibling Gulf + Middle East skill (no Iran sanctions, no GCC banking, no maritime chokepoint content here).
2. [`AGENTS.md`](AGENTS.md) — canonical project rules: scope, evidence rules, per-claim provenance tags (Axis A/B + table-cell discipline), currency triggers, three-value response logic, README priorities, and the Bar 1 / Bar 2 Definition of Done.
3. [`STATUS.md`](STATUS.md) — honest current state per Bar 1 / Bar 2 criterion. This is where you find out what's actually shipped vs what's claimed.

**2. Get the validator running locally:**

```bash
git clone https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill
cd central-asia-caspian-hybrid-intelligence-skill
python3 scripts/validate.py
```

Requirements: Python 3.8+. No additional packages — the validator uses the standard library. Expected success output: `ok: skill files validated`. CI runs this on every push; run it locally before pushing or `main` will go red.

**3. Read one concrete artifact end-to-end:**

- A `live-source-backed` flagship example, e.g. [`examples/live-source-backed-bank-correspondent.md`](examples/live-source-backed-bank-correspondent.md). Look for: evidence mode declaration at top, per-claim provenance tags inside the body and in tables (table-cell discipline), retrieval date, mechanism-first structure, what the limitation note actually limits.
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
- `README.md` — public positioning per AGENTS.md "README priorities"
- `AGENTS.md` — canonical project contract (identity, scope, evidence rules, Definition of Done)
- `CLAUDE.md` — Claude Code working rules (inherits AGENTS.md)
- `SKILL.md` — runtime skill contract
- `STATUS.md` — honest Bar 1 / Bar 2 status
- `CONTRIBUTING.md` — this file
- `LICENSE`
- `SECURITY.md`
- `llms.txt` — orientation for LLMs and agent indexers
- `.gitignore`

**Directories (required):**
- `runtimes/{claude,codex,openclaw}/SKILL.md` — runtime variants per platform
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

Expected success output: `ok: skill files validated`.

The validator enforces structural and honesty invariants. Common reasons it fails:

- **Required root files missing.** `AGENTS.md`, `README.md`, `STATUS.md` must all be present.
- **README forbidden claims.** Phrases like `guarantees compliance`, `guarantees accuracy`, `detects sanctions evasion`, `fully autonomous`, `trusted by`, `used by` are blocked.
- **README disclosure missing.** README must contain the line: `no production-usage, adoption or benchmark numbers are claimed`.
- **Companion repo links missing.** README must link to [Gulf + Middle East](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill), [Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst), and [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md).
- **STATUS.md must state Bar 2 status honestly.** The exact phrase `**Bar 2 — not cleared.**` must appear (until Bar 2 is genuinely cleared with verifiable evidence).
- **Example evidence-mode count is stale.** Every file in `examples/*.md` (except `README.md`) must declare an `Evidence mode:` of `reasoning-only`, `illustrative source packet`, `live-source-backed`, or `user-provided sources`. The README's mode-count summary line and STATUS.md's source-anchored ratio must match the actual count. If you add or change an example, update both.
- **Live-source-backed and user-provided sources examples** must include a `Retrieval date: YYYY-MM-DD`.
- **Skill files** under `runtimes/{openclaw,codex,claude}/SKILL.md` must:
  - have YAML frontmatter with a lowercase-slug `name` and a `description` of at least 120 characters;
  - contain every required `##` section (see `REQUIRED_SECTIONS` in the validator);
  - contain required body phrases (`Primary driver is:`, `Compliance note`, `Disclaimer`, `Author: Vassiliy Lakhonin`, `official sanctions lists`, `Do not use for formal legal/compliance determinations`);
  - avoid determinative or unsafe phrases (`fully compliant`, `no sanctions risk`, `guaranteed compliant`, `this is a legal determination`, `constitutes legal advice`);
  - have balanced fenced code blocks.

Read [`scripts/validate.py`](scripts/validate.py) directly for the authoritative list of constraints — the validator is the source of truth.

## Content rules

When editing docs, examples, or skill instructions:

- Separate facts, assessments, assumptions, scenarios, and unknowns.
- Preserve evidence-mode labels and uncertainty language.
- Do not fabricate citations, dates, policy changes, sanctions details, incidents, or metrics.
- Do not add hype or unsupported claims.
- Keep the project credible, conservative, and decision-useful.

The full content contract for this repo lives in [AGENTS.md](AGENTS.md). [CLAUDE.md](CLAUDE.md) inherits from it for Claude Code sessions.

## Project boundaries

This repo is a domain skill, not an infrastructure product. Do not add or imply:

- MCP server functionality
- CLI tooling
- schemas or validators beyond `scripts/validate.py`
- runtime infrastructure
- live intelligence collection
- factuality verification guarantees
- legal, sanctions, investment, or security advice
- production-grade monitoring guarantees

Validation, schemas, scoring and audit tooling belong in the [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) repo. Cross-region maritime and Gulf-specific content belongs in [Gulf + Middle East Hybrid Intelligence Skill](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill).

## PR checklist

- [ ] `python3 scripts/validate.py` passes locally
- [ ] If an example was added or renamed: README.md examples list, `examples/README.md`, and the README mode-count summary line are all updated in the same PR
- [ ] Behavior or positioning change noted in commit message or PR description
- [ ] No claims of external verification, validation, MCP, CLI, or CI checks unless truly implemented in this repo
- [ ] No exaggerated language ("revolutionary", "production-grade", "guarantees correctness", "fully autonomous")

## Contact

Author: Vassiliy Lakhonin · [vassiliylakhonin.github.io](https://vassiliylakhonin.github.io/)

For questions about positioning, the broader Agenda Intelligence portfolio, or potential review collaboration, open an issue or use the contact path on the portfolio site.
