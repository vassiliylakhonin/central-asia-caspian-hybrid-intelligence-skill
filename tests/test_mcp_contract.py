import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("regional_mcp_contract", ROOT / "src" / "mcp_contract.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class McpContractTests(unittest.TestCase):
    def test_unavailable_tool_is_explicitly_not_implemented(self):
        payload = json.loads(
            MODULE.unimplemented_response(
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

    def test_structured_contract_cannot_approve_or_enforce(self):
        schema = json.loads((ROOT / "schemas" / "compliance-decision.schema.json").read_text())
        serialized = json.dumps(schema).lower()
        self.assertNotIn('"approve"', serialized)
        self.assertNotIn('"block"', serialized)
        self.assertNotIn("freeze_funds", serialized)
        self.assertEqual(schema["properties"]["human_review_required"]["const"], True)


if __name__ == "__main__":
    unittest.main()
