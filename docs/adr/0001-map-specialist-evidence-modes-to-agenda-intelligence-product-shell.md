# Map Specialist Evidence Modes to the Agenda Intelligence Product Shell

Central Asia + Caspian examples may use specialist-facing evidence labels such as `live-source-backed` because those labels describe how the example was authored and reviewed. When the specialist is routed through Agenda Intelligence MD's `analyze` product shell, those labels must be mapped into the product-shell contract (`reasoning_only`, `user_provided`, or `mixed`) rather than extending the request/memo schema vocabulary. This keeps live retrieval upstream of Agenda Intelligence MD while preserving richer specialist example language in the authoring source.

**Consequences**

- `live-source-backed` remains valid in specialist documentation and examples.
- `live-source-backed` does not become an `analyze` request or memo evidence mode unless Agenda Intelligence MD deliberately changes its product contract.
- Source-backed specialist runs passed through `analyze` should use `user_provided` when the retrieved packet is supplied to the product shell, or `mixed` when supplied evidence is combined with reasoning.
