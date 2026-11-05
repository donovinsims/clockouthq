# Current optimization — v2.1, 2026-11-01

This targeted pass improves the existing system's use of Corey reference intelligence. The earlier v2.0 transformation report and tree below are retained as a dated historical snapshot.

## What changed

- Existing retrieval now supports structure/category/format/topic selection and balanced, relevant, representative and best-performance modes. Default substantial writing context contains four examples (3–6 configurable), attribution, source text/URLs/IDs/dates, source-quality caveats, provenance/archive pointers, technique cues and historical performance annotations.
- Added `brief` to the existing CLI for single/batch context preparation. The assistant studies the sources and writes prose; the command does not call a model or generate a post itself.
- Performance remains a secondary signal. Balanced selection reserves one comparable top-tier slot only when supported by the relevant shortlist, retains everyday references and includes available lower-performing contrasts. Stored within-format relative baselines are reused; raw likes do not set quality. Individual count/views ratios require positive views and are labeled fractions, not unique-person engagement rates. The 11 unavailable/ambiguous view records have unknown exposure, never zero-view rates.
- Added a separate nontraining ledger and `record` command. Generated drafts, approved edits and owner-verified published records retain separate statuses and independent authorship labels. No record automatically becomes authenticated original writing. Approval/publication attestations require actual evidence; important identity/position changes still require owner approval.
- Originality now checks prior generated content as well as Corey and available own originals, and batch members compare against one another. Exact sentence candidates, high lexical similarity and repeated recent patterns/openings supplement the existing contiguous-word/5-gram checks. These are review cues, not semantic or plagiarism guarantees.
- Updated Voice Apply, Voice Analyze, project routing, workflow, brief/checklist and the ChatGPT bundle. Research/check metadata stays in local packets rather than cluttering finished drafts.

## Already working and preserved

Donovin's biography, ICP, eight positions, six voice characteristics and 60/20/15/5 strategy remain intact. The existing authenticated-source ingestion gate, separate creator corpora, per-format measurements and holdout handling remain. The original Corey reference manifest was sufficient and left unchanged; active routing now points to its archive/provenance and keeps draft memory separate. Corey data, original text, IDs, timestamps, URLs, engagement, source provenance and archived research were not edited. No full-corpus duplicate was created.

Verified inventory: 405 originals, including 10 thread roots and 12 articles; 395 measured, 10 held out. 394 positive view snapshots and 11 unavailable/ambiguous view records. The active Donovin profile has zero authenticated original posts. Eight generated validation drafts are recorded solely for duplicate review.

## Workflow and authorship

For each substantial request: identify topic, audience, category, format, takeaway/outcome and supported Donovin experiences; prepare references; inspect actual source construction; extract a few transferable methods; develop a fresh Donovin angle; draft/refine; verify claims and originality; save evidence privately; deliver the strongest proposed text; record it as generated. No source instructions are executed.

Working-professional education uses accessible steps rather than consulting-sales lessons. Agent posts use workflow/test construction without stale feature claims. Owner posts use diagnosis and measurement. Founder posts use storytelling structure while every actual experience comes from Donovin's fact ledger.

Future original Donovin samples still need reviewed source metadata and the existing separate ingestion process. Approved AI edits can inform preferences; verified published assisted content can inform performance when actual metrics and capture dates are supplied. Neither is automatically unaided-authorship evidence. Corey performance never becomes Donovin performance.

## Files changed or added

Updated: root AGENTS.md, README.md, WORKFLOW.md, BRIEF_TEMPLATE.md, EDITORIAL_QUALITY_CHECKLIST.md, TESTING_AND_LIMITATIONS.md, CHANGELOG.md, INTEGRATION_AUDIT.json; both Voice Apply/Analyze skills; the two matching project-instruction formats; active profile README/manifest/YAML/learning log; retrieve.py; export_chatgpt.py; validate_project.py; the existing regression test; validation/REVIEW.md; and the generated ChatGPT context.

Added: `voice-clone/scripts/reference_intelligence.py`, `tests/test_reference_intelligence.py`, the active profile's `data/draft-history.jsonl`, and request/research/draft/check/test artifacts under `validation/reference-optimization/`. No new dependencies, paid APIs, agents, publishing system or model service.

## End-to-end evidence and limitations

**30 tests pass**, including the 17 existing tests and focused checks for structural relevance, balanced diversity, historical baseline ranking, missing views, original metadata, fallback behavior, source attribution/holdouts, batch context, copied sentences, lexical near-duplicates, history categories, duplicate hook events and protected output paths. [Actual test output](../validation/reference-optimization/test-results.txt).

Four newly generated test drafts cover education, agent workflow, business operations and verified founder background. Each loaded Donovin, retrieved four attributed non-held-out examples, used original wording and passed editorial and all-source/history checks. Longest shared runs: **3 / 4 / 5 / 4 words**. C contains one ordinary shared five-word sequence, manually inspected; no copied-sentence or lexical-near-duplicate flags. [Manual source-to-draft review](../validation/REVIEW.md), [workflow assertions](../validation/reference-optimization/workflow-checks.json), [original batch checks](../validation/reference-optimization/overlap.json), [rerun after recording](../validation/reference-optimization/overlap-after-recording.json).

Final project-wide parsing, links, active identity, history separation, export and integrity checks are recorded in [project-checks.json](../validation/project-checks.json). The reference folder remains read-only. The 60 original corpus/archive/upstream files remain byte-identical; all 241 reference-folder files match the recorded hashes. The remote Clockout knowledge base was not modified; this optimization needed no new business claims or external service calls.

Remaining limits: pattern/category and source-completeness cues are heuristics; the editor must inspect semantic fit, source claims and paraphrase risk. Historical snapshots have unequal exposure and often unknown collection dates. No original Donovin posting sample, independent human blind test, actual publishing or measured engagement result was added. Current tool-specific features still need fresh official verification before publication.

## Simple use

Ask Codex:

> Use Donovin Voice Apply: write a long X post for a nine-to-five professional about making a repetitive task easier with AI. Retrieve relevant Corey examples first, check the draft, and return the strongest version.

For an inspectable context packet:

```sh
python3 voice-clone/scripts/retrieve.py brief "clear instructions for an AI work task" --category practical_education --audience A --format long --out drafts/current/research.json
```

The assistant uses that packet to write. ChatGPT can use the regenerated curated bundle plus a topic packet; where code/file analysis is available, the existing original corpus can be attached directly as attributed research. No full-corpus copy or prompt dump is needed. Without corpus/execution access, disclose that retrieval or automated checks were unavailable.

---

# Implementation report — Donovin Sims voice system

Completed 2026-11-01, America/Chicago, inside `/Users/forex/Donovin_Voice_Guide`.

## Result and positioning

**Donovin Sims teaches practical AI so people can build useful things.** His personal content serves working professionals and everyday learners seeking capability and independence, alongside owners/founders/operators seeking practical operational improvements. Clockout diagnoses bottlenecks, improves processes and implements appropriate technology: **Find the bottleneck. Fix the process. Automate the rest.** Method: **Audit → Optimize → Automate**.

The initial configurable content target is **60/20/15/5**, with **12/4/3/1** ideas per 20, counted once by primary purpose. This is editorial intent, not measured posting history. No agency-startup/sales coaching, income promises, main-product business coaching or in-person workshop offering is inherited.

## Main changes

- Renamed `Corey_Ganim_Brand_Profile/` to `Donovin_Sims_Brand_Profile/`, renamed its identity-specific files and rewrote the active identity, bio, ICP and matching .md/.txt instructions. All 14 bio sections and six voice characteristics remain.
- Added `voice-clone/profiles/donovin-sims/` with separate facts, adopted positions, mechanics, lexicon, hooks, top-post research guidance, machine profile, manifest, learning log and empty authentic-writing data.
- Kept the original Corey corpus, source archive, statistics, provenance and measured authorship intact. Historical profile metadata now routes the archived brand source paths; original versions are recoverable.
- Updated both Ghostwriter adapters and the universal skill's project routing. The original upstream source and MIT license remain byte-identical. No blanket bans or human-detector claims govern the active system.
- Updated editorial, retrieval and ingestion scripts. Profile-based routing is configurable; legacy corpus arguments still work. Editorial baselines name their actual author. Overlap checks available own and reference data. Ingestion rejects missing/mixed author provenance and marked generated text for Donovin, uses stable fallback IDs in generic normalization and preserves holdouts.
- Added local AGENTS routing, curated ChatGPT export, usage docs, tests, four unpublished drafts and a 20-post plan.
- Preserved the original active brand/docs/scripts in `docs/archive/original-active/`. A file-by-file change inventory appears below.

## Evidence and conflicts

Compared 97 canonical GitHub blobs at tree `0a3d45f9cc04c6c3446409c4f21034634fbd1fcb`: 71 matched local bytes, 26 differed. Retrieved all differences plus two canonical records and verified all 28 fetched files against their Git blob hashes. The newer October 31 website proposal is $500 / $250 + $250, superseding the local $650 / $325 + $325 proposal. This remains a temporary proposal, not evergreen positioning or proven sales.

See [source reconciliation](SOURCE_RECONCILIATION.md), [local source audit](LOCAL_SOURCE_AUDIT.md), [comparison](canonical/comparison.json) and [active facts](../voice-clone/profiles/donovin-sims/facts.md). Documented career background is owner-authored evidence; exact titles and quantitative employment claims are omitted. Mentor examples are not Donovin experiences.

## Verification

- **17 behavioral tests passed**, covering default/explicit routing, own-versus-reference labels, actual configured baselines, invalid profile failures, legacy retrieval, working-directory independence, holdout exclusion, all-corpus overlap, overlap flags, required draft arguments, author/provenance rejection, cross-author merge rejection, deduplication, unknown metrics, stable IDs, holdout preservation and planning allocation.
- Four actual validation drafts passed all-corpus overlap thresholds: longest shared runs **3 / 3 / 4 / 3 words**, with **zero shared 5-word sequences**. Editorial review found only the expected personal-claim verification flag on the founder draft, reviewed against the canonical founder profile. Manual idea/structure review is in [validation/REVIEW.md](../validation/REVIEW.md).
- Project validation parses JSON/JSONL and all YAML using the already-installed PyYAML, checks active identity, 14 sections, six characteristics, instruction copies, strategy consistency, relative links, routing, export freshness and source integrity. Final outcome is recorded in [project-checks.json](../validation/project-checks.json).
- All **60 original corpus/archive/upstream files** are byte-identical to the initial project hashes. The original 405 unique Corey posts include 395 measured and 10 held out. **241 read-only reference files** match the captured SHA-256 manifest.
- No new dependency was installed. No repository commit/push, external publication, outgoing message or account change occurred. This folder had no Git repository; no existing project Git history was present to preserve.

Actual command evidence: [test-results.txt](../validation/test-results.txt), [draft results](../validation/results.json). Heuristic results are not factual verification or a plagiarism guarantee. No human blind study or engagement evaluation occurred.

## Source limitations

Authentic Donovin X samples ingested: **0**. Corey's measurements are never labeled Donovin statistics. X and LinkedIn were inaccessible (403/999). Exact employment titles/dates, quantitative career claims, current client/revenue figures, public case-study permission, live website behavior and actual new tool experiments remain unverified. Omit unresolved claims or verify them before publication. Private source context is excluded from the public-safe export and generated drafts.

## Exact use

**Codex:** Open this folder. Ask: “Read AGENTS.md and integrations/voice-apply/SKILL.md. Write a long X post for Audience A about [task], using these verified facts: [...]. Run editorial and all-corpus originality checks. Return one proposed draft.” Defaults load Donovin; no global skill installation is needed.

**ChatGPT:** Run `python3 scripts/export_chatgpt.py` from this root. Create a ChatGPT Project, upload `exports/CHATGPT_CONTEXT.md`, and paste `Donovin_Sims_Brand_Profile/03_Donovin_Sims_Project_Instructions.txt` into its project instructions. Add a completed `BRIEF_TEMPLATE.md` and request a draft. The bundle embeds the curated identity, audiences, positions, mechanics and checklist. Without the reference corpus/execution, it cannot run full automated originality; bring the saved draft back here and run:

```sh
python3 scripts/check_draft.py --format long --draft-file PATH_TO_DRAFT.txt
python3 voice-clone/scripts/retrieve.py overlap --profile donovin-sims --draft-file PATH_TO_DRAFT.txt --strict
```

Use the actual format, complete manual claim/idea review, and approve content yourself before publication. See [WORKFLOW.md](../WORKFLOW.md) for future authenticated sample ingestion and separate learning.

## File-by-file inventory

Machine-readable additions and original-path changes: [change-inventory.json](change-inventory.json). Source evidence directories are deliberately retained.

| Original file | Disposition | Current file |
|---|---|---|
| `BRIEF_TEMPLATE.md` | updated | `BRIEF_TEMPLATE.md` |
| `CHANGELOG.md` | updated | `CHANGELOG.md` |
| `Corey_Ganim_Brand_Profile/01_Corey_Ganim_Brand_Voice_and_Bio.md` | renamed_and_adapted | `Donovin_Sims_Brand_Profile/01_Donovin_Sims_Brand_Voice_and_Bio.md` |
| `Corey_Ganim_Brand_Profile/02_Corey_Ganim_Ideal_Customer_Profile.md` | renamed_and_adapted | `Donovin_Sims_Brand_Profile/02_Donovin_Sims_Ideal_Customer_Profile.md` |
| `Corey_Ganim_Brand_Profile/03_Corey_Ganim_Project_Instructions.md` | renamed_and_adapted | `Donovin_Sims_Brand_Profile/03_Donovin_Sims_Project_Instructions.md` |
| `Corey_Ganim_Brand_Profile/03_Corey_Ganim_Project_Instructions.txt` | renamed_and_adapted | `Donovin_Sims_Brand_Profile/03_Donovin_Sims_Project_Instructions.txt` |
| `Corey_Ganim_Brand_Profile/README.md` | renamed_and_adapted | `Donovin_Sims_Brand_Profile/README.md` |
| `EDITORIAL_QUALITY_CHECKLIST.md` | updated | `EDITORIAL_QUALITY_CHECKLIST.md` |
| `INTEGRATION_AUDIT.json` | updated | `INTEGRATION_AUDIT.json` |
| `README.md` | updated | `README.md` |
| `TESTING_AND_LIMITATIONS.md` | updated | `TESTING_AND_LIMITATIONS.md` |
| `WORKFLOW.md` | updated | `WORKFLOW.md` |
| `integrations/voice-analyze/SKILL.md` | updated | `integrations/voice-analyze/SKILL.md` |
| `integrations/voice-apply/SKILL.md` | updated | `integrations/voice-apply/SKILL.md` |
| `scripts/check_draft.py` | updated | `scripts/check_draft.py` |
| `voice-clone/COREY_GANIM_QUICK_START.md` | archived | `docs/archive/original-active/COREY_GANIM_QUICK_START.md` |
| `voice-clone/SKILL.md` | updated | `voice-clone/SKILL.md` |
| `voice-clone/profiles/corey-ganim/README.md` | updated | `voice-clone/profiles/corey-ganim/README.md` |
| `voice-clone/profiles/corey-ganim/corey-voice-profile.yaml` | updated | `voice-clone/profiles/corey-ganim/corey-voice-profile.yaml` |
| `voice-clone/scripts/ingest.py` | updated | `voice-clone/scripts/ingest.py` |
| `voice-clone/scripts/retrieve.py` | updated | `voice-clone/scripts/retrieve.py` |

## Final directory tree

All non-system files below, excluding Finder metadata and generated Python caches.

```text
Donovin_Voice_Guide/
├── docs/
│   ├── archive/
│   │   ├── original-active/
│   │   │   ├── Corey_Ganim_Brand_Profile/
│   │   │   │   ├── 01_Corey_Ganim_Brand_Voice_and_Bio.md
│   │   │   │   ├── 02_Corey_Ganim_Ideal_Customer_Profile.md
│   │   │   │   ├── 03_Corey_Ganim_Project_Instructions.md
│   │   │   │   ├── 03_Corey_Ganim_Project_Instructions.txt
│   │   │   │   └── README.md
│   │   │   ├── integrations/
│   │   │   │   ├── voice-analyze/
│   │   │   │   │   └── SKILL.md
│   │   │   │   └── voice-apply/
│   │   │   │       └── SKILL.md
│   │   │   ├── scripts/
│   │   │   │   └── check_draft.py
│   │   │   ├── voice-clone/
│   │   │   │   ├── profiles/
│   │   │   │   │   └── corey-ganim/
│   │   │   │   │       ├── corey-voice-profile.yaml
│   │   │   │   │       └── README.md
│   │   │   │   ├── scripts/
│   │   │   │   │   ├── ingest.py
│   │   │   │   │   └── retrieve.py
│   │   │   │   └── SKILL.md
│   │   │   ├── BRIEF_TEMPLATE.md
│   │   │   ├── CHANGELOG.md
│   │   │   ├── COREY_GANIM_QUICK_START.md
│   │   │   ├── EDITORIAL_QUALITY_CHECKLIST.md
│   │   │   ├── INTEGRATION_AUDIT.json
│   │   │   ├── README.md
│   │   │   ├── TESTING_AND_LIMITATIONS.md
│   │   │   └── WORKFLOW.md
│   │   └── README.md
│   ├── canonical/
│   │   ├── docs/
│   │   │   ├── 01-founder/
│   │   │   │   └── profile.md
│   │   │   ├── 02-business-foundation/
│   │   │   │   ├── business-plan.md
│   │   │   │   └── services-and-mentor-boundaries.md
│   │   │   ├── 04-offers-and-sales/
│   │   │   │   ├── website-offer.md
│   │   │   │   └── website-sales-operating-system.md
│   │   │   ├── 05-delivery-and-operations/
│   │   │   │   └── delivery-playbook.md
│   │   │   ├── 08-finance-and-goals/
│   │   │   │   └── cash-and-metrics.md
│   │   │   ├── 09-execution-and-decisions/
│   │   │   │   ├── contradictions.md
│   │   │   │   ├── decision-log.md
│   │   │   │   ├── history-2026-09-to-10.md
│   │   │   │   └── november-10-review.md
│   │   │   ├── 10-reference-and-archive/
│   │   │   │   ├── source-extracts/
│   │   │   │   │   ├── S01.md
│   │   │   │   │   ├── U02.md
│   │   │   │   │   └── U04.md
│   │   │   │   ├── templates/
│   │   │   │   │   └── scope-and-proposal.md
│   │   │   │   ├── ACCURACY_AND_DEPTH_REVIEW.md
│   │   │   │   ├── claims.yaml
│   │   │   │   ├── CONSOLIDATION_REPORT.md
│   │   │   │   ├── file-coverage.csv
│   │   │   │   ├── FUNCTIONAL_SCENARIOS.md
│   │   │   │   └── PROVENANCE.md
│   │   │   ├── AGENTS.md
│   │   │   ├── CHANGELOG.md
│   │   │   ├── CHECKPOINT.md
│   │   │   ├── CURRENT_STATE.md
│   │   │   ├── OPEN_DECISIONS.md
│   │   │   ├── README.md
│   │   │   └── SHA256SUMS
│   │   ├── comparison.json
│   │   ├── SNAPSHOT.md
│   │   └── tree.json
│   ├── change-inventory.json
│   ├── IMPLEMENTATION_REPORT.md
│   ├── LOCAL_SOURCE_AUDIT.md
│   ├── original-project-hashes.json
│   ├── reference-readonly-baseline.json
│   ├── SOURCE_RECONCILIATION.md
│   └── TRANSFORMATION_PLAN.md
├── Donovin_Sims_Brand_Profile/
│   ├── 01_Donovin_Sims_Brand_Voice_and_Bio.md
│   ├── 02_Donovin_Sims_Ideal_Customer_Profile.md
│   ├── 03_Donovin_Sims_Project_Instructions.md
│   ├── 03_Donovin_Sims_Project_Instructions.txt
│   └── README.md
├── exports/
│   └── CHATGPT_CONTEXT.md
├── integrations/
│   ├── ghostwriter-upstream/
│   │   ├── ai-tells-original.md
│   │   ├── LICENSE
│   │   ├── voice-analyze-original.md
│   │   └── voice-apply-original.md
│   ├── voice-analyze/
│   │   └── SKILL.md
│   └── voice-apply/
│       └── SKILL.md
├── scripts/
│   ├── check_draft.py
│   ├── export_chatgpt.py
│   └── validate_project.py
├── tests/
│   └── test_voice_system.py
├── validation/
│   ├── drafts/
│   │   ├── 01-education.txt
│   │   ├── 02-agent.txt
│   │   ├── 03-operations.txt
│   │   └── 04-founder.txt
│   ├── 20-post-plan.json
│   ├── project-checks.json
│   ├── results.json
│   ├── REVIEW.md
│   └── test-results.txt
├── voice-clone/
│   ├── profiles/
│   │   ├── _template/
│   │   │   ├── flops.md
│   │   │   ├── hooks.md
│   │   │   ├── learning-log.md
│   │   │   ├── lexicon.md
│   │   │   ├── positions.md
│   │   │   ├── top-posts.md
│   │   │   └── voice-dna.md
│   │   ├── corey-ganim/
│   │   │   ├── data/
│   │   │   │   ├── corpus.jsonl
│   │   │   │   ├── ingest-report.txt
│   │   │   │   ├── normalized-input.json
│   │   │   │   ├── replies.jsonl
│   │   │   │   ├── source-audit.json
│   │   │   │   ├── source-provenance.json
│   │   │   │   ├── stats.json
│   │   │   │   └── stats.md
│   │   │   ├── source-archive/
│   │   │   │   ├── items/
│   │   │   │   │   ├── article-2049837999534318073.md
│   │   │   │   │   ├── article-2051293720138432635.md
│   │   │   │   │   ├── article-2054569765071372600.md
│   │   │   │   │   ├── article-2078058885257076908.md
│   │   │   │   │   ├── article-2084974468347121940.md
│   │   │   │   │   ├── article-2087907515795443846.md
│   │   │   │   │   ├── article-2089766791321133401.md
│   │   │   │   │   ├── article-2093074260361347474.md
│   │   │   │   │   ├── article-2094066129790755304.md
│   │   │   │   │   ├── article-2095505027536224349.md
│   │   │   │   │   ├── article-2100948018434281701.md
│   │   │   │   │   ├── article-2112577969617092879.md
│   │   │   │   │   ├── post-2066581137191776483.md
│   │   │   │   │   ├── post-2092375719292862933.md
│   │   │   │   │   ├── post-2092559429275447742.md
│   │   │   │   │   ├── post-2099808193178485185.md
│   │   │   │   │   ├── post-2108697389389295908.md
│   │   │   │   │   ├── post-2109989049305842150.md
│   │   │   │   │   ├── post-2110467523418194103.md
│   │   │   │   │   ├── post-2110700709448499694.md
│   │   │   │   │   ├── post-2111182906370781683.md
│   │   │   │   │   ├── post-2111888819079291157.md
│   │   │   │   │   ├── post-2112663410043470281.md
│   │   │   │   │   ├── post-2113243121358147638.md
│   │   │   │   │   ├── post-2113313048316272831.md
│   │   │   │   │   ├── post-2113405523018006966.md
│   │   │   │   │   ├── post-2113681829945315380.md
│   │   │   │   │   ├── post-2114703733007188231.md
│   │   │   │   │   ├── post-2114771654098530627.md
│   │   │   │   │   ├── post-2115115153540669747.md
│   │   │   │   │   ├── post-2115389605851599038.md
│   │   │   │   │   ├── post-2115476203184218336.md
│   │   │   │   │   ├── post-2115881525543653394.md
│   │   │   │   │   ├── post-2116142364058157232.md
│   │   │   │   │   ├── thread-2062474022269395074.md
│   │   │   │   │   ├── thread-2066873370520551810.md
│   │   │   │   │   ├── thread-2067913325229306159.md
│   │   │   │   │   ├── thread-2074076221302874178.md
│   │   │   │   │   ├── thread-2097270723194781853.md
│   │   │   │   │   ├── thread-2098536815175340180.md
│   │   │   │   │   ├── thread-2099260836632260647.md
│   │   │   │   │   ├── thread-2100257655461982416.md
│   │   │   │   │   ├── thread-2100981172272865755.md
│   │   │   │   │   └── thread-2102735796826681771.md
│   │   │   │   ├── collection-report.json
│   │   │   │   ├── index.json
│   │   │   │   ├── INDEX.md
│   │   │   │   └── README.md
│   │   │   ├── validation/
│   │   │   │   ├── draft-01.txt
│   │   │   │   ├── draft-02.txt
│   │   │   │   ├── draft-03.txt
│   │   │   │   ├── draft-04.txt
│   │   │   │   ├── draft-05.txt
│   │   │   │   ├── draft-06.txt
│   │   │   │   ├── draft-07.txt
│   │   │   │   ├── draft-08.txt
│   │   │   │   ├── draft-09.txt
│   │   │   │   ├── draft-10.txt
│   │   │   │   ├── overlap-results.json
│   │   │   │   ├── README.md
│   │   │   │   └── synthetic-candidates.md
│   │   │   ├── corey-voice-profile.yaml
│   │   │   ├── hooks.md
│   │   │   ├── learning-log.md
│   │   │   ├── lexicon.md
│   │   │   ├── manifest.json
│   │   │   ├── positions.md
│   │   │   ├── README.md
│   │   │   ├── top-posts.md
│   │   │   ├── validation-notes.md
│   │   │   └── voice-dna.md
│   │   └── donovin-sims/
│   │       ├── data/
│   │       │   ├── corpus.jsonl
│   │       │   ├── replies.jsonl
│   │       │   ├── source-audit.json
│   │       │   ├── stats.json
│   │       │   └── stats.md
│   │       ├── donovin-voice-profile.yaml
│   │       ├── facts.md
│   │       ├── hooks.md
│   │       ├── learning-log.md
│   │       ├── lexicon.md
│   │       ├── manifest.json
│   │       ├── positions.md
│   │       ├── README.md
│   │       ├── top-posts.md
│   │       └── voice-dna.md
│   ├── references/
│   │   ├── ai-tells.md
│   │   ├── engagement.md
│   │   ├── extraction.md
│   │   ├── formats.md
│   │   ├── ghostwriting-engine.md
│   │   ├── learning.md
│   │   └── validation.md
│   ├── scripts/
│   │   ├── ingest.py
│   │   ├── profile_config.py
│   │   └── retrieve.py
│   ├── DONOVIN_SIMS_QUICK_START.md
│   └── SKILL.md
├── AGENTS.md
├── BRIEF_TEMPLATE.md
├── CHANGELOG.md
├── content-strategy.json
├── EDITORIAL_QUALITY_CHECKLIST.md
├── INTEGRATION_AUDIT.json
├── README.md
├── TESTING_AND_LIMITATIONS.md
└── WORKFLOW.md
```
