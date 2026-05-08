# Worked scoring example

A worked example of applying [`evals/starter-rubric.md`](starter-rubric.md) to a memo in this repo. **Honest label:** worked example, not a validated benchmark. Scores below are reviewer judgments by the author against the rubric, not aggregate or peer-reviewed scores.

## Memo under review

[`examples/fintech-sanctions-routing.md`](../examples/fintech-sanctions-routing.md) — fintech sanctions and routing exposure across KZ / UZ / Caspian-connected trade routes. Evidence mode: `reasoning-only`.

## Scorecard

Scale: 0 (missing or wrong) / 1 (partial) / 2 (solid). Hard-fail dimensions are marked ⚠.

### A. Scope and framing

| # | Dimension | Score | Note |
|---|---|---|---|
| 1 | Geography correctly scoped | 2 | KZ / UZ core; Caspian included only via routing (Aktau, Baku, Middle Corridor); no decorative geography. |
| 2 | Concrete risk / strategy framing | 2 | Framed around correspondent de-risking and routing exposure with explicit consequences for the fintech, not as a regional essay. |
| 3 | Time horizon stated | 2 | "Next 6–12 months" stated in question and assumptions. |
| 4 | Audience / role identified | 2 | SME-facing cross-border fintech in KZ / UZ; role explicit throughout. |

Section A: **8 / 8**.

### B. Reasoning quality

| # | Dimension | Score | Note |
|---|---|---|---|
| 5 | Primary driver explicitly stated | 2 | `Primary driver is:` Western enforcement attention on Russia-adjacent re-export and dual-use corridors transmitted via correspondent banks and acquirers. |
| 6 | Mechanism before implications | 2 | 5-step transmission chain provided before exposure / actions. |
| 7 | Exposure map | 2 | Banking rails, counterparties, routing, ownership and geography all mapped. |
| 8 | Actor incentives and leverage | 2 | "Who gains / who loses leverage" section explicit. |
| 9 | Trigger points and watch-next | 2 | Seven concrete triggers including HS-code mirror-data anomalies and correspondent withdrawals. |
| 10 | Role-based implications | 2 | Bank, fintech, investor, logistics operator each addressed. |

Section B: **12 / 12**.

### C. Evidence discipline ⚠

| # | Dimension | Score | Note |
|---|---|---|---|
| 11 | Evidence mode stated with canonical label | 2 | `Evidence mode: reasoning-only` stated at top. |
| 12 | `Verified` / `Plausible` / `Judgment` / `Unknown` labels used | 2 | Bottom-line labeled `Judgment`; specific items labeled `Plausible` and `Unknown`. |
| 13 | No fabricated citations / IDs / dates / prices | 2 | No invented designations, statutes, dates or numbers. |
| 14 | Time-sensitive claims flagged for re-verification | 2 | Sanctions / list / AML claims flagged as `Unknown` and explicitly requiring verification. |

Section C: **8 / 8**. No hard fails.

### D. Tone and safety ⚠

| # | Dimension | Score | Note |
|---|---|---|---|
| 15 | No determinative compliance language | 2 | "Subject to internal policy and regulatory review" used; no `fully compliant`, `no risk`, `guaranteed`. |
| 16 | No legal / advice posture | 2 | Actions framed as illustrative; explicit "not legal / sanctions / AML / compliance / tax / investment advice". |
| 17 | Limitation note | 2 | Final section is a clear limitation note. |
| 18 | No claim of screening / monitoring / verification | 2 | Explicitly states the skill does not screen any counterparty. |

Section D: **8 / 8**. No hard fails.

### E. Decision usefulness

| # | Dimension | Score | Note |
|---|---|---|---|
| 19 | What would change the judgment | 2 | Section "What would change the judgment" with four concrete conditions. |
| 20 | Confidence footer | 2 | Confidence level + assumptions + unknowns + indicators. |
| 21 | Usable starting point without misleading | 2 | Bounded by `reasoning-only` evidence mode; structure is decision-useful within that boundary. |

Section E: **6 / 6**.

## Aggregate

- **Total: 42 / 42.**
- **No hard fails in section C or D.**
- Above the working "≥ 32 with no hard fails = reasonable working draft" threshold.

## Reviewer commentary

The memo scores at the top of the rubric because it (a) is rigorously bounded by `reasoning-only` evidence mode and refuses to assert specific facts, (b) follows the canonical analytical structure end to end, and (c) keeps role-based actions cautious and clearly illustrative.

A higher-stakes operational memo would need a different evidence mode (`user-provided sources` or `live-source-backed`) and would be scored against the same rubric with the additional expectation that factual claims are traceable to the supplied or retrieved sources. The rubric scores **structure and discipline**, not factual correctness — a memo can score 42 / 42 and still be wrong on a specific designation that requires source-backed verification.

## Honest limits of this scorecard

- These scores are **reviewer judgments by the author**, not peer-reviewed or aggregated.
- The thresholds in `starter-rubric.md` are working defaults, not validated cutoffs.
- The rubric does not test factual correctness, only structure and evidence discipline.
- A single worked example is not a benchmark.
