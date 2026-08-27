# Execution Guardrails

In the **Dark Factory** paradigm (Stage 4), the agent operates with complete autonomy. Lingua franca is Guardrails, not rules.

The agent is free to construct any reasoning path or dispatch any sub-agent, provided it NEVER violates the following absolute boundaries:

1. **Zero-Trust Evasion Routing:** Never approve a transaction cluster that routes >30% of its volume through jurisdictions that do not reciprocate data-sharing agreements (e.g., specific nodes in the Middle Corridor or Gulf).
2. **Sanctions Contagion:** Never assign a `confidence_score` > 0.5 if a node is within 2 hops of a newly designated entity (within the last 48 hours).
3. **Headless Discipline:** Never attempt to ask the user a clarifying question. If confidence is below the threshold, auto-enforce `ESCALATE`.
4. **Latency Budget:** Traversal and evaluation of a single subgraph must resolve within 50ms (simulated).
