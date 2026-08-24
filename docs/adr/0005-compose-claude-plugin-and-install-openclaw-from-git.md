# Compose the Claude plugin and install OpenClaw from Git

Status: accepted, 2026-08-24

## Context

ADR 0004 made the root `SKILL.md` the common contract and kept `skills/central-asia-caspian/SKILL.md` as a symlink to it. A Claude Code 2.1.233 smoke test loaded the root contract but did not load `runtimes/claude/SKILL.md`; a Markdown link from the root did not compose the overlay into the skill. The documented ClawHub slug also returned `Skill not found` with ClawHub CLI 0.7.0.

Claude Code plugin skills can attach supporting files with `@` references and resolve `${CLAUDE_PLUGIN_ROOT}` to the plugin root. This behavior is documented in the [official Claude Code skills documentation](https://code.claude.com/docs/en/skills).

## Decision

`skills/central-asia-caspian/SKILL.md` is a regular Claude Code composition adapter. It attaches exactly two files, in this order:

1. `${CLAUDE_PLUGIN_ROOT}/SKILL.md`
2. `${CLAUDE_PLUGIN_ROOT}/runtimes/claude/SKILL.md`

The adapter repeats only the package frontmatter and a short composition instruction. It does not copy common or Claude-specific analytical sections.

OpenClaw installation uses the repository directly:

```bash
openclaw skills install git:https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill.git --as central-asia-caspian
```

`scripts/validate.py` enforces the adapter's file type, name, root-description parity, references, order, and absence of copied sections. It also checks the exact OpenClaw installation command.

## Consequences

- A Claude plugin invocation loads the common contract and the Claude overlay through a supported composition mechanism.
- The root remains the only copy of common analytical behavior; the package adapter is a platform seam, not another contract.
- OpenClaw no longer depends on an unavailable ClawHub listing. Direct GitHub and local-checkout installations work with OpenClaw 2026.7.1.
- The structural smoke test is recorded in [`../../evals/2026-08-24-runtime-loading-smoke.md`](../../evals/2026-08-24-runtime-loading-smoke.md).
- This decision supersedes ADR 0004 only for the package symlink and ClawHub installation path. It does not add factual verification, measure model quality, or establish OpenClaw model behavior.
