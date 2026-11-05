# Editorial Quality Checklist | Corey Ganim X

Use this as the final human/editor pass. Each item is a **check**, not a promise of authenticity or virality.

## 1. Audience and purpose
- [ ] This draft is for **AI service operators** *or* **business owners**, not both by accident.
- [ ] The reader gets one concrete idea, technique, diagnosis or informed opinion.
- [ ] Any call to action directly fits an active, authorized offer, or is omitted.

## 2. Fact and identity controls (publication blockers)
- [ ] Every first-person client story, "I built", "I made", revenue number and claimed outcome has a verified source and applicable date.
- [ ] Distinguish Corey-reported historical results from independently verified facts. Avoid treating prices and platform features as current by default.
- [ ] No fabricated screenshots, results, quotes, personal experiences, endorsements or named relationships.
- [ ] Any 2026+ tool/product claim requiring freshness has been verified or phrased as a dated observation.
- [ ] Attribution and publishing are authorized by the creator; absent authorization, label as **style-informed draft**.

## 3. Voice match (use actual profile, not generic stylistic bans)
- [ ] Opening is direct and supported, not a generic "here's why" setup.
- [ ] Details are specific where warranted: buyer, problem, mechanism, time/cost and practical next action.
- [ ] Sentence and paragraph lengths vary naturally; line breaks, numbering and casing are format-appropriate.
- [ ] Contractions, ordinary spoken language and occasional sharpness appear when appropriate, not artificially on every line.
- [ ] No default em dashes, hashtag packs, decorative emojis or thoughtless question endings.
- [ ] Signature phrases are occasional, not required; the draft does not recycle another post's signature line.
- [ ] Language has a real argument or tradeoff, rather than templated hype or forced contrarianism.

## 4. Ghostwriter AI-tells review (heuristic, never blanket veto)
- [ ] Replace empty boilerplate ("in today's fast-paced world", "unlock your potential", "game-changer") where present.
- [ ] Remove fabricated numerical precision, stacked superlatives and empty suspense.
- [ ] Avoid repeated "It's not X, it's Y", tidy three-part maxims and symmetrical bullet rhythms unless the specific draft actually calls for them.
- [ ] Keep authentic domain language: `optimize`, `framework`, `roadmap` and `leverage` are **not automatically forbidden**.
- [ ] Do not assume an AI detector or banned-word list proves human authorship.

## 5. Originality and performance
- [ ] Retrieve non-holdout typical + stronger reference posts for the same **format**.
- [ ] Run: `python voice-clone/scripts/retrieve.py overlap voice-clone/profiles/corey-ganim/data/corpus.jsonl --draft-file draft.txt`.
- [ ] Any overlap warning is resolved by rewriting, not by swapping two synonyms.
- [ ] Never use the 10 held-out originals while drafting or tuning the blind test.
- [ ] Judge voice separately from response/engagement: high engagement has multiple causes.
- [ ] Log only user-approved edits and actual measured results in `voice-clone/profiles/corey-ganim/learning-log.md`.

## Decision
**PASS** only after factual, originality, and attribution checks. Style concerns trigger a revision, not false factual claims. A passing checklist is still not proof that a draft is indistinguishable from Corey's writing.
