# Ghostwriting Engine

How to turn a request into a post that sounds like the creator, thinks like the creator and is built like their best work.

## 1. Understand the brief

Get: topic or idea, goal (reach, authority, leads, community), format (short, long, thread, article, quote post, reply), and any real material the user can supply (a story, a number, a result, a link).

If the post needs a personal experience or fact and none was supplied, check the experiences ledger in `positions.md`. If it isn't there, ask for the real detail, or write the post as an observation or opinion. Never invent one.

## 2. Fit check

Compare the topic to the creator's expertise and stances in `positions.md`.

- **In their lane and aligned with a known stance:** proceed.
- **In their lane but no stated stance:** write it as a question, an observation or a hedge they'd actually make, and flag that the stance is new.
- **Outside their lane or against a known position:** say so and ask the user before writing.

## 3. Find the angle

An original idea built from their worldview, not a remix of old posts. Choose how this creator builds ideas (see "How they build an idea" in `positions.md`) and a hook type that performs for them (`hooks.md`). The idea should be new. The construction should feel familiar.

## 4. Retrieve examples

Run retrieval twice against `corpus.jsonl`:

```
python scripts/retrieve.py search data/corpus.jsonl "<topic in plain words>" -k 6
python scripts/retrieve.py search data/corpus.jsonl "<hook type or structure>" -k 6 --tier top --format short
```

The first finds how they talk about the subject. The second finds posts built the way you want to build this one. Read 5 to 8 results. Use them to calibrate voice and structure. Don't reuse their sentences or their content. Holdout posts are excluded automatically.

## 5. Draft three variants

Three different hooks or structures, written fast. Vary format and opener across variants so you aren't producing one idea three times.

## 6. Pick and refine

Choose the strongest. Refine against `lexicon.md` (rhythm numbers, casing, punctuation, signature phrases at natural frequency). Keep the flaws the corpus shows. Then run the `references/ai-tells.md` pass.

## 7. Check originality

```
python scripts/retrieve.py overlap data/corpus.jsonl --draft-file draft.txt
```

If it flags 8 or more words in a row or heavy 5-word overlap, rewrite. Reusing the creator's own old lines is still copying.

## 8. Deliver with flags

Give the post, then a short note covering:

- Details the user needs to confirm or supply
- Any stance that's new or stretched
- Which hook type it uses and why that fits this creator
- Alternatives, if useful

Don't claim it will go viral. Say what it's built on.

## Formats beyond the single post

For threads, articles, quote posts and replies, apply `references/formats.md`, and retrieve examples of that specific format first, because the same person writes differently in each.
