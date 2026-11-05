---
name: corey-voice-apply
version: 1.0.0
description: Apply the Corey voice profile to original X content and revise drafts using measured per-format habits, source-grounded facts and a restrained Ghostwriter AI-tells pass.
---

# Corey Voice Apply (adapted Ghostwriter)

**Purpose:** Write and edit useful, original X content with high fidelity to the documented Corey voice, not copy his posts or claim to be an authorized representative. Adapted from Ghostwriter `voice-apply` 1.1.0 (MIT).

## Required inputs

- Audience: **AI service operators** (default for educational content) or **business owners**.
- A specific point, topic, or real case with source facts. Ask for one material missing fact only when essential; otherwise write without unsupported claims.
- Format: short, long, quote, thread, article; quote drafts require the quoted material.
- Goal: teach, explain a position, drive qualified interest, announce a verified product or reflect on a real experience.

## Load and execute

1. Read `../../voice-clone/profiles/corey-ganim/corey-voice-profile.yaml` and `voice-dna.md`, `lexicon.md`, `positions.md`, plus both Brand Profile MD files when the audience matters.
2. Retrieve 5–8 *non-held-out* similar posts from the corpus, including ordinary and stronger examples; use `python ../../voice-clone/scripts/retrieve.py search ... -k 8` from this integration folder. Retrieve, **do not paste the whole corpus**.
3. Select one original, commercially relevant idea. Pick *one* target audience, a narrow problem and a genuine useful takeaway; do not default to a CTA.
4. Create 3 substantially different drafts, then select the strongest for accuracy, clarity and format. Apply per-format distributions as examples of tendencies, not quotas. Use October 2026 as the default contemporary long-post register, not a permanently frozen style.
5. Read `../ghostwriter-upstream/ai-tells-original.md` as diagnostic prompts. Rewrite generic abstractions, fabricated precision, predictable parallelism, forced transitions and fake urgency. **Never ban an attested word automatically.** Authentic Corey's "optimize", "framework", "roadmap", "leverage", occasional contrarian flips and selective excitement are allowed when relevant and not overused.
6. Run the editorial checklist `../../EDITORIAL_QUALITY_CHECKLIST.md`. A final proof pass checks every amount, timeframe, named client, personal experience, claim of present activity, and tool ability.
7. Run originality overlap with `python ../../voice-clone/scripts/retrieve.py overlap ../../voice-clone/profiles/corey-ganim/data/corpus.jsonl --draft-file PATH`, fixing any flag. Use `../../scripts/check_draft.py` to check basic format and AI-tell *review* flags too.
8. Deliver one preferred draft, optionally alternatives when asked, and a brief factual confirmation note for unresolved specifics. Never claim validation of identity, actual creator authorship, viral potential or publication approval.

## Quality and precedence

Factually accurate and original content > evidence from actual Corey posts > per-format profile > adapted Ghostwriter guidelines > generic AI writing advice. Holdouts must stay hidden from retrieval during blind tests. Prefer edits that preserve actual cadence; do not shoehorn in repeated catchphrases or excessive all-caps.

See `../../integrations/ghostwriter-upstream/voice-apply-original.md` for original method and `../../WORKFLOW.md` for the end-to-end brief.
