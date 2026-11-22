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
                "amount_consistency": "not_checked",
                "currency_consistency": "not_checked",
                "date_ordering": "consistent",
                "party_consistency": "not_checked",
                "incoterms_allocation": "consistent",
            },
        )
        self.assertEqual(payload["aggregate"], "needs_human_review")
        self.assertEqual(
            sorted(payload["human_review_fields"]),
            ["amount", "currency", "parties"],
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

    def test_documents_of_the_same_type_all_count_regardless_of_order(self):
        p = packet()
        p["documents"].insert(
            1,
            {
                "type": "invoice",
                "label": "later invoice",
                "hs_codes": ["860719"],
                "date": "2026-02-05",
            },
        )
        first = json.loads(audit_trade_packet_json(p))
        p["documents"].reverse()
        second = json.loads(audit_trade_packet_json(p))
        self.assertEqual(first, second)
        self.assertEqual(results(first)["hs_code_consistency"], "inconsistent")
        self.assertEqual(results(first)["date_ordering"], "inconsistent")
        self.assertIn("invoice (later invoice) lacks: 732690", first["flags"][0])
        self.assertIn("invoice (later invoice) dated 2026-02-05", first["flags"][1])

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
        self.assertEqual(results(payload)["date_ordering"], "not_checked")
        self.assertEqual(results(payload)["incoterms_allocation"], "not_checked")

    def test_dates_without_a_supported_pair_are_not_checked(self):
        p = packet(
            documents=[
                {"type": "contract", "date": "2026-01-01"},
                {"type": "insurance", "date": "2026-01-02"},
            ]
        )
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["date_ordering"], "not_checked")

    def test_single_document_is_rejected(self):
        payload = json.loads(audit_trade_packet_json({"documents": [{"type": "invoice"}]}))
        self.assertEqual(payload["status"], "invalid_input")

    def test_bad_date_format_is_rejected(self):
        p = packet()
        p["documents"][0]["date"] = "10.01.2026"
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(payload["status"], "invalid_input")

    def test_invalid_calendar_date_is_rejected(self):
        p = packet()
        p["documents"][0]["date"] = "2026-02-31"
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


def rich_packet(**overrides):
    """A packet where every critical field is supplied."""
    p = packet()
    for doc in p["documents"]:
        doc.update(
            {
                "amount": "1 250,000.00",
                "currency": "usd",
                "seller": "Atyrau Trading LLP",
                "buyer": "Hartley Building Services, Ltd.",
            }
        )
    p.update(overrides)
    return p


def verdicts(payload):
    return {v["field"]: v["verdict"] for v in payload["field_verdicts"]}


class PerFieldVerdictTests(unittest.TestCase):
    def test_full_packet_passes_every_field_and_the_aggregate(self):
        payload = json.loads(audit_trade_packet_json(rich_packet()))
        self.assertEqual(
            verdicts(payload),
            {
                "hs_code": "pass",
                "amount": "pass",
                "currency": "pass",
                "dates": "pass",
                "parties": "pass",
                "incoterms": "pass",
            },
        )
        self.assertEqual(payload["aggregate"], "pass")
        self.assertEqual(payload["human_review_fields"], [])

    def test_one_failed_field_fails_the_packet_regardless_of_the_rest(self):
        p = rich_packet()
        p["documents"][1]["amount"] = "1250000.01"  # one tiyin off
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["amount_consistency"], "inconsistent")
        self.assertEqual(verdicts(payload)["amount"], "fail")
        self.assertEqual(payload["aggregate"], "fail")
        self.assertTrue(any("1250000.01" in f for f in payload["flags"]))

    def test_currency_mismatch_is_flagged(self):
        p = rich_packet()
        p["documents"][2]["currency"] = "EUR"
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["currency_consistency"], "inconsistent")
        self.assertEqual(payload["aggregate"], "fail")

    def test_party_names_match_after_normalization(self):
        p = rich_packet()
        p["documents"][1]["seller"] = "ATYRAU   TRADING L.L.P."
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["party_consistency"], "consistent")

    def test_different_party_is_flagged(self):
        p = rich_packet()
        p["documents"][1]["buyer"] = "Aktau Terminal Properties LLP"
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(results(payload)["party_consistency"], "inconsistent")
        self.assertEqual(verdicts(payload)["parties"], "fail")

    def test_unsupplied_field_is_routed_to_human_review_not_passed(self):
        payload = json.loads(audit_trade_packet_json(packet()))
        self.assertEqual(verdicts(payload)["amount"], "needs_human_review")
        self.assertEqual(verdicts(payload)["currency"], "needs_human_review")
        self.assertEqual(verdicts(payload)["parties"], "needs_human_review")
        self.assertEqual(payload["aggregate"], "needs_human_review")

    def test_bad_amount_format_is_rejected(self):
        p = packet()
        p["documents"][0]["amount"] = "about a million"
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(payload["status"], "invalid_input")

    def test_bad_currency_format_is_rejected(self):
        p = packet()
        p["documents"][0]["currency"] = "US DOLLARS"
        payload = json.loads(audit_trade_packet_json(p))
        self.assertEqual(payload["status"], "invalid_input")

    def test_rich_output_is_deterministic(self):
        self.assertEqual(
            audit_trade_packet_json(rich_packet()),
            audit_trade_packet_json(rich_packet()),
        )


if __name__ == "__main__":
    unittest.main()
