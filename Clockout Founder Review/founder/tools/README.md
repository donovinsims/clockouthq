# Clockout reporting copies

These standard-library-only scripts were copied from the installed `founder-cfo/unit_economics.py` and `founder-plan/compile.py` on November 4, 2026. The installed originals remain unchanged. This project is not a Git checkout.

Local changes preserve fractional service volumes to six decimal places, pluralize the unit before its parenthetical explanation, report monthly break-even equivalents, flag every over-capacity ramp month, and include peak planned volume in the compiler's existing capacity check. The compiler loads its sibling economics module. The economics result includes the additive `days_per_month` field for reporting.

From the project root:

```sh
python3 founder/tools/unit_economics.py founder/numbers.json
python3 founder/tools/unit_economics.py founder/numbers.json --volume 0.5 --json
python3 founder/tools/compile.py --dir founder --check
python3 -m unittest discover -s founder/tools -p 'test_*.py' -v
python3 founder/tools/compile.py --dir founder
```

The current compiler verdict is **Not yet**, with expected `--check` exit code **1**. Normal compilation writes the plan and exits 0. A passing verification confirms that these results reproduce; it does not mean the business passed the buyer threshold.

`--price` holds dollar costs fixed, including the entered processor and provision costs. Use that output only as a fixed-cost sensitivity. Price-specific unit comparisons in the pricing and CFO narratives recalculate the 2.9% + $0.30 fee and the 10% provision against the stated acceptance balance. `--volume` scales the steady plan and all ramp months while retaining physical capacity.

The [CFO document](../cfo.md) contains a reviewed narrative followed by computed tables. Regenerate the tables with `unit_economics.report(spec, unit_economics.analyse(spec))`, preserving the narrative before its separator. Avoid `--out founder/cfo.md`, which would replace the narrative. After updating any compiled section, regenerate the [business plan](../business-plan.md).

[Historical inputs](../numbers-pre-reconciliation.json) retain the original ramp and all original costs. [Verification](../verification.json) records the corrected inputs, checks, preservation hashes and remaining limitations. Panel, board, pitch and price-curve artifacts are historical evidence and are not rewritten by reconciliation.
