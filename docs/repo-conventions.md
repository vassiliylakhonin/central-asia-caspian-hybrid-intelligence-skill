# Repository conventions

Contributor-facing conventions for this repo: how the README is structured, what examples must carry, how evaluation docs must be labelled, and what to run before finalizing a change.

Referenced from `AGENTS.md`. Bar 1 criterion B1.1 refers to the "README priorities" section below.

## README priorities

README should make value clear in 30 seconds.

Recommended structure:
1. One-line positioning
2. Problem
3. Try this prompt
4. What it does
5. What it is not
6. Relationship to Agenda Intelligence MD and Global Think Tank Analyst
7. Quick usage
8. Before / after
9. Flagship examples and examples learning path
10. Skill files
11. Source guide
12. Risk archetypes
13. Review checklist
14. Limitations
15. Roadmap

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

Examples should be navigable as a learning path, not only as a flat file list. Keep `examples/README.md` aligned with the flagship examples section in `README.md`.

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
