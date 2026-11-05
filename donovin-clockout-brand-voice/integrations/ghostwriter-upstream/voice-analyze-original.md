---
name: voice-analyze
description: "Reverse-engineer voice profiles from writing samples by extracting reusable voice patterns. Use when pasting writing samples to extract style, rhythm, vocabulary, and tone while filtering AI tells."
version: 1.1.0
platforms: [all]
---

# voice-analyze

Most voice extraction tools measure surface metrics and call it style. But voice isn't just sentence length or vocabulary choice. It's the habits that make writing feel distinctly human: the rhythm of sentences, the words chosen over others, the level of certainty, warmth, and energy that comes through.

The problem is that AI-generated samples contaminate extraction. When you feed AI-tainted writing into analysis, you extract AI's voice instead of the intended one. This skill solves that by extracting measurable patterns from samples while detecting and filtering AI writing artifacts, producing a reusable YAML voice profile that can actually reproduce the analyzed style.

## Why Default Voice Extraction Fails

Without explicit guidance, voice extraction tends to go wrong in predictable ways:

- **It extracts averages, not habits.** Counting average sentence length misses burstiness — the natural swing between short fragments and longer thoughts that makes writing feel human.
- **It copies AI tells.** If a sample contains overused AI phrasing ("leverage", "delve", "it's worth noting"), naive extraction will treat those tells as part of the voice and propagate them.
- **It conflates genre with voice.** Formal documentation reads differently than casual blog posts. Without separating structure from style, extraction captures context instead of the writer's underlying voice.
- **It produces documentation, not usable instructions.** Generic analysis dumps numbers without translating them into actionable constraints that can reproduce the style.
- **It misses what wasn't said.** Voice is defined as much by what a writer avoids as by what they prefer. Default extraction rarely captures deliberate exclusions.

## Core Principles

### 1. Extract Habits, Not Statistics
Voice lives in repetition and variation. A single average sentence length flattens the rhythm. What matters is **variance** — humans naturally vary. AI tends to cluster. The key signal is burstiness (high sentence-length variance), because it's one of the strongest markers of human rhythm.

**Why this matters:** Reproducing an average produces robotic output. Reproducing the *range and variation* reproduces the feel.

### 2. Filter AI Artifacts First
If a sample contains AI tells, they must be excluded from the extracted voice. The profile should document what was found and explicitly avoid propagating it. This is defensive extraction — clean the signal before modeling it.

**Why this matters:** Extracting contaminated samples creates a feedback loop that amplifies AI artifacts with each generation.

### 3. Capture Constraints, Not Suggestions
A usable voice profile constrains output. It needs concrete prefer/avoid lists, calibrated dimensions (0-1), and structural preferences. Vague adjectives ("friendly tone") don't reproduce voice. Measurable constraints do.

**Why this matters:** Reproducibility requires specificity. The profile must be actionable enough to generate in-character output without guessing.

### 4. Voice Is Defined By Exclusions
Every writer has words they wouldn't use, constructions they avoid, and rhythms they don't default to. Conspicuous absences in samples reveal just as much as frequent patterns. Extract both.

**Why this matters:** Without avoid patterns, generated output tends to drift toward generic, overused phrasing.

### 5. Minimum Viable Signal Over Maximum Noise
Better to extract fewer, high-confidence patterns from clean samples than to over-extract from noisy ones. Confidence scoring matters — weak signals shouldn't pollute the profile.

**Why this matters:** Focused extraction produces profiles that actually improve output. Over-extraction creates friction and dilutes the voice.

## Frameworks

### The 5-Dimension Voice Model
Extract voice across five calibrated dimensions (0-1). These map measurable features to reproducible constraints.

| Dimension | What It Captures | Key Signals | Calibration |
|---|---|---|---|
| **Formality** | Distance vs. familiarity | Contractions (inverse), complete vs. fragment sentences, hedging | 0.0-0.3: casual/fragments OK. 0.4-0.6: professional-accessible. 0.7-1.0: formal, complete sentences |
| **Confidence** | Certainty vs. humility | Direct statements vs. hedges, passive voice (inverse), qualifiers | 0.0-0.3: heavy hedging. 0.4-0.6: balanced. 0.7-1.0: direct, conclusions-first |
| **Warmth** | Personal vs. clinical | 2nd person ("you"), 1st person ("I/we"), inclusive language, passive voice (inverse) | 0.0-0.3: clinical/impersonal. 0.4-0.6: professional-personable. 0.7-1.0: empathetic, inclusive |
| **Energy** | Calm vs. dynamic | Exclamation marks, action verbs, dynamic phrasing | 0.0-0.3: measured, understated. 0.4-0.6: balanced. 0.7-1.0: dynamic, engaged |
| **Complexity** | Accessible vs. nuanced | Sentence length, technical/domain terms, layered ideas | 0.0-0.3: simple, accessible. 0.4-0.6: clear but nuanced. 0.7-1.0: technical, layered |

### Human Rhythm Detection
Burstiness separates human from AI. Measure variance, not just averages.

| Signal | Human Range | AI-Like Range | Why It Matters |
|---|---|---|---|
| Sentence length std dev (words) | 6-12 | 2-4 | Low variance = unnaturally uniform clustering |
| Paragraph length variance (sentences) | 2-5 | 0.5-1.5 | Uniform paragraphs are a strong AI tell |
| Em dash frequency (per 1000 words) | ~0.1-1.0 | ~3.0-10.0+ | Heavy em-dash usage strongly correlates with AI output |

### AI Tells Detection Pass
Run this as a mandatory second pass after feature extraction. For each category, detect, count, and record findings.

1. **Vocabulary scan** — Check against banned verbs/adjectives/nouns/adverbs/connectors from AI tells reference. Any found must go to `vocabulary.avoid`.
2. **Structure scan** — Detect negation flips ("It's not X, it's Y"), self-posed questions answered immediately, anaphora abuse, present participle trailing clauses, false ranges, hedge-stacking.
3. **Punctuation scan** — Count em dashes, semicolons, Oxford commas, Unicode ellipsis. Flag abnormal frequencies.
4. **Rhythm scan** — Calculate sentence length std dev. Flag clustering if < 4 words.
5. **Formatting scan** — Check bold-first bullets, excessive headers, erratic bolding, emoji decoration.
6. **Transition scan** — Detect throat-clearing/pedagogical openers, fake-suspense, hype phrases, banned conclusion phrases.
7. **Repetition scan** — Flag Rule of Three overuse (back-to-back tricolons) and other AI fingerprint patterns.

Report all findings under `ai_tells_report`. Nothing from banned vocabulary enters `prefer` or signature patterns.

### Feature Extraction Mapping
Map extracted measurements to the output structure.

| Feature | Measurement | Maps To |
|---|---|---|
| Sentence length | Avg words/sentence | `structure.sentence_length`, `tone.complexity` |
| Sentence length variance | Std dev (words) | `structure.sentence_length_variance`, `ai_tells_report.sentence_length_std_dev` |
| Contractions | Freq/100 words | `tone.formality` (inverse) |
| 1st person ("I", "we") | Frequency | `tone.warmth`, `perspective.person` |
| 2nd person ("you") | Frequency | `tone.warmth` |
| Passive voice | % of sentences | `tone.confidence` (inverse), `perspective.voice` |
| Questions | Per paragraph | `tone.warmth`, `structure.use_questions` |
| Hedging | "might","perhaps","could","may" | `tone.confidence` (inverse) |
| Exclamations | Frequency | `tone.energy` |
| Technical/domain terms | Density | `tone.complexity`, `vocabulary.prefer` |
| Em dash frequency | Per 1000 words | `ai_tells_report.em_dash_frequency`, `structure.em_dash_usage` |
| Paragraph length variance | Std dev (sentences) | `ai_tells_report.paragraph_length_std_dev` |
| Banned vocab | Count from tells list | `ai_tells_report.banned_vocabulary_found`, forces `vocabulary.avoid` |

### Vocabulary Extraction Logic
Extract vocabulary with discipline:

- **Signature phrases** — Repeated patterns across samples, distinctive constructions, opening/closing patterns. Only include phrases that appear naturally multiple times.
- **Domain vocabulary** — Technical terms, specialized jargon, industry language that appear with meaningful frequency (not one-offs).
- **Avoid patterns** — Combine two sources: (1) Conspicuous absence of overused generic phrasing relative to samples, and (2) **Any AI tells found** (mandatory inclusion). Never infer generic AI vocabulary unless detected in samples or explicitly required by the tells pass.

## Anti-Patterns

Avoid these extraction mistakes:

1. **Copying contamination** — Extracting AI tells as preferred patterns. *Fix:* Run AI tells pass first; anything flagged goes to avoid, never prefer.
2. **Average-only thinking** — Flattening rhythm to means. *Fix:* Prioritize variance (burstiness). High variance = human-like.
3. **Genre bleed** — Confusing documentation style with writer voice. *Fix:* Look for consistent habits across samples; treat structural conventions separately from voice.
4. **Over-extraction** — Dumping every repeated word into prefer. *Fix:* Keep prefer/signature_phrases tight and high-confidence.
5. **Ignoring absences** — Only tracking what appears. *Fix:* Build avoid from tells + patterns conspicuously missing from natural samples.
6. **Insufficient samples** — Analyzing < 500 words gives low confidence. *Fix:* Require adequate sample size; reflect confidence in `analysis_source.confidence`.
7. **Mixed genres** — Blending different styles reduces accuracy. *Fix:* Prefer consistent genre samples when possible; note confidence impact.
8. **Blind trust of samples** — Assuming samples are purely human. *Fix:* Always run AI tells detection and report `overall_human_score`.

## Before/After Examples

### Example 1: Technical Documentation

**Before (naive extraction):** Captures only averages — formality high, warmth low, no rhythm variance.

**After (disciplined extraction):**

```yaml
name: analyzed-technical-docs
version: 1.1.0
description: Voice profile extracted from sample content
analysis_source:
  sample_size: 1500
  sample_count: 3
  confidence: 0.85
tone:
  formality: 0.70
  confidence: 0.85
  warmth: 0.25
  energy: 0.30
  complexity: 0.80
vocabulary:
  prefer:
    - "contextual clarification"
    - "explicit constraint"
  avoid:
    - "leverage"      # AI tell
    - "delve"         # AI tell
    - "comprehensive" # AI tell
  signature_phrases:
    - "The key point is..."
structure:
  sentence_length: medium
  sentence_length_variance: high  # preserves human rhythm
  paragraph_length: medium
  paragraph_length_variance: high
  sentence_variety: high
  use_lists: when-appropriate
  use_examples: frequently
  use_questions: rarely
  em_dash_usage: avoid
perspective:
  person: third
  voice: active
  tense: present
ai_tells_report:
  tells_found: 3
  em_dash_frequency: 0.5
  sentence_length_std_dev: 7.2
  paragraph_length_std_dev: 2.8
  banned_vocabulary_found:
    - "leverage (1x)"
    - "comprehensive (2x)"
  banned_structures_found: []
  banned_transitions_found: []
  formatting_tells_found: []
  overall_human_score: 0.82
```

### Example 2: Conversational Blog Voice

**Before:** Misses burstiness, might absorb AI phrasing if present.

**After:** Captures conversational rhythm with high variance, filters tells.

```yaml
name: conversational-blog-voice
version: 1.1.0
description: Voice profile extracted from blog samples
analysis_source:
  sample_size: 1200
  sample_count: 3
  confidence: 0.88
tone:
  formality: 0.30
  confidence: 0.70
  warmth: 0.85
  energy: 0.75
  complexity: 0.40
vocabulary:
  prefer:
    - "simple observation"
  avoid:
    - "it's worth noting"  # AI tell if detected
  signature_phrases:
    - "Here's the thing..."
structure:
  sentence_length: short
  sentence_length_variance: high  # natural swing (fragments + longer sentences)
  paragraph_length: short
  paragraph_length_variance: high
  sentence_variety: high
  use_lists: when-appropriate
  use_examples: frequently
  use_questions: occasionally
  em_dash_usage: avoid
perspective:
  person: second
  voice: active
  tense: present
ai_tells_report:
  tells_found: 0
  em_dash_frequency: 0.2
  sentence_length_std_dev: 8.5
  paragraph_length_std_dev: 3.2
  banned_vocabulary_found: []
  banned_structures_found: []
  banned_transitions_found: []
  formatting_tells_found: []
  overall_human_score: 0.95
```

## Usage Examples

### Analyze Existing Documentation
```
User: "Analyze this writing style" + [paste technical docs]

Skill produces: analyzed-technical-docs.yaml with calibrated dimensions,
AI tells report, and filtered vocabulary.
```

### Match Brand Voice
```
User: "Extract voice from our marketing copy" + [paste samples]

Skill produces: brand-marketing-voice.yaml capturing conversational
rhythm, signature phrases, and structural preferences.
```

### Capture Personal Style
```
User: "Create profile from my blog posts" + [paste samples]

Skill produces: personal-blog-voice.yaml with extracted quirks,
signature patterns, and AI artifacts filtered out.
```

## Analysis Methodology

### Step-by-Step Process

1. **Ingest samples** — Accept multiple samples (3+ recommended). Note word counts per sample.
2. **Feature extraction** — Compute all measurements in the feature table (averages + variance).
3. **AI tells detection pass** (mandatory) — Scan all categories against `../voice-apply/references/ai-tells.md`. Count every occurrence. Build avoid list from findings.
4. **Dimension calibration** — Map extracted features to 5-dimension model (0-1). Use ranges above as guidance, calibrated to actual sample patterns.
5. **Vocabulary extraction** — Identify prefer, signature_phrases, domain terms. Merge AI tells into avoid. Add conspicuous absences if meaningful.
6. **Structure mapping** — Determine sentence/paragraph length categories (short/medium/long) and variance (low/medium/high) based on measured std dev and averages.
7. **Perspective inference** — Infer person (first/second/third/mixed), voice (active/passive/mixed), tense from sample patterns.
8. **Confidence scoring** — Compute `analysis_source.confidence` (0-1) based on sample size, count, genre consistency. Compute `overall_human_score` from tells density.
9. **Generate YAML profile** — Output in exact format below. Include all sections.

### Confidence Guidelines

- **Minimum sample:** 500+ words for reliable analysis (confidence drops below ~0.7 under 500 words).
- **Multiple samples:** 3+ samples improve accuracy; prefer consistent genre.
- **Consistent genre:** Mixing genres reduces accuracy — reflect in confidence score.
- **AI contamination:** If `tells_found > 0`, overall_human_score decreases accordingly. Profile still extracts clean voice by filtering artifacts.

## Output Format

```yaml
name: analyzed-sample-voice
version: 1.1.0
description: Voice profile extracted from sample content
analysis_source:
  sample_size: 1500  # total words analyzed
  sample_count: 3    # number of samples
  confidence: 0.85   # analysis confidence (0-1)
tone:
  formality: 0.65
  confidence: 0.80
  warmth: 0.40
  energy: 0.50
  complexity: 0.70
vocabulary:
  prefer:
    - "extracted signature phrase 1"
    - "detected domain terminology"
  avoid:
    - "leverage"       # AI tell: banned verb
    - "delve"          # AI tell: banned verb
    - "comprehensive"  # AI tell: banned adjective
    - "landscape"      # AI tell: banned noun
    - "furthermore"    # AI tell: banned adverb
    - "patterns not found in samples"
  signature_phrases:
    - "The key point is..."
    - "This demonstrates..."
structure:
  sentence_length: medium           # short/medium/long (based on avg)
  sentence_length_variance: high     # low/medium/high (based on std dev)
  paragraph_length: medium
  paragraph_length_variance: high
  sentence_variety: high
  use_lists: when-appropriate        # rarely/occasionally/frequently/when-appropriate
  use_examples: frequently
  use_questions: rarely
  em_dash_usage: avoid               # avoid/use-sparingly/use-naturally (based on samples)
perspective:
  person: third                      # first/second/third/mixed
  voice: active                      # active/passive/mixed
  tense: present                     # past/present/future/mixed
extracted_patterns:
  opening_style: "context-first"     # context-first/direct/question/problem-first/mixed
  closing_style: "conclusion-summary"
  transition_style: "logical-flow"
ai_tells_report:
  tells_found: 3
  em_dash_frequency: 2.1             # per 1000 words
  sentence_length_std_dev: 7.2       # words
  paragraph_length_std_dev: 2.8      # sentences
  banned_vocabulary_found:
    - "leverage (1x)"
    - "comprehensive (2x)"
  banned_structures_found:
    - "negation pattern (1x)"
  banned_transitions_found: []
  formatting_tells_found: []
  overall_human_score: 0.82           # 0 = clearly AI, 1 = clearly human
```

## Quality Checklist

Before producing a voice profile, verify:

- [ ] AI tells detection pass completed (mandatory)
- [ ] Any banned vocabulary found in samples appears in `vocabulary.avoid`
- [ ] Sentence length variance captured (burstiness) — not just average
- [ ] `overall_human_score` and `analysis_source.confidence` included and reasonable
- [ ] Prefer/signature_phrases are high-confidence (not one-offs)
- [ ] Dimensions calibrated to actual measurements (0-1), not guessed
- [ ] Structure reflects variance (high when human rhythm detected)
- [ ] Profile is actionable for voice-apply (no vague abstractions)
- [ ] AI artifacts filtered — no tells in prefer lists
- [ ] Sample size meets minimum (500+ words) or confidence reflects shortfall

## Integration

- **Output compatibility:** Profiles are designed for use by `voice-apply`.
- **Chaining:** `voice-analyze` → `voice-create` (to refine) → `voice-apply`.
- **Blending:** `voice-analyze` + `voice-analyze` → `voice-blend` (combine styles).
- **Reference:** AI Writing Tells at `../voice-apply/references/ai-tells.md`.

## Accuracy Considerations

- **Minimum viable:** 500+ words per analysis for reliable extraction.
- **Better with multiple samples:** 3+ samples improve pattern stability and confidence.
- **Genre consistency matters:** Mixing genres dilutes voice signal; prefer samples from the same context.
- **Confidence transparency:** Always report both `analysis_source.confidence` and `overall_human_score`.
- **Contamination handling:** If samples contain AI artifacts, the profile filters them and documents findings — this is by design.