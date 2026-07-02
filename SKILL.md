---
name: central-asia-caspian-hybrid-intelligence
description: Vertical specialist skill for AI agents working on Central Asia and the Caspian region — sanctions, AML, correspondent banking, beneficial-ownership opacity, corridor and logistics risk, and energy flows. Produces mechanism-first, evidence-aware, role-based risk memos. Use for Kazakhstan, Uzbekistan, Azerbaijan, Turkmenistan, Kyrgyzstan, Tajikistan, Caspian, Middle Corridor, and cross-border flows involving Russia, China, Iran, and the EU when they affect regional risk transmission.
---

# Central Asia + Caspian Hybrid Intelligence Skill

This file is the root entry point for agent discovery.

Three platform-specific variants are available — choose the one matching your environment:

| Environment | File |
|---|---|
| Claude | [`runtimes/claude/SKILL.md`](runtimes/claude/SKILL.md) |
| Codex | [`runtimes/codex/SKILL.md`](runtimes/codex/SKILL.md) |
| OpenClaw / other | [`runtimes/openclaw/SKILL.md`](runtimes/openclaw/SKILL.md) |

All three variants share the same analytical contract: mechanism-first reasoning, evidence labels (`Verified` / `Plausible` / `Judgment` / `Unknown`), role-based implications, trigger points, confidence footer, and explicit limitation notes. Platform additions are documented inside each file.

For project identity, scope, evidence rules, and agent behavior contract, read [`AGENTS.md`](AGENTS.md).
For current status against the Definition-of-Done bars, read [`STATUS.md`](STATUS.md).
