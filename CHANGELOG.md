# Changelog

All notable changes to this repository are documented here.

## Unreleased

- Fixed the packaged skill identifier so `skills/central-asia-caspian/SKILL.md` matches its discovery directory and the `central-asia-caspian` plugin name.
- Extended `scripts/validate.py` into the single local/CI interface for required files, package metadata, runtime overlays, examples, the evidence-packet handoff, links, and safety gates.
- Corrected stale contributor and agent-index documentation, removed unsupported "production stack" wording, and documented the existing Claude Code marketplace install path.

- Fixed a dead link to the author's site: `deal-risk-gate.html` has returned 404 since the site was restructured, and the README described two browser demos that are no longer published. The sentence now points at `examples/`.
- Extended `scripts/check_markdown_links.py` to fail on 404/410 for links to the author's own site, which previously went unchecked because every `http(s)://` target was skipped. Network errors and other statuses are reported without failing; `SKIP_SITE_LINK_CHECK=1` skips the network step.

- Conformed the repo to the Agent Plugins 1.0.0 layout: added a root `plugin.json` with the `$schema` identifier from <https://agent-plugins.org>. `.claude-plugin/plugin.json` is unchanged and still serves the Claude Code install path; the specification ignores that directory. `skills/central-asia-caspian/SKILL.md` is the single plugin discovery path, with its name/path invariant now enforced by `scripts/validate.py`. The manifest validates against the published Draft 2020-12 schema.

- Added an Agenda Intelligence v1.3 evidence-packet handoff, a runnable synthetic regional packet, a dependency-free CI validator, and ADR 0003. Reclassified the older `analyze` / memo-validation composition as compatibility behavior.

- Renamed the runtime-overlay directory `skills/{claude,codex,openclaw}/` to `runtimes/{claude,codex,openclaw}/` and updated every path reference (README, AGENTS, CLAUDE, CONTRIBUTING, STATUS, evals, validator, CI workflow). `skills/` is now reserved for Claude Code plugin packaging, because plugin installs auto-discover every `skills/*/SKILL.md` as a separate skill and the overlay layout produced junk-named skills (`claude`, `codex`, `openclaw`).
- Packaged the repo as an installable Claude Code plugin: added `.claude-plugin/plugin.json` and `skills/central-asia-caspian/SKILL.md` (a symlink to the canonical root `SKILL.md`). Installable via `/plugin marketplace add vassiliylakhonin/agenda-intelligence-md`, then `/plugin install central-asia-caspian@agenda-intelligence`.

- Clarified the repo's commercial role: Central Asia + Caspian remains a regional specialist reasoning layer and portfolio/demo support module, not the active Agenda Intelligence MD commercial wedge. Added README/AGENTS guidance to avoid reviving Kazakhstan/local-forwarder or Middle Corridor buyer-facing positioning without fresh discovery evidence.
- Added the unified portfolio stack-map table to `README.md` section 7, with the vertical-specialist row bolded for this repo.
- Added a "Project maturity" callout under section 7 pointing readers to [STATUS.md](STATUS.md) (Bar 1 / Bar 2 framework) and [AGENTS.md](AGENTS.md) "Definition of done".
- Added `.github/ISSUE_TEMPLATE/{bug_report,feature_request}.md` and `.github/pull_request_template.md` so contributors have a structured entry point.
- Added this CHANGELOG.
- Cross-referenced the portfolio-wide skill packaging convention in `AGENTS.md` "Relationship to the broader stack".
