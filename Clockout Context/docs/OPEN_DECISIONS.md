# Open decisions

As of 2026-10-29. One canonical decision register; closed items retain their resolution. U02 corrects historical acquisition activity and Pietro completion; neither is an open decision. Unknown records are not assumed absent.

## Priority groups

P0: current blockers (OD01–04). P1: next-phase or engagement-dependent needs (OD05–10). P2: later evidence/maintenance decisions (OD11–19; OD14 initial setup closed). P3: optional strategic expansion (OD20). Reprioritize only from actual conditions.



## OD01 — P0 · before selling

- **Topic / current understanding:** Payment method, account readiness, payout timing, fees and holds UNKNOWN

- **Evidence:** U02; S01

- **Why / impact:** $500 means available funds

- **Dependencies:** Verified account access and actual payout schedule

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Verify a real collection route and settlement schedule

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD02 — P0 · first quote

- **Topic / current understanding:** Proposed $500 baseline now includes one page, one revision, contact method, metadata and domain connection. Donovin revised the price on 2026-10-31. Client-specific timing, acceptance, ownership, cancellation and support still require agreement.

- **Evidence:** U02; A02 website offer

- **Why / impact:** Prevent unprofitable or ambiguous promises

- **Dependencies:** Payment route, client needs and approval

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Fill scope template before accepting deposit

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD03 — P0 · now

- **Topic / current understanding:** No new prospects/sales conversations since Oct 13 confirmed on Oct 29; actual receipts, available cash, older contacts and post-confirmation activity remain unverified.

- **Evidence:** U02; S01

- **Why / impact:** Cannot calculate the cash gap

- **Dependencies:** Private payment records and owner confirmation

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Reconcile owner records without copying private financial data here

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD04 — P0 · before launch

- **Topic / current understanding:** Client content rights, approval, ownership and launch authority

- **Evidence:** U02; S04

- **Why / impact:** Needed to deliver responsibly

- **Dependencies:** Accepted scope and authorized client materials

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Written acceptance and named owner

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD05 — P1 · when needed

- **Topic / current understanding:** Current clockout.us contact flow, noindex/preview wording and site owner access

- **Evidence:** S10; L01/L03; U02

- **Why / impact:** Prospects need a reliable way to respond

- **Dependencies:** Correct live origin and owner-approved test

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Verify the Clockout CTA and an existing preview destination, access policy and removal path. Seek separate release approval for the pilot artifact.

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD06 — P1 · post-sprint unless blocking sales

- **Topic / current understanding:** GBP verification, saved services, hours and website field UNKNOWN

- **Evidence:** S10; L03; U02

- **Why / impact:** Approval did not equal successful save

- **Dependencies:** Existing owner-managed profile and current access

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Inspect existing profile; compare original five versus intended eight

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD07 — P1 · Nov 10 review

- **Topic / current understanding:** Continue sprint, revise offer, or start PM validation?

- **Evidence:** U02; S01

- **Why / impact:** Calendar date does not settle priorities

- **Dependencies:** Sprint results and unfinished obligations

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Actual cash, obligations, conversion evidence and owner decision

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD08 — P1 · after review

- **Topic / current understanding:** PM segment, accessible buyers, painful workflow and willingness to pay

- **Evidence:** S13; U02

- **Why / impact:** Niche remains unvalidated

- **Dependencies:** November review, reachable buyers and capacity

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** 10–15-company research and founder interviews

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD09 — P1 · before pilot

- **Topic / current understanding:** PM system permissions, sensitive data, approval and support responsibilities

- **Evidence:** S13; S04; U02

- **Why / impact:** Feasibility and reliable delivery

- **Dependencies:** Buyer workflow, existing systems and permission

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Map existing tools and obtain permission for bounded pilot

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD10 — P1 · before relevant contract

- **Topic / current understanding:** Legal entity/registration, tax handling, insurance, agreement readiness UNKNOWN

- **Evidence:** U02; S04

- **Why / impact:** Avoid guessing company status

- **Dependencies:** Owner records and engagement requirements

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Donovin confirms records; obtain appropriate professional advice where required

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD11 — P2 · after evidence

- **Topic / current understanding:** Permanent pricing and flagship paid implementation

- **Evidence:** S04; U02

- **Why / impact:** No universal rate card exists

- **Dependencies:** Actual delivery time, costs and paid demand

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Costs, delivery hours, buyer response and outcomes

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD12 — P2

- **Topic / current understanding:** Paid assessment / Concierge / managed service adoption

- **Evidence:** S04; S08/S09

- **Why / impact:** Potential services are not launched products

- **Dependencies:** Validated buyer need, competence and support economics

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Demand, scope, margins and explicit adoption decision

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD13 — P2

- **Decision confirmed (U10 / D24, November 8):** Local SQLite plus owner-private artifact storage is authoritative for all Clockout-managed operations. Attio is the existing CRM for companies, contacts, deals and sales follow-up. Use controlled outbound synchronization to support sales work and keep operations independent of CRM availability.
- **Rationale:** Durable full local evidence and approvals protect recoverability and scope. A bounded Attio projection avoids duplicate work while preserving CRM-owned fields.
- **Schema evidence:** W06 verified Companies, People, Deals and the Companies-backed Clockout Pipeline list. See the [field mapping and ownership](07-tools-and-systems/attio-sync-spec.md).
- **Status:** Architecture confirmed; actual sync readiness OPEN. Field usage and existing identifier values, permissions, side effects, matches, retries and automatic execution are unverified.
- **Next action:** Verify the local storage and backup boundary in Phase 2. Before enabling Attio sync, recheck the observed schema and prove the scoped tests and protections in the sync spec. Donovin owns activation approval.

## OD14 — CLOSED · initial repository setup

- **Topic / current understanding:** Repository/account/folder and initial sync are established. These initial records refer to the predecessor. See the [current Git layout](07-tools-and-systems/github-setup-and-maintenance.md#exact-layout) for the consolidated checkout.
- **Evidence:** October 30 setup checkpoint; U05/W04 direct November 2 local Git and GitHub observations.
- **Status:** CLOSED for initial setup. On November 2 the predecessor was PUBLIC. Donovin chose to leave that predecessor public and prepare the update locally.
- **Resolution:** Existing remote changes were preserved by fast-forwarding local main to 0a3d45f before corrections. No duplicate repository was created. Initial setup is not a pending authorization request.
- **Continuing requirement:** Review changes, permissions and actual visibility before any future authorized push. The November 2 predecessor update’s push was paused. Initial setup closure does not establish authority for a current push.
- **Decision owner:** Donovin.
- **Last reviewed:** 2026-11-02.


## OD15 — P2

- **Topic / current understanding:** Website component policy reconciliation

- **Evidence:** L05/L08; S04

- **Why / impact:** Sept checkout COSS/Kibo conflicts with Oct Obsidian/COSS context

- **Dependencies:** Latest explicit website directive and actual checkout

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Verify later owner instruction and actual checkout; no automatic redesign

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD16 — P2

- **Topic / current understanding:** Agent-template license/use rights

- **Evidence:** L01; L09

- **Why / impact:** Master context reports permission; cleanup log says license unverified

- **Dependencies:** Written permission/license and intended use

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Retrieve written permission and intended-use terms

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD17 — P2

- **Topic / current understanding:** Founder public claims/titles and quantitative achievement approval

- **Evidence:** L01/L02/L10

- **Why / impact:** Biography includes unsupported precise claims

- **Dependencies:** Original career evidence and publication consent

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Verify exact title, scope and attribution before publishing

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD18 — P2

- **Topic / current understanding:** Costs, gross margin, monthly revenue baseline and reserve

- **Evidence:** S04; U02

- **Why / impact:** Goals are not performance

- **Dependencies:** Private bookkeeping records and known obligations

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Build private books and aggregate summary

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD19 — P2

- **Topic / current understanding:** Missing October 13 ZIP/transcripts and earlier September events

- **Evidence:** S08; coverage register

- **Why / impact:** Source coverage is incomplete

- **Dependencies:** Original attachment availability; not a cash-sprint blocker

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Recover original attachments if available; integrate with provenance

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



## OD20 — P3

- **Topic / current understanding:** Recurring model, expansion, workshops, software products

- **Evidence:** S04; U02

- **Why / impact:** Avoid premature scope

- **Dependencies:** Repeatable acquisition/delivery evidence

- **Status:** OPEN; unverified where evidence is missing.

- **Next action:** Revisit after repeatable acquisition and delivery

- **Decision owner:** Donovin; professional review where the specific engagement requires it.

- **Last reviewed:** 2026-10-29.



Resolve by recording source/date/owner/decision and implementation evidence in the decision log. Preserve the OD ID. Do not close an item merely because a template or plan exists.

## OD21 — P0 · before enabling Phase 2 controls

- **Decision:** Choose the actual restricted research identity and founder-only execution boundary.
- **Status:** OPEN. The proposed design is documented; isolation has not been tested on the actual runtime.
- **Next action:** After Phase 2 authorization, review permissions and validate bypass probes from the actual identity. Verify OD13 private local storage and keep CRM credentials outside the research identity.
- **Owner and evidence:** Donovin. U08 / D22 and the [Operations Manager spec](07-tools-and-systems/operations-manager-spec.md).

## OD22 — P0 · before enabling pilot outreach

- **Decision:** Confirm an existing founder-owned sender, suppression handling, evidence lookup and approved test destination.
- **Status:** OPEN. Provider selection and sender readiness are unverified.
- **Next action:** Verify sender and receipt lookup with applicable approval. Resolve OD05 preview and CTA readiness, verify the approved live artifact, and obtain separate exact-message approval.
- **Owner and evidence:** Donovin. D21 and the [outreach verification plan](09-execution-and-decisions/clockouthq-2-0-implementation.md#phase-5--prove-the-prospect-pilot-and-economics).

## OD23 — P2 · before scheduling Phase 6

- **Decision:** Confirm restricted scheduling profile, cadence and capacity.
- **Status:** OPEN. Manual workflow is the starting point. The actual scheduled boundary is unverified.
- **Next action:** After manual pilot evidence and separate authorization, probe the scheduled identity and verify machine/app availability, caps, no privileged paths, restart and recovery. Retain manual operation if isolation cannot be proven.
- **Owner and evidence:** Donovin. D21 and the [scheduled research plan](09-execution-and-decisions/clockouthq-2-0-implementation.md#phase-6--schedule-bounded-research-and-review-results).

## Implementation readiness review — 2026-11-07

U09 / D23 reviewed OD01–OD23. The matrix includes the November 8 OD13 architecture decision under U10 / D24. OD14 remains closed. OD13 architecture is confirmed and sync readiness remains open. The other decisions retain their open status.

| ID | Confirmed or documented evidence | Still open and simplest next step | When it matters |
| --- | --- | --- | --- |
| OD01 | U02 and S01 identify collection readiness as a priority. | Verify the existing payment route, fees, holds and time to cleared funds using private records. | Before quoting payment terms or accepting money. |
| OD02 | U02 and D14 record the proposed $500 one-page offer, $250 upfront and $250 before launch. D21 separates demo from paid scope. | Use the proposed terms as a quoting baseline. Agree each actual scope, acceptance, ownership and support in writing. | First paid quote; independent of Phase 2. |
| OD03 | U02 confirms only the October 13–29 acquisition interval. | Reconcile private receipts, spendable cash and later activity with Donovin. | Business priority and November 10 review; no dependency for inert fixtures. |
| OD04 | D21 and paid delivery guidance require separate production construction and launch authority. | Verify written client rights, ownership, acceptance, payment conditions and exact launch approval. | Before affected production work or launch. |
| OD05 | D21 requires separate pilot preview approval and live verification. | Verify the Clockout CTA, an existing preview destination, access, indexing and removal. Prefer the smallest existing authorized host. | Before real preview release and outreach. |
| OD06 | S10/L03 are dated profile evidence. D21 permits only appropriately sourced public observations in research. | Leave the owner profile alone until access and actual saved state are verified. | When Clockout GBP changes or private data are in scope. |
| OD07 | U02 records the November 10 review. D21 changes website acquisition, while the cash objective and review remain dated. | Decide after actual cash, pipeline, capacity and obligations are reconciled. | Before changing the business priority. |
| OD08 | S13 and U02 defer property-management validation until review. | Keep it parked pending the founder's market decision and evidence of a painful workflow. | Separate property-management work. |
| OD09 | S13, S04 and U02 record pilot permission and privacy concerns. | Agree access, data handling and support with the specific participant. | Before a property-management pilot. |
| OD10 | U02/S04 leave legal, tax, insurance and agreement readiness unverified. | Review owner records and the actual engagement requirements. | Before the affected contract or regulated work. |
| OD11 | D14 and D21 retain a proposed introductory offer. | Decide permanent pricing after actual demand, costs and delivery effort are known. | After pilot evidence. |
| OD12 | S04/S08/S09 are business references. | Keep additional paid services deferred until a buyer need, margin and support scope justify explicit adoption. | Later offer expansion. |
| OD13 | D24 selects private SQLite and local artifacts as the operational authority and Attio as the CRM. W06 verifies the schema. | Verify storage and backup boundaries, then mapping, permissions, deduplication, conflicts and independent operation before activation. | Local boundary in Phase 2; live sync readiness before Phase 5 activation. |
| OD14 | Initial predecessor setup is closed under U05/W04. W05 records the consolidated private repository separately. | Recheck current checkout and obtain applicable Git authorization at the time of action. | No implementation blocker. |
| OD15 | D19 adopts the website playbook. D21 separates the demo from existing production sites. | For the approved master, default to minimal Astro and component CSS per spec. Historical component conflicts stay open for any affected existing site. | Before adopting a disputed dependency or changing that site. |
| OD16 | L01/L09 conflict about agent-template permission. | Use original or clearly licensed assets and code. Retrieve exact terms before reusing the disputed library. | Only if the affected asset or template is proposed. |
| OD17 | L01/L02/L10 are source references with unresolved public-claim approval. | Use substantiated and authorized titles or evidence. Omit disputed claims. | Before using affected claims publicly. |
| OD18 | S04/U02 establish planning context, not current finances. | Keep detailed books private and reconcile cleared funds, costs and obligations before judging margins or reserves. | Business review and pilot economics. |
| OD19 | The coverage register identifies missing historical sources. | Recover originals with provenance when available. Preserve unknowns in the meantime. | Historical recovery; no Phase 2 dependency. |
| OD20 | S04/U02 and D22 favor evidence before expansion. | Defer recurring products and broader tools until repeatable demand and delivery support a decision. | After pilot evidence. |
| OD21 | D21/D22 require a founder-operated boundary that research cannot bypass. | Use the simplest existing enforceable identity or isolation profile. Probe actual permissions and alternate paths. Seek separate approval for any account or permission changes. | First Phase 2 preflight and before enabling protected actions. |
| OD22 | D21 requires separate exact-message approval and reliable outcome evidence. | Prefer a founder-owned existing sender with suppression and receipt lookup. Verify an authorized founder-owned test and keep real sends disabled until it passes. | Before enabling pilot outreach. |
| OD23 | D22 specifies bounded research-only scheduling after the manual pilot. | Start manual. Select and test a restricted scheduler and founder-approved cadence only after pilot evidence. | Before Phase 6 scheduling. |

Implementation authorization is separate from resolving an OD item. Phase 2 starts with local storage verification under OD13 and isolation under OD21. The other items constrain their specific business, release, outreach, or later automation actions.

## Decision support and closing rule

The business plan's administration table lists options, tradeoffs and evidence needed for payment, entity/tax, banking, insurance, agreements, pricing, CRM, recurring work and industry selection. Do not interpret UNKNOWN as nonexistent. Before closing an item, record Donovin's decision, source/date, rejected alternative, implementation owner and review trigger in the decision log; an editorial recommendation cannot close a business decision. Priorities above reflect the October 29 baseline and should be reconsidered when actual conditions change.

