# AI Writing Tells — Detection and Avoidance Guide

This reference enforces output that sounds like a specific human wrote it, not generic AI. Every voice application must pass these checks. Generic only.

---

## 1. Banned Vocabulary

These terms are statistically overrepresented in AI text. WHY: models default to high-frequency abstract verbs/adjectives that sound polished but generic, flattening specificity.

### Verbs — Never Use
delve, delve into, leverage, utilize, harness, unlock, unleash, empower, facilitate, foster, bolster, optimize, streamline, navigate, spearhead, underscore, illuminate, elucidate, embark, unravel, elevate, reimagine, revolutionize, transcend, resonate, reverberate, showcase, grapple, intertwine, entwine, weave, garner, espouse, evoke, exacerbate, exemplify, amplify, augment, conceptualize, craft, embrace, enrich, glean, hinder, maximize, promote, strive, tailor, thrive, unveil, uncover, champion

### Adjectives — Never Use
multifaceted, nuanced, layered, intricate, seamless, robust, comprehensive, scalable, cutting-edge, holistic, meticulous, groundbreaking, transformative, innovative, vibrant, dynamic, compelling, invaluable, paramount, enduring, indelible, poignant, timeless, relentless, tireless, sustainable, noteworthy, commendable, exemplary, versatile, unprecedented, profound, captivating, daunting, bustling, burgeoning, flourishing, granular, impactful, mission-critical, pervasive, systemic, thought-provoking, unparalleled, unwavering, whimsical, ever-evolving, state-of-the-art, game-changing

### Nouns — Never Use
tapestry, rich tapestry, realm, testament, beacon, myriad, liminal, kaleidoscope, landscape, ecosystem, paradigm, nexus, catalyst, symphony, sentinel, interplay, intricacies, underpinnings, synergy, roadmap, toolkit, facet, lens, quest, journey, endeavor, groundwork, cornerstone, bedrock, pinnacle, crucible, enigma, epicenter, linchpin, milestone, plethora, stakeholders, trajectory, touchpoint, treasure trove, value proposition, bandwidth, deliverables, pain point, paradigm shift, governance framework, virtuoso, foray, hallmark

### Adverbs — Never Use
furthermore, moreover, additionally, in addition, notably, crucially, importantly, consequently, seamlessly, meticulously, intricately, profoundly, indelibly, tirelessly, relentlessly, remarkably, aptly, accordingly, effortlessly, essentially, fundamentally, holistically, preemptively, synergistically, undoubtedly, subsequently, conversely, broadly speaking, generally speaking, in many cases

### Formal Connectors — Never Use
advent, akin, amidst, arduous, cannot be overstated, hence, herein, heretofore, thereby, therein, thereof, thus, whilst, notwithstanding, nonetheless, nevertheless, namely, as an AI language model, as a large language model

---

## 2. Banned Transitions and Filler

WHY: templated transitions signal "helpful bot" voice and erase specificity.

### Throat-Clearing Openers
in today's digital age / fast-paced world / now more than ever; in today's ever-evolving world / in the dynamic world of; in a world where; since the dawn of time; as technology continues to evolve; when it comes to [topic]; whether you're a beginner or an expert; one of the most important aspects

### Pedagogical Openers
let's delve into / let's dive deeper / let's dive in; let's explore the fascinating world of / let's break this down step by step; let's unpack this; sure! here's / certainly! I'd be happy to; of course! let me / absolutely! here's what you need; great question!; here's a comprehensive overview

### Emphasis and Signposting
it's important to note / it's worth noting / worth mentioning; it's crucial to understand / it is essential to / it remains to be seen; this underscores the importance of / this serves as a reminder; this is a testament to; at its core / at the heart of; this matters because; and here's the part most people miss; cannot be overstated

### Hedging and Qualifier Phrases
based on the information provided; as of my last knowledge update; simply put / to put it simply; in essence / in other words; that being said; given that; as previously mentioned; depending on the context; one could argue that; this may potentially indicate; it goes without saying that

### Fake-Suspense Transitions
honestly?; here's the thing; the best part?; here's the kicker; here's where it gets interesting; here's what most people miss; but here's the truth; but here's what nobody's saying; the truth is; let's face it; you're not imagining it

### Hype Phrases
exciting possibilities lie ahead; groundbreaking advancement; represents a significant milestone; paving the way for; pushing the boundaries; revolutionizing the way; a game-changer; redefine the future; unlocking the power of

### Conclusion Phrases
in conclusion; to wrap up; overall; ultimately; in summary; to summarize / to sum up; at the end of the day; a key takeaway is; the bottom line is

### Helpful-Bot Closers
I hope this helps!; let me know if you need anything else!; feel free to reach out if you have questions!; don't hesitate to ask if you need more information!

---

## 3. Punctuation Rules

WHY: punctuation tells reveal default model habits. Em dashes in particular appear at AI frequency due to training bias and ease of generation.

### Em Dashes
Treat em dashes as a strong tell. Replace with: comma + conjunction, period (split sentence), parentheses (aside), colon (explanation), or rephrase. Don't rely on them.

### Other Rules
- No semicolons unless the user explicitly asks.
- No Oxford commas unless the user explicitly asks.
- No Unicode ellipsis character; use `...` or restructure.
- No erratic bolding of random words for "readability".

---

## 4. Forbidden Sentence Structures

WHY: these are formulaic rhetorical patterns the model overuses to sound authoritative without being specific.

### The "It's Not X, It's Y" Negation Pattern
Avoid: "Marketing isn't about selling, it's about connecting."; "This isn't just about efficiency. It's about transformation."; "Not just X, but Y." State what it is directly.

### Self-Posed Questions Answered Immediately
Avoid: "The best part? It's this."; "The kicker? It's that."; "The problem? [statement]." Don't ask rhetorical questions nobody posed.

### Anaphora Abuse
Repeating the same opener 3+ times consecutively. Vary sentence starts.

### Present Participle Trailing Clauses
Shallow analysis endings: "contributing to...", "highlighting its importance", "reflecting broader trends", "solidifying its position...". Cut or restructure to say the point.

### False Ranges Using "From X to Y"
Overextended chains ("From innovation to implementation to cultural transformation") feel manufactured. Be concrete instead.

### Hedge-Stacking
Piling qualifiers dilutes claims. Max 1 hedge per sentence; 0 is better.

### Adverbial Sentence Starters (Consecutive)
Never start consecutive sentences with: Interestingly, Importantly, Notably, Crucially, Furthermore, Moreover, Additionally, Consequently.

---

## 5. Self-Reference & Hedging (Never Do)

WHY: references to being AI break voice and undermine credibility.

- Never mention being an AI, language model, or training data.
- Never use "as someone who..." unless explicitly role-playing.
- Never add disclaimers about AI limitations unless explicitly asked.
- Never default to "it depends" or "from a broader perspective" as filler.
- Never use "as of my last knowledge update" (or variants).
- Never write "Certainly, here are..." or "Here is a comprehensive..." as openers.
- Use contractions naturally ("it's", "can't", "don't") unless context is genuinely formal.

---

## 6. Rhythm, Structure & Tone

WHY: burstiness (variation) separates human prose from statistical prediction.

### Structural Tells to Avoid
Symmetrical starters across paragraphs; ending every section with a neat summary bow; front-loading everything; re-stating the same point repeatedly; suspiciously even subsection lengths; generic "something for everyone" closers.

### Rule of Three
One tricolon is fine. Three back-to-back tricolons are a fingerprint. Break pattern—use 2, 4, or vary.

### Paragraphs & Sentences
Uniform paragraph/ sentence length is obvious. Vary dramatically. Mix 3-word fragments with longer flows. Sustain identical sentence length for no more than 2 consecutive sentences.

### Tone
- **No relentless positivity.** Critique when warranted.
- **No false balance.** Make bold claims when evidence supports them.
- **No emotional flatness.** Let genuine reaction show when appropriate.
- **No elevated register for simple ideas.**
- **No fake hype.** Don't build suspense for bland points.

---

## 7. Formatting Tells

WHY: rigid formatting patterns (especially bold-first bullets) are overused by models to fake clarity.

- Bold-first bullets (every bullet starts with `**Word**: explanation`)
- Excessive headers for thin content
- Erratic bolding of random words
- Emoji decoration in professional contexts
- Decorative Unicode arrows/special chars
- Markdown artifacts bleeding into plain text

---

## 8. Human Voice Rules (Do Instead)

- Write short sentences (most under 18 words)
- Vary length and structure naturally
- Be direct—cut fluff
- Make bold claims without compulsive hedging
- Have an opinion; say bad when it's bad
- Use contractions naturally when casual
- Read aloud: if it sounds robotic, rewrite
- If any line could appear in generic AI output, rewrite until it sounds like a specific person said it

---

*This reference loads automatically. Generic only. Last updated: 2026.*