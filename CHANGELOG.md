# Changelog

All notable changes to this repository are documented here.

## Unreleased

- Renamed the runtime-overlay directory `skills/{claude,codex,openclaw}/` to `runtimes/{claude,codex,openclaw}/` and updated every path reference (README, AGENTS, CLAUDE, CONTRIBUTING, STATUS, evals, validator, CI workflow). `skills/` is now reserved for Claude Code plugin packaging, because plugin installs auto-discover every `skills/*/SKILL.md` as a separate skill and the overlay layout produced junk-named skills (`claude`, `codex`, `openclaw`).
- Packaged the repo as an installable Claude Code plugin: added `.claude-plugin/plugin.json` and `skills/central-asia-caspian/SKILL.md` (a symlink to the canonical root `SKILL.md`). Installable via `/plugin marketplace add vassiliylakhonin/agenda-intelligence-md`, then `/plugin install central-asia-caspian@agenda-intelligence`.

- Clarified the repo's commercial role: Central Asia + Caspian remains a regional specialist reasoning layer and portfolio/demo support module, not the active Agenda Intelligence MD commercial wedge. Added README/AGENTS guidance to avoid reviving Kazakhstan/local-forwarder or Middle Corridor buyer-facing positioning without fresh discovery evidence.
- Added the unified portfolio stack-map table to `README.md` section 7, with the vertical-specialist row bolded for this repo.
- Added a "Project maturity" callout under section 7 pointing readers to [STATUS.md](STATUS.md) (Bar 1 / Bar 2 framework) and [AGENTS.md](AGENTS.md) "Definition of done".
- Added `.github/ISSUE_TEMPLATE/{bug_report,feature_request}.md` and `.github/pull_request_template.md` so contributors have a structured entry point.
- Added this CHANGELOG.
- Cross-referenced the portfolio-wide skill packaging convention in `AGENTS.md` "Relationship to the broader stack".
