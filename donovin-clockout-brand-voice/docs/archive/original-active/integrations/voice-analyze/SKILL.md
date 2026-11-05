---
name: corey-voice-analyze
version: 1.0.0
description: Recalibrate the Corey Ganim X profile from verified original writing, adapting the supplied Ghostwriter voice-analyze method without blanket AI-vocabulary bans.
---

# Corey Voice Analyze (adapted Ghostwriter)

**Purpose:** Update measurement and editorial constraints when *new, genuinely authored* Corey samples are supplied. Do not fabricate extra training material or use generated drafts as author evidence. This adapter draws on Ghostwriter `voice-analyze` 1.1.0 (MIT), with important project overrides.

## Load in this order

1. `../../voice-clone/profiles/corey-ganim/data/source-audit.json`
2. `../../voice-clone/profiles/corey-ganim/data/stats.json`
3. `../../voice-clone/profiles/corey-ganim/voice-dna.md` and `lexicon.md`
4. `../../voice-clone/profiles/corey-ganim/corey-voice-profile.yaml`
5. `../../integrations/ghostwriter-upstream/voice-analyze-original.md` for the underlying method

## Workflow

1. **Source gate:** Verify the new content is authored by the person, with date, ID, text and format; exclude reposts, quoted third-party text and duplicate exports. Track provenance. Separate replies, articles and threads. Do not count the same piece twice.
2. **Corpus split:** Preserve the existing holdout and provenance. Never train on held-out content when evaluating blind fidelity. Add new material in an auditable revision; do not silently reclassify archives.
3. **Per-format measurement:** Calculate post-level p10 / median / p90 lengths; opener/ender patterns; lowercase starts; contractions; colons; formatting and vocabulary. Measure length spread/variance descriptively; do not label "human" from a fixed sentence-variance threshold.
4. **Temporal analysis:** Compare the new date window to July/August and September/October 2026 separately. Different contexts and post types are not one voice metric.
5. **AI-default scan:** Use upstream `ai-tells-original.md` as a *review queue*, not a banned-word list. Log actual repeated boilerplate and unearned cliches. If an expression is genuinely in authentic posts, it is not forbidden. `optimize`, `framework`, `roadmap`, `leverage` are illustrative exceptions.
6. **Calibrate:** Update only rules supported by repeated authentic examples. Track measured facts separately from subjective 0–1 tone estimates. Preserve confidence, sample sizes and source examples.
7. **Report changes:** Produce a changelog: sample counts, added vs deduplicated, drift by format, profile changes with citations to post IDs, unresolved uncertainty. Require review before modifying primary experience and stance ledgers.

## Do not

- Infer authorship from a "human score", style detector or high rhythm variation.
- Treat AI-tell flags as evidence a real Corey post is AI-generated.
- Use unsupported 0–1 scores as calibrated probabilities.
- Contaminate the profile with self-generated drafts, unverified replies, or third-party quotes.
- Overwrite original `stats.json`, `source-audit.json`, or voice rules to make them fit a template.

**Output:** An evidence-labeled update proposal for `corey-voice-profile.yaml`, never an unsourced complete rewrite.
