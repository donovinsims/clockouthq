# Lean execution system
D21 adopts the website workflow and approval policy. The proposed Operations Manager and its controls await separate implementation and verification. The tracking model derives from S02/L01/S11.

Use the private local SQLite ledger and artifact store as the authority for Clockout operational work. Attio is the existing sales CRM and receives a controlled projection under [OD13](../OPEN_DECISIONS.md#od13--p2). Keep payment records in their approved private system and link to verified results where needed.

## Minimum records
**Prospect:** alias/business, evidence, qualification, proof type, stage, last contact, next action/date.
**Delivery:** agreed outcome, scope link, owner, payment gates, status, acceptance and launch.
**Company:** current three outcomes, waiting items, open decisions and parked ideas.

## Proposed stages
Prospects follow the [website sales operating system](../04-offers-and-sales/website-sales-operating-system.md). Record build approval, QA, preview release and verification, outreach approval and actual contact outcomes separately. Keep failed, deferred, revoked, opted-out and uncertain outcomes visible.
Delivery: ready → doing → waiting on client → QA → approved → balance verified → launched → handed off.
Company work: inbox → next → doing → waiting → done, with parked ideas separate.

A sale and a receipt are separate events; a launched project can still have support obligations.

## Demo authorization and enforcement

Phase 1 records policy. Until enforcement is verified, stop before website construction, preview publication and prospect outreach. Donovin controls privileged execution for the pilot. Research may read approved public sources and submit a validated brief. Deny it write access to the approval store, executor and build workspace. Keep publication and messaging credentials, authenticated browser sessions and equivalent connectors outside research and build. Test this separation from the actual runner. Drafts, chat claims, sandbox approvals and scheduled tasks cannot issue founder grants.

| Operation | Required founder approval |
| --- | --- |
| Website construction | Before the first website file, scaffold or component, verify a grant for the exact prospect or reusable master-template ID, brief revision and input digest, permitted scope, founder identity, expiry and revocation/use state. Production construction requires its own authorization for written paid scope. |
| Preview publication | For the pilot, require separate approval after QA for the exact reviewed artifact digest and named preview destination. Future build approvals may explicitly include publishing to a specifically named, preconfigured preview environment with a fixed destination, access policy and allowed route scope. The executor must verify QA and bind release to the exact artifact from the approved build. Reject implied permission, unknown environments and destination drift. Verify the released artifact before outreach. |
| Prospect outreach | Always separate. Bind approval to the verified preview/build, sender, recipient, channel and exact payload. Recheck suppression, record actual send evidence, and reconcile uncertain results before retrying. |
| Production launch | Always separate. Verify written scope, client acceptance, payment conditions and applicable launch authority. |

**Proposed minimum.** Start with one founder-operated CLI, local SQLite, private artifacts and inert build, release, send and CRM adapters. Test owner-only entry points and reject missing, mismatched, stale, revoked and replayed grants before side effects. The [Attio sync policy](attio-sync-spec.md) keeps CRM access outside research and authorization paths. Measure success by demo quality, preparation cost and reliable controls.

Read the [Operations Manager implementation specification](operations-manager-spec.md) for protected command and data contracts, recovery, and restricted research scheduling. Use the [roadmap](../09-execution-and-decisions/clockouthq-2-0-implementation.md) for implementation order and tests. Both are future execution specifications.

## Daily routine
Check due customer obligations and revenue follow-ups, choose one major outcome, perform the next action, record result and next date. Do not let an exciting tool become today's priority without a clear business dependency.

## Weekly review
Reconcile overdue promises, cash, pipeline, delivery, scope changes and decisions. Keep no more than three major company outcomes active as a proposed attention limit. Review parked items only after current obligations.

## Plane history
The October 4 conversation proposed Growth Pipeline, Clockout HQ and one project per paid client, using states/labels/dates and project pages. Its Free-plan feature claims conflict within the recovered conversation. Do not reproduce that feature matrix as current advice or build around paid/unsupported features. Check the actual workspace if Plane is chosen.

## Interruption recovery
Write a checkpoint before stopping: last verified action, actual saved state, unresolved uncertainty, exact next step and relevant source. Reopen current records on resume. Do not rely on stale UI indices or an old unsaved state.
## Minimum operating loop

Maintain one tracker with item, stage, owner, next action, due date, evidence link and blocker. Daily: choose one cash or delivery outcome, check dependencies, complete the smallest reversible action and record the result. Weekly: reconcile active commitments, settled cash, hours, blockers and decisions; close stale items or assign a date. At handoff, record the last verified transaction and resume point. A tool is subordinate to the tracker: do not create parallel systems whose status can diverge.
