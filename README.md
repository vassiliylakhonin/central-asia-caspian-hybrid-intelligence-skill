# Central Asia + Caspian Hybrid Intelligence Skills

<p align="left">
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/stargazers"><img src="https://img.shields.io/github/stars/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="GitHub stars"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/network/members"><img src="https://img.shields.io/github/forks/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="GitHub forks"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/blob/main/LICENSE"><img src="https://img.shields.io/github/license/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/validate.yml?branch=main&style=for-the-badge" alt="Validate"></a>
  <a href="https://clawhub.ai/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-v3-1"><img src="https://img.shields.io/badge/ClawHub-OpenClaw%20Skill-111827?style=for-the-badge" alt="ClawHub"></a>
</p>

**Decision-grade geopolitical and risk analysis framework for Central Asia + Caspian** — packaged for **OpenClaw**, **Codex**, and **Claude**.

> Built for teams that need clear causal analysis, practical implications, and decision-ready structure — not generic geopolitics filler.

## Why this repo

- Produces structured outputs in three modes: **Risk / Compliance**, **Strategic / Think Tank**, **Hybrid**
- Enforces uncertainty discipline: `Verified`, `Plausible`, `Judgment`, `Unknown`
- Focuses on mechanisms: flows, chokepoints, transmission channels, value capture
- Ends with action relevance: trigger points, implications, confidence footer

## Quick start

### OpenClaw
Install from ClawHub:

```bash
clawhub install central-asia-caspian-hybrid-intelligence-v3-1
```

ClawHub page: `https://clawhub.ai/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-v3-1`

### Codex / Claude
Use the corresponding `SKILL.md` file as operating instruction in your agent setup.

## What’s inside

- `skills/openclaw/SKILL.md` — canonical OpenClaw skill
- `skills/codex/SKILL.md` — Codex variant with expanded trigger description
- `skills/claude/SKILL.md` — Claude variant with valid YAML frontmatter
- `scripts/validate_skills.py` — dependency-free validation for skill metadata and safety gates

## Best use cases

- cross-border risk, sanctions, AML, banking, routing, ownership
- political economy, system dynamics, corridors, strategic competition
- investment, logistics, energy, infrastructure, AI, state capacity
- questions requiring both explanation and decision implications

## Not intended for

- formal legal advice or compliance determinations
- purely local issues without cross-border relevance
- generic summaries without analytical mechanism
- highly technical specialist-only domains

## If this helps your work

⭐ Star the repo — it helps others discover serious analytical skills faster.

## Disclaimer

This repository provides analytical guidance only and does not constitute legal, regulatory, tax, audit, or investment advice.

## Validation

```bash
python3 scripts/validate_skills.py
```

## Example Prompts

**Risk mode:**
```
Analyze sanctions exposure for a bank operating in Kazakhstan.
```

**Strategic mode:**
```
Explain the impact of Middle Corridor developments on regional power dynamics.
```

**Hybrid mode:**
```
Assess investment risks in Uzbekistan's energy sector over the next 12 months.
```
