# Pricing — Clockout

November 4, 2026. Provisional. Every price below is a **proposal to test**, not adopted policy and not a rate card Donovin has published. Prices are pre-tax; Illinois sales tax treatment for services is unverified and needs an accountant. The $500 one-page website stays a separate experiment throughout.

## Current local-pass decision

Two differently scoped paid jobs are now owner-reported: $1,000 salon booking work and $2,000 Pietro's Toast activation ([evidence](customer-evidence.md)). Their actual labor and costs are unknown. The proposed ladder and experiments below remain historical comparison hypotheses, not approved rate cards or automatic fixed quotes. Use the pre-deposit process in [operations](ops.md); price the inspected scope and reconcile total labor/costs first. This pass does not adopt discounts, payment terms, deeper-assessment prices or publication.

## 1. What the buyers said

`van_westendorp.py` was run twice: once on the baseline price answers, once on the revised-offer answers. The second run is the one that matters, because the pitch now names its prices.

| Point | Baseline (range "$1,500–$3,500") | Revised ("$950 / $2,500") |
|---|---:|---:|
| PMC — too cheap to trust | $500.88 | **$308.25** |
| OPP — least resistance | $504.50 | $308.25 |
| IPP — bargain = expensive | $1,497.75 | **$810.50** |
| PME — above this, too many won't buy | $3,500.42 | **$2,497.66** |
| Median "a bargain" | $1,200 | **$600** |
| Median "getting expensive" | $3,000 | **$2,200** |
| Median "too expensive" | $5,000 | **$4,000** |

Curves: [revised](pricing-curve.md) (17 complete, 3 dropped) and [baseline](pricing-curve-v1.md) (18 complete, 2 dropped). Both drop the same way: a $0 "too cheap" answer is discarded by the tool.

**Price anchoring is a hypothesis from this simulation.** IPP fell from ~$1,500 to ~$810 and PME from ~$3,500 to ~$2,498 between runs. The pitch changed in scope, framing and price presentation together; agent variability and method deviations also limit comparison. The result does not isolate the effect of publishing $950 or establish a real market ceiling.

**Do not use OPP.** It is where "too cheap" and "too expensive" cross, and with 17 simulated respondents clustered on round numbers and several naming $0 or $100, the crossing collapses onto the PMC. Report the range and the medians, not the point.

**What the revised band means.** These buyers now call $600 a bargain, $2,200 the point where it starts to hurt, and $2,498 the wall. The recommended core price of $2,500 sits **$2.34 above the ceiling** — i.e. at the edge, not comfortably inside it. That is a simulated test signal, not a measured market constraint (see §4).

## 2. What competitors charge

From [competitors.md](competitors.md), comparable fixed-scope project fees:

| Comparable | Price |
|---|---:|
| Local web project, low (CW Dynamic) | $1,500 |
| National readiness assessment, low (BlueShore) | $1,499 |
| National fixed assessment (Earley) | $2,500 |
| **Median of ten published project points** | **$3,500** |
| Local web essentials (Waivium) | $3,500 |
| National AI readines + prototype (Clear Function) | $3,500 |
| Local web growth (Waivium) | $6,500+ |
| Local fractional CFO retainer | $3,000–$10,000/mo |

**The published comparison points cluster around $2,500–$3,500 for a fixed-scope first project**, and both national assessment products credit the fee forward into implementation. Clockout's $1,500–$3,500 pitch range was *below and wider* than the market: it opened under the local floor and read to buyers as a range with a change order inside it (P012 said so directly).

## 3. What the business needs

Reconciled against [numbers.json](numbers.json) and [cfo-sources.md](cfo-sources.md), using the project-local `tools/unit_economics.py`. Fixed costs are $380/month. Each price includes $125 of software, travel and printing; estimated card fees of 2.9% + $0.30; and a 10% provision against the acceptance balance.

| Price | Contribution per engagement | Contribution % | Average frequency covering fixed costs |
|---:|---:|---:|---:|
| $950 | **$727.15** | 76.54% | 1 every 57.4 model days |
| $2,500 | **$2,127.20** | 85.09% | 1 every 167.9 model days |
| $3,500 (comparison scenario) | **$3,028.20** | 86.52% | 1 every 239.1 model days |

The $950 balance is $700 and the $2,500 balance is $1,750. The $3,500 comparison assumes a 30% deposit / 70% acceptance balance; it is not another proposed rung. Frequency uses 30-day model months and is an average, not a cash-settlement forecast.

**Contribution is before founder pay, tax, acquisition time and fixed overhead.** At 18 illustrative delivery hours, the $2,500 contribution is approximately **$118 per delivery hour**. At the One Fix's separate 8-hour allowance, $727.15 is approximately **$91/hour**. These are contribution-per-hour ratios, not wages or take-home earnings. Neither scope's hours have been measured on a real engagement.

## 4. The decision

### The price: **$2,500 fixed for one scoped implementation**

- Sits **at the top edge** of the revised acceptable range: $2,500 against a PME of $2,497.66 and a median "getting expensive" of $2,200. Slightly above this simulated threshold; real willingness to pay remains untested.
- Sits below the $3,500 published median of comparison projects, so it is defensible without a discount story.
- Leaves $2,127.20 contribution and roughly $118 per illustrative delivery hour before fixed overhead, founder pay, tax and selling time.
- Is a **single number**. The old "between $1,500 and $3,500 depending on what it takes" had to go: three buyers independently called it a hidden change order.

**Price presentation remains a test.** The simulation suggests checking whether the entry price influences expectations for the Core.

1. **$950 is the proposed first ask** for a narrow, qualified fix, with the $2,500 Core available for a separately scoped workflow.
2. **Keep the Core at its proposed $2,500 fixed price.** There is no real-buyer evidence for a routine $2,200–$2,400 discount. If scope changes, quote the revised scope in writing.

This review recommends a visible $950 starting price and a $2,500 Core description in the pricing section. Donovin must adopt the prices and approve publication first (Q4–Q5 and Q14). A conversation-only price remains an owner decision, not adopted policy.

### The ladder (two public rungs, one quoted rung)

| Rung | Price | What it is | Why someone steps up |
|---|---:|---|---|
| **One Fix** | **$950 fixed** | One narrow change: one queue, one follow-up rule, one form, one report. Up to ~8 hours, one revision, handover note. | The cheapest way to test whether Donovin is straight, on a real piece of work |
| **The Core** | **$2,500 fixed** | One workflow end to end: map it, change the process, configure what exists, automate the smallest reliable part, test it, hand it over. ~18 hours, one revision. | Solves the whole recurring problem, not one symptom |
| **Phase 2** | **Quoted, from $2,500** | A second workflow, or ongoing help after the handover | Only offered after the first engagement works |

Do not introduce another rung in this reconciliation. The baseline simulated PME was ~$3,500 and the revised PME ~$2,498; neither establishes a real price ceiling. Phase 2 remains a scoped proposal after a completed first engagement.

### The deeper assessment, optional

**$1,500, credited 100% against an implementation started within 30 days.** This is a proposal: Clockout's paid assessment is documented as optional with no established price. The credit structure is the one national competitors actually publish (Clear Function, WorkWise), and it answers the objection that a diagnostic fee is a toll booth. It must never be a required step before the free look or the One Fix.

### The opening offer

**No discount, no countdown.** Instead, a real trade for the first three engagements:

> The first three clients get the written finding and the fixed price in writing before any work starts, and in exchange Donovin asks permission to write up the outcome (measured before/after, the client's own words) and to be a reference call for the next two prospects.

That is a genuine exchange of value, it is limited by an actual count, and it produces one asset the simulated buyers repeatedly requested. It trains nobody to wait for a sale.

### The $500 website, kept separate

The $500 website is outside the implementation panel's scope, so the revised price curve cannot establish whether website buyers trust that price. Published local website comparisons are $1,500–$3,500 or more. At 10 illustrative build hours, $500 yields $50/hour of revenue before fees and other costs; the $950 One Fix yields about $91/hour of contribution at its separate 8-hour allowance. Those bases differ and neither is a wage. Keep the website experiment separate and measure its own receipts, costs and hours.

## 5. What to test with real buyers

1. **Two prices, one scope, real conversations.** Quote $1,950 to one group of qualified owners and $2,500 to another, same written scope, and record which produces a signed agreement. Small numbers: treat it as a signal, not a measurement.
2. **The One Fix as the front door.** Offer $950 first to owners who balk at $2,500, and record whether it converts and whether it leads to Phase 2. This tests the panel's repeated "under a thousand" request.
3. **A published starting price.** Put "$950 to start, $2,500 for a full workflow" on the site once it is updated. Price visibility is the cheapest differentiator found in the competitor work; measure inquiries before and after.
4. **Never test by discounting after a quote.** If a price is challenged, reduce scope in writing, not the number.

## 6. The panel's price objections, verbatim

- *"He quotes his fee before he has seen my books, so $1,500 to $3,500 is a guess I'm the one holding. I need to know what the fix is and what it saves me per month in actual dollars before I sign anything."* (P006)
- *"I'm not paying $1,500 to $3,500 for somebody to tell me what I already know about my own quotes."* (P018)
- *"…I'm looking at fifteen hundred to thirty-five hundred for a fix I probably could half-do myself with the software I already pay for."* (P019)

Marketing and the offer have to answer these with a number the owner can check, not with reassurance.

## Limits

- Simulated buyers choose what to test; they do not prove a price. The baseline had 19 passes; the retest had 16, categorized as trust (9), habit (4), price (2) and timing (1). These are hypotheses for real conversations, not validated demand or sales-channel evidence.
- Fixed costs, insurance, bookkeeping and processor fees are **estimates**; Donovin's actual accounts were not reviewed.
- No quote, contract or receipt was inspected in this pass; two past paid jobs are now owner-reported. Actual economics and repeatable demand remain unknown.
- An accountant should confirm entity, tax treatment and payroll/contractor structure before money moves.

The arithmetic is reconciled in [cfo.md](cfo.md). Price, demand, actual costs and delivery feasibility remain provisional.
