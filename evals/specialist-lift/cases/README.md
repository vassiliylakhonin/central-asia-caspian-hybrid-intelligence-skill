# Cases

One JSON file per case:

```json
{
  "id": "kebab-case-id",
  "question": "The question, exactly as it goes to the model.",
  "decision_context": "Who is deciding what, on what horizon.",
  "archetype": "Payment-rail exposure",
  "negative_control": false
}
```

`archetype` must match a heading in [`docs/risk-archetypes.md`](../../../docs/risk-archetypes.md).

Set `negative_control` on at least one case: a question inside the region's
geography where regional mechanism should **not** change the substance. Without
it, the measurement cannot distinguish added signal from added words.

No cases are defined yet. Bar 3 is not attempted.
