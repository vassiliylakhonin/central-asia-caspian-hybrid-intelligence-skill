# Use the root contract with additive runtime overlays

Status: accepted, 2026-08-24

## Context

The repository convention already named the root `SKILL.md` as the canonical runtime-neutral contract and `runtimes/{claude,codex,openclaw}/SKILL.md` as additive overlays. The files did not follow that convention. The root was a 22-line selector, while each runtime file copied the full analytical contract.

That structure caused two problems. The packaged Claude Code skill points to the root, so installation exposed the selector instead of the analytical contract. The three full copies also drifted: Codex had unrecorded edits to common instructions that were neither required by the platform nor shared with the other runtimes.

## Decision

The root `SKILL.md` is the complete runtime-neutral contract. Its common analytical sections use the previously documented OpenClaw baseline, with relative links adjusted for the root location.

Runtime files are small adapters loaded after the root:

- Claude adds retrieval, document-reading, and evidence-mode guidance.
- Codex adds multi-step loop, file-output, and downstream-validation guidance.
- OpenClaw adds ClawHub packaging and installation guidance without changing analytical behavior.

The packaged skill remains a symlink to the root. `scripts/validate.py` checks the full root contract, requires every overlay to load it first, allowlists each overlay's sections, and rejects common contract sections inside overlays.

## Consequences

- A plugin install receives the complete baseline skill without following a selector to another file.
- Common behavior changes in one place. Runtime adapters stay local to platform behavior.
- The documented Claude and Codex differences remain intact. Unrecorded wording drift is removed rather than treated as platform behavior.
- OpenClaw keeps its package identifier and install command, but it is no longer described as the canonical content source; the root is canonical.
- This is a structural refactor. It does not add factual validation, live retrieval, or new evidence that the skill improves model output.
