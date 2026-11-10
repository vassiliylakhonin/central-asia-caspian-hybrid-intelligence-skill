# Changelog

All notable changes to this repository are documented here.

## Unreleased

- Published shadow case `cku-public-shadow-01` under `examples/cku-public-shadow-01/`: a DRAFT public-source bankability screen of the China–Kyrgyzstan–Uzbekistan railway JV financing, produced with the corridor-bankability-analyst toolkit (separate private repo) under its public shadow test contract v1.0 (`PROSPECTIVE_BLIND`, 9 frozen public model sources, 3 sealed holdouts, internal-agent review). Published verbatim with its claim ledger (28 claims: 20 supported, 0 fabricated, 8 conflicting and carried as explicit gaps), review notes and harness report (`evidenceClass: INTERNAL_TECHNICAL_ONLY`, `marketEvidence: NONE`). This is rehearsal evidence, not market validation; it changes no Bar status, no evidence-mode counts and no flagship-example claims.
- Added a GTTA composition rule. `SKILL.md` gains a `Composition with the Horizontal Method (GTTA)` section and `docs/analysis-contract.md` expands its composition note into a shared confidence vocabulary (`Low` / `Moderate` / `High`; this repo's earlier `medium` spelling is GTTA's `Moderate`). When both skills are loaded, GTTA's memo mode and canonical output labels govern the memo structure, while this skill's mechanisms, archetypes, evidence requirements and confidence ceilings apply unchanged and narrow, never raise, the confidence level. The Confidence Footer scale is renamed to the shared labels with unchanged criteria and hard rules. Documentation-only alignment; no mode, schema, eval or benchmark change. This is Bar 2 content, not Bar 3 progress.
- Added archetype 17, **Cyber / digital-hybrid exposure**, to `docs/risk-archetypes.md` (mechanism, indicators, evidence needed, false positives, watch-next triggers, role-based mitigation questions, hard stops and confidence ceilings, anti-criteria, concrete examples, source-class row). Cyber is framed as a transmission channel into sanctions, AML, corridor and data-localisation exposure, linked to archetypes 5 and 12-14, not as a sector label. Added a scope entry in `docs/regional-logic.md`, a cyber source class and a 3-month freshness horizon in `docs/source-guide.md`, and a new `docs/currency-watch.md` topic (partly verified 2026-11-09; original legal texts and national CERT sources were not retrieved).
- Added a `live-source-backed` example, `examples/live-source-backed-cyber-digital-hybrid.md` (retrieval date 2026-11-09), with vendor threat reports, secondary reporting and explicit limits. Evidence-mode counts updated (`live-source-backed`=8).
- This is Bar 2 content. It is not Bar 3 progress: no specialist-lift run was made, frozen evals and cases were not changed, and nothing here shows that the new archetype improves analysis. The repo's own anti-criterion that examples do not substitute for measurement still applies.

- Added a fresh `live-source-backed` example on the 2026 collapse of the A7A5 ruble-stablecoin network and Kyrgyzstan's VASP-sector cleanup (`examples/live-source-backed-a7a5-collapse-kg-cleanup.md`, retrieval date 2026-11-09), using canonical Axis A / Axis B tags with primary sources (US Treasury, Council of the EU, Kyrgyz Finnadzor, FATF) cross-checked against two independent blockchain-analytics firms, and with the issuer-vs-analyst volume dispute surfaced rather than resolved. Per the Bar 3 anti-criteria in `docs/definition-of-done.md`, this example is currency maintenance for the cleared Bar 2 source-anchored ratio, **not** progress toward Bar 3: adding examples does not substitute for running the specialist-lift measurement.
- Revised `docs/currency-watch.md` in one pass: re-verified the EU sanctions-package, FATF/EAG status, and Middle Corridor (TITR) topics against primary sources dated at check, added an A7A5-network / Kyrgyz VASP-cleanup topic, and left untouched topics explicitly unverified.
- Merged the two duplicated `## Unreleased` sections in this file into one.

- Add Caspian maritime-capacity reasoning, source requirements and an optional
  quantitative-model handoff; retain the unimplemented MCP boundary and document
  separate SDK environments.

- Correct current UK source routing and preserve unverified topic status.
- Align evidence modes, calibration, and regional reference loading.
- Restore substantive documentation checks and harden specialist evaluation.

- Removed the mock streaming engine and all claims of autonomous enforcement,
  continuous graph traversal, persistent memory, or no-human-review operation.
- Replaced the enforcement-shaped JSON schema with a non-enforcing reviewer
  recommendation contract that always requires human review.
- Added a transport-independent MCP fallback contract and a standard-library CI
  test proving unavailable tools return `not_implemented` and never clearance.
- Corrected MCP docstrings and documented the graph and memory files as proposed
  data shapes rather than implemented services.
- Replaced unsupported autonomous-compliance labels in public examples with an
  explicit human-review boundary, and added a validator regression guard.
- Added a structural runtime-loading smoke record for Claude, Codex, and OpenClaw. The check covers instruction loading, safety behavior, installation, and discovery only; it is not a model-quality benchmark.
- Replaced the packaged Claude skill symlink with a composition adapter that attaches the root contract and Claude overlay in order. The validator now enforces both references, their order, and description parity with the root skill.
- Replaced the unavailable ClawHub package command with a verified direct GitHub installation command for OpenClaw. OpenClaw model behavior remains untested.
- Moved the complete runtime-neutral analytical contract into the root `SKILL.md`, which is also the packaged plugin target.
- Reduced Claude, Codex, and OpenClaw runtime files to additive overlays and added ADR 0004. The validator now rejects duplicated common sections, missing root references, and non-allowlisted overlay sections.

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
