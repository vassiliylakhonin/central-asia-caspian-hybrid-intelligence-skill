"""Invariant tests for the MCP transport skeleton.

These import the package the way a consumer does — through its installed name —
rather than by file path. That is deliberate: a test that loads a module through
``importlib.util.spec_from_file_location`` proves the module's logic and proves
nothing about whether the shipped artifact can reach it. C1 and C2 in STATUS.md
exist because that gap hid a server that could not start.
"""

import json
import unittest
from pathlib import Path

from central_asia_caspian_compliance_server import unimplemented_response

ROOT = Path(__file__).resolve().parents[1]


class PackagingInvariantTests(unittest.TestCase):
    """C1 and C2: the shipped artifact imports and runs."""

    def test_server_module_imports_from_the_installed_package(self):
        # Covers both halves of the defect this test was written for: the
        # `mcp` import path the server depends on, and the intra-package
        # import that only resolved when the working directory was `src/`.
        from central_asia_caspian_compliance_server import server

        self.assertTrue(callable(server.main))
        self.assertEqual(server.mcp.name, "central-asia-caspian-compliance-server")

    def test_declared_tools_are_registered_on_the_server(self):
        import anyio

        from central_asia_caspian_compliance_server import server

        tools = {tool.name for tool in anyio.run(server.mcp.list_tools)}
        self.assertEqual(
            tools,
            {
                "query_regional_sanctions",
                "analyze_graph_relationships",
                "retrieve_memory_context",
            },
        )


class McpContractTests(unittest.TestCase):
    """C3: no tool can return, or even express, a fabricated finding."""

    def test_unavailable_tool_is_explicitly_not_implemented(self):
        payload = json.loads(
            unimplemented_response(
                "query_regional_sanctions",
                "a current official list source",
                entity="Example LLC",
            )
        )
        self.assertEqual(payload["status"], "not_implemented")
        self.assertTrue(payload["result_is_not_a_finding"])
        self.assertTrue(payload["human_review_required"])
        self.assertEqual(payload["entity"], "Example LLC")
        self.assertNotIn("clear", json.dumps(payload).lower())
        self.assertNotIn("approved", json.dumps(payload).lower())

    def test_every_declared_tool_refuses_rather_than_answering(self):
        import anyio

        from central_asia_caspian_compliance_server import server

        for name, arguments in (
            ("query_regional_sanctions", {"entity_name": "Example LLC"}),
            ("analyze_graph_relationships", {"node_id": "example-node"}),
            ("retrieve_memory_context", {"client_id": "example-client"}),
        ):
            with self.subTest(tool=name):
                result = anyio.run(lambda: server.mcp.call_tool(name, arguments))
                payload = json.loads(result.content[0].text)
                self.assertEqual(payload["status"], "not_implemented")
                self.assertTrue(payload["result_is_not_a_finding"])
                self.assertTrue(payload["human_review_required"])

    def test_structured_contract_cannot_approve_or_enforce(self):
        schema = json.loads((ROOT / "schemas" / "compliance-decision.schema.json").read_text())
        serialized = json.dumps(schema).lower()
        self.assertNotIn('"approve"', serialized)
        self.assertNotIn('"block"', serialized)
        self.assertNotIn("freeze_funds", serialized)
        self.assertEqual(schema["properties"]["human_review_required"]["const"], True)


if __name__ == "__main__":
    unittest.main()
