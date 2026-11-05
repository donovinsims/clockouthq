# Clockout Founder Review

Prepared November 4, 2026. A whole-business review of Donovin Sims and Clockout — not a website review. It follows the founder-board review (Offers 6/10, Monopoly 5/10, Product 6/10, all FUND IF, preserved untouched) through the ten remaining skills: competitors → consumer → pricing → offer → CFO → marketing → brand → ops → launch → plan.

## Current local improvement pass

Prepared November 4: [customer evidence and interview drafts](customer-evidence.md), pre-deposit [operations templates](ops.md), separate actual-project reconstruction in [CFO](cfo.md), and [unsent acquisition test](marketing.md). Owner reports two paid jobs totalling $3,000 and full-time availability; actual margins and productive capacity remain unknown. See [improvement-plan.md](improvement-plan.md) for completed preparation and external/evidence gates. This pass replaces the earlier fixed launch calendar with a relative, evidence-gated test; no outreach was executed.

## Completion and file status

[Completion status](completion-status.md) is the current readiness map. The packet is complete as a local planning-and-preparation product with explicit evidence gaps; it is not a verified-profitability or public-launch certificate. Blank client templates are intentionally unfilled; historical panels, pitches, curves and board files are retained as historical evidence. Current offer decisions and relative launch gates supersede earlier simulated proposals.

## Final supplied-source review

[Corey context and transfer decisions](corey-context.md) covers all **57 supported files** (33 podcast files including an index, 23 video/article files and one tweet export). [The source register](corey-source-register.json) contains per-file hashes and dispositions. The export contains 478 date-delimited entries; these are source records, not verified independent observations. Sources were screened and relevant passages examined; claims were not independently audited. Arabic auto-translation and derivative articles are flagged. No linked content was fetched or supplied file modified. Current findings are integrated into offer, operations, CFO and marketing; this is the final content-enrichment pass, not a new skill sequence.

## Start here

1. **[Summary](summary.md)** — half a page. The verdict, the three numbers, the one thing to do this week.
2. **[Business plan](business-plan.md)** — everything compiled, with the computed verdict at the top.
3. **[One-pager](one-pager.md)** — for someone deciding in two minutes.
4. **[Website direction](website-direction.md)** — what clockout.us should say, in what order. No build.
5. **[Evidence and questions](evidence-and-questions.md)** — what is established, and the single register of questions for Donovin.

## The verdict, in one line

**Not yet.** Three of four computed checks pass; the buyer panel buys at **20%** against a 25% bar. The capacity-capped scenario has positive contribution and operating results before founder pay. Demand, actual capacity, cash and delivery costs remain unverified; a repeatable, measured, bounded sale is the next proposed evidence test; two different paid projects are owner-reported.

## The evidence

| Stage | Artifact | Headline |
|---|---|---|
| Board (pre-existing) | [board.md](board.md) | 3 FUND IF, 5.67/10 average |
| Competitors | [competitors.md](competitors.md) · [csv](competitors.csv) | 25 competitors/substitutes (19 providers, 6 substitutes); three named providers serving the area publish starting prices; comparable project median ~$3,500 |
| Consumer | [panel/results.md](panel/results.md) · [baseline](panel-baseline/results.md) | Historical simulation: 1/20 → 4/20; objection hypotheses, not observed demand |
| Pricing | [pricing.md](pricing.md) · [curve](pricing-curve.md) | Provisional $950/$2,500 comparison scopes; scope-specific quotes await economics; anchoring remains a hypothesis |
| Offer | [offer.md](offer.md) | Scope-first proposal; fit check, optional investigation, written scope/acceptance before implementation deposit |
| CFO | [cfo.md](cfo.md) · [sources](cfo-sources.md) | 85% contribution; Year 1 $51,215 projected, $23,328 at half demand; $800 to start |
| Marketing | [marketing.md](marketing.md) | Unsent warm/direct drafts; relative 30-day scoped-sales test; channels and results unvalidated |
| Brand | [brand.md](brand.md) | Keep Clockout; promise is clarity, not results |
| Ops | [ops.md](ops.md) | Reusable scope/change-control templates; provisional WIP cap two; actual capacity unknown |
| Launch | [launch.md](launch.md) | Relative 30-day scoped-sales experiment; no adopted price or public launch date |

## Method and limits

**Simulation, not demand.** The buyer panel is 20 simulated buyers on seeded persona cards (seed 4242). The same cards were used for both rounds, but several offer elements changed together and agent variability and method deviations limit comparison. The 20% is a simulated tally with no established relationship to real conversion, not a forecast or an upper bound. Objections are hypotheses to test. Panel quotes are research, never testimonials.

**Executor deviation.** The skill expects one sub-agent per buyer through the Agent/Task tool. On this machine Claude Code's OAuth was expired, `codex exec` rejected the configured model, `gemini` returned 402 and `cursor-agent` was not logged in. Each buyer instead received its brief verbatim, inline, in a separate `researcher-web` agent and printed its JSON, which was filed with `panel.py save`. Every buyer was a separate agent and no answer was written by the chair — but this is not the intended swarm and is recorded as a method limitation.

**Numbers are projections.** No bank statement, invoice, receipt, tax record or processor statement was reviewed. Every cost is a labelled estimate or scenario ([cfo-sources.md](cfo-sources.md)). Unknown is never treated as zero.

**Competitor research** is public-page reading with named gaps: Reddit was blocked (403/login), G2/Capterra/Trustpilot/BBB returned no usable review text, Clutch returned 403. Themes 1–5 are usable as hypotheses; 6–8 are marked thin.

**Nothing external happened.** No outreach, purchase, publishing, site change, deployment, commit, push or account change. The $500 website remains a separate proposed experiment, excluded from the Core annual model; its unresolved unit/cash worksheet is in cfo-sources.md.

## Reproducing this review

Use the project-local reporting copies; installed skills remain unchanged:

```sh
python3 founder/tools/unit_economics.py founder/numbers.json
python3 founder/tools/compile.py --dir founder --check
python3 -m unittest discover -s founder/tools -p 'test_*.py' -v
python3 founder/tools/compile.py --dir founder
```

`--check` intentionally exits **1** for the unchanged **Not yet** verdict; it is not a verification-tool failure. The CFO document combines reviewed narrative with computed tables; do not overwrite its narrative with raw report output. See [tool notes](tools/README.md) for provenance. [Historical inputs](numbers-pre-reconciliation.json) preserve the former over-capacity scenario. No new dependencies were added.

**Not advice.** Not financial, legal or tax advice. An accountant should confirm entity, tax and payment structure; a lawyer or adviser should review any guarantee wording.

## Prior artifacts preserved

The founder-board files (`board.md`, `board/`, `idea.md`, `sources.json` from the earlier pass) and the original `pitch-v1.md` and `panel-baseline/` are unchanged. The earlier `verification.json` was superseded by the current one, which records both passes.
