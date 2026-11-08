# Tools and systems register
Tool roles retain their 2026-10-29 baseline. Core readiness checked 2026-11-02 (U05/W04); see [verification evidence](../10-reference-and-archive/CORE_WORKFLOW_VERIFICATION.md). Installation, authentication, execution and synchronization are separate checks. A tool discussed or installed for personal experimentation is not automatically production Clockout infrastructure.

| Tool/system | Supported role | Configuration status in this package |
|---|---|---|
| Codex | Research, document maintenance, website/implementation work | CLI 0.166.0-alpha.5.1; ChatGPT login confirmed; this Codex session completed the local research, deliverable and review workflow. Production delivery not certified |
| OpenCode | Implementation and lower-cost development options | v2.2.5; stored Console integrations listed; existing default run succeeded on the source-to-JSON smoke test, with no provider/model override. Production delivery not certified |
| Hermes | Assistant/agent workflow | Mentioned in continuity context; no production Clockout dependency established |
| Gemini / NotebookLM | Source-grounded reference and business context | Discussed in S15; missing attached package not recreated verbatim |
| Lovable | Optional site-building aid | Use when helpful, not mandatory or a new subscription authorization |
| Plane Cloud Free | Proposed execution system | S02 contains recommendations and conflicting historical plan claims; no current feature audit or configured workspace established |
| Things 3 | Personal task/execution possibility | No canonical Clockout integration established by sources reviewed |
| Git/GitHub | Versioned knowledge base | Active consolidated origin `donovinsims/clockouthq`, branch `main`. Authenticated metadata reported PRIVATE on 2026-11-07 (W05). U05/W04 describes the predecessor. |
| clockout.us | Business domain | Historical live/shareable report; current routing/contact flow unverified |
| Sites / Vercel / D1 | Historical review implementation | Recorded Sept checkout; not certified current production |
| GBP | Local business presence | Current verification/saved services unknown |
| Agent example library | Reusable starting concepts | Local library exists; deployment/results not implied; permission conflict unresolved |

## Operating rules
Use existing tools before custom code. Keep the smallest useful prospect/delivery tracker. Avoid new dependencies and recurring costs without owner approval. Confirm current official docs and the actual account plan before relying on a feature.

No credentials, model-provider tokens, runtime passwords, .env contents, cookies, session IDs or pairing codes belong in these docs. Record the responsible account owner and storage location descriptively, never the secret value.

## Cost record
For each tool: purpose, owner, status, monthly/annual cost, renewal, dependency, cancellation consequence and measured value. All actual amounts remain UNKNOWN until verified. A free tier recommendation is not evidence of current availability.

## Mentor material
The existing AI-Playbook folder is a reference library with business context, transcripts, research and examples. This package establishes a newer priority and evidence layer; it does not overwrite the original archive or import all old instructions as policy.

## Current priority
A payment route, a prospect tracker and a dependable delivery process matter more than a new business operating platform during the cash sprint.

## Verification before relying on a tool
Confirm current version, actual plan limits, account owner/access, credential storage, registrar, hosting route, costs/renewals, and Git permissions before treating them as configured facts. Do not dump credentials or make a new tool purchase as part of checking. Use the least costly adequate current tool, and keep business documentation separate from site source. Source A02/U02.
For any proposed tool, record purpose, owner, account type, cost, data handled, export/rollback path, permissions, current capability evidence and a stop condition. Test the smallest representative workflow in a non-production context before promising a feature. Confirm client ownership and access transfer for delivery tools. Do not treat an installed tool, historical mention or mentor recommendation as current production infrastructure.

## Attio CRM

W06 confirms Companies, People, Deals and the Companies-backed Clockout Pipeline list by read-only metadata. Use the existing Attio connector for schema and capability verification, then use an approved scoped transport only after sync tests and separate authorization. Local SQLite remains the operational authority and must work offline from CRM. See the [field mapping and sync policy](attio-sync-spec.md). The existing workspace is the only CRM target. Schema changes, record imports, live write readiness and access from the future runner are unverified.

## Demo pilot routing

Start with the [website sales operating system](../04-offers-and-sales/website-sales-operating-system.md) and its forms. Phase 0 found 40 readable workspace skill links. Apply relevant local SEO and GBP checklists with dated public evidence. Hold provider-dependent or owner-only work pending verification of access, cost and terms. Use `build-local-site` only as a reference after construction approval. The pilot excludes its bulk generation and deployment workflow.

The restored global `codex-quota-optimizer` instructions were read on 2026-11-07 (W05). Use them with Context Mode and the root workspace guidance. Use the smallest approved frontend and browser QA toolchain at the construction stage. Existing rollout triggers still govern deferred installation. Extract a custom skill only after repeated approved demos reveal a concrete gap.

Use the [implementation roadmap](../09-execution-and-decisions/clockouthq-2-0-implementation.md) for phase-specific dependencies and the [Demo Factory spec](../04-offers-and-sales/demo-factory-spec.md) for the approved-build QA boundary. Phase 2 uses local fixture tools only; Phase 3 uses public evidence; Phase 4 introduces approved static build and browser dependencies. Phase 6 may reuse the restricted research path under an authorized scheduler.

## Toolkit rollout plan

Reviewed 2026-11-07 against Donovin's repository and website skill shortlists. The entries below are planned work. Use the [website sales operating system](../04-offers-and-sales/website-sales-operating-system.md) for project scope and approvals. The [website playbook](../04-offers-and-sales/clockout_website_playbook_2026.md) and its project forms own the design and launch standards.

### Conditional local installs and pilots

The shortlist below records earlier candidate pins and smoke tests. Install only after the relevant phase, trigger and separate authorization. Verify compatibility, license and advisories at that time. Keep tool code, lockfiles, browser binaries, reports and prospect exports under `~/.local/share/clockout-toolkit/` where applicable. Record the installed version, smoke-test result and blocker.

| Tool | Setup and acceptance check |
|---|---|
| [Leadgen](https://github.com/Dukotah/leadgen) | Pilot reviewed commit `36784ad5125ac51e61741a478d0c7e3877e69d16` with `requests` and `openpyxl` in isolated Python 3.12. Pass its offline demo. Review OpenStreetMap source policies and attribution, then run one OSM-only `web_design` search around Roscoe, Illinois, capped at 10 candidates with automated enrichment disabled. Verify up to three public business sites manually and record one reproducible issue if found. Review the local CSV before any tracker import. |
| [Unlighthouse](https://unlighthouse.dev/api-doc/config) and [Linkinator](https://github.com/JustinBeckwith/linkinator) | Install `@unlighthouse/cli@0.19.1` and `linkinator@8.1.0` in one local npm workspace. Save a mobile lab report for two local preview pages. Confirm Linkinator passes a working route and flags a deliberate 404. Cap prospect scans at five public routes and reproduce findings manually. |
| [CodeStitch Astro](https://github.com/CodeStitchOfficial/Intermediate-Astro-Decap-CMS) and [Playwright Test](https://playwright.dev/docs/intro) | Build reviewed starter commit `a3552e3e0face8e536a59d0dfa806af3e206463d` from its lockfile. Add `@playwright/test@1.65.0` and Chromium locally. Test the production preview on desktop and mobile emulation for navigation, contact controls and form validation with submission intercepted. Keep Decap inactive until a client needs editing access. |
| [Local SEO skills](https://github.com/garrettjsmith/localseoskills) | Reuse the existing workspace installation. Verify the skill links and apply its audit checklist to one pilot finding using public evidence and free tools. |

### Website design, build and SEO

Use existing skills and the planned QA tools. Load only what the current stage requires. The playbook already covers landing-page intake, real content, brand and CTA decisions, metadata and launch review. Use the existing frontend builder for design, the current framework for implementation, and Playwright Test for repeatable browser checks. This covers the shortlist's practical needs without another skill pack, browser CLI or design hook. [Landing Page Design](https://github.com/elayadesign/ai-design-skills/blob/main/skills/landing-page-design/SKILL.md) · [Impeccable](https://github.com/pbakaus/impeccable) · [Web Quality Skills](https://github.com/addyosmani/web-quality-skills)

| Stage | Use | Required evidence |
|---|---|---|
| Discover | Playbook and discovery form | Verify services, service area, contact paths and proof. Record customer intent, the primary action and the content needed to support it. Clearly label demonstration content. |
| Design | `build-web-apps:frontend-app-builder`. Use `improve-ui` for a redesign when the existing visual identity needs review. | Record the client's visual direction, type, color and component conventions in a short `DESIGN.md` when needed for handoff or continuity. Review the mobile first screen for a recognizable service, service area, credible proof where available, and an obvious next action. [Source for the mobile review](https://x.com/noahiglerSEO/status/2087499847326630281) |
| Build | Astro starter or the project's existing framework. Use an installed framework-specific skill only when that framework is already in the project. | Build responsive pages and test the agreed call, quote or booking path. For an in-scope form, verify validation, failure handling, spam protection, delivery and approved conversion tracking. Preserve working routes and actions during redesigns. |
| Optimize | `local-seo-audit`, `local-schema` and `performance` as needed. | Check business details against verified sources and the GBP if in scope. Review titles, descriptions, canonicals, indexability, sitemap, internal links and applicable structured data. Create separate service-area pages only when supported by distinct, useful local content. Record mobile performance as lab data unless representative field data is available. [Source for the service-area review](https://x.com/boringlocalseo/status/2095481217571487838) |
| Verify | `build-web-apps:frontend-testing-debugging`, `better-accessibility`, Playwright Test, Unlighthouse and Linkinator. | Record desktop and mobile screenshots, browser test results, link checks and the playbook's launch checklist. Manually test keyboard navigation, focus, labels, contrast and form feedback. Resolve and retest blockers for the primary customer action, accessibility or business accuracy. |

Use the [Demo Factory spec](../04-offers-and-sales/demo-factory-spec.md) for the fictional master and three-type prospect pilot. Start with the minimal approved Astro and Playwright setup. CodeStitch, Unlighthouse and Linkinator are optional candidates with separate triggers. Real contact-path tests and production SEO in the general table apply to authorized paid delivery. Pilot simulations remain local-only. Revisit a factory skill after the three-type pilot identifies a repeated gap that the existing workflow and installed skills cannot cover. Follow the root skill-creation instructions and obtain applicable authorization before adding one.

### Install during matching work

When a future task establishes a trigger below, install and verify the matching tool as part of that work. Paid services, client account access and production changes follow their existing approval requirements.

| Tool | Trigger |
|---|---|
| [Crawl4AI](https://github.com/unclecode/crawl4ai/security/advisories) | Two qualified audits need structured extraction across multiple pages and manual review is the bottleneck. Pilot a currently patched version as a local library on public pages. |
| Lighthouse CI, Pa11y, schema-dts | Add Lighthouse CI when the first reusable template passes local QA. Add Pa11y when the first client preview has a working lead form to audit. Add schema-dts when a TypeScript site generates reusable JSON-LD. |
| PhantomReach, Google-Maps-SERP | Pilot PhantomReach when an assessment needs a repeatable report the current workflow cannot produce. Revisit Google-Maps-SERP for a scoped geo-grid deliverable after verifying a usable license and permitted collection method under the applicable [Google Maps terms](https://cloud.google.com/maps-platform/terms). |
| Umami, Uptime Kuma | Set up Umami when the first managed site has approved analytics scope and hosting. Add Uptime Kuma when Clockout is responsible for uptime alerts on at least three live sites. |
| Activepieces, OpenGMB, Chatwoot | Add Activepieces for a paid workflow the existing stack cannot handle. Add OpenGMB for ongoing GBP work with approved Google API access. Add Chatwoot when a client needs a shared inbox and has assigned someone to respond. |

Reference only, with no automatic install trigger: the two Google Maps scrapers, Open SEO, the CodeStitch Eleventy starter, Twenty, Cuelead, OpenProperty and Zite property-management.
