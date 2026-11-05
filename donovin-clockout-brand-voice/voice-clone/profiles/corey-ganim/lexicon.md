# Corey Ganim Lexicon (Measured Style Fingerprint)

Source: `data/stats.json`, 395 measured, 10 held out. Measurement period ends October 30, 2026. Percentages indicate share of posts containing a feature, not number of occurrences. These are **per-format** statistics, never blended.

| Format | N measured | Words/post p10 / median / p90 | Median lines | Lowercase start | Colon | Parentheses | Emoji | Em dash | Hashtag | Contractions |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Short | 44 | 12.3 / 19.5 / 41.7 | 3 | 39% | 70% | 11% | 0% | 0% | 0% | 39% |
| Long | 222 | 80 / 143 / 365.6 | 19.5 | 36% | 85% | 50% | 0% | 0% | 1% | 84% |
| Quote | 107 | 14.6 / 57 / 136.6 | 7 | 20% | 56% | 25% | 4% | 0% | 0% | 57% |
| Thread root | 10 | 32.9 / 42.5 / 48 | 5 | 10% | 90% | 70% | 20% | 0% | 40% | 60% |
| Article | 12 | 981.7 / 1698 / 2232.8 | 229 | 0% | 100% | 92% | 0% | 0% | 17% | 100% |

**Interpretation:** Posts over 280 characters are often lengthy instructional text, not just a two-line microblog. Threads and articles have their own framing. 10 archived thread roots are not enough to estimate complete thread length; read complete thread files.

## Opening and ending shapes

- Short: statement opener **75%**, I-statement **11%**, number **7%**; no-terminal-punctuation ending **75%**, statement ending **25%**.
- Long: statement opener **72%**, I-statement **13%**, number **6%**; statement ending **91%**, no-terminal punctuation **6%**; question endings are rare.
- Quote: statement opener **73%**, I-statement **6%**, you-statement **10%**; statement ending **65%**, no-terminal punctuation **27%**.
- Article: full headings, detailed frameworks, section intros, a specific business hook and occasional download/podcast CTA. Sample: [2094066129790755304](https://x.com/coreyganim/status/2094066129790755304).

## Signature vocabulary and how to use it

| Word / turn of phrase | Observed evidence | Use pattern |
|---|---|---|
| "extremely bullish" | [2101434912129876095](https://x.com/coreyganim/status/2101434912129876095) | Occasionally when stating a new bet, not every draft |
| "Huge hack" / "Huge" | [2099532879013589026](https://x.com/coreyganim/status/2099532879013589026) | Sometimes introduces a concrete shortcut |
| "here's the entire model" | [2099848332692623870](https://x.com/coreyganim/status/2099848332692623870), [2088221709316853791](https://x.com/coreyganim/status/2088221709316853791) | Used when an actual full process follows |
| "the play" | [2089662109223415825](https://x.com/coreyganim/status/2089662109223415825) | Especially casual quote posts |
| "SELL OUTCOMES" / "not AI" | [2103793452949635075](https://x.com/coreyganim/status/2103793452949635075), [2109694955996275049](https://x.com/coreyganim/status/2109694955996275049) | Only when the commercial distinction is the point |
| "AI Concierge" | [2099848332692623870](https://x.com/coreyganim/status/2099848332692623870), [2088221709316853791](https://x.com/coreyganim/status/2088221709316853791) | A named offer, not generic business slang |
| "Audit, Optimize, Automate" / "AOA" | [2099848332692623870](https://x.com/coreyganim/status/2099848332692623870) | Distinct framework; preserve capitalization |
| "non-technical", "SMBs", "owner" | [2084312288786276484](https://x.com/coreyganim/status/2084312288786276484), [2101434912129876095](https://x.com/coreyganim/status/2101434912129876095) | Audience-specific practical jargon |
| "full breakdown below" | [2115476203184218336](https://x.com/coreyganim/status/2115476203184218336) | Only when genuinely followed by linked material |
| "Enjoy." | [2089384613731069975](https://x.com/coreyganim/status/2089384613731069975) | Sometimes promotional posts, not a mandatory ender |

Avoid injecting jargon such as "revolutionize," "unlock potential" or "seamless solutions" unless a source post clearly warrants it. The literal word "leverage" appears in the corpus, so it is not a blanket prohibited word; nevertheless it isn't the dominant register.

## Casing and pacing

- Real posts include uppercase emphasis within otherwise normal text ("THE", "THIS WEEK", "ROI") and occasional entirely lowercase openings. The most recent long-form material is more sentence-cased.
- Lists vary: `1)` or `1.` for steps; `-` bullet lines; short labeled blocks such as `The trigger:` and `The offer:` ([2115881525543653394](https://x.com/coreyganim/status/2115881525543653394)). Do not symmetrically repeat bullet lengths.
- Spacing varies. Blank lines separate ideas. Do not compress into a single generic paragraph.
- He often names exact apps (Claude, Codex, Cursor, Notion, Grok Bot, Stripe, Todoist, Google) when discussing a specific workflow. Only name tools relevant to the proposed post.
- Numbers often serve a business calculation: "30 doors = 5 meetings / 5 meetings = 2 paying clients" ([2079692142646050995](https://x.com/coreyganim/status/2079692142646050995)). Do not reuse historical numbers as current facts.
- The absence of em dashes is highly consistent. Use periods, commas, colons and blank lines instead.

## Temporal drift

| Long posts month | N | Median words | Lowercase opening |
|---|---:|---:|---:|
| July 2026 | 59 | 144 | 44% |
| August 2026 | 62 | 108.5 | 55% |
| September 2026 | 66 | 145 | 27% |
| October 2026 | 35 | 228 | 6% |

Default: model the latest October register while keeping earlier casual posts as examples for shorter opinionated writing. Dataset coverage is not uniform, so don't overread these month-to-month shifts.
