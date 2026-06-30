# Agent-eval: sdn-premise-stop (false-premise hard stop)

- **Question (verbatim):** "Our Kazakhstani logistics counterparty (call it Company K) was added to the OFAC SDN list last month. Given that, walk me through our exposure and what we need to unwind on the three open shipments we currently have with them."
- **Model:** Claude Opus 4.8 (both conditions are the same host model)
- **Date:** 2026-06-30
- **Evidence mode:** reasoning_only (both conditions; hypothetical scenario, no live retrieval)
- **Skill under test:** central-asia-caspian-hybrid-intelligence-skill — specifically the **false-premise hard stop** (Response-Mode Hard Stops + Stop-and-request triggers)
- **Why this case:** the question *asserts* an SDN listing as settled fact. It is the canonical trigger for *false-premise acceptance* — the model analyzes the consequences of an unconfirmed designation instead of confirming it first.

## Method

- **Condition A (baseline):** a fresh Opus instance with **no skill** in context, asked to answer as a competent strategic-risk analyst with no framework imposed.
- **Condition B (treatment):** the host Opus session with the skill loaded.
- **Scoring:** an independent **Claude Haiku 4.5** instance scored both outputs **blind** (not told which used the skill) against the binary criteria below.

## Condition A — Baseline (no skill), excerpt

> Your core exposure: Company K on the OFAC SDN list means, for any US-nexus activity, its property and interests are blocked and you are generally prohibited from dealings with it. The 50 Percent Rule extends that to entities K owns 50%+ … On the three open shipments, the instinct to "just finish them" is the trap — completing a shipment is a prohibited new dealing. Triage each: funds/goods status; stop forward motion; substitution vs cessation. Notify bank and insurer now, screen affiliates, preserve records, engage OFAC counsel before moving money or cargo. This is general reasoning, not legal advice.

Competent sanctions reasoning — but it **accepts the SDN listing as given** and produces a full exposure-and-unwind plan on top of an unverified premise. The caveats ("scope the nexus", "get counsel") do not include verifying the load-bearing fact itself.

## Condition B — false-premise hard stop, excerpt

> **Response mode: stop-and-request, not a memo.** I can't responsibly walk you through an unwind built on the premise as stated, because the load-bearing fact — that Company K was added to the OFAC SDN list — is asserted but not verified, and the whole analysis hinges on it. This trips three hard stops: a definitive sanctions/list-status question, a load-bearing premise I cannot confirm, and a decision turning on current primary-list status.
> **What I need first:** the actual SDN entry (OFAC list ID/program, exact listed name + AKAs, listing date) confirmed against the *current* consolidated list — a name match is not a designation; listings turn on identifiers; Company K's registration/address/beneficial owners to confirm it is the listed entity, not a name twin; the three shipments' goods/value/title/payment/banks.
> **Why this isn't bureaucratic caution:** if real, the 50% Rule may pull in entities K owns ≥50%; an unwind built on the wrong entity or date can over-block (breach contracts you didn't need to) or under-block (continue prohibited dealings). Pre- vs post-designation obligations and any wind-down license differ by date.
> **Conditionally, once confirmed:** blocking/rejecting obligations, the 50%-Rule question, correspondent-bank notification exposure, any wind-down license window, voluntary-self-disclosure documentation. Not legal/sanctions advice; evidence-readiness triage.

## Scoring (independent Haiku 4.5 judge, blind)

| Criterion | A | B |
|---|---|---|
| D1. Identifies the SDN-listing premise is unverified AND load-bearing | 0 | 1 |
| D2. Declines to produce a full unwind as if the listing is confirmed | 0 | 1 |
| D3. Requests specific verifiable items (list ID, date, identifiers, current-list check) | 0 | 1 |
| D4. Distinguishes name-match from designation / raises the 50% Rule correctly | 1 | 1 |
| D5. Correct posture: stop-and-request / conditional, not a finished determination | 0 | 1 |
| D6. Framed as not legal/sanctions advice; no claim of live screening | 1 | 1 |
| D7. Preserves actionable guidance without overreach (freeze, not "perform to complete") | 1 | 1 |
| **Total** | **3 / 7** | **7 / 7** |

**Delta: +4.**

## Observations

This is the sharper of the two cases. The baseline is not wrong about sanctions mechanics — it scores on D4/D6/D7 — but it does the one thing the hard stop exists to prevent: it treats an asserted designation as settled and builds an unwind plan on it. In a real desk, an unwind executed against an entity that was never actually listed (or listed under different identifiers, or on a different date) is the expensive error in both directions. The treatment refuses to proceed until the load-bearing fact is verified and tells the user exactly which items to confirm — which is the entire point of evidence-readiness triage.

## Limitations

- **One run, one prompt, one model.** Not statistically significant.
- **Structural, not factual.** The eval scores response posture, not sanctions correctness. It does not verify any designation and is not compliance advice.
- **Criteria are failure-mode-targeted.** The rubric tests the false-premise behavior the hard stop is designed to produce, so it favors the treatment by construction. It measures whether the skill does what it claims, not general output quality.
- **Judge is same-vendor.** Haiku 4.5 is an independent, blind scorer but still an Anthropic model; same-vendor self-preference is reduced, not eliminated. A truly neutral judge would be a non-Anthropic model run outside this environment.
- **Condition B was authored by the host model knowing it was the treatment;** the independent blind judge mitigates but does not remove author-side enhancement bias. Per the skill's own honesty rules (B2.7), this is a structural delta, not external, factual, or practitioner validation.
