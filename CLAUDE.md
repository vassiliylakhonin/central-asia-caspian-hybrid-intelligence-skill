@AGENTS.md

# Claude Code working rules

`AGENTS.md` is the canonical project contract — apply it, do not restate it. It points to three detail files, loaded when the task needs them:

- [docs/analysis-contract.md](docs/analysis-contract.md) — provenance tags, calibration, response modes, input-claim accounting. Read before producing or reviewing a memo.
- [docs/definition-of-done.md](docs/definition-of-done.md) — Bar 1 / Bar 2 criteria and anti-criteria.
- [docs/repo-conventions.md](docs/repo-conventions.md) — README structure, example requirements, eval labelling.

## Repo-specific anchors

- [STATUS.md](STATUS.md) — the only place bar status lives. Update truthfully; never advance without verifiable evidence.
- [scripts/validate.py](scripts/validate.py) — authoritative structural and honesty checks; it enforces hardcoded section counts, headings, and safety gates.
- [docs/cold-start-interview.md](docs/cold-start-interview.md) + [templates/practice-profile.md](templates/practice-profile.md) — preflight for profile-expecting workflows; the STOP rule in AGENTS.md applies.
- [docs/currency-watch.md](docs/currency-watch.md) — topics needing re-verification, 90-day staleness rule.
- [evals/failure-modes.md](evals/failure-modes.md) — known canon-failure modes, including table-cell tag drift.
- [docs/source-guide.md](docs/source-guide.md) — regional source tiers and freshness horizons.

## Validator before push

```
python3 scripts/validate.py
```

CI (`.github/workflows/validate.yml`) runs file-presence checks plus this validator. If it fails locally, `main` fails too. Run it after any change to README, AGENTS, SKILL files, examples, evals, or docs.

## Boundary

Do not add infrastructure here — MCP server, CLI, schemas, or validators beyond the existing one belong in Agenda Intelligence MD. See AGENTS.md "Relationship to the broader stack".
