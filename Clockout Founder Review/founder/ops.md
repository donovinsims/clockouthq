# Operations — Clockout

November 4, 2026. A solo, founder-delivered service business in Roscoe, Illinois. This is the operating plan for one person with roughly 12 delivery hours a week — the documented illustrative capacity, not a confirmed availability. Where a real supplier price exists it is linked; where only a quote will tell, it is marked as such.

**Current-pass integration note (November 4, 2026):** Donovin reports full-time availability, but productive delivery capacity is still unknown. The 12 weekly delivery hours, 18-hour Core allowance, 8-hour One Fix allowance and two-engagement work-in-progress cap are provisional planning hypotheses. The cap of two is retained as a provisional control, not a measured throughput limit. The current workflow is **15-minute free fit check → optional One-Page Read or paid investigation when useful → scope/quote → customer approval and deposit → implementation**. These templates supersede older deposit-before-scope interpretations.

## 1. Historical proposal and current weekly rhythm

The original weekly schedule was a planning proposal. The current pass replaces automatic 90-minute reads with a short factual qualification step.

The cycle, in order. **(C)** marks the steps the customer sees.

1. **Pipeline block.** Update the tracker: approaches, conversations, qualified problems, quotes, cleared money, work in progress and next action.
2. **15-minute fit checks.** Ask about one recent factual problem, current workaround, systems involved and the desired observable change. Record a short factual observation; do not promise a dollar saving or automatically produce a read.
3. **Qualified follow-up.** Where useful, prepare the optional One-Page Read after qualification, or propose a separately scoped paid investigation when uncertainty is substantial.
4. **Scope and quote.** Map dependencies, customer responsibilities, exclusions, acceptance test, ownership and support before any implementation deposit.
5. **Delivery, acceptance and handover.** Change the process first, configure existing tools second, test on representative real work, and hand over customer-owned access and a runbook.
6. **Weekly books.** Record sales, investigation, build, testing, revision, handover and support time, direct costs, invoices and cleared money.
7. **Monthly reconcile.** Compare estimates with actuals and update matching scope assumptions only when evidence exists.

**Work in progress cap: two engagements.** This remains a provisional control while actual capacity is unknown; it is not a measured throughput limit.

## 2. Suppliers and tools

Clockout is a service business, so its "suppliers" are software, payment processing and the occasional subcontractor. Published prices below; anything unverified is marked.

| Need | Option | Published price | Status |
|---|---|---|---|
| Payments | **Stripe** (or Square) | Standard US online card rate 2.9% + $0.30 | **Verify on the actual account.** The processor is recorded as UNKNOWN in the source documents; this is an assumption in the CFO model |
| Email/calendar/docs | Google Workspace | ~$7–$14/user/month depending on tier | Verify current tier price at purchase |
| Booking a 20-minute slot | Cal.com (free tier) or Google Appointment Schedules | $0 | Free tier is adequate at this volume |
| Automation build tools | The **client's** Zapier/Make/n8n/Airtable tiers | $19.99 / $12–$38 / €20 / $20 per month (annual) | Billed to the client's account, not Clockout's — this is an ownership point, not a cost |
| Invoicing | Stripe Invoicing | Included in processing | |
| Bookkeeping | A local bookkeeper (e.g. the Rockford firms in [competitors.md](competitors.md)) | No published price — quote required | **Quote needed.** Modelled at $100/mo as an estimate |
| Insurance | A commercial liability broker | No published price — quote required | **Quote needed.** Modelled at $75/mo |
| Notes/documentation | Any plain text/markdown tool the client can read | $0 | Deliverables must be readable without a licence |
| Password/access handling | A password manager with sharing | ~$3–$5/month | Required if clients grant access |
| Mileage log | A phone app or a notebook | $0 | Needed for the tax deduction and the $70/engagement estimate |

**Reconciliation with the CFO:** the modelled software line is $120/month; the items above that Clockout actually pays for total roughly $30–$60/month at this volume, plus the password manager. That means the CFO's fixed cost is, if anything, **conservative** — good. The two genuinely unknown lines are **insurance** and **bookkeeping**; a real quote could move fixed costs by ±$150/month, which changes break-even by well under one engagement. No change to [numbers.json](numbers.json) is warranted until a quote exists.

## 3. People

One person. No employees, no contractors, no rota. The weekly split that makes the model work:

| Block | Hours/week | What |
|---|---:|---|
| Delivery | 12 | Build, test, handover for up to two engagements |
| Sales and first reads | 6 | Reads, conversations, quotes, follow-up |
| Admin and books | 2 | Books, invoicing, records |
| Learning and tooling | 2 | Only where it serves a live engagement |

**If measured work approaches the provisional 12 delivery hours:** pause new commitments, inspect total hours and support load, then adjust scope, schedule or price before accepting more work. Do not take a third concurrent engagement while the two-job cap remains the chosen control.

## 4. Routines (SOPs)

Each fits on one page and is meant to be followed on a bad day.

**SOP-1 Qualification (15 minutes per prospect).** Source and date recorded. Ask what happened the last time the problem occurred, what the owner did, what tools or people were involved, what remains unresolved, and what observable change would matter. Confirm owner/decision authority, access dependencies and willingness to continue. Record a short factual observation; do not infer a dollar saving. If the problem or access is unclear, do not quote yet.

**SOP-2 Optional One-Page Read (scoped, not automatic).** Prepare only after qualification when a concise written observation would help the owner decide. State what was reviewed, the observed bottleneck, the evidence source, a possible change, assumptions and next step. Do not invent a dollar value. The read is not required for every prospect and is not a substitute for investigation on uncertain work.

**SOP-3 The Written Test (30 minutes).** After investigation and before any implementation deposit: name the observable that proves it worked (calls returned within X hours, quotes followed up within 3 days, the report exists by Monday 8am). Name what is out of scope. Name who signs off. If the owner will not agree to a test, do not take the work.

**SOP-4 Access (15 minutes).** Minimum access, time-boxed. Client creates the account and grants access; Clockout never owns the domain, the phone system or the CRM. Revoke at handover. Write down what was accessed and when.

**SOP-5 Delivery.** Re-map the process before touching a tool. Change the process first. Configure existing software second. Automate last, and only the part with stable inputs and a human approval step for anything customer-facing. There is no automatic 18-hour qualification rule; the agreed scope and investigation determine the estimate.

**SOP-6 Acceptance (45 minutes, owner present).** Run the test on real work, not a demo. Record pass/fail per line. If it fails: fix or waive the balance — no arguing about what "pass" means, because it was written down.

**SOP-7 Handover (60 minutes).** The Runbook: what changed, how to run it, how to undo it in one step, who to call for what. Walk the owner's own person through it once. Confirm every account is in the client's name.

**SOP-8 The 30-day check (20 minutes).** One call: did it hold, what broke, what was never used. Write the answer down. This is the raw material for the first case study and the first reference.

**SOP-9 Complaint or incident.** Acknowledge the same day. Say what happens next and when. Fix first, explain second, never blame the tool. If it exposed customer data or sent a wrong message, stop the automation immediately and revert using the runbook.

**SOP-10 Weekly books (30 minutes).** Every engagement: hours, rework hours, direct costs, invoice status, money cleared. If a number is unknown, write "unknown," never zero.

## 4A. Reusable pre-deposit and delivery templates

These are working templates, not contracts or client messages. Complete them for the actual client and scope before accepting an implementation deposit. Do not treat elapsed calendar duration as labor hours.

### Template A — Qualification and fit check

| Field | Record |
|---|---|
| Prospect, owner and decision authority | |
| Source and date | |
| What happened the last time the problem occurred? | |
| Observable workflow/problem | |
| Current tool/process and workaround | |
| What has already been tried, and cost/effort | |
| Consequence the owner recognizes (time, error, missed work) | |
| Desired observable change | |
| Required systems, vendors, accounts or permissions | |
| Customer responsibilities and availability | |
| Feasible bounded intervention | |
| Fit decision | Proceed to free fit read / investigate further / decline |

The free fit check is one page: observed problem, evidence reviewed, one recommendation, assumptions, and a next-step choice. It is not a hidden sales meeting and does not promise an outcome. If systems, integrations, ownership or requirements remain materially unclear, pause before quoting and offer a separately scoped paid investigation only if the customer wants that work.

### Template B — Scope and quote before implementation deposit

| Field | Record |
|---|---|
| Scope name and customer outcome | |
| Starting state and evidence | |
| Deliverables, in plain language | |
| Systems/tools changed | |
| Explicit exclusions | |
| Customer inputs, access and approvals | |
| Implementation allowance (hours or days) | |
| Schedule and dependencies | |
| Price, deposit, balance and payment trigger | |
| Included revision allowance | |
| Acceptance test reference | |
| Ownership, credentials and third-party fees | |
| Support period and response boundary | |
| Expiration/approval date | |

No implementation work begins until the customer has approved this scope, the payment route is known, required access is available, and the acceptance test is agreed. A $950 One Fix or $2,500 Core is used only when the actual scope matches its written boundaries; custom booking or multi-system work requires its own scope and quote.

### Template C — Written acceptance test

| Test line | Pass condition | Evidence/source | Owner sign-off |
|---|---|---|---|
| Observable workflow behavior | | | |
| Customer-facing message or output | | | |
| Error/recovery path | | | |
| Handover/runbook reviewed | | | |
| Out-of-scope items acknowledged | | | |

Run the test on representative real work with the owner present. Record pass, fail, blocked-by-customer, or deferred. The balance is tied to this written test; do not invent a new definition of done after delivery begins.

### Template D — Change request

| Field | Record |
|---|---|
| Requested change and reason | |
| Why it is outside the approved scope | |
| Added deliverables and exclusions | |
| Added hours/cost and revised price | |
| Schedule impact/dependencies | |
| Acceptance-test change | |
| Customer approval/date | |

Pause the affected work until the change is approved in writing. If the request is rejected, deliver the original scope and record the limitation.

### Template E — Ownership, handover and support

- Customer-owned accounts, domain, phone/POS/scheduling systems and credentials confirmed: ___
- Access granted by customer and revoked or transferred at handover: ___
- What changed and how to run it: ___
- One-step undo/recovery path tested: ___
- Runbook delivered and customer operator walked through it: ___
- Third-party subscriptions, fees and renewals assigned to: ___
- Included support window and response boundary: ___
- Out-of-scope support route and future quote requirement: ___
- 30-day check date and questions: ___

### Template F — Full time and cost log

| Date | Project phase/task | Person | Hours | Cash cost | Evidence/notes |
|---|---|---|---:|---:|---|
| | Sales/qualification | Donovin | | | |
| | Investigation/discovery | Donovin | | | |
| | Build/configuration | Donovin | | | |
| | Testing/acceptance | Donovin | | | |
| | Revisions/rework | Donovin | | | |
| | Handover/training | Donovin | | | |
| | Support/incident | Donovin | | | |
| **Total** | | | **UNKNOWN** | **UNKNOWN** | Calculate only from complete actual records; blank is not zero |

At close, record amount invoiced, amount cleared, direct project costs, total hours, unresolved support and whether the customer permitted a reference or case note. Use these records to update the matching scope's economics; do not generalize from calendar duration alone.

### Template G — Baseline, priority and adoption review

Added from the [Corey source review](corey-context.md), especially C046/C057. This is a reusable record, not a mandatory paid assessment or another free 90-minute deliverable. Use it only to the depth needed for the actual scope.

| Field | Record for this workflow |
|---|---|
| Service being bought | Fit check / investigation and recommendations / implementation / separately agreed follow-up |
| Owner problem and current process | Last real event, existing workaround/tools, responsible decision maker |
| Baseline and evidence | Date range, volume/frequency, time per occurrence, errors/quality or current cost; source for each value |
| Outcome lever | Effectiveness / efficiency / quality; separate time, cash and service-quality changes |
| Candidate intervention | Existing feature, process change or new tool only if needed; include doing nothing as a comparison |
| Expected impact and confidence | Owner estimate / measured baseline / hypothesis; no invented savings |
| Effort and risk | Access, data, integration, training, dependencies, recurring fees, reversal and support |
| Priority | Low-effort/high-impact first where evidence supports it; high-effort items separately scoped, low-value items deferred |
| Recommendation decision | Selected one bounded change / investigate / defer; owner and reason |
| Adoption owner and next action | Who implements, by when, prerequisites and training/handover |
| Review and measurement | Agreed date/window and comparison method; unknown baseline means benefit unverified |
| Result status | Technical test passed / customer using it / benefit measured; these are separate states |

Before recording or uploading a client conversation, agree permission, destination, retention and data boundaries. A report-only engagement does not imply installation or unlimited support. Track research, report preparation, meetings, training and follow-up in Template F. Time returned is capacity unless actual spending falls; incremental revenue is not automatically incremental profit. Rollback and normal/error tests remain required for implementation.

## 5. Licences, permits and insurance — a checklist to confirm, not a compliance claim

Rules differ by place and change. Each item below must be confirmed with the authority or a professional. Nothing here establishes that Clockout is compliant.

| Item | Where to confirm | Status |
|---|---|---|
| Business structure (sole proprietor vs LLC) | [Illinois Secretary of State](https://www.ilsos.gov/) | **UNKNOWN** — existing records not reviewed. An accountant should advise |
| EIN / federal tax | [IRS](https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online) | UNKNOWN |
| Illinois tax registration and whether services are taxable | [Illinois Department of Revenue](https://tax.illinois.gov/) | UNKNOWN — service taxability must be confirmed, not assumed |
| Local business licence / home-occupation rules (Roscoe, Winnebago County) | Village of Roscoe / county clerk | UNKNOWN |
| Business liability insurance | A licensed broker | UNKNOWN — modelled at $75/mo as a placeholder |
| Written client agreement | A qualified adviser | **Does not exist yet.** The scope template in the source records is a template, not a contract |
| Data handling / client permissions | Self-audit + agreement | No policy exists. Needed before touching customer lists or phone logs |

## 6. Risk register

| # | Risk | Likelihood | Impact | Plan |
|---|---|---|---|---|
| 1 | **No buyer responds to the first 40 reads** | Unknown (simulation cannot estimate likelihood) | High | Pause; review actual replies, qualification, observation quality, pricing and channels before choosing the next test |
| 2 | **Guarantee claims exceed 15%** | Medium | Medium | Tighten qualification and the Written Test; provision already modelled. Above 25%, withdraw the guarantee |
| 3 | **Scope creep on a fixed price** | High | High | The Written Test and out-of-scope list are signed. Any addition is a new quote, in writing |
| 4 | **Engagement takes 25+ hours instead of 18** | Medium | High | Hours logged weekly; if a build passes 20 hours, stop and renegotiate scope, not price |
| 5 | **A client's automation sends a wrong message** | Low–Medium | **Severe** | Draft-only mode for the first 30 days; human approval on every outbound message; one-step revert in the runbook |
| 6 | **Client data or credentials exposed** | Low | Severe | Minimum access, password manager, revoke at handover, no client data on personal devices |
| 7 | **Donovin gets sick / unavailable** | Medium | High | Max two engagements, written delivery dates with slack, clients own everything so work is not blocked by him |
| 8 | **Cash gap while waiting for balances** | Medium | Medium | The $950 rung collects faster; keep the deposit; never count invoiced money as available |
| 9 | **A local competitor copies the offer** | Medium (Stateline AI is one page away) | Medium | Compete on the written test, the handover and named references — not on price |
| 10 | **The business drifts back to websites** | Medium | Medium | The $500 site experiment stays separate and time-boxed; the Core offer is the business |

## 7. Capacity, stated plainly

At 18 hours per engagement and 12 delivery hours a week, Clockout can carry **about 2.7 engagements a month** — and that assumes every hour is billable, which it will not be. The reconciled CFO ramp caps months 7–12 at 2.7/month and retains lower earlier volumes. Actual capacity and demand remain unverified. Keep the separate two-engagement work-in-progress cap; monthly completions and concurrent jobs are different measures. Rework and support may reduce throughput.
