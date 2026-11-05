# Transformation plan and audit map

2026-11-01. Scope: this project only. The adjacent Clockout reference and GitHub knowledge base are read-only. No publishing, messaging, dependencies, commits or pushes.

1. Audit the existing brand, voice pack, corpus metadata, references, Ghostwriter adapters/license and scripts. Preserve originals before changing active entry points.
2. Compare the local reference against the current GitHub tree by Git blob hash; retrieve differing files and relevant canonical founder/current-state/decision records. Resolve material conflicts with dated evidence.
3. Rename the active brand directory, implement Donovin identity and two ICPs, preserve 14 biography sections and six voice characteristics. Create a Donovin profile with separate reference mechanics, facts and future own-writing data.
4. Update both adapters, default profile routing, retrieval, ingestion and editorial checks. Preserve explicit historical-corpus commands.
5. Update workflows, build a portable curated ChatGPT context file, four validation drafts and a 20-idea plan. Run identity, paths, structured-data, source-integrity and behavioral checks.

## Original dependency map

- Root README/WORKFLOW/brief/checklist and both integrations pointed to `Corey_Ganim_Brand_Profile`, `profiles/corey-ganim` and `corey-voice-profile.yaml`.
- `check_draft.py` accepted a profile path but only checked its existence; length numbers were always hardcoded Corey measurements.
- `retrieve.py` took an explicit corpus, excluded holdouts for search, and checked overlap against one corpus. Preserve that positional interface and add profile routing.
- `ingest.py` normalized/scored per format but had no author gate, used nondeterministic missing IDs and could mix authors in a merge. Add provenance and measurement boundaries.
- Historical profile holds 405 originals, 395 measured and 10 holdouts. Its data and source archive must remain byte-identical. Original active brand/docs/scripts are preserved under `docs/archive/original-active/`.
- Upstream Ghostwriter source and MIT license remain unchanged. Diagnostic AI-tells are useful; its detector claims, blanket vocabulary bans and numeric human scores do not govern this system.

## Audit coverage and completion

Local coverage: [LOCAL_SOURCE_AUDIT.md](LOCAL_SOURCE_AUDIT.md). Canonical reconciliation: [SOURCE_RECONCILIATION.md](SOURCE_RECONCILIATION.md). Original hashes: [original-project-hashes.json](original-project-hashes.json). Final changed-file map, tree and evidence: [IMPLEMENTATION_REPORT.md](IMPLEMENTATION_REPORT.md). All steps above are complete subject to the source limitations recorded there.
