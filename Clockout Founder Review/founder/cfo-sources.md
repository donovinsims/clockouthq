# Where the CFO's numbers come from

November 4, 2026. Nothing here is an audited figure. **No bank statement, invoice, receipt, tax return or processor statement was reviewed.** Every line is one of: (a) historical source research, (b) a labelled estimate with its reasoning, (c) a named scenario, or (d) a separately identified owner report. Current processor rates and account terms were not verified. Where the true number is unknown it is marked UNKNOWN rather than set to zero.

## Added owner evidence and unresolved inputs

O01–O06 in [customer-evidence.md](customer-evidence.md) are chat reports from November 4. Salon payment $1,000 and Pietro's payment $2,000 are owner-reported, not audited collections. Two elapsed weeks and one elapsed month do not supply hours. Direct costs, taxes, settlement, refunds, remaining support and income requirement are UNKNOWN. Therefore no historical margin, realized hourly return or profit is calculated.

The separate reconstruction is in [the CFO note](cfo.md). No historical payment was inserted into `numbers.json`; annual model costs, volumes and capacity remain unchanged scenarios. Owner-reported full-time availability updates the evidence register but does not validate a higher delivery ramp.

## Read-only workspace corroboration

[Customer evidence R01–R03](customer-evidence.md) links the inspected Oct 29 owner recap, business goals extract and cash record. Pietro's completion is documented as a founder confirmation; payment is undocumented. The salon fee remains a chat report. $5,000/month and $20,000/month are business-revenue goals; $500 by Nov 10 is an available-cash goal. None is an actual financial input or owner wage. No annual model value changes from this cross-check.

## Unit

| Input | Value | Status |
|---|---|---|
| Unit | one engagement (one scoped implementation project) | Defined for this model. A service unit is days of work, not a physical item — fractional daily rates are displayed explicitly in [cfo.md](cfo.md). |
| Price | $2,500 | **Proposal** from [pricing.md](pricing.md); not published, not charged, not evidence. |
| Second rung | $950 (One Fix) | **Proposal.** Separate 8-hour scope. At $950: card fee $27.85, software/travel/printing $125, and 10% × $700 balance = $70 provision; contribution $727.15 (76.54%). This unit calculation is separate from the $2,500 Core-only annual ramp. |

## Variable costs (per engagement)

| Line | Value | Status / reasoning |
|---|---:|---|
| Card processing 2.9% + $0.30 | $72.80 | **ESTIMATED rate for this scenario, not verified current processor pricing.** Donovin's processor, payment method, fees and holds are UNKNOWN. Confirm them on his actual account before quoting cash timing. |
| Software/licences for the build | $40.00 | **ESTIMATE.** A typical automation build carries one paid tier for a month or two. Unverified. |
| Travel/mileage, 2 trips ~100 mi | $70.00 | **ESTIMATE.** A flat $70 travel allowance for an assumed 100 miles. Retained as a planning estimate; it is not represented as a current IRS rate or tax deduction. Actual travel cost and tax treatment are unverified. |
| Handover pack printing/binding | $15.00 | **ESTIMATE.** |
| Guarantee provision | $175.00 | **ASSUMPTION:** 10% claim rate × $1,750 balance waived. No claim history exists. Scenario, not a cost. |
| **Total variable** | **$372.80** | |

## Fixed costs (per month)

| Line | Value | Status |
|---|---:|---|
| Software subscriptions (workspace, hosting, AI tools) | $120.00 | **ESTIMATE.** Actual stack unaudited. |
| Phone and internet share | $60.00 | **ESTIMATE.** |
| Business liability insurance | $75.00 | **ESTIMATE.** Actual policy status is an open decision in the source records. |
| Bookkeeping/accounting | $100.00 | **ESTIMATE.** |
| Banking and miscellaneous | $25.00 | **ESTIMATE.** |
| **Total fixed** | **$380.00** | |

## Startup

| Line | Value | Status |
|---|---:|---|
| Proof-demo build and printed samples | $600.00 | **SCENARIO.** No quote exists. |
| Simple site message/contact update | $200.00 | **SCENARIO.** Not a rebuild; no owner authorization to spend. |

## Volume — the assumption that decides everything

| Input | Value | Status |
|---|---|---|
| plan_per_day | 0.067 | 2.01 engagements per 30-day model month |
| capacity_per_day | 0.09 | ~2.7 engagements/month, from the documented illustrative capacity of 12 delivery hours a week at ~18 hours per engagement. **Planning example, not Donovin's actual availability.** |
| ramp (per month) | 0.99, 0.99, 2.01, 2.01, 2.01, 2.01, 2.7, 2.7, 2.7, 2.7, 2.7, 2.7 engagements | **SCENARIO, not demand.** Months 7–12 are capped at 0.09/day. Earlier months retain the saved inputs exactly. Fractional counts are averages. The old over-capacity ramp is preserved in [numbers-pre-reconciliation.json](numbers-pre-reconciliation.json). This annual model contains only $2,500 Core engagements; $950 pilots and a mixed-sales ramp need actual evidence. |

## What is deliberately not in the model

- **Founder pay.** There is no wage or draw line. Every "profit" figure is money before Donovin is paid, so it is a ceiling, not a living.
- **Founder acquisition time.** Sales conversations, the free one-page read (~1.5 hrs each) and follow-up are not costed. At 10 reads per engagement, that is ~15 uncompensated hours per sale.
- **Tax, entity, payroll and contractor costs.** UNKNOWN, and an accountant should confirm them.
- **The website experiment.** Modelled nowhere here; see below.
- **Living costs and cash runway.** The model says the business needs $800; it says nothing about Donovin's household.

## The $500 website, kept separate

This is a proposed experiment, not an adopted offer or the unit behind the Core annual ramp. The source proposal is $500 with $250 upfront and $250 after approval before launch; third-party costs, maintenance and complex work are excluded unless agreed. The 10–12 build hours used in earlier comparisons are illustrative and exclude unknown sales, revision and support time.

| Separate unit/cash worksheet | Value or rule | Status |
|---|---|---|
| Proposed project price | $500 | Scenario; not a verified sale |
| Proposed payment milestones | $250 / $250 | Subject to written scope, agreement and settlement |
| Gross revenue per illustrative build hour | $50 at 10 hours; ~$41.67 at 12 hours | Before all costs; not contribution or wages |
| Processor fees, hosting/domain/build tools and other direct costs | UNKNOWN | Do not substitute Core costs or assume zero |
| Total selling, investigation, build, revision and support hours | UNKNOWN | Calendar duration and build hours alone are insufficient |
| Cash contribution | Cleared project collections minus project cash costs | Cannot calculate until inputs exist |
| Contribution per total hour | Cash contribution divided by all attributable labor hours | Cannot calculate while hours/costs are unknown |
| Cash available for the Nov 10 target | Cleared accessible receipts minus fees/refunds and costs/reserves still required for delivery | A deposit is not automatically free available cash |
| Adoption / continue-stop decision | Donovin reviews scope, obligations and actual cash before quoting | Open; no website campaign or spend authorized |

This separately addresses the website economics without inventing a margin or adding it to the Core projection. Measure real receipts and full effort if the experiment runs; unknown values keep the result unresolved.
