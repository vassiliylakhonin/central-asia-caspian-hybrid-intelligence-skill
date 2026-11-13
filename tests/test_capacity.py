"""Tests for the deterministic Caspian capacity estimator.

The estimator's contract: it combines caller-supplied figures into a low/high
range, names the binding constraint, echoes every input with its source, and
never substitutes a default for a missing or source-less figure.
"""

import json
import unittest

from central_asia_caspian_compliance_server.capacity import estimate_capacity_json


def figure(low, high, source="caller-supplied test figure", unit=""):
    return {"low": low, "high": high, "source": source, "unit": unit}


def scenario(**overrides):
    base = {
        "name": "test scenario",
        "route": "Baku-Aktau",
        "vessel_groups": [
            {
                "name": "train ferries",
                "vessels": figure(2, 2),
                "payload_tonnes_per_departure": figure(3000, 4000, unit="t"),
                "cycle_hours": figure(96, 120, unit="h"),
                "operating_days_per_year": figure(300, 330, unit="d"),
            }
        ],
        "interface_constraints": [
            {
                "name": "Aktau rail allocation",
                "tonnes_per_year": figure(500_000, 600_000, unit="t"),
            }
        ],
    }
    base.update(overrides)
    return base


class CapacityEstimateTests(unittest.TestCase):
    def test_known_scenario_computes_exact_range(self):
        payload = json.loads(estimate_capacity_json(scenario()))
        self.assertEqual(payload["status"], "estimate")
        # low: 2 * 3000 * (300*24 / 120) = 360_000
        # high: 2 * 4000 * (330*24 / 96) = 660_000
        group = payload["vessel_groups"][0]
        self.assertEqual(group["capacity_tonnes_per_year"]["low"], 360_000)
        self.assertEqual(group["capacity_tonnes_per_year"]["high"], 660_000)
        self.assertEqual(payload["fleet_capacity_tonnes_per_year"]["low"], 360_000)

    def test_binding_constraint_tracks_the_minimum(self):
        payload = json.loads(estimate_capacity_json(scenario()))
        # low side: fleet 360k binds under the 1M interface; high side: interface binds.
        self.assertEqual(payload["usable_throughput_tonnes_per_year"]["low"], 360_000)
        self.assertEqual(payload["binding_constraint"]["low"], "fleet")
        self.assertEqual(payload["usable_throughput_tonnes_per_year"]["high"], 600_000)
        self.assertEqual(payload["binding_constraint"]["high"], "Aktau rail allocation")

    def test_every_input_is_echoed_with_its_source(self):
        payload = json.loads(estimate_capacity_json(scenario()))
        inputs = payload["vessel_groups"][0]["inputs"]
        for key in ("vessels", "payload_tonnes_per_departure", "cycle_hours", "operating_days_per_year"):
            self.assertEqual(inputs[key]["source"], "caller-supplied test figure")
        self.assertEqual(
            payload["interface_constraints"][0]["tonnes_per_year"]["source"],
            "caller-supplied test figure",
        )

    def test_result_is_never_a_finding(self):
        payload = json.loads(estimate_capacity_json(scenario()))
        self.assertTrue(payload["result_is_not_a_finding"])
        self.assertTrue(payload["human_review_required"])
        self.assertNotIn("probability", json.dumps(payload).lower())

    def test_missing_source_is_rejected_not_defaulted(self):
        bad = scenario()
        bad["vessel_groups"][0]["payload_tonnes_per_departure"] = {"low": 3000, "high": 4000}
        payload = json.loads(estimate_capacity_json(bad))
        self.assertEqual(payload["status"], "invalid_input")
        self.assertTrue(payload["result_is_not_a_finding"])

    def test_blank_source_is_rejected(self):
        bad = scenario()
        bad["vessel_groups"][0]["vessels"] = figure(2, 2, source="   ")
        payload = json.loads(estimate_capacity_json(bad))
        self.assertEqual(payload["status"], "invalid_input")

    def test_inverted_range_is_rejected(self):
        bad = scenario()
        bad["vessel_groups"][0]["cycle_hours"] = figure(120, 96)
        payload = json.loads(estimate_capacity_json(bad))
        self.assertEqual(payload["status"], "invalid_input")

    def test_zero_cycle_time_is_rejected(self):
        bad = scenario()
        bad["vessel_groups"][0]["cycle_hours"] = figure(0, 0)
        payload = json.loads(estimate_capacity_json(bad))
        self.assertEqual(payload["status"], "invalid_input")

    def test_negative_figure_is_rejected(self):
        bad = scenario()
        bad["vessel_groups"][0]["operating_days_per_year"] = figure(-5, 10)
        payload = json.loads(estimate_capacity_json(bad))
        self.assertEqual(payload["status"], "invalid_input")

    def test_no_interface_constraints_means_fleet_binds(self):
        payload = json.loads(estimate_capacity_json(scenario(interface_constraints=[])))
        self.assertEqual(payload["binding_constraint"], {"low": "fleet", "high": "fleet"})

    def test_output_is_deterministic(self):
        self.assertEqual(estimate_capacity_json(scenario()), estimate_capacity_json(scenario()))


def draft_constraint(depth_low, depth_high, clearance_low=0.5, clearance_high=1.0,
                     design_low=5.0, design_high=5.5, tpm_low=800, tpm_high=900):
    return {
        "available_depth_m": figure(depth_low, depth_high, source="caller depth sounding", unit="m"),
        "underkeel_clearance_m": figure(clearance_low, clearance_high, source="caller clearance policy", unit="m"),
        "vessel_design_draft_m": figure(design_low, design_high, source="caller class record", unit="m"),
        "payload_tonnes_per_metre_draft": figure(tpm_low, tpm_high, source="caller specialist estimate", unit="t/m"),
    }


class DraftConstraintTests(unittest.TestCase):
    def test_draft_limited_group_uses_reduced_payload(self):
        s = scenario()
        # permissible draft: low side 6.0 - 1.0 = 5.0 vs design high 5.5 -> 0.5m shortfall;
        # reduction low = min(3000, 0.5 * 900) = 450 -> effective payload low 2550.
        # high side permissible 6.5 - 0.5 = 6.0 vs design low 5.0 -> no shortfall.
        s["vessel_groups"][0]["draft_constraint"] = draft_constraint(6.0, 6.5)
        payload = json.loads(estimate_capacity_json(s))
        draft = payload["vessel_groups"][0]["draft"]
        self.assertEqual(draft["permissible_draft_m"], {"low": 5.0, "high": 6.0})
        self.assertEqual(draft["draft_limited"], {"low": True, "high": False})
        self.assertEqual(draft["payload_reduction_tonnes"], {"low": 450.0, "high": 0.0})
        self.assertEqual(
            draft["effective_payload_tonnes_per_departure"], {"low": 2550.0, "high": 4000.0}
        )
        # low capacity: 2 * 2550 * 60 = 306_000
        self.assertEqual(
            payload["vessel_groups"][0]["capacity_tonnes_per_year"]["low"], 306_000
        )

    def test_unlimited_draft_leaves_payload_unchanged(self):
        s = scenario()
        s["vessel_groups"][0]["draft_constraint"] = draft_constraint(9.0, 10.0)
        payload = json.loads(estimate_capacity_json(s))
        draft = payload["vessel_groups"][0]["draft"]
        self.assertEqual(draft["draft_limited"], {"low": False, "high": False})
        self.assertEqual(
            draft["effective_payload_tonnes_per_departure"], {"low": 3000.0, "high": 4000.0}
        )

    def test_reduction_is_capped_at_full_payload(self):
        s = scenario()
        # permissible low 2.0 - 1.0 = 1.0 vs design 5.5 -> 4.5m * 900 = 4050 > 3000 payload.
        s["vessel_groups"][0]["draft_constraint"] = draft_constraint(2.0, 2.5)
        payload = json.loads(estimate_capacity_json(s))
        draft = payload["vessel_groups"][0]["draft"]
        self.assertEqual(draft["payload_reduction_tonnes"]["low"], 3000.0)
        self.assertEqual(draft["effective_payload_tonnes_per_departure"]["low"], 0.0)

    def test_draft_figures_echo_their_sources(self):
        s = scenario()
        s["vessel_groups"][0]["draft_constraint"] = draft_constraint(6.0, 6.5)
        payload = json.loads(estimate_capacity_json(s))
        inputs = payload["vessel_groups"][0]["draft"]["inputs"]
        self.assertEqual(inputs["available_depth_m"]["source"], "caller depth sounding")
        self.assertEqual(inputs["underkeel_clearance_m"]["source"], "caller clearance policy")

    def test_draft_source_less_figure_is_rejected(self):
        s = scenario()
        bad = draft_constraint(6.0, 6.5)
        del bad["available_depth_m"]["source"]
        s["vessel_groups"][0]["draft_constraint"] = bad
        payload = json.loads(estimate_capacity_json(s))
        self.assertEqual(payload["status"], "invalid_input")

    def test_draft_assumptions_appear_only_when_draft_is_supplied(self):
        with_draft = scenario()
        with_draft["vessel_groups"][0]["draft_constraint"] = draft_constraint(6.0, 6.5)
        payload = json.loads(estimate_capacity_json(with_draft))
        self.assertTrue(
            any("sea-level" in a for a in payload["arithmetic_assumptions"])
        )
        payload = json.loads(estimate_capacity_json(scenario()))
        self.assertFalse(
            any("sea-level" in a for a in payload["arithmetic_assumptions"])
        )


if __name__ == "__main__":
    unittest.main()
