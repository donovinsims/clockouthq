---
name: voice-clone
description: "Turn a creator's scraped X content into a reusable ghostwriting system: posts, threads, articles, quote posts and replies that sound like them, think like them and are built the way their best content is built. Use when building a voice profile from scraped posts, writing new content as a person who has a profile, or logging edits and new results to improve a profile. Triggers on: build voice profile, write as [name], ghostwrite, clone voice, sound like me, match my voice, refresh the profile, log my edits. Produces: a profile folder with data, or drafts that pass originality, accuracy and voice checks."
---

# Voice Clone

Most AI ghostwriting fails the same way. The post is competent, tidy and anonymous. Readers can't say why, but they scroll past, because it reads like the average of the internet and not like anyone.

Matching vocabulary isn't enough either. A real ghostwriter does three things: sounds like the person, thinks like the person, and builds posts the way that person's best posts are built. This skill does all three from the person's own history.

The skill is universal. The learned voice is personal. Every profile lives in its own folder, and voices, data and corrections never mix.

No pack can promise perfect indistinguishability or virality. Those are targets to test against, never claims to make to the user.

---

## Why Default AI Fails

- **It writes the mean.** "A viral X post" returns the most common phrasing of every viral post, which is the opposite of a person.
- **It's too clean.** Fragments, uneven rhythm and odd casing are the voice. Polishing them out kills the clone.
- **It's specific about nothing.** "A founder I know" is the loudest tell. People use the real detail.
- **It invents.** Models fabricate stories and opinions to make a post work. A ghostwriter who does that gets the creator in trouble.
- **It dumps or ignores.** Pasting hundreds of posts into context drowns the signal. Ignoring them loses the voice. The fix is retrieval.

---

## The Five Stages

| Stage | What happens | Where |
|---|---|---|
| 1. Ingest | Clean scraped posts, score each against the creator's own baseline, measure the voice | `scripts/ingest.py` |
| 2. Creator intelligence | Extract fingerprint, thinking, stances, real experiences | `references/extraction.md` |
| 3. Engagement intelligence | Learn what resonates with THIS audience, from top vs typical vs weak | `references/engagement.md` |
| 4. Ghostwriting engine | Develop an original idea, retrieve examples, draft, refine | `references/ghostwriting-engine.md` |
| 5. Validate and learn | Test voice, originality, accuracy, performance; fold in feedback | `references/validation.md`, `references/learning.md` |

---

## Three Modes

### Mode 1: Build a profile

Don't skip the explore step.

1. **Ingest.** Run `scripts/ingest.py` on the scraped file with `--out profiles/[name]/data`. It cleans, separates replies, scores every post against the creator's baseline, tags top/typical/weak, holds out 10 posts for the blind test and measures the voice separately for each format. Read the report. Tell the user the counts and gaps.
2. **Check corpus size.** Under 40 originals: preliminary profile, label every rule low-confidence. 40 to 150: working profile. 150 to 300: strong. 300+: style measurements stop improving, but retrieval gets better topic coverage.
3. **Explore.** Write 3 posts as this person with no guidance, on topics they actually post about. Show the user and list every spot that sounds fake. These failures become "why default AI fails for this person."
4. **Extract and interpret.** Follow `references/extraction.md`, then `references/engagement.md`. Measure first, then interpret.
5. **Write the profile.** Copy `profiles/_template/` to `profiles/[name]/` and fill each file from evidence, with counts and real examples. Delete any file that has nothing true to say.
6. **Validate.** Run `references/validation.md`. Two rounds max on a first build.

### Mode 2: Write as [name]

Follow `references/ghostwriting-engine.md`. In short: understand the brief, check the topic against the creator's real stances, find an original angle, retrieve relevant real posts with `scripts/retrieve.py`, draft three variants, refine, check originality and accuracy, deliver with flags.

Always load `voice-dna.md`, `lexicon.md` and `positions.md`. Load `hooks.md` and `references/formats.md` for the format. Never load the whole corpus. Retrieve.

If code can't run (no code execution), fall back to `top-posts.md` and search it by eye.

### Mode 3: Learn

Follow `references/learning.md`. Log editorial corrections, record how published posts performed against baseline, and refresh the profile with newly scraped posts using `--merge`.

---

## Core Principles

**1. Examples beat adjectives.** The model imitates what it sees. One real post teaches more than a paragraph of tone description. Every rule ships with a real example.

**2. Measure, then interpret.** Numbers anchor the clone. Interpretation lets it handle topics the corpus never covered. They live in separate files so neither drowns the other.

**3. Typical posts carry the voice. Top posts carry the virality.** Hits are the person on their best day. Build from both.

**4. Performance is relative to the creator's own baseline.** A post with 5,000 likes from an account that normally gets 8,000 underperformed. Audience size, timing, topic and distribution all move raw numbers, so judge posts by how they did against that creator's norm at that time.

**5. What they never do identifies them more than what they do.** Hunt for absences.

**6. Signature phrases are seasoning.** A phrase in 4 of 30 posts belongs in about 1 of 8 drafts, not all of them.

**7. Think like them, not only sound like them.** Know their expertise, worldview, recurring arguments and how they build an idea. A draft with the right voice and a stance they'd never take is a miss.

**8. Original ideas, borrowed construction.** New posts argue new points built from the creator's worldview. Retrieved posts teach voice and structure. Never remix old posts, and run the overlap check.

**9. Never invent.** No personal stories, results, numbers, clients or opinions the creator hasn't expressed or supplied. If a post needs one, ask for the real one, or write it as an observation instead of an experience.

**10. Keep the flaws.** Lowercase starts, fragments, a missing period. If it's in the corpus at a real frequency, it's the voice.

**11. Authorization.** Build profiles for yourself or for creators who've authorized you. When emulating someone's style for your own account, copy patterns and structure, never their lines, and never imply they said it.

---

## Anti-Patterns

- Describing the voice in adjectives instead of showing examples
- Building from under 20 posts without labeling the profile thin
- Ranking posts by raw likes instead of baseline-relative performance
- Using only top posts, so the clone has no everyday register
- Blending two people into one profile
- Pasting the whole corpus into context instead of retrieving
- Treating every AI tell as banned: if this person really uses one, it's theirs
- Stuffing every signature phrase into every post
- Inventing stories, stats or stances
- Skipping the explore step, the originality check or the blind test

---

## Before / After

Illustrative only: a made-up profile for a blunt, lowercase founder who writes short and ends without a lesson.

**Default AI:**
> Here's the thing about building in public: consistency beats talent every time. 🧵
> Here are 5 lessons I learned in my first year...

**Written from a profile:**
> shipped 3 days late again.
> told the client the truth. they said "ok." that's it. that's the whole story.
> i spent 3 days dreading a 4 second conversation.

What changed: the opener is a plain event, not a claim. The contrast is the point. No moral, no emoji, no list promise, and the sentence lengths are uneven.

---

## Quality Checklist

Before delivering any post:

- [ ] Opens the way this person opens, per their hook types?
- [ ] Rhythm and line breaks match the lexicon numbers?
- [ ] Argues something this person actually believes (positions.md)?
- [ ] Every story, number and claim traces to the user's input or the corpus?
- [ ] Overlap check passed (nothing copied from their old posts)?
- [ ] No AI tell the person doesn't actually use?
- [ ] Ends the way they end, not with a neat moral?
- [ ] Would their regular readers scroll past it thinking "that's not them"?

The last one matters most. Read it as someone who follows this person daily.
