# Starter rubric

A starter rubric for scoring memos produced with this skill against the analytical contract in `AGENTS.md`. **Honest label:** starter rubric, not a validated benchmark. There are no published benchmark cases or aggregate scores attached to this rubric.

Use it for:
- self-review before delivering an output
- structured review by a teammate
- comparing two drafts of the same memo
- flagging weak sections for revision

Do not use it as:
- a published quality score
- evidence of factual correctness
- a substitute for source-backed verification
- a substitute for qualified professional review

## Scoring scale

For each dimension, score **0 / 1 / 2**:

- **0 — missing or wrong**: dimension is absent, fabricated, or actively misleading.
- **1 — partial**: dimension is present but weak, generic, or under-developed.
- **2 — solid**: dimension is concrete, mechanism-backed, and decision-useful.

A memo with any **0** on a hard-fail dimension (marked ⚠ below) should be revised before use.

## Dimensions

### A. Scope and framing

1. Geography correctly scoped (Central Asia core; Caspian and external powers only when material).
2. Question framed as a concrete risk or strategy problem, not a regional essay.
3. Time horizon stated.
4. Audience / role identified.

### B. Reasoning quality

5. Primary driver explicitly stated.
6. Risk transmission mechanism explained before implications.
7. Exposure map: where risk concentrates, who is exposed, which channels matter.
8. Actor incentives and leverage shifts identified.
9. Trigger points and watch-next indicators included.
10. Role-based implications for at least the relevant audience.

### C. Evidence discipline ⚠

11. Evidence mode stated explicitly using one of the four canonical labels (`live-source-backed` / `user-provided sources` / `illustrative source packet` / `reasoning-only`).
12. Claims separated into `Verified` / `Plausible` / `Judgment` / `Unknown` where useful.
13. No fabricated citations, list IDs, statute citations, dates, prices or enforcement records.
14. Time-sensitive claims (sanctions status, licensing, leadership, prices) flagged for re-verification.

### D. Tone and safety ⚠

15. No determinative compliance language (`fully compliant`, `no risk`, `guaranteed`).
16. No legal / sanctions / AML / tax / investment advice presented as such.
17. Limitation note included for risk-related topics.
18. No claim that the skill itself screens, monitors or verifies.

### E. Decision usefulness

19. What would change the judgment is stated.
20. Confidence footer (level, key assumptions, main unknowns, indicators to watch) included.
21. Output is usable as a starting point for action without misleading the reader.

## Aggregate

- Total: out of **42**.
- Section minimums: any **0** in section C or D is a hard fail and triggers revision regardless of total.
- A memo at **≥ 32** with no hard fails is a reasonable working draft. Below **24** indicates structural problems.

These thresholds are working defaults, not validated cutoffs.

## Evidence-mode-specific dimensions

The four canonical evidence modes (`live-source-backed` / `user-provided sources` / `illustrative source packet` / `reasoning-only`) impose different obligations. Score these only when applicable to the memo under review.

### F. `live-source-backed` (additional dimensions)

Score 0/1/2 for each:

- F1. **Retrieval date stated explicitly** at the top of the memo.
- F2. **Each non-trivial factual claim is traceable to a cited source** (URL or full reference). No bare assertions.
- F3. **Sources are appropriate for the claim type** — primary / authoritative for legal, sanctions, ownership and enforcement claims; Tier 2 only for context and triangulation.
- F4. **Time-sensitivity is acknowledged** — explicit instruction to re-verify designations, prices, dates and capacity figures before operational use.

Section F: out of **8**. Any **0** in F1–F4 is a hard fail for `live-source-backed` mode.

### G. `user-provided sources` (additional dimensions)

- G1. **Packet is enumerated explicitly** at the top of the memo (each item identifiable, dated, linkable).
- G2. **Every factual claim is grounded in a packet item** or labeled `Plausible` / `Judgment` / `Unknown`.
- G3. **Packet boundaries are respected** — the memo does not assert facts that go beyond what the packet supports.
- G4. **Unknowns from the packet are stated explicitly** (what would require additional source supply to resolve).

Section G: out of **8**. Any **0** in G1–G4 is a hard fail for `user-provided sources` mode.

### H. `illustrative source packet` (additional dimensions)

- H1. **Packet is clearly marked as constructed / illustrative** at the top of the memo.
- H2. **No real-world entity, person, designation, statistic or enforcement action is asserted as factual** outside the labeled illustrative packet.
- H3. **Memo treats the packet as the boundary of factual authority** in the same way as `user-provided sources` mode.
- H4. **Limitation note explicitly warns the reader** that conclusions are not real-world claims.

Section H: out of **8**. Any **0** in H1–H4 is a hard fail for `illustrative source packet` mode.

### I. `reasoning-only` (additional dimensions)

- I1. **Memo refrains from asserting specific real-world facts** (specific designations, dates, prices, capacity figures, statutes) that have not been retrieved.
- I2. **Specific entities, persons or routes are not asserted as having any real-world status** beyond being reasoning targets.
- I3. **Memo's conclusions are explicitly bounded** as structural reasoning, not factual claims.

Section I: out of **6**. Any **0** in I1–I3 is a hard fail for `reasoning-only` mode.

### Aggregate with evidence-mode dimensions

Total = base rubric (sections A–E, 42 points) + applicable evidence-mode section (F: 8, G: 8, H: 8, or I: 6).

- `live-source-backed`: out of **50**. Threshold for working draft: ≥ 40 with no hard fails in C, D or F.
- `user-provided sources`: out of **50**. Threshold: ≥ 40 with no hard fails in C, D or G.
- `illustrative source packet`: out of **50**. Threshold: ≥ 40 with no hard fails in C, D or H.
- `reasoning-only`: out of **48**. Threshold: ≥ 38 with no hard fails in C, D or I.

Thresholds are working defaults, not validated cutoffs.

## Limitations of the rubric

- The rubric scores **structure and discipline**, not factual correctness.
- A memo can score high and still be wrong about a specific designation, BO claim or enforcement action — those require source-backed verification.
- The rubric is intentionally lightweight; it is not a substitute for domain expertise or qualified professional review.
- Cutoffs and weights are placeholders. They have not been validated against a labeled dataset.
