"""Tests for the field due-diligence checklist tool.

The checklist's contract: it returns a fixed template of requests for local
counsel, every item marked verify_with_local_counsel, and never a finding
about a counterparty.
"""

import json
import unittest

from central_asia_caspian_compliance_server.dd_checklist import (
    draft_field_dd_checklist_json,
)


class FieldDdChecklistTests(unittest.TestCase):
    def test_returns_checklist_template(self):
        payload = json.loads(draft_field_dd_checklist_json("Kazakhstan"))
        self.assertEqual(payload["status"], "checklist")
        self.assertEqual(payload["country"], "Kazakhstan")
        self.assertEqual(payload["counterparty_type"], "company")
        self.assertTrue(payload["result_is_not_a_finding"])
        self.assertTrue(payload["human_review_required"])
        self.assertGreaterEqual(len(payload["items"]), 10)

    def test_every_item_is_marked_for_local_counsel(self):
        payload = json.loads(draft_field_dd_checklist_json("Azerbaijan"))
        for item in payload["items"]:
            self.assertTrue(item["verify_with_local_counsel"], item)
        self.assertIn("local counsel", payload["note"])

    def test_no_verdict_or_screening_language(self):
        payload = json.loads(draft_field_dd_checklist_json("Uzbekistan"))
        serialized = json.dumps(payload).lower()
        for word in ("clear", "approved", "compliant", "risk score"):
            self.assertNotIn(word, serialized)

    def test_blank_country_is_rejected_without_default(self):
        payload = json.loads(draft_field_dd_checklist_json("   "))
        self.assertEqual(payload["status"], "invalid_input")
        self.assertTrue(payload["result_is_not_a_finding"])

    def test_output_is_deterministic(self):
        self.assertEqual(
            draft_field_dd_checklist_json("Kazakhstan"),
            draft_field_dd_checklist_json("Kazakhstan"),
        )


if __name__ == "__main__":
    unittest.main()
