# QA, launch and support checklist
PROPOSED operational template. Apply the relevant checks; do not create busywork unrelated to scope.

Use the [two-page demo QA form](../10-reference-and-archive/templates/website-project-forms.md#two-page-demo-qa) for speculative previews. The production checklist below governs paid delivery, including real operation of any agreed customer inquiry path.

## Website acceptance
- Approved business name, offer, contact details, hours and geographic claims.
- Owner has rights to copy, images, logos and testimonials.
- Phone/text/email links point to agreed destinations.
- Form validation and submission reach the agreed destination; test with authorized synthetic data.
- Missing input, duplicate submission, offline/failure behavior and retry feedback are understandable.
- No secrets in browser code, source, logs or handoff.
- Layout works on a narrow phone and desktop; no clipped text or horizontal overflow.
- Keyboard focus, labels, readable contrast, useful headings and touch targets work.
- Links and navigation function; loading and error states are clear.
- Titles, descriptions, canonical origin, robots/indexing and social preview match the launch plan.
- HTTPS and domain routing are correct at the authorized destination.
- No fake metrics, client logos, testimonials, example results or unsupported response-time promises.
- Hosting/domain cost, ownership and renewals are documented.

## Launch evidence
Record date/time/timezone, exact source/build, review URL, approved destination, approver, payment state and live checks. Keep deployment success separate from customer approval and indexing. Verify the live version after the change.

## Automation acceptance
Use an approved test/draft flow first. Exercise valid/invalid input, duplicates, missing data, access loss, provider failure, retries, rate limits, escalation and rollback. Confirm that a human can see and recover failed work.

Do not automate consequential customer commitments, spending, housing decisions or other high-impact actions merely because a tool supports them. Obtain explicit authority and appropriate review for the actual use.

## Support agreement fields
Support start/end, covered defects, excluded new work, response expectations, business hours, communication channel, third-party outages, recurring charges, update ownership and emergency escalation.

There is no established unlimited lifetime support policy. Do not promise a response time or SLA without an adopted agreement.

## Incident pattern
Acknowledge the reported symptom, preserve evidence, stop harmful repetition, restore or isolate the affected behavior if authorized, identify cause, fix the smallest surface, verify, and document. Keep the customer informed through the approved channel. Never report restoration based only on a restarted process.

## Trial-specific checks
Confirm the single revision round is complete or explicitly waived; acceptance and balance gates are satisfied; domain/hosting accounts and recurring costs belong to the agreed owner; contact delivery is tested with permission; and the prior version or rollback/recovery path is documented. One-time pricing does not imply unlimited maintenance or support. Source A02/U02.

## Record a reproducible acceptance test

For every agreed critical behavior record: requirement ID, input and starting state, action, expected outcome, actual outcome, environment/version/date, evidence location, tester, pass/fail/blocked and issue owner. “Blocked” is not “pass.” Use synthetic data for tests, with permission before any external submission or message. Check normal behavior and at least the relevant failure path. Retest affected paths after a fix; broaden only when shared behavior changed.

| System behavior | Minimum test cases | Acceptance decision |
|---|---|---|
| Contact form | Valid, missing/invalid fields, failure, retry and duplicate | Correct private destination and understandable states; no false success or duplicate effect |
| Reminder workflow | Due/not due, already sent, missing owner, stale record | One intended action or reviewed exception; never repeated unintended sends |
| AI summary | Clear input, incomplete/ambiguous input, unsupported claim | Source-grounded output; uncertainty visible; reviewer can reject/correct |
| Access and provider | Permission revoked, timeout, rate limit, recovery | Visible failed state, safe stop and authorized recovery |
| Handoff | Client can log in and perform a routine task | Confirmed client access and instructions, not merely an invitation |

Classify issues by impact: release blocker prevents the agreed critical task or creates unacceptable risk; important needs resolution or explicit documented acceptance; cosmetic can be scheduled by agreement. Do not waive a security or permission failure to hit a date. Record exact known exceptions in client acceptance rather than hiding them in internal notes.

For automation launch, run in draft/shadow mode where feasible, compare a bounded sample with a human process, and explicitly approve any change from draft to external effects. Keep a named monitor, recovery instructions and a way to disable the effect. A rollback does not undo an already sent message; plan containment accordingly. Support reviews should examine missed/duplicate work, reviewer corrections, new vendor behavior and access changes, not just whether the process ran.

