# Engagement Intelligence

Goal: learn what resonates with this creator's audience, and why, without relying on generic viral templates.

## Judge against the creator's own baseline

`ingest.py` already scores every post as a multiple of the creator's typical performance within +-45 days (`perf`). A 3.0 means three times their norm for that period. Use `perf`, not raw likes, because:

- Audience growth makes old posts look weak and new posts look strong
- Topics, timing and distribution (a big account reposting it) swing results
- One outlier can distort the picture, so look for patterns across several top posts, not one

## Each format has its own baseline

Threads, articles, long posts and quote posts perform on different scales than short posts, so `ingest.py` scores each format against its own baseline. A format with fewer than 10 posts (usually threads and articles) can't be fairly ranked, so it's scored roughly against all posts and tagged `unranked`. For those, treat `perf` as directional only. Judge thread and article quality by reading them against the creator's strongest examples, not by the number. Thread posts are scored one post at a time, and the first post usually carries most of the reach, so don't compare later posts in a thread to standalone posts.

## Compare three groups

Pull `tier=top`, `tier=typical`, `tier=weak` from `corpus.jsonl`. For each dimension, compare how often it appears in each group:

- **Topic and angle:** what subjects and stances show up in top posts and are absent from weak ones
- **Hook type:** number, bold claim, scene, question, contrarian flip, confession, observation
- **Specificity:** real numbers, names, places, scenes
- **Length and shape:** words, line breaks, list vs prose
- **Format:** short, long, thread, quote post
- **Tension:** is there a contrast, a surprise, a cost, a reversal?
- **Ending:** stop vs lesson vs question
- **Timing and media:** only if the data shows a real difference

Only keep a finding if it shows up in at least 3 top posts and is meaningfully rarer in weak ones. State it as a hypothesis with confidence (high, medium, low).

## What to record

- **hooks.md:** hook types with the pattern (not exact lines), how often each appears, and how each performs against baseline
- **Topics that spike and topics that don't**
- **top-posts.md:** a curated set with `perf`, format and a one-line "why it worked"
- **flops.md:** only if the weak posts share something. If they're just slightly worse versions of good posts, say so and delete the file.

## Two warnings

- **Don't confuse style with resonance.** A post can be perfectly on-voice and weak because the idea is weak. Record resonant topics and structures separately from voice rules.
- **Don't promise results.** These are patterns from past posts. They raise the odds, they don't guarantee anything. Test them (see `learning.md`) and update.
