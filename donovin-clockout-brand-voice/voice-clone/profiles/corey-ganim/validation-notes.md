# Cold Exploration and First-Build Limitations

## Three cold drafts before using the profile

These are intentionally **generic synthetic negative controls**. They are not real posts by Corey Ganim and are not approved content.

**Cold draft A**

> AI is changing the way small businesses work. The winners will be the entrepreneurs who adopt automation today. Here are three ways to get started.

Failure: no buyer, observed pain, actual tool, price or measured outcome. Compare post 2092031293370294316.

**Cold draft B**

> Building an AI business isn't about the technology. It's about impact. Focus on strategy, execution and relationships. The future belongs to the builders.

Failure: a neat generic triad and slogan instead of the specific mechanics and ROI present in posts 2088221709316853791 and 2099848332692623870.

**Cold draft C**

> Every local business needs AI to stay competitive. Are you ready to embrace the opportunity? Let me know in the comments!

Failure: unsupported universal claim and artificial engagement CTA, both uncommon in the measured register.

## First-build checks

- Deduplication by post ID across the JSON, CSV, spreadsheet, top-post ZIP and archived threads/articles.
- Source-preserving normalization, with date conversion and distinct short, long, quote, thread-root and article formats.
- Ten held-out originals for independent evaluation. They remain in `data/corpus.jsonl` with `holdout=true`; retrieval omits them by default.
- Missing view counts are not scored as failed posts. Historical snapshots are not necessarily age-normalized.
- Mechanical overlap results and synthetic samples in `validation/`. An independent blind judge has **not** run.

## Limitations

1. The current export is a narrow slice of the total publishing history, skewing recent in its main feed.
2. The prior spreadsheet supplies few earlier originals and does not provide reliably comparable engagement capture dates.
3. The 10 thread roots come from an archive; archive post counts are not guaranteed to be complete.
4. Reply-specific data are insufficient; do not use long-post punctuation statistics as a reply model.
5. Historical first-person earnings, client outcomes and tool capabilities are creator statements, not independently checked current facts.
6. All originality checks are heuristic. Human review remains necessary.
