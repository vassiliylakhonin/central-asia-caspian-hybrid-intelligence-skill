@AGENTS.md

# Claude Code working rules

This repository is Central Asia Caspian Hybrid Intelligence Skill.

It should remain a focused AI-agent skill and intelligence-analysis repository for Central Asia, the Caspian region, hybrid risks, infrastructure, geopolitics, and strategic monitoring.

## See also

The canonical contract for this repo is [AGENTS.md](AGENTS.md) (imported above for Claude Code; read it directly when reviewing as a human). Before editing, also consult:

- [README.md](README.md) — public positioning, structure invariants and the 15-section template.
- [STATUS.md](STATUS.md) — current Bar 1 / Bar 2 honesty status. Update truthfully; do not advance without verifiable evidence.
- [CONTRIBUTING.md](CONTRIBUTING.md) — local validator workflow and CI invariants enforced on `main`.
- [scripts/validate_skills.py](scripts/validate_skills.py) — authoritative list of structural and honesty checks. Run before finalizing changes.

## How to work in this repo

Before editing, inspect relevant project files when present:
- README.md
- AGENTS.md
- SKILL.md
- llms.txt
- examples/
- docs/
- signals/
- evals/

Prefer small, safe, reviewable changes.

Do not rewrite the project unless explicitly asked.

## Preserve project boundaries

Do not add or imply:
- MCP server functionality;
- CLI tooling;
- schemas or validators;
- runtime infrastructure;
- live intelligence collection;
- factuality verification guarantees;
- legal, sanctions, investment, or security advice;
- production-grade monitoring guarantees.

If any of these are discussed, present them as possible future work only when explicitly requested.

## Content rules

When editing docs, examples, or skill instructions:
- separate facts, assessments, assumptions, scenarios, and unknowns;
- preserve evidence-mode labels and uncertainty language;
- do not fabricate citations, dates, policy changes, sanctions details, incidents, or metrics;
- do not add hype or unsupported claims;
- keep the project credible, conservative, and decision-useful.

## Definition of done

Before finishing, report:
1. what changed;
2. why it matters;
3. what was not changed;
4. how I can verify it;
5. risks or follow-ups.
