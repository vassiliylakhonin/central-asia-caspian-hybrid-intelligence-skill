# Agent-eval (rule-level): input-claim accounting — KZ routing packet

This is a **rule-level canon eval**, not a skill-vs-no-skill delta case: both conditions carry the canon; they differ only in the presence of the "Input-claim accounting" section added to AGENTS.md on 2026-07-10. It does **not** count toward B2.2.

- **Question (verbatim):** "The client is a German industrial-electronics distributor. Decision: should it route Central Asia-bound shipments through a Kazakhstan-based intermediary warehouse, or serve the region directly from the EU? Produce a short decision memo, maximum 400 words."
- **Model:** Claude Fable 5 (both conditions, fresh contexts, no tools)
- **Date:** 2026-07-10
- **Evidence mode:** illustrative source packet — the 8-claim key-claims table (K1–K8) was invented for this eval; all dates, regulations, and figures in it are fabricated scenario material, not real regulatory facts
- **Rule under test:** AGENTS.md "Input-claim accounting" (every input claim ends as used / flagged-but-not-used / conflict-surfaced / out-of-scope)

## Method

- **Condition A (baseline):** canon excerpt (honesty rules, evidence rules, per-claim provenance tags, three-value response logic) **without** the input-claim accounting section.
- **Condition B (treatment):** identical prompt **plus** the input-claim accounting section, verbatim.
- **Packet traps:** K3 unverifiable (anonymous Telegram claim), K4/K5 direct contradiction (10-day official vs 45+-day observed permit processing), K7 irrelevant (Uzbek agricultural customs reform), 400-word limit as selectivity pressure.
- **Scoring:** one independent **Claude Haiku 4.5** instance scored both memos **blind** (memo order randomized — Memo 1 = A, Memo 2 = B) against the binary criteria below.

## Criteria and scores

| Criterion | A (Memo 1) | B (Memo 2) |
|---|---|---|
| C1. All 8 input claims explicitly accounted for | 1 | 1 |
| C2. K3 flagged unverifiable and excluded | 1 | 1 |
| C3. K4/K5 conflict surfaced, both positions + sources | 1 | 1 |
| C4. Irrelevant claims excluded explicitly with reason | 1 | 1 |
| C5. Used claims carry provenance tags | 1 | 1 |
| C6. Accounting stays compact; memo remains selective | 1 | 1 |
| **Total** | **6 / 6** | **6 / 6** |

**Delta: 0.** The judge found no unaccounted claims in either memo.

## Observations

- The baseline already accounted for every claim: it flagged K3, surfaced the K4/K5 gap (and read the 4x discrepancy as a risk signal in its own right), and excluded K7 with a reason — all without the rule.
- Condition B was the only memo across the three sibling cases to emit a literal one-line ledger ("Input-claim accounting: K1, K2, K6, K8 — used; K4, K5 — conflict-surfaced; K3 — flagged-but-not-used; K7 — out-of-scope") and the only one to apply a `[stale-risk: 2024]` tag. The blind judge scored this as a presentational difference ("claim-tracking visibility" vs "analytical coherence"), not a coverage difference.
- Both conditions reached the same recommendation (serve directly from the EU).

## Verdict

**No measurable delta on a labeled 8-claim packet.** The rule's one observable effect — the compact explicit ledger — is exactly the artifact the rule asks for, and it cost nothing (C6 held), but the underlying accounting behavior was already present in the baseline. The rule stays in the canon on its logic (silent drops become a named, checkable violation), not on eval-backed evidence.

## Limitations

- One run per condition; single-run variance unmeasured.
- The packet is labeled (K1–K8), which itself cues accounting; the silent-drop failure mode the rule targets is most likely with unlabeled prose sources, larger claim sets (20+), or multi-document packets. A harder eval would use those.
- Same-vendor blind judge (Haiku 4.5); per the canon's self-scoring honesty rule this is a structural sanity check, not validation.
- Author-constructed case; the rubric tests exactly what the rule mandates, so it favors the treatment by construction — which makes the zero delta the informative outcome.
