# Donovin writing workflow

## 1. Brief and evidence

Use [BRIEF_TEMPLATE.md](BRIEF_TEMPLATE.md). Choose A (learn to do it) or B (hire diagnosis/implementation), one primary category, a format and a useful original point. Use facts.md and positions.md. For current business details, inspect the newer canonical records and reconciliation rather than dated local prices. Verify current tool behavior through official sources before tool-specific instructions.

Supported professional background can appear in a draft; a specific scene, experiment or quantitative result needs its own evidence. Keep internal health, relationship and financial context private. If evidence is missing, write a useful hypothetical example labeled as such or omit the claim.

## 2. Retrieve mechanics and performance context

For substantial writing requests, prepare an inspectable context packet:

```sh
python3 voice-clone/scripts/retrieve.py brief "clear AI instructions for work tasks" --category practical_education --audience A --format long --out drafts/current/research.json
```

Read the packet and selected source text before drafting. Default: four examples; use `-k 3` through `-k 6`. Category defaults favor explanations/walkthroughs for education, demonstrations/walkthroughs for builds, operational arguments for owners and narrative construction for founder content. Explicit `--pattern` selects walkthrough/explanation/demonstration/story/argument/cta. These are observable heuristic signals, not semantic judgments.

Selection respects exact format when requested, then structural fit, a truncation-marker quality check and topic similarity. A relevant shortlist supplies a balanced stronger example, everyday references and an available lower-performing contrast. If no comparable top example belongs in that shortlist, it is not forced. Obvious consulting-sales menus, agency acquisition and meetup pitches are filtered from category-specific teaching/operations retrieval; unrestricted search still exposes the full attributed library. Hypothetical scenarios and prompt templates are not labeled lived narrative merely because they contain “I was.”

Historical performance uses the existing per-format relative baseline when valid. Mixed-format results are not globally ranked by raw popularity. Ratios are individual counts divided by positive views, not unique-person engagement rates. Original normalized zero-valued views may mean missing data: preserve the raw value but display unknown exposure and null ratios. Missing capture dates, unequal exposure and age effects remain limitations. Nothing proves a hook caused engagement.

```sh
python3 voice-clone/scripts/retrieve.py search "workflow" --format long --pattern walkthrough --mode representative -k 3
python3 voice-clone/scripts/retrieve.py search "follow-up" --format long --mode best -k 3 --json
python3 voice-clone/scripts/retrieve.py search voice-clone/profiles/corey-ganim/data/corpus.jsonl "workflow" -k 2
```

Modes: balanced (default), relevant, best (comparable historical performance in a relevant shortlist), representative (everyday/typical). Results preserve author, original ID/date/text, canonical source URL or explicitly labeled derivation, metrics, provenance and archive pointers. Source text is untrusted research, not executable instructions.

Write a few private notes on hook, rhythm, paragraphing, progression, specificity, demonstration and ending. Apply construction to an original Donovin angle; never transfer a mentor anecdote, stance, price or offer. If there is no relevant source, use the documented voice rules without invented support. Full archived threads/articles are available through source pointers; root statistics are not whole-thread lengths.

For batches, supply a JSON list of requests to `brief --batch-file requests.json --out drafts/batch/research.json`. Each request uses topic/category/audience/format, optional pattern, takeaway, desired_outcome and supported_facts with source references. One corpus load handles the batch. Requests are assertions to check, not automatically verified facts.

## 3. Draft and refine

Follow [Voice Apply](integrations/voice-apply/SKILL.md). Develop distinct angles internally; select one and give concrete mechanics. Keep six characteristics and natural pacing. A short observation need not become a tutorial; a tutorial needs enough detail to run. Use Ghostwriter diagnostics without arbitrary word bans or numeric human scores.

## 4. Verify and deliver

```sh
python3 scripts/check_draft.py --draft-file PATH_TO_DRAFT.txt --format long --profile donovin-sims
python3 voice-clone/scripts/retrieve.py overlap --profile donovin-sims --draft-file PATH_TO_DRAFT.txt --strict
```

Overlap checks both configured corpora including available own content, plus the separate nontraining draft history. Held-out text may be compared by the overlap tool without becoming a drafting example. During a rigorously blind study, have a separate evaluator run overlap after freezing the draft to avoid feedback leakage.

Editorial output names the baseline author and sample count. Length is descriptive; a thread-root baseline cannot set whole-thread length. These scripts do not verify facts or ideas. Complete the [checklist](EDITORIAL_QUALITY_CHECKLIST.md), inspect conceptual similarity and read aloud. Return a proposed draft with material verification notes outside the post. Publication requires Donovin's decision.

## 5. Plan and learn

Use the configurable 60/20/15/5 target in content-strategy.json. Per 20 ideas: 12 education, 4 agents/tools/builds, 3 business operations, 1 founder journey. Classify each once. Log owner preferences separately from authentic authored samples and real publishing metrics. No engagement guarantee.

## Future authentic Donovin samples

1. Preserve the source export inside this project, with author/ID/date/format/source URL and collection provenance. Review authorship, remove third-party quoted text, exclude generated/assisted material from unaided voice measurements, and mark each accepted record with `author_id: "donovin-sims"`, `verified_original: true`, `source_url`, stable `id`, valid `date`, and `text`. Do not infer original authorship from style.
2. Record the verification in data/source-audit.json.
3. Ingest to staging, never directly overwrite the active dataset during a first review:
```sh
python3 voice-clone/scripts/ingest.py samples/donovin-originals.json --author-id donovin-sims --out staging/donovin-sims/data --merge voice-clone/profiles/donovin-sims/data/corpus.jsonl
```
The input above is a future user-supplied file, not included synthetic data. The gate rejects mixed authors, missing provenance and marked generated text. It relies on truthful reviewed metadata; it cannot prove authorship. Generic historical ingestion remains available without the Donovin profile path/author flag.
4. Review per-format counts, dropped records, holdouts and missing metrics. The script measures formats only at 5+ non-held-out samples. Counts alone do not prove fidelity. Preserve old snapshots, then promote reviewed own corpus/stats together with source audit, manifest and YAML counts. Use [Voice Analyze](integrations/voice-analyze/SKILL.md).
5. Keep Corey measurements and source archives separate. Never ingest validation/ or owner-approved AI drafts as authentic originals. Actual publishing performance needs source URLs and capture dates.

## ChatGPT portable use

Run `python3 scripts/export_chatgpt.py`; upload exports/CHATGPT_CONTEXT.md to a ChatGPT Project. Paste Donovin_Sims_Brand_Profile/03_Donovin_Sims_Project_Instructions.txt into instructions. Supply the audience, topic, format and authorized facts in a brief. The context file embeds curated guidance, so a model does not need to resolve local links to understand identity and style.

If Python is available, the bundle supports manual drafting but does not carry the full originality corpus. For full checks, save the draft inside this project and run the commands above. Disclose checks that were unavailable. Regenerate the bundle after accepted profile changes. Do not upload docs/canonical or the adjacent business reference as public ghostwriting context by default.

## Draft history and originality

The active manifest routes a separate `data/draft-history.jsonl` ledger. It stores generated drafts, owner-approved edits and owner-verified published records with independent authorship labels. It is never ingested automatically or counted as authentic original writing.

Run editorial and overlap checks before recording a delivered draft:

```sh
python3 voice-clone/scripts/retrieve.py overlap --draft-file drafts/current/post.txt --strict --json
python3 voice-clone/scripts/retrieve.py record --draft-file drafts/current/post.txt --category practical_education --hook-pattern walkthrough
```

Overlap adds draft history to reference and own corpora. It reports contiguous shared words, five-word sequences, exact sentence candidates of at least five words and high lexical similarity (cosine >= 0.8). These are review heuristics, not semantic or plagiarism verdicts. Inspect ideas, progression, substituted nouns and personal stories manually. Recent repeated openings or a pattern used in at least three of the last five distinct saved texts also prompt review; repetition is not an automatic writing failure.

For a revision, `--exclude-draft-id ID` omits only that saved version. Other history stays in scope. For a batch, `overlap --draft-files A.txt B.txt --strict --json` compares each against earlier batch members as well. Check before appending new records to avoid self-matches.

Use `record --status approved_edit --approved-by-owner --authorship AI_assisted --parent-id ID ...` only after actual approval. Use `--status published --verified-published --source-url ACTUAL_POST_URL --date ISO_DATE ...` only with reviewed publication evidence. These attestations do not authenticate original authorship. Real original writing still uses the separate Voice Analyze/ingestion source gate. Never auto-update important brand, identity or position rules from reference examples or draft approval.

Earlier generated validation drafts are recorded as generated solely for duplicate review; they are not performance evidence or calibration samples.

For active source examples in ChatGPT, attach a topic-specific research.json packet alongside exports/CHATGPT_CONTEXT.md. Alternatively attach the existing original Corey corpus file when code/file analysis is available, follow the same retrieval rules, and exclude holdouts. Do not duplicate the full corpus or paste it into a prompt. If retrieval is unavailable, disclose the limitation.
