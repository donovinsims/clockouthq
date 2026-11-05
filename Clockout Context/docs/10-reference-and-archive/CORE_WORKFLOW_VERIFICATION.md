# Core workflow verification — 2026-11-02

Scope: U05 owner-authorized local readiness/status reconciliation; W04 direct observations. This is a bounded smoke test, not production certification. Business baseline and optional-service unknowns remain unchanged.

## Observed checks

| Surface | Installation | Authentication/access | Execution and result | Boundary |
|---|---|---|---|---|
| Codex | CLI 0.166.0-alpha.5.1 | `codex login status`: logged in using ChatGPT | This active Codex session researched canonical documents, prepared a local action brief, reviewed OpenCode output and performed the documentation checks | No separate Codex CLI inference test or production deployment |
| OpenCode | v2.2.5 | `opencode auth list`: stored Console integrations; successful run demonstrates usable inference access | `opencode run --format json --file <local fixture> <prompt>` exited 0; used existing default configuration with no provider/model override | No credential values, provider configuration changes or production implementation tested |
| Git | 2.54.0 (Apple Git-157) | Existing origin readable | Clean main was fast-forwarded from 6d6836d to 0a3d45f, preserving four remote commits | This update remains uncommitted and local |
| GitHub | gh 2.92.0 | Authenticated metadata: ADMIN permission, main default branch | `git ls-remote` and GitHub comparison confirmed remote main; local checkout synchronized before corrections | Write/push path not exercised because the owner paused publication |

GitHub metadata reported `isPrivate: false`. Donovin explicitly chose to keep the repository PUBLIC and prepare this update locally without pushing. Historical October 30 private-setup observations do not establish current privacy. No visibility change was made. Initial repository setup is complete; OD14 is closed for that scope.

## Representative research → deliverable → review

Inputs: CURRENT_STATE.md, execution-system.md and cash-and-metrics.md from the synchronized checkout. A temporary fixture and outputs were kept outside the tracked tree, with no client records or credential values. Codex prepared a dated action brief from these sources; OpenCode received the same documents as an attachment with an instruction to return JSON without tools or edits.

OpenCode returned: offer $500, upfront $250, balance $250, cash target $500, deadline 2026-11-10, payment/settlement verification as the first next action, and a warning to preserve capacity for the delivery obligations created by deposits. All five numeric/date fields matched the source evidence; the next action and caveat were reviewed against the original documents. Output parsed as JSON, no error/tool events were emitted, and stderr was empty.

The Codex brief additionally states that two $250 deposits equal $500 gross, not necessarily $500 available after fees, holds and reserved delivery costs. Neither output establishes an actual prospect, sale, payment or completed client delivery. No provider/model selection or account configuration was changed for this check.

## Reproduction and final acceptance

1. Confirm core versions and login status without printing secrets; query repository metadata and compare local/remote main.
2. Build a temporary fixture from the three source documents; run OpenCode with its existing default configuration and no tool/auto-approval options. Validate the five fields above and manually review the action/caveat.
3. Review active canonical status/visibility statements and the full diff. Preserve source extracts and dated historical reports.
4. Check coverage, source/claim integrity, links, structured records and credential-pattern scan; regenerate SHA256SUMS after final content and run the included validator. Build a separate snapshot and validate its bytes against the current docs tree.
5. Leave the reviewed update local and uncommitted. A later owner instruction is required to resume publication; recheck visibility, remote changes and the diff first.

The original dated ZIP and earlier validation records remain historical. Current automated results are emitted by the read-only validator and reported at handoff, rather than changing an old result into evidence for this run. No claim of zero possible future issues is made.
