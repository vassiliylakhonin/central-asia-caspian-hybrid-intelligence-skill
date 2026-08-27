# Agentic Memory Protocol

This skill relies on Long-Term Memory (LTM) to maintain continuous context. 

## Protocol

1. **Initialization:** On every invocation, query the `retrieve_memory_context` tool to load the user's risk appetite, institutional context, and historical verdicts.
2. **Persistence:** Do not ask the user for context they have already provided in past sessions.
3. **Updating:** When rendering an `ESCALATE` or `BLOCK` decision, seamlessly update the memory store so future sessions apply the same scrutiny to similar counterparties.

*This protocol deprecates the static `cold-start-interview` in favor of dynamic context windows.*
