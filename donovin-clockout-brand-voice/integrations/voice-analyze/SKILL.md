---
name: donovin-voice-analyze
version: 2.0.0
description: Calibrate Donovin Sims's voice from verified original Donovin writing while keeping Corey mechanics, generated drafts and performance evidence separate.
---

# Donovin Voice Analyze (adapted Ghostwriter)

Adapted from [Ghostwriter voice-analyze](../ghostwriter-upstream/voice-analyze-original.md) 1.1.0 under the preserved [MIT license](../ghostwriter-upstream/LICENSE).

Load [source audit](../../voice-clone/profiles/donovin-sims/data/source-audit.json), [own stats](../../voice-clone/profiles/donovin-sims/data/stats.json), [active YAML](../../voice-clone/profiles/donovin-sims/donovin-voice-profile.yaml), [learning log](../../voice-clone/profiles/donovin-sims/learning-log.md), and the own voice DNA/lexicon. Initial own authentic sample count is zero.

1. Verify author, source URL/record, ID, date, text and format. Remove quoted third-party text from quote commentary; keep reposts excluded and replies separate. Generated or merely approved AI drafts cannot become evidence of original unaided writing.
2. Record provenance in source-audit.json before ingestion. Each accepted record needs `author_id: donovin-sims`, `verified_original: true`, `source_url`, stable `id`, valid date and text. This metadata records a human/source review; a script cannot independently prove authorship.
3. Ingest into a separate staging directory inside this project using `ingest.py --author-id donovin-sims`; merge only an existing Donovin corpus. Never merge Corey's data. Preserve established holdout IDs and don't expose holdouts while tuning.
4. Review deduplication, dropped records and per-format statistics. Under 5 measured samples a format has no length baseline; larger samples still need genre/context review. Do not promote a blended statistic into a universal voice rule.
5. Compare real Donovin samples across their own date windows. Corey July–October drift remains Corey evidence, not Donovin history. Keep adopted mechanics and observed Donovin habits explicitly labeled.
6. Use AI-tells as a diagnostic queue; do not remove attested words automatically, use human scores or infer authenticity from sentence variance.
7. Log proposed profile changes with source IDs, counts, supported rules, confidence and unresolved gaps. Owner-approved editorial preferences belong in learning-log.md even if the writing was assisted; they are separate from authentic sample measurements.
8. After reviewing the staging output, update the active own corpus/stats, manifest sample count, YAML provenance and source audit together. Preserve original exports and previous stats within this project. Do not mutate the reference profile to fit the new identity.

Output an evidence-labeled calibration proposal and counts. Report actual metrics only from published, identified posts with capture dates and own-format comparisons. No empirical Donovin measurements exist until this process has real source data.

## Separate learning records

The manifest's `draft_history` ledger distinguishes `generated`, `approved_edit` and `published` records, with an independent authorship label. It is never a training corpus. `record --status approved_edit` requires actual owner approval and `--approved-by-owner`; link the prior ID using `--parent-id`. Verified published records require owner-attested `--verified-published`, an actual Donovin post URL and publication date. These flags record reviewed evidence; the script cannot independently prove approval, authorship or publication.

Original Corey writing and original Donovin writing stay in separate corpora. A verified published AI-assisted post is still assisted, and an owner-approved edit is preference evidence. Authentic original Donovin samples still pass the existing provenance/ingestion review separately. Preserve actual source metadata and collection dates. Compare Donovin performance against Donovin's own format/time baseline, never Corey's audience results. Owner approval is required before changing important identity, positioning or personal positions.
