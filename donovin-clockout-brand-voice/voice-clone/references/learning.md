# Learning Loop

A profile gets better from three inputs: editorial corrections, new posts, and real performance.

## 1. Editorial corrections

Whenever the creator edits a draft, add a row to `learning-log.md`: what the draft said, what they changed it to, and why if they said. Edits are the best data this system gets.

After 3 similar edits, turn the pattern into a rule: lexicon (rhythm, words), voice-dna (thinking, never-list) or positions (stance, ledger). One edit is an anecdote. Three is a rule.

Only approved edits count. If a change was a one-off for a specific post, don't generalize it.

## 2. New posts (refresh)

Scrape only posts newer than the last scrape, then merge:

```
python scripts/ingest.py new.json --out profiles/[name]/data --merge profiles/[name]/data/corpus.jsonl
```

The merge keeps existing holdout posts, dedupes by id, and re-scores everything against the updated baseline. Refresh about every 30 new posts. After a refresh, check whether voice or topics have drifted, and update `lexicon.md`, `positions.md` and `hooks.md` where the data says to.

## 3. Performance

After 48 hours or a week, record how each published post did against baseline: perf multiple, format, hook type, topic. Add it to `learning-log.md`.

Update hypotheses carefully:

- A hook type or topic that beats baseline across 3+ posts moves up in confidence
- One good or bad result changes nothing
- If a post that followed the profile flopped, record it as data, not as a bug in the voice

## 4. Keep the files honest

Every rule carries a count and a date. When new data contradicts a rule, change the rule. Leave a short note in the log so the change is traceable.
