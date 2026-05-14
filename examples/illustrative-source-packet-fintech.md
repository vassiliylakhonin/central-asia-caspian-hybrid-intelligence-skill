# Worked example — `illustrative source packet` mode

> **Evidence mode: `illustrative source packet`.** This memo is grounded in a **constructed, illustrative** source packet defined in this file. The packet is **not real data**. No company, person, designation, statistic, dwell-time, freight rate or enforcement action below corresponds to a real-world entity or event. The purpose is to demonstrate how a memo should ground its claims in a supplied source packet and use evidence labels honestly.
>
> For real operational use, replace the packet with `user-provided sources` (a real packet you supply) or `live-source-backed` retrieval, and treat any conclusions accordingly.

## The illustrative source packet

This is the only material the memo is allowed to treat as factual within this exercise. Every factual claim in the memo must be traceable to one of these items, or labeled `Judgment` / `Plausible` / `Unknown`.

- **[S1]** *Illustrative regulator notice (constructed):* "Country A's central bank issued an updated guidance on enhanced due diligence for cross-border SME flows involving HS-code clusters X, Y, Z, effective Q+0."
- **[S2]** *Illustrative customs anomaly (constructed):* "Country A's reported imports of HS cluster X rose 4× year-on-year while corresponding origin-country exports rose 1.2×, producing a mirror-data divergence."
- **[S3]** *Illustrative correspondent communication (constructed):* "Tier-1 correspondent T notified respondent banks that EDD documentation requirements for trade-finance instruments referencing HS clusters X, Y, Z would tighten effective Q+1."
- **[S4]** *Illustrative port throughput (constructed):* "Caspian east-coast port P reported dwell time rising from baseline B to baseline B + 60% over the prior two quarters."
- **[S5]** *Illustrative case (constructed):* "Trading group G operates 11 LLPs across Country A, B and an offshore vehicle, with three shared addresses and four directors holding seats on multiple entities. No designation has been recorded."

That is the full packet. No other facts may be asserted as true. All five items are constructed for demonstration.

## User question

> "Given the source packet above, what is the near-term sanctions / AML / banking / routing risk for an SME-focused fintech operating in Country A, and what should they do?"

## Bottom line

The packet shows three independent stress signals (regulatory tightening, customs anomaly, correspondent EDD tightening) clustering around the same HS-code clusters [S1, S2, S3], plus a corridor-throughput signal [S4] and an unresolved BO opacity case [S5]. For an SME-focused fintech in Country A, the dominant near-term risk is **trade-finance and corridor flow exposure to HS clusters X, Y, Z, transmitted via correspondent EDD and regulatory enforcement**. `Judgment` based on convergence of [S1], [S2], [S3].

## Primary risk driver

`Primary driver is:` convergence of regulator action [S1], customs-data anomaly [S2] and correspondent EDD tightening [S3] on the same HS-code clusters, indicating coordinated near-term scrutiny.

## Risk transmission mechanism

1. Regulator [S1] raises EDD obligations for cross-border SME flows in HS clusters X, Y, Z.
2. Customs anomaly [S2] suggests possible re-export / circumvention pressure on the same clusters; this raises the prior that flows in those clusters require documentary scrutiny.
3. Correspondent EDD [S3] tightens at the same time, which means rejection / delay risk on trade-finance instruments referencing those clusters propagates regardless of local regulatory grace periods.
4. Corridor signal [S4]: rising dwell time at port P is `Plausible` as compounding exposure for any flow routed through that node, but the packet does not link [S4] directly to HS clusters X, Y, Z. Treat as `Plausible` overlay, not `Verified` causation.
5. BO opacity case [S5]: the structure described is a known archetypal pattern for adjacency risk, but the packet records no designation. Treat onboarding of similar structures as elevated EDD, not as restricted; `Judgment`.

## Exposure map

- **HS clusters X, Y, Z** (per packet): primary documentary and screening exposure — `Verified` from [S1, S2, S3].
- **Correspondent rails** for trade-finance instruments referencing those clusters — `Verified` from [S3].
- **Port P** dwell-time stress — `Verified` from [S4]; routing-impact on the fintech depends on whether its flows transit P, which is `Unknown` from the packet.
- **Counterparties** structurally similar to group G — `Plausible` higher BO scrutiny by analogy from [S5]; not a designation claim.

## Sanctions / AML / banking / routing considerations

- **Sanctions**: no designation recorded in the packet for any party. `Unknown`. Real operational use requires direct screening against current official lists.
- **AML / EDD**: documentary requirements are tightening per [S1] and [S3]. The fintech should presume that any flow in the named clusters requires documentary defense (BO, end-use, route rationale).
- **Banking**: trade-finance instruments referencing those clusters carry rejection / delay risk per [S3].
- **Routing**: corridor stress [S4] is real; relevance to any specific flow depends on routing data not in the packet.

## Leverage shifts

- **Gains leverage**: tier-1 correspondent T (selectivity), Country A regulator (deterrence), institutions with mature EDD on the named clusters.
- **Loses leverage**: SME importers in those clusters, fintechs without HS-code-aware monitoring, counterparties resembling group G's structure during onboarding.

## Trigger points (watch-next)

- Updates extending or narrowing the HS clusters in [S1].
- Persistent or widening customs divergence beyond [S2]'s 4× / 1.2× pattern.
- Public enforcement action that ties [S2]-style anomalies to designations.
- Correspondent T's published EDD criteria becoming more specific [S3].
- Dwell-time at port P returning to baseline B or worsening beyond [S4].
- Any designation referencing structures similar to group G [S5].

All triggers are framed against the supplied packet. Real monitoring requires live retrieval against authoritative sources.

## Role-based actions

- **Fintech (compliance)**: build HS-cluster-aware monitoring on X, Y, Z; tighten EDD documentation packets to anticipate correspondent T's review; segment merchant book by cluster exposure.
- **Fintech (commercial)**: stress-test rejection / delay risk on trade-finance instruments referencing the named clusters; price for documentation overhead; consider corridor diversification if port P routing is material.
- **Fintech (onboarding)**: treat structures resembling group G's pattern [S5] as elevated EDD by default; do not treat them as restricted absent designation.
- **Bank (correspondent)**: align respondent EDD expectations with [S1] / [S3] to avoid blanket de-risking.
- **Investor**: stress correspondent concentration on T and HS-cluster concentration in revenue.

All actions are illustrative against an illustrative packet.

## Unknowns (not in the packet)

- Whether the fintech's actual flows include HS clusters X, Y, Z (and at what share of volume).
- Whether port P is on the fintech's actual routes.
- The precise text of regulator notice [S1] and correspondent T's criteria [S3].
- Designation status of any counterparty.
- Internal data quality at the fintech.

## Confidence

`Confidence`: medium for the structural claim (three stress signals converging on the same HS clusters); low for any conclusion about the fintech's own positioning, since the packet does not include the fintech's flow composition.

## What would change the judgment

- Packet expansion showing the fintech's flow composition by HS code and route.
- New packet items recording designations or enforcement actions on the named clusters.
- Reversal of [S1] / [S3] (regulatory or correspondent loosening).
- Sustained recovery of [S2]'s mirror divergence and [S4]'s dwell time.

## Limitation note

This memo is bounded by an illustrative source packet that is **not real data**. It is not legal, sanctions, AML, compliance, banking, customs or investment advice. It does not screen any counterparty against any list. It does not verify any factual claim. The pattern shown — grounding claims in a labeled packet, marking each claim with `Verified` against a packet item or `Plausible` / `Judgment` / `Unknown` — is the part to reuse with real `user-provided sources` or `live-source-backed` retrieval.

`Author: Vassiliy Lakhonin`
