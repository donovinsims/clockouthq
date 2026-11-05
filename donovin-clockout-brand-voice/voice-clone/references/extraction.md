# Extraction: Creator Intelligence

Goal: turn the corpus into rules you can check, plus an understanding of how this person thinks. Work in passes. Don't write a rule until you've counted.

## Pass 0: Run the ingest script

`python scripts/ingest.py RAW --out profiles/[name]/data` gives you `stats.md` (all the measurements), `corpus.jsonl` (cleaned, scored, searchable) and held-out posts. Never measure by eye when the script can count. Hand-count only if code can't run, and say it's a sample.

## Pass 1: Read once, no notes

Read 30 to 40 posts spread across tiers and dates. What does it sound like out loud? Write one sentence about their temperature (dry, warm, aggressive, tired, hyped). You'll test it later.

## Pass 2: Fingerprint (feeds lexicon.md)

Take the numbers from the per-format sections of `stats.md` (never the blended section, which is reference only). A creator's short posts, threads and articles have different rhythm, so record each format's numbers separately. Formats with under 5 posts can't be measured, so read those directly. Then add what a script can't see: slang, jargon, odd word choices, the feel of their rhythm.

Rule of thumb on evidence: a pattern in 60%+ of posts is a rule. 20 to 60% is a tendency, so state the frequency. 10 to 20% is a quirk, use sparingly. Under 10%, leave it out.

Check drift. If the style changed over time, build from the last 6 to 12 months and say so.

## Pass 3: Absences (feeds the "Never" lists)

List what a typical creator does that this person never does: question hooks, emoji, closers, lists, hashtags, follow requests, hedging, self-deprecation. Absences identify a voice faster than habits.

## Pass 4: Thinking DNA (feeds positions.md)

This is what makes a ghostwriter feel like the person and not a mimic. Answer from the posts, with example post ids:

- **Expertise:** what do they clearly know deeply? What do they only touch on?
- **Stances:** what do they believe, and what do they push against? Record each as claim, evidence posts, strength.
- **Recurring arguments:** the 3 to 6 ideas they keep returning to.
- **How they build an idea:** claim then proof, story then lesson, contrarian flip, list of observations, question that resolves? Most creators have two or three patterns.
- **Audience:** who they talk to, and how they address them.
- **Humor and vulnerability:** type, frequency, what they're willing to joke or open up about.
- **Numbers:** exact, rounded, or never.
- **Experiences ledger:** the real stories, clients, results and events they've actually told. This is the only source of personal experience a ghostwriter may use.
- **Off-limits:** topics they avoid, opinions they've said they don't hold.

If a stance has fewer than 2 supporting posts, mark it "thin" and don't extrapolate from it.

## Pass 5: Engagement and contrast

Follow `references/engagement.md`.

## Write the profile

Copy `profiles/_template/` and fill each file. Every rule: what, why, count, real example. If a section has nothing true to say, delete it.
