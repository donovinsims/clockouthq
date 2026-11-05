# Validation

A profile isn't done because it reads well. Check four things.

## 1. Voice fidelity (blind test)

1. Use the 10 held-out posts. They're flagged `holdout` in `corpus.jsonl` and excluded from measurements and retrieval.
2. Write 10 new posts with the profile, on topics the person really posts about, across the formats they use.
3. Shuffle all 20. Remove anything that gives away which is which, including formatting differences.
4. Have an **independent judge** guess which 10 are real. Independent means not the writer and not holding the profile: the creator, a regular reader, or a fresh Claude chat given only the 20 posts and the question. In Claude Code, a subagent works.

Pass: the judge does no better than about 60%, and no single tell gets flagged twice.

## 2. Originality

Run `scripts/retrieve.py overlap` on every draft. Any flag means rewrite. Ideas should be new, not remixed.

## 3. Accuracy and no invention

Audit each draft. List every personal story, number, result, client, date and stance. Each must trace to something the user supplied or to the experiences ledger and stances in `positions.md`. Anything that doesn't gets removed, replaced with a placeholder for the real detail, or flagged.

## 4. Performance

Voice can't tell you whether a post works. After posts are published, compare their results to baseline (see `learning.md`) and update the engagement hypotheses.

## When the blind test fails

Ask the judge why they picked each one. Each reason is one of four things:

| The tell was... | Fix it in... |
|---|---|
| A rhythm, length or punctuation habit | `lexicon.md` |
| A way of thinking or arguing | `positions.md` or `voice-dna.md` |
| A generic AI pattern | `voice-dna.md` "Never" list, and `references/ai-tells.md` if universal |
| Missing feel for a kind of post | add a closer example to `top-posts.md` |

Retest with fresh posts, not the same 10. Two rounds is the cap on a first build. After that, ship the profile and let real use and edits find the rest.
