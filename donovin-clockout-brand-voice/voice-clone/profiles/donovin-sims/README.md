# Donovin Sims active voice profile

This is the default operational profile. It combines three explicitly separate layers:

- **Identity and adopted positions:** [facts.md](facts.md), [positions.md](positions.md), and the [brand profile](../../../Donovin_Sims_Brand_Profile/README.md).
- **Corey-derived style guidance:** [voice-dna.md](voice-dna.md), [lexicon.md](lexicon.md), [hooks.md](hooks.md), and [top-posts.md](top-posts.md). The original [Corey research](../corey-ganim/README.md) retains authorship, corpus, measurements and performance snapshots.
- **Future authentic Donovin writing:** [data/corpus.jsonl](data/corpus.jsonl), initially empty; [data/stats.json](data/stats.json) explicitly records no measurements. Synthetic drafts live under root validation/, never in training data.

[donovin-voice-profile.yaml](donovin-voice-profile.yaml) uses JSON syntax, a valid YAML 1.2 subset, so standard-library scripts can read it without new dependencies. [manifest.json](manifest.json) routes own and reference corpora. [learning-log.md](learning-log.md) separates editorial preferences from genuine authored samples and measured performance.

Run commands from the project root:
```sh
python3 voice-clone/scripts/retrieve.py search "repetitive office tasks" --profile donovin-sims --format long -k 3
python3 voice-clone/scripts/retrieve.py overlap --profile donovin-sims --draft-file drafts/current/post.txt
python3 scripts/check_draft.py --format long --draft-file drafts/current/post.txt
```

See [WORKFLOW.md](../../../WORKFLOW.md) for collection, provenance, separate ingestion and review.

## Active reference intelligence

Use retrieve.py brief to prepare 3-6 balanced attributed examples with structure/technique cues, source quality, provenance, archive pointers and historical performance context. The manifest routes the source library and a separate nontraining draft-history.jsonl. Original own writing, generated drafts, approved edits and verified published records retain distinct roles. See the root WORKFLOW.md and Voice Apply skill.

Run draft-check examples after saving a fresh post to drafts/current/post.txt. For a saved revision, exclude only its own ledger record ID; other history remains in scope.
