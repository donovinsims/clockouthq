---
name: voice-apply
description: "Applies a voice profile to transform content. Use when user asks to write in a specific voice, match a tone, apply a style, or transform content to sound like a particular voice profile."
version: 1.1.0
platforms: [all]

---

# Voice Apply Skill

## Opener

Voice isn't style. It's identity. The difference between output that reads generic and output that reads human isn't word choice alone—it's consistency under pressure. This skill forces that consistency by transforming content to match a target voice while stripping every trace of AI handwriting.

## Why It Fails Without This Skill

Default output falls back to safe, statistical phrasing. Without constraints, it defaults to hedged claims, overused transitions, and templated vocabulary. The result sounds like "any AI" instead of a specific voice. Every unconstrained generation drifts toward the mean—polished, impersonal, and immediately recognizable as machine-written.

## Core Principles (With WHY)

1. **Voice is a system, not a list.** A voice profile is a set of tradeoffs (formality vs warmth, confidence vs nuance). Treating it as isolated word swaps creates inconsistency. WHY: Systems force decisions under pressure; lists don't.

2. **Elimination beats decoration.** Removing AI tells does more for authenticity than adding "human" phrases ever will. WHY: AI fingerprints come from overuse patterns, not from missing color.

3. **Specificity beats generality.** A concrete claim in the target voice lands harder than vague praise. WHY: Specificity forces natural phrasing and breaks templated constructions.

4. **Tradeoffs, not perfection.** Authentic voices acknowledge tension—constraints, uncertainty, or downsides when warranted. WHY: Relentless positivity reads synthetic. Honest tradeoffs read human.

5. **Burstiness is required.** Sentence length must vary. Paragraph length must vary. Rhythm must breathe. WHY: Statistical uniformity is one of the strongest AI tells.

6. **Apply last, verify always.** The AI tells elimination pass must run after voice application—never before. WHY: Transformation can reintroduce patterns; only a final pass guarantees they stay gone.

## When This Skill Applies

- User asks to "write in X voice" or "use Y tone"
- User wants to "make this sound more [casual/formal/technical/etc.]"
- User provides content and asks to transform its style
- User references a voice profile by name
- User wants content to match a specific audience/context

## Frameworks

### 1) Load Voice Profile
Check locations in order: project `.aiwg/voices/`, user `~/.config/aiwg/voices/`, built-in `voice-framework/voices/templates/`. Load the named profile (YAML). If blending, compute weighted values per field before applying.

### 2) Analyze Source Content (if transforming)
Identify gaps vs. target: tone, vocabulary, sentence/paragraph structure, narrative perspective. Focus on deltas, not a full rewrite of everything.

### 3) Apply Voice Characteristics
- **Tone calibration:** formality, confidence, warmth, energy. Adjust at the sentence level, not globally.
- **Vocabulary:** apply `prefer`/`avoid` deliberately; introduce domain terms naturally without forcing jargon.
- **Structure:** shift sentence/paragraph length to match target rhythm; adjust lists/examples only when they serve clarity.
- **Perspective:** set person (I/we/you/they) and reader relationship to match target.

### 4) AI Tells Elimination Pass (MANDATORY)
Run every output through `references/ai-tells.md`. Remove banned vocabulary, transitions, structures, punctuation violations, rhythm uniformity, formatting tells, and self-reference. Fix them by rewriting, not masking.

### 5) Verify Authenticity Markers
Check for warranted uncertainty, tradeoffs, specific numbers, and real constraints where relevant. Only include what fits the voice.

### 6) Final Read-Aloud Test
Read the output aloud (mentally). If any sentence could appear in any other AI-generated text, rewrite until it sounds like a specific person said it.

## Built-in Voice Profiles

| Profile | Description | Best For |
|---|---|---|
| `technical-authority` | Direct, precise, confident | Docs, architecture, engineering |
| `friendly-explainer` | Approachable, encouraging | Tutorials, onboarding, education |
| `executive-brief` | Concise, outcome-focused | Business cases, stakeholder comms |
| `casual-conversational` | Relaxed, personal | Blog posts, social, newsletters |

## Usage Examples

### Apply Named Voice
**Input request:** "Write release notes in technical-authority voice"
- Load profile, generate with precise terms, specific versions, direct claims, tradeoffs where relevant.
- Run mandatory elimination pass. Deliver clean output.

### Transform Existing Content
**Before:** "The API endpoint accepts a JSON payload containing the requisite parameters..."
**After:** "To use this endpoint, send it JSON with the info it needs..."
Process: analyze, transform to target, eliminate AI tells.

### Calibrate Voice
**Request:** "This is too formal, dial it back 30%"  
Target formality = current - 0.3. Adjust vocabulary and structure accordingly, then verify.

### Voice Blending
**Request:** "70% technical-authority, 30% friendly-explainer"  
Weighted merge of profile fields, apply merged profile, run elimination pass last.

## Anti-Patterns

- **Swapping words only.** Replacing "utilize" with "use" while keeping templated transitions still reads AI.
- **Running passes out of order.** Doing elimination before transformation almost guarantees reintroduction.
- **Over-applying jargon.** Forcing terms breaks natural rhythm; introduce only when useful.
- **Template positivity.** Forcing relentless optimism erases credibility.
- **Hedge-stacking.** Multiple qualifiers in one sentence dilute confidence without adding nuance.
- **Negation formula.** The "It's not X, it's Y" pattern is a major tell—rewrite to state what it is directly.

## Before/After

**Before (AI-default):**
> "It's important to note that this approach leverages robust mechanisms to optimize outcomes."

**After (clean, specific):**
> "This approach cuts overhead by focusing on the constraints that matter most."

**Before (template):**
> "This isn't just about efficiency—it's about transformation."

**After (direct):**
> "This change shifts the bottleneck from speed to coordination."

## Checklist

- [ ] Correct voice profile loaded (or blended weights calculated)
- [ ] Source analyzed; deltas identified (if transforming)
- [ ] Tone/vocab/structure/perspective applied to match profile
- [ ] **AI tells elimination pass completed** against `references/ai-tells.md` (non-negotiable)
- [ ] Banned vocab, transitions, structures, punctuation fixed
- [ ] Rhythm varies (sentence/paragraph length, burstiness)
- [ ] Tradeoffs/uncertainty included only where warranted
- [ ] No self-references (AI/LLM/disclaimers) remain
- [ ] Read-aloud passes: no sentence could be from generic AI output
- [ ] Output matches target voice consistently end-to-end

## References

- AI Writing Tells (MANDATORY): `references/ai-tells.md`