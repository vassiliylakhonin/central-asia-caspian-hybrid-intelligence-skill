# User-provided-sources example — Middle Corridor capacity for an EU shipper

> **Evidence mode: `user-provided sources`.**
>
> **Retrieval date of the user-supplied packet: 2026-05-08.** The packet below was supplied to the skill by the user (illustrated here using real public sources the user retrieved). Within this memo, **only items in the packet may be treated as factual**. Everything else is `Judgment` / `Plausible` / `Unknown`.
>
> This memo is illustrative analysis and not legal, sanctions, AML, compliance, tax, audit, investment, customs, energy or insurance advice. It does not screen any counterparty. It does not verify any factual claim beyond what the packet itself supports. Any operational decision requires source-backed re-verification at the time of decision and qualified professional review.

## How this evidence mode works

In `user-provided sources` mode the user is the source of authority. The user hands the skill a packet — links, PDFs, internal documents, regulator notices — and tells the skill: *"these are the only facts you may treat as established for this question."* The skill grounds every factual claim in a packet item and uses `Verified` (against the packet) / `Plausible` / `Judgment` / `Unknown` for the rest.

This is different from `live-source-backed` (skill / tooling does retrieval) and from `illustrative source packet` (the packet is constructed for demonstration). In `user-provided sources` the packet is real, but its scope and freshness are bounded by what the user actually supplied.

## The user-supplied packet

The user supplied four public sources, time-stamped at retrieval:

- **[U1]** Astana Times (28 November 2023), *World Bank Estimates Tripling Trade Volumes on Middle Corridor by 2030* — World Bank projection of ≈3× freight volumes (≈11 million tonnes by 2030); ≈37% rise in intra-region trade and ≈28% rise in trade with the EU; named bottleneck at Aktau (equipment for windy days); fragmentation across "three railways, three ports and customer services" with non-integrated information systems causing border-crossing delays. https://astanatimes.com/2023/11/world-bank-estimates-tripling-trade-volumes-on-middle-corridor-by-2030/
- **[U2]** Astana Times (25 April 2024), *World Bank Identifies 10 Steps to Address Middle Corridor Bottlenecks* — 10 priority steps including Almaty railway bypass, KZ–UZ rail connection, Aktau port equipment and berth capacity, Georgia rolling stock, Akhalkalaki–Türkiye border rail, Akhalkalaki rail station, Poti port maritime handling, Sivas–Kars–Georgia border rail modernization, Bosphorus rail link via Istanbul's Third Bridge, Romania/Bulgaria onward connectivity and digitalized customs/border management. https://astanatimes.com/2024/04/world-bank-identifies-10-steps-to-address-middle-corridor-bottlenecks/
- **[U3]** Caliber.az (6 November 2024), *EBRD: €18.5 billion investment needed to boost Middle Corridor infrastructure* — EBRD modernization roadmap 2022–2027 with €18.5 bn investment need; container targets at Aktau and Alat (300,000+, longer-term 600,000); BTK target of up to 5 million tonnes; Alat International Trade Port expansion to 25 million tonnes; reported 65% volume increase in 2023 (≈3 million tonnes), projected 4.2 million tonnes by end of 2024. https://caliber.az/en/post/ebrd-18-5-billion-investment-needed-to-boost-middle-corridor-infrastructure
- **[U4]** Asia House (20 July 2025), *The Middle Corridor: The future of Central Asian growth and cooperation* — 2025 container traffic of 76,900 TEUs (≈36% growth over 2024); Middle Corridor annual capacity ≈6 million tonnes in 2024 vs Northern Corridor's >100 million tonnes per year; Caspian Sea level pressure on port operations and ferry capacity failing to keep up with booking requests. https://www.asiahouse.org/2025/07/20/the-middle-corridor-the-future-of-central-asian-growth-and-cooperation/

The packet is the boundary of factual authority for this memo.

## User question

> "We are an EU-based shipper moving containers from Chinese east-coast ports to EU destinations. Our procurement is asking how realistic it is to plan capacity on the Middle Corridor over the next 18–24 months, and what to watch. Use only the packet I supplied."

## Bottom line

Within the supplied packet, the picture is consistent: **demand and policy momentum on the Middle Corridor are real but capacity is structurally lumpy and well below the Northern alternative**. Container TEU growth has been strong year-on-year (36% in 2025 [U4]), but absolute capacity (≈6 million tonnes in 2024 [U4]) is small versus the Northern Corridor's 100+ million tonnes and versus the World Bank's 11-million-tonne 2030 trajectory [U1]. The headline 2030 trajectory is *conditional on a coordinated investment package* (10 World Bank steps [U2]; EBRD €18.5 bn 2022–2027 [U3]); without delivery against that package, capacity remains binding at named nodes. `Judgment` against [U1, U2, U3, U4].

For 18–24-month planning: assume *continued growth on a small base*, expect *binding-node fragility* at Aktau, ferry leg, BTK and onward EU connections, and treat the Middle Corridor as a complement to, not a replacement for, the Northern alternative.

## Primary risk driver

`Primary driver is:` capacity concentration at named nodes (Aktau equipment and berth capacity, Caspian ferry, BTK, EU-side onward links) where the binding constraints are documented and investment delivery is uneven. From [U1, U2, U3, U4].

## Risk transmission mechanism

1. The Middle Corridor's headline growth trajectory (~3× freight volumes, ~halved travel time by 2030, 11 million tonnes target [U1]) is *conditional* on the World Bank's 10 priority steps [U2] and a multi-year EBRD-backed investment program totaling €18.5 bn over 2022–2027 [U3].
2. Several of those steps are at *physical chokepoints* — Aktau port equipment for wind days [U1, U2], Aktau and Alat container capacity [U3], BTK throughput [U3], Akhalkalaki–Türkiye and onward EU rail [U2]. A delay or under-delivery at any one of these caps the achievable share of the headline trajectory.
3. Container traffic is growing fast in percentage terms (76,900 TEUs in 2025; +36% over 2024 [U4]), but the absolute base is small and the ceiling is the slowest-binding node, not the demand curve.
4. The Caspian sea-leg has its own physical pressure: dropping sea level and ferry capacity not keeping up with booking requests [U4]. This is independent of pure investment-rate progress and adds tail risk to ferry-dependent flows.
5. Fragmentation across "three railways, three ports and customer services" with non-integrated information systems at borders [U1] means capacity additions need to be paired with coordination, not just CapEx, to translate into reliable transit times.

## Exposure map

| Channel | What's exposed | Packet item(s) |
|---|---|---|
| Aktau port operations under wind conditions | Operational downtime; dwell-time risk | [U1, U2] |
| Aktau / Alat container terminal capacity | Throughput ceiling vs growing demand | [U3] |
| BTK rail throughput | Onward-leg ceiling at ~5 million tonnes target | [U3] |
| Akhalkalaki–Türkiye border rail | Cross-border bottleneck on EU-bound flows | [U2] |
| EU-side onward connections (Romania/Bulgaria) | Last-leg constraints | [U2] |
| Caspian ferry capacity vs booking demand | Slot availability and schedule reliability | [U4] |
| Customs / information-system fragmentation | Border-crossing delays | [U1] |
| Comparative scale vs Northern Corridor | Substitutability ceiling at portfolio level | [U4] |

## Trigger points (watch-next)

- Implementation milestones on each of the 10 World Bank steps [U2] and the EBRD modernization roadmap [U3].
- Aktau port equipment additions and reported wind-day downtime trends [U1, U2].
- BTK throughput updates against the ~5 million-tonne target [U3].
- Caspian ferry capacity (additions, retirements) and booking-vs-capacity reporting [U4].
- Container TEU growth trajectory beyond the 2025 reading of 76,900 TEUs [U4].
- Northern-corridor capacity re-pricing that materially shifts demand onto the Middle Corridor [U4].

The packet does not include data on insurance / freight-rate trends or on specific shipping-line allocations; treat those as **`Unknown` from the packet** and source separately if needed.

## Role-based actions

- **EU shipper / 3PL (procurement)**: plan Middle-Corridor capacity at the *node-binding* level, not the headline-trajectory level; pre-book ferry slots aware of [U4]'s capacity-vs-bookings imbalance; reflect [U1]'s wind-day risk in transit-time SLAs; treat [U2]'s 10 steps as the implementation watchlist. *Subject to commercial review.*
- **EU shipper (commercial)**: keep the Middle Corridor as a complement to the Northern alternative, not a replacement, given [U4]'s scale comparison.
- **Operator / port / rail**: communicate node-level metrics (dwell time, wind-day downtime, throughput) transparently; align CapEx with the [U2] / [U3] sequence to avoid stranded investment.
- **Investor / financier**: stress-test single-node revenue concentration at constrained nodes; price tenor against the 2022–2027 EBRD horizon [U3].
- **Regulator / IFI**: prioritize the coordination dimension flagged in [U1] (information systems and border integration), not only physical CapEx.

All actions are illustrative against the user-supplied packet. Real implementation requires verification beyond the packet and qualified commercial / operational counsel.

## Unknowns from the packet

- Insurance and freight-rate trends; shipping-line allocation patterns; specific contract economics for major shippers.
- Sanctions / export-controls overlay (the packet is logistics-focused; compliance overlay is not in scope here).
- Up-to-date metrics for any node beyond the figures in [U1–U4] at the cited dates.
- Energy-price effects on bunker fuel and locomotive operations.

## Confidence

`Confidence`: medium for the structural claim that capacity is node-bound and that the 2030 trajectory is conditional on coordinated investment delivery; lower confidence on any 18–24-month *quantitative* claim, since the packet's freshest data point is mid-2025 and operational metrics move.

## What would change the judgment

- Visible delivery on a majority of the 10 World Bank steps [U2] within the 2022–2027 horizon [U3], particularly at Aktau and BTK.
- Material Caspian ferry-tonnage additions that close the booking-vs-capacity gap flagged in [U4].
- A durable shift in Northern-corridor pricing that re-rates Middle-Corridor demand at a scale closer to the 11-million-tonne 2030 target [U1].
- Sustained customs / information-system harmonization that meaningfully reduces the fragmentation flagged in [U1].

## Limitation note

This memo is bounded by the user-supplied packet [U1–U4]. It is not a comprehensive Middle Corridor assessment. It is not legal, sanctions, AML, compliance, customs, commercial or insurance advice. It does not verify any factual claim beyond what the packet itself supports. The packet is time-sensitive: re-verify capacity, throughput and policy figures before any operational or contractual decision.

`Author: Vassiliy Lakhonin`
