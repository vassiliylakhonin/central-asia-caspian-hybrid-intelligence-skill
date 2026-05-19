# Contributing

This repo is a vertical specialist skill in the Agenda Intelligence portfolio (see [AGENTS.md](AGENTS.md) for positioning and the relationship to Global Think Tank Analyst, the Gulf + Middle East sibling vertical, and Agenda Intelligence MD).

## Before opening a PR

1. **Open an issue first** with context, the change you intend, and the evidence behind it.
2. **Keep edits tightly scoped** and evidence-driven. Prefer small, additive changes over rewrites.
3. **For prompt or skill updates, include before/after examples.**
4. **Run the validator locally** — see below. PRs that break CI on `main` will be rejected.
5. **Open a PR** with concise rationale and risk notes.

## Local validation

CI runs `scripts/validate_skills.py` on every push. Run it locally before opening a PR:

```bash
python3 scripts/validate_skills.py
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
- **Skill files** under `skills/{openclaw,codex,claude}/SKILL.md` must:
  - have YAML frontmatter with a lowercase-slug `name` and a `description` of at least 120 characters;
  - contain every required `##` section (see `REQUIRED_SECTIONS` in the validator);
  - contain required body phrases (`Primary driver is:`, `Compliance note`, `Disclaimer`, `Author: Vassiliy Lakhonin`, `official sanctions lists`, `Do not use for formal legal/compliance determinations`);
  - avoid determinative or unsafe phrases (`fully compliant`, `no sanctions risk`, `guaranteed compliant`, `this is a legal determination`, `constitutes legal advice`);
  - have balanced fenced code blocks.

Read [`scripts/validate_skills.py`](scripts/validate_skills.py) directly for the authoritative list of constraints — the validator is the source of truth.

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
- schemas or validators beyond `scripts/validate_skills.py`
- runtime infrastructure
- live intelligence collection
- factuality verification guarantees
- legal, sanctions, investment, or security advice
- production-grade monitoring guarantees

Validation, schemas, scoring and audit tooling belong in the [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) repo. Cross-region maritime and Gulf-specific content belongs in [Gulf + Middle East Hybrid Intelligence Skill](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill).

## PR checklist

- [ ] `python3 scripts/validate_skills.py` passes locally
- [ ] If an example was added or renamed: README.md examples list, `examples/README.md`, and the README mode-count summary line are all updated in the same PR
- [ ] Behavior or positioning change noted in commit message or PR description
- [ ] No claims of external verification, validation, MCP, CLI, or CI checks unless truly implemented in this repo
- [ ] No exaggerated language ("revolutionary", "production-grade", "guarantees correctness", "fully autonomous")

## Contact

Author: Vassiliy Lakhonin · [vassiliylakhonin.github.io](https://vassiliylakhonin.github.io/)

For questions about positioning, the broader Agenda Intelligence portfolio, or potential review collaboration, open an issue or use the contact path on the portfolio site.
