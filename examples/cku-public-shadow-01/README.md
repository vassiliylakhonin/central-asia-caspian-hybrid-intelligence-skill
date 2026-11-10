# Shadow case: CKU railway bankability screen (`cku-public-shadow-01`)

A public-source shadow case run with the corridor-bankability-analyst toolkit (a separate, private repo in the same portfolio) under its public shadow test contract v1.0, published here as a worked example of claim-ledgered corridor analysis on a live Central Asian corridor project: the China–Kyrgyzstan–Uzbekistan (CKU) railway JV financing.

## What this is and is not

- The deliverable is a **DRAFT** bankability screen with all 30 `[verify]` markers intact. Every figure marked `[verify]` must be confirmed before reliance.
- Harness classification: `evidenceClass: INTERNAL_TECHNICAL_ONLY`, `marketEvidence: NONE`. This is rehearsal evidence; it is not market validation and does not establish analytical quality.
- The review was an `INTERNAL_AGENT` self-review under the shadow-test contract — rehearsal review, not human or external review.
- Protocol: `PROSPECTIVE_BLIND`; 9 public model sources frozen 2026-11-10; 3 public holdouts sealed until the draft hash was fixed, then revealed and audited. `integrityVerified: true`; `holdoutChangedConclusion: false`.
- All sources are public; no party was contacted; nothing here has been verified with the JV, the lenders, or any government.
- The shadow-test contract itself (`docs/public-shadow-test.md`) lives in the private toolkit repo and is not published here; `cku-shadow-report.json` is its machine-readable output for this case.

## Audit metrics (from `cku-shadow-report.json`)

- 28 material claims audited: 20 supported, 0 fabricated, 8 unsupported-or-conflicting — all 8 carried in the draft itself as explicit gaps, not smoothed over.
- 0 calculation mismatches (M-001 to M-004 recomputed); 3 material corrections made in drafting; decision-usefulness score 78.
- Holdouts did not change the conclusion: the financing structure and the demand-risk blocker stand.

## Files

- [cku-railway-bankability-screen.md](cku-railway-bankability-screen.md) — the draft bankability screen (source of the DOCX export)
- [cku-railway-bankability-screen.docx](cku-railway-bankability-screen.docx) — exported document
- [cku-claim-ledger.md](cku-claim-ledger.md) — 28-claim ledger with facility reconciliation, calculation ledger and open-evidence register
- [cku-shadow-review-notes.md](cku-shadow-review-notes.md) — internal-agent review notes, including holdout findings
- [cku-shadow-report.json](cku-shadow-report.json) — machine-readable harness report (schema v1.0, status REVIEWED)

Case date: 2026-11-10.
