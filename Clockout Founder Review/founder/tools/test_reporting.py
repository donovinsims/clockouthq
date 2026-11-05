"""Regression checks for fractional service volumes and capacity gating."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

import unit_economics as ue

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("clockout_compiler", Path(__file__).with_name("compile.py"))
compiler = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compiler)


class ReportingTests(unittest.TestCase):
    def setUp(self):
        self.numbers = json.loads((ROOT / "numbers.json").read_text())

    def test_fractional_volumes_are_visible(self):
        a = ue.analyse(self.numbers)
        report = ue.report(self.numbers, a)
        self.assertIn("0.005955 engagements", report)
        self.assertIn("0.178639 engagements (one scoped implementation project) per 30-day", report)
        self.assertIn("(0.067 a day)", report)
        self.assertIn("| 1 | 0.033 |", report)
        self.assertIn("| 7 | 0.09 |", report)
        self.assertNotIn("project)s", report)

    def test_corrected_financial_totals(self):
        a = ue.analyse(self.numbers)
        self.assertAlmostEqual(a["year1_profit"], 51215.184)
        self.assertAlmostEqual(a["year1_revenue"], 65550)
        self.assertAlmostEqual(ue.analyse(self.numbers, volume=.5)["year1_profit"], 23327.592)
        self.assertTrue(all(m["per_day"] <= a["capacity_per_day"] for m in a["months"]))
        old = json.loads((ROOT / "numbers-pre-reconciliation.json").read_text())
        self.assertEqual(self.numbers["ramp_per_day"][:6], old["ramp_per_day"][:6])
        restored = copy.deepcopy(self.numbers)
        restored["ramp_per_day"] = old["ramp_per_day"]
        self.assertEqual(restored, old)

    def test_monthly_overshoot_fails_even_with_low_steady_plan(self):
        n = copy.deepcopy(self.numbers)
        n["ramp_per_day"][6] = .1
        self.assertLess(n["plan_per_day"], n["capacity_per_day"])
        self.assertTrue(any("Month 7 ramp (0.1 a day)" in f for f in ue.analyse(n)["flags"]))
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "numbers.json").write_text(json.dumps(n))
            verdict, checks, _, _ = compiler.verdict(directory)
        self.assertEqual(verdict, "Not yet")
        self.assertFalse(checks[2][0])
        self.assertIn("peak planned volume is 0.1", checks[2][1])

    def test_saved_panel_remains_the_only_failing_check(self):
        verdict, checks, _, panel = compiler.verdict(str(ROOT))
        self.assertEqual(verdict, "Not yet")
        self.assertEqual([ok for ok, _ in checks], [True, True, True, False])
        self.assertEqual((panel["buys"], panel["answered"]), (4, 20))
        self.assertIn("bar is 25%", checks[-1][1])
        _, report = compiler.compile_plan(str(ROOT))
        self.assertIn("0.005955 engagements", report)


if __name__ == "__main__":
    unittest.main()
