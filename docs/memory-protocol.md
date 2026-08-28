# Proposed Memory Contract

No long-term memory store is implemented in this repository. The
`retrieve_memory_context` MCP tool returns `status: not_implemented`.

## Protocol

1. Use the populated practice profile when the user has explicitly supplied it.
2. Never claim to remember earlier sessions unless the runtime provides a named,
   inspectable record.
3. Do not persist counterparties, risk appetite, or reviewer decisions without an
   explicit retention policy and user authorization.
4. Treat a missing record as unknown, not as a clean history.

Until a memory store is implemented, the cold-start interview and practice
profile remain the supported context mechanism.
