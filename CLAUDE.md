@AGENTS.md

# Claude Code working rules

AGENTS.md is the canonical project contract: identity, scope, evidence rules, retrieved-content trust, per-claim provenance tags (Axis A/B + table-cell discipline), currency triggers, linguistic faithfulness, three-value response logic, README priorities, examples, and the Bar 1 / Bar 2 Definition of Done with honest current status. Follow it. Do not re-derive or restate those rules — apply them.

This file (CLAUDE.md) contains only Claude-Code-specific working rules for this repo, on top of the global `~/.claude/CLAUDE.md`.

## See also (project-specific anchors)

- [README.md](README.md) — public positioning, 15-section structure.
- [STATUS.md](STATUS.md) — current Bar 1 / Bar 2 status. Update truthfully; do not advance without verifiable evidence.
- [CONTRIBUTING.md](CONTRIBUTING.md) — local validator workflow and CI invariants enforced on `main`.
- [scripts/validate.py](scripts/validate.py) — authoritative structural and honesty checks.
- [docs/cold-start-interview.md](docs/cold-start-interview.md) + [templates/practice-profile.md](templates/practice-profile.md) — preflight for profile-expecting workflows.
- [docs/currency-watch.md](docs/currency-watch.md) — fast-moving topics that need re-verification.
- [evals/failure-modes.md](evals/failure-modes.md) — known canon-failure modes (incl. table-cell tag drift).

## Project-specific paths to inspect

In addition to the global pre-edit checklist:
- SKILL.md and `skills/{claude,codex,openclaw}/SKILL.md`
- examples/ (15-section flagship structure)
- docs/ (especially `source-guide.md`, `cold-start-interview.md`, `currency-watch.md`)
- evals/
- signals/ if present
- scripts/validate.py
- templates/
- .github/workflows/validate.yml

## Validator before push

CI (`.github/workflows/validate.yml`) runs file-presence checks and the skill validator. Mirror locally:

```
python3 scripts/validate.py
```

The validator enforces hardcoded structural and honesty invariants (section counts, headings, safety gates). If it fails locally, CI on `main` will fail too. Run it after any change to README, AGENTS, SKILL files, examples, evals, or docs.

## Working style in this repo

Small, reviewable changes. Do not rewrite the project unless I explicitly ask.

Do not add new infrastructure (MCP server, CLI, schemas, validators beyond the existing one) — that belongs in Agenda Intelligence MD. See AGENTS.md "Relationship to the broader stack".

When updating STATUS.md or Bar 2 criteria in AGENTS.md, the rule from AGENTS.md "Definition of done" applies: do not pretend a bar is cleared if it is not, and do not advance status without verifiable evidence.
