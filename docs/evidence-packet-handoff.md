# Evidence-packet handoff

This skill produces Central Asia and Caspian regional reasoning. [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) is primarily a deterministic evidence-packet linter for claim-backed AI output.

The handoff seam is a small JSON packet:

1. Produce the specialist memo with an explicit evidence mode.
2. Select externally checkable factual and quantitative claims. Keep scenarios, assumptions, `[inference]`, and `[analyst-judgment]` statements in the memo rather than presenting them as sourced facts.
3. Give every selected claim a stable `claim_id` and declare the `source_ids` it relies on.
4. Copy caller-supplied source text into `sources[]`. A URL, list ID, or citation alone is not source text.
5. Add `quotes[]` only for verbatim spans present in the named source.
6. Run the packet through Agenda Intelligence MD before human review.

If a factual claim has no supplied support, keep it in the packet with an empty `source_ids` array. Do not invent sanctions-list text, registry data, or corridor evidence to make the packet pass.

## Runnable synthetic example

The example is intentionally synthetic and describes no real corridor or operator:

```bash
pip install "agenda-intelligence-md==1.3.0"
agenda-intelligence check examples/evidence-packet-handoff.json --strict
```

Example: [`examples/evidence-packet-handoff.json`](../examples/evidence-packet-handoff.json).

## Interface limits

The linter checks references, declared quotes, lexical support, and unmatched numbers. It reports packet completeness, not factual truth, sanctions status, beneficial ownership, legal sufficiency, or whether the regional judgment is sound. Human review remains required.

Decision record: [`docs/adr/0003-use-evidence-packet-handoff-as-primary-agenda-seam.md`](adr/0003-use-evidence-packet-handoff-as-primary-agenda-seam.md).
