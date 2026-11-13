"""Tests for the trade-packet consistency audit.

The audit's contract: it compares caller-supplied fields, flags disagreement
without calling it fraud, never substitutes defaults, and reads no external
data.
"""

import json
import unittest

from central_asia_caspian_compliance_server.trade_packet import audit_trade_packet_json


def packet(**overrides):
    base = {
        "documents": [
            {"type": "contract", "hs_codes": ["8607.19", "7326.90"], "date": "2026-01-10"},
            {"type": "invoice", "hs_codes": ["860719", "732690"], "date": "2026-01-20"},
            {"type": "bill_of_lading", "hs_codes": ["860719", "732690"], "date": "2026-02-01"},
            {"type": "certificate_of_origin", "date": "2026-01-25"},
        ],
        "incoterm": "FOB",
        "freight_paid_by": "buyer",
        "insurance_paid_by": "buyer",
    }
    base.update(overrides)
    return base


def results(payload):
    return {c["check"]: c["result"] for c in payload["checks"]}


class TradePacketTests(unittest.TestCase):
    def test_consistent_packet_flags_nothing(self):
        payload = json.loads(audit_trade_packet_json(packet()))
        self.assertEqual(payload["status"], "audit")
        self.assertEqual(payload["flags"], [])
        self.assertEqual(
            results(payload),
            {
                "hs_code_format": "consistent",
                "hs_code_consistency": "consistent",
                "hs_heading_subdivision": "consistent",
                "date_ordering": "consistent",
                "incoterms_allocation": "consistent",
            },
        )

    def test_hs_code_missing_from_one_document_is_flagged(self):
        p = packet()
        p["documents"][1]["hs_codes"] = ["860719"]
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["hs_code_consistency"], "inconsistent")
        self.assertTrue(any("732690" in f for f in payload["flags"]))

    def test_heading_split_across_subdivisions_is_flagged(self):
        p = packet()
        p["documents"][2]["hs_codes"] = ["8607191000", "732690"]
        p["documents"][1]["hs_codes"] = ["8607199000", "732690"]
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["hs_heading_subdivision"], "inconsistent")

    def test_malformed_hs_code_is_flagged_as_format_only(self):
        p = packet()
        p["documents"][0]["hs_codes"] = ["123"]
        p["documents"][1]["hs_codes"] = ["123"]
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["hs_code_format"], "inconsistent")
        self.assertIn("not checked", payload["checks"][0]["detail"])

    def test_inverted_dates_are_flagged(self):
        p = packet()
        p["documents"][3]["date"] = "2026-02-05"  # origin cert after shipment
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["date_ordering"], "inconsistent")
        self.assertTrue(any("certificate_of_origin" in f for f in payload["flags"]))

    def test_incoterms_payer_mismatch_is_flagged(self):
        p = packet(freight_paid_by="seller")  # FOB allocates freight to buyer
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["incoterms_allocation"], "inconsistent")

    def test_cif_requires_seller_insurance(self):
        p = packet(incoterm="cif", freight_paid_by="seller", insurance_paid_by="buyer")
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["incoterms_allocation"], "inconsistent")

    def test_unknown_incoterm_is_not_checked_not_an_error(self):
        payload = json.loads(audit_trade_packet_json(packet(incoterm="XXX")))
        self.assertEqual(payload["status"], "audit")
        self.assertEqual(results(payload)["incoterms_allocation"], "not_checked")

    def test_missing_optional_fields_degrade_to_not_checked(self):
        payload = json.loads(
            audit_trade_packet_json(
                {
                    "documents": [
                        {"type": "contract"},
                        {"type": "invoice"},
                    ]
                }
            )
        )
        self.assertEqual(payload["status"], "audit")
        self.assertEqual(results(payload)["hs_code_consistency"], "not_checked")
        self.assertEqual(results(payload)["incoterms_allocation"], "not_checked")

    def test_single_document_is_rejected(self):
        payload = json.loads(audit_trade_packet_json({"documents": [{"type": "invoice"}]}))
        self.assertEqual(payload["status"], "invalid_input")

    def test_bad_date_format_is_rejected(self):
        p = packet()
        p["documents"][0]["date"] = "10.01.2026"
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(payload["status"], "invalid_input")

    def test_no_fraud_or_clearance_language(self):
        payload = json.loads(audit_trade_packet_json(packet()))
        serialized = json.dumps(payload).lower()
        import re

        for word in ("fraud", "clear", "approved", "genuine", "forgery"):
            self.assertIsNone(re.search(rf"\b{word}\b", serialized), word)
        self.assertTrue(payload["result_is_not_a_finding"])
        self.assertTrue(payload["human_review_required"])

    def test_output_is_deterministic(self):
        self.assertEqual(audit_trade_packet_json(packet()), audit_trade_packet_json(packet()))


if __name__ == "__main__":
    unittest.main()
