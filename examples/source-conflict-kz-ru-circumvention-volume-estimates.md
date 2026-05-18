# Source-conflict surfacing — KZ→RU circumvention volume estimates (illustrative)

> **Illustrative source packet.** Evidence mode: `illustrative source packet`. No live verification was performed in this environment; figures below are representative of the magnitude and direction of disagreement that policy research institutes, EU official channels, and industry advisories regularly publish on Kazakhstan→Russia circumvention volumes for Common High Priority List (CHPL) goods, not a snapshot of any specific reporting period. The purpose of this example is to demonstrate how the skill surfaces a load-bearing source conflict in a sanctions-circumvention estimation problem rather than silently resolving it. Do not use the specific numbers below for any operational decision.

**User question:** Our trade-finance bank's sanctions risk function needs an assumed annual value of CHPL-aligned goods circumventing into Russia via Kazakhstan to calibrate counterparty EDD thresholds and risk-appetite parameters for the KZ counterparty book through H2 2026. Policy research institutes, EU Commission documentation, and industry advisories publish figures that differ by a factor of two or more. How should we treat that disagreement in the EDD-threshold decision?

```text
Question: H2 2026 KZ→RU circumvention volume disagreement across KSE / Bruegel / EU Commission / industry advisories for CHPL goods.
Decision: EDD threshold calibration and risk-appetite parameters for KZ counterparty book at a European trade-finance bank.
Audience: Head of sanctions risk; head of trade finance.
Time horizon: 6 months.
Evidence mode: illustrative source packet.
Confidence: Moderate, conditional on the conflict being surfaced rather than collapsed.
```

EVIDENCE ACCESS LIMITED: no live verification performed in this environment. Representative figures below are illustrative.

## Executive takeaway

**Key judgment `[analyst-judgment]`:** Policy research institutes, EU official documentation, and industry advisories publish materially different KZ→RU CHPL-circumvention volume estimates. The divergence is load-bearing for EDD-threshold calibration: a posture calibrated to either end of the range carries direct regret. Apply **flag-but-don't-use** to the absolute volume figure; calibrate EDD triggers to the upper research-institute range for regret-asymmetry reasons, and preserve the EU official figure as a sensitivity / defense reference rather than as a primary input.

## Source conflict (load-bearing)

Multiple credible sources publish materially different KZ→RU CHPL-circumvention estimates. None is fully independent of the others at the data layer.

| Position | Source | Provenance | Representative figure (annual, USD) | Methodology basis |
|---|---|---|---|---|
| Lower (official) | EU Commission DG TRADE / 14th sanctions package documentation (illustrative) | `[primary][verify]` | ~€0.4–0.7 bn | Customs-flagged shipments; explicit CHPL HS code matches |
| Middle (think-tank) | Bruegel / European policy-research (illustrative) | `[secondary][verify]` | ~€0.8–1.2 bn | Mirror-statistic gap adjusted for legitimate KZ re-export demand baseline |
| Higher (research institute) | KSE Institute / Yermak-McFaul working group (illustrative) | `[secondary][verify]` | ~€1.5–2.0 bn | Mirror-statistic gap treated as primary circumvention proxy; broader HS-code attribution |
| Industry-aligned | Industry advisory aggregations (illustrative) | `[secondary][verify]` | ~€1.2–1.8 bn | Mixed methodology; often anchored to KSE upper range with own counterparty filters |

**Why this is a real conflict, not a measurement-noise problem:**
- The gap between the lowest (EU official) and highest (KSE) estimates exceeds 3× — large enough to shift counterparty EDD-trigger thresholds across decision regimes, not a rounding difference `[inference]`.
- The estimates do not converge over reporting cycles. Persistent gaps reflect *methodology* divergence, not transient measurement variance.
- Each source publicly states *different interpretive choices* — what fraction of the mirror-statistic gap to attribute to circumvention vs. legitimate re-export demand, and which HS codes to include in the CHPL-equivalent basket.

**Source independence assessment (critical for Rule 2):**
- **The three secondary sources are NOT fully independent.** KSE, Bruegel, and industry advisories all draw on UN Comtrade bilateral trade data, KZ Stat Agency reporting, and pre-2022 Russian Federal Customs Service publications (post-2022 partially substituted by mirror-statistic reconstruction). Their methodological differences are in *interpretation and attribution*, not in the underlying data inputs.
- **EU Commission figures draw on member-state customs flagging** — a partially independent input that the research institutes do not have direct access to. But the EU figure is also informed by KSE / Bruegel research in the unclassified policy-input chain `[analyst-judgment]`, so the partial independence runs in both directions.
- **Agreement between any two research-institute estimates does NOT count as independent corroboration**, because they share the upstream data layer.
- **Agreement between an industry advisory and KSE does not strengthen confidence** if the advisory anchored its methodology to KSE's framework — common practice in this estimation space `[inference]`.

**Preferred position for EDD calibration — and why:** The **upper research-institute range (KSE)** is preferred as the calibration anchor for EDD triggers, not because it is more likely correct, but because sanctions-compliance regret is asymmetric: under-detecting circumvention exposure creates direct secondary-sanctions and reputational risk for the bank (irreversible once enforcement lands); over-detecting causes commercial friction and KZ-client churn (reversible, manageable through tiered EDD). The EU official lower figure is preserved as the natural defense reference if the bank's posture is later challenged externally as over-restrictive.

**What is NOT done:** averaging the four estimates into a single point figure. Averaging would silently collapse the methodology disagreement and embed a number none of the sources publishes.

## Facts (where sources agree)

- **Fact `[secondary]`:** Mirror-statistic gap between KZ-reported exports to Russia and Russia-reported imports from KZ (where the latter is available) is present and material; the disagreement is about attribution and magnitude, not about whether the gap exists.
- **Fact `[primary]`:** EU has formalized the CHPL (Common High Priority List) framework through successive sanctions packages; the basket of HS codes that EU regulators treat as priority-targets is itself public.
- **Fact `[secondary]`:** Multiple FATF / EAG / OECD reports document that KZ has been a structural transit hub for goods subject to Russian import-substitution demand post-2022.

## Assessments (linguistic faithfulness)

- **Assessment `[analyst-judgment]` (Moderate confidence):** The structural cause of the disagreement appears to lie in how each source attributes the mirror-statistic gap between (a) deliberate circumvention, (b) legitimate KZ re-export demand growth, and (c) pre-existing measurement asymmetries that have widened post-2022 `[inference]`.
- **Assessment `[analyst-judgment]` (Low–Moderate confidence):** If the EU Commission's official figure rises materially toward the research-institute range over consecutive sanctions packages, the convergence direction is informative — official upward revision would signal classified-channel re-estimation; sustained low official figure with rising research-institute figures would signal a widening interpretation gap.
- **Assessment `[analyst-judgment]` (Moderate confidence):** A bank calibrating EDD to the midpoint of the four sources would likely be the worst of both worlds — over-restrictive against the EU official case and under-prepared against the KSE upper case.

## Scenarios (6 months)

1. **Persistent divergence, no convergence (most likely).** EDD calibration must remain conflict-aware throughout the period; no single number ever becomes "the" circumvention volume. **Indicators:** KSE quarterly updates retain current gap to EU figures; new policy-research publications stay within current ranges.
2. **EU figures revised upward toward research range.** Suggests classified or member-state customs evidence supports higher figures. **Indicators:** next EU sanctions package documentation cites higher KZ-transit figures; new designations targeting KZ-incorporated entities in CHPL-aligned trade.
3. **Research-institute figures revised downward.** Suggests methodology refinement reduced over-attribution. **Indicators:** KSE / Bruegel publish methodology updates; downward revisions in subsequent quarterly reports.
4. **Major EU enforcement action against named KZ-incorporated entities.** Resolves the attribution question for specific flows; does not resolve the aggregate gap. **Indicators:** EU SDN additions naming KZ entities previously research-flagged; secondary-sanctions enforcement of EU banks for CHPL-related KZ exposure.

## Options and trade-offs

| Option | Pros | Cons |
|---|---|---|
| Calibrate EDD to upper research range (KSE) | Asymmetric regret protection; minimizes sanctions-detection failure | Higher operational friction; KZ counterparty churn risk |
| Calibrate to EU official lower range | Lower operational friction; defensible against over-restriction challenge | Sanctions-detection gap risk if research institutes are closer to true volume |
| Calibrate to midpoint of all four | Simplest implementation | Silently resolves the conflict; worst-of-both regret profile |
| Maintain dual calibration (trigger on upper, defense reference on lower) | Preserves both for different purposes | Operational complexity; requires explicit policy documentation of when each applies |

## Decision-relevant takeaway

The disagreement between EU official figures and policy-research institute estimates of KZ→RU circumvention volume is not a measurement problem that will close — it is a structural methodology divergence over interpretation of overlapping data inputs. Surface this in the bank's sanctions-policy documentation explicitly. Anchor EDD triggers to the upper research-institute range on regret-asymmetry grounds. Preserve the EU official figure as a sensitivity / defense reference, not a primary input. Re-evaluate quarterly as estimates narrow, widen, or persist.

## Watch-next indicators

- Publication cycles of KSE Institute, Bruegel, and EU Commission DG TRADE; whether the gap narrows or widens.
- EU SDN additions naming KZ-incorporated entities previously research-flagged but not officially designated (would shift independence assessment toward research institutes).
- Methodology disclosure changes from any research institute; HS-code basket changes; baseline-demand correction changes.
- EU sanctions package documentation citing higher KZ-transit figures (would itself reset the conflict toward convergence).
- New entrants with genuinely independent inputs — e.g. customs-side analysis from a non-EU jurisdiction with bilateral data access — would change the independence assessment.

## Confidence and key unknowns

- **Confidence: Moderate**, conditional on the methodology above — surfacing the conflict rather than collapsing it. If the bank silently picked any single number as "the" KZ→RU circumvention figure for EDD calibration, confidence in the resulting policy would be Low regardless of which source eventually proved closest to truth.
- **Key unknowns `[verify]`:** the true circumvention volume — by definition not directly observable; how member-state customs flagging compares to research-institute mirror-statistic attribution at the HS-code level; whether EU Commission figures incorporate research-institute inputs in their public documentation (partial dependence vs full independence).

## What would change the judgment

- A genuinely independent estimate from a non-Comtrade, non-mirror-statistic methodology (e.g., end-buyer-side customs data from a non-EU jurisdiction with KZ trade-data access) aligning with one source cluster and not the other.
- Convergence of EU official and research-institute figures within 2 sanctions-package cycles — convergence direction would itself be load-bearing.
- A regulatory ruling requiring EU banks to use a specific source for sanctions modeling — would shift the question from "which is right" to "which is required."

## Why this example exists

This memo demonstrates the **source-conflict-surfacing rule** from `AGENTS.md` applied to a sanctions-circumvention estimation problem in the CA-Caspian regional context:

- Four credible sources on a load-bearing fact (KZ→RU CHPL-circumvention volume) are NOT silently averaged.
- All four positions are named, tagged, and shown with their methodology basis.
- Source independence is explicitly assessed — research institutes share Comtrade / KZ Stat / pre-2022 Russian customs data; EU Commission is only partially independent through member-state customs flagging; industry advisories often anchor to research-institute frameworks.
- A preferred position is stated **with the reason** (regret asymmetry for compliance), not as "we picked KSE because KSE."
- The conflict is carried through to the decision (dual-calibration option) instead of being collapsed at the takeaway.
- Linguistic faithfulness is observed: `[analyst-judgment]` and `[inference]` tags throughout; hedges ("appears to", "would likely", "the upper of") on judgment claims; plain framing reserved for the `[primary]` / `[secondary]` factual layer.

This complements the GREY case in [`live-source-backed-circumvention-and-corridor.md`](live-source-backed-circumvention-and-corridor.md) — where two EBRD investment figures (€3.5 bn immediate vs €18.5 bn 2022–2027 roadmap) are correctly flagged as "different framings, not conflicting" — by showing the contrasting case where the disagreement is a genuine load-bearing conflict requiring active surfacing and a preferred-position decision, not a framing-difference reconciliation.

## Limitation note

Illustrative. Figures are representative, not retrieved. Not sanctions, compliance, legal, AML, trade-finance, or investment advice. A real KZ→RU circumvention-volume EDD calibration requires current KSE Institute / Bruegel / EU Commission publications, qualified sanctions counsel, and integration with the bank's specific KZ counterparty book and HS-code exposure profile.
