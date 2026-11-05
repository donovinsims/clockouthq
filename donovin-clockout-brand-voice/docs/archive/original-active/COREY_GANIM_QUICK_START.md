# Corey Ganim X Writing Profile: Quick Start

The reusable skill is in `SKILL.md`, with the creator-specific learned profile in `profiles/corey-ganim/`.

## What was built

- A cleaned, deduplicated author corpus with 405 unique original posts in `data/corpus.jsonl` and a separate provenance audit.
- Quantitative voice fingerprints by format, source-grounded beliefs and experience ledger, engagement hypotheses, and curated examples.
- Ten synthetic drafts with an originality overlap test. No external blind-style judge has evaluated these drafts.
- Source archives for 10 threads and 12 articles, plus ingest and retrieval scripts.

## How to use with an AI assistant that can read local files

Give the assistant access to the extracted `voice-clone/` directory and this writing brief:

```text
Use voice-clone/SKILL.md in Mode 2 with the creator profile in voice-clone/profiles/corey-ganim/. Read voice-dna.md, lexicon.md, positions.md and hooks.md. Retrieve relevant examples from data/corpus.jsonl, including typical and top posts. Write three original candidate posts on the topic I supply, select the strongest, and validate both voice and originality with scripts/retrieve.py. Do not reuse existing post wording or invent real personal experiences, named clients, current results or tool capabilities. Treat the output as style-informed drafting, not content approved or written by Corey Ganim, and flag anything that needs factual confirmation.
```

For a first test, provide an actual topic or verified source material. For business copy, specify the intended audience and whether to publish as your own or under explicit creator authorization. For source-grounded writing, the real example is more important than hype.

## Running from the extracted folder

```bash
python scripts/retrieve.py search profiles/corey-ganim/data/corpus.jsonl "local business AI" -k 8
python scripts/retrieve.py search profiles/corey-ganim/data/corpus.jsonl "business opportunity" -k 6 --tier top --format quote
python scripts/retrieve.py overlap profiles/corey-ganim/data/corpus.jsonl --draft-file my-draft.txt
```

The skill accepts new creator data through `scripts/ingest.py`, but `data/normalized-input.json` was prepared from multiple attachment formats. Re-ingest only after reviewing changes and keeping provenance. Replies were not sufficiently represented to train or validate a reply-specific voice.
