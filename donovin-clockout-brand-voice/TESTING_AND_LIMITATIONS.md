# Testing and source limitations

Donovin has zero verified original X posts ingested. The adopted voice is initialized with Corey-derived mechanics, owner-selected positions and documented Donovin background. It is not an empirically measured Donovin fingerprint.

Corey's historical 405 originals / 395 measured / 10 held out remain attributed. The corpus has limited thread/article coverage and insufficient reply evidence. Earlier synthetic drafts and overlap checks were not a human blind study. Historical engagement snapshots are uneven and do not establish causation.

The active YAML uses JSON syntax valid under YAML 1.2. Production scripts need only Python standard library; the local environment's existing PyYAML validates all YAML during this implementation. No dependency was installed. Ingestion metadata is a provenance gate, not independent proof of authorship. Review source data before marking verified_original true.

check_draft.py reads configured own per-format statistics when supported, otherwise explicitly identifies the Corey reference baseline. It flags only selected patterns and cannot catch every fabricated claim. Root statistics for threads do not describe whole-thread length. retrieve.py overlap compares contiguous words and 5-word sequences across available own and reference corpora; conceptual copying and outside sources still need manual review.

[Four validation drafts](validation/REVIEW.md) are synthetic unpublished tests, not authentic training samples or observed successful content. See [validation/REVIEW.md](validation/REVIEW.md), [validation/results.json](validation/results.json) and [implementation report](docs/IMPLEMENTATION_REPORT.md) for checks actually run. No human blind evaluation, public publishing or engagement test was performed.

X (403) and LinkedIn (999) were inaccessible; no public-profile details were independently verified. Employment titles/dates, quantitative career contributions, current customer counts/revenue, public case-study permission, live website behavior and current tool-use anecdotes remain unverified. Tool-specific tutorials require fresh official documentation checks.

The newer GitHub website-price decision overrides the dated local proposal; neither is evergreen pricing. [Source reconciliation](docs/SOURCE_RECONCILIATION.md) records exact comparison scope. Internal canonical snapshots are reference-only and excluded from the ChatGPT export.

## Reference optimization, v2.1

The current retrieval pipeline adds structural/category heuristics, balanced examples and source/performance annotations. Original Corey counts and metrics are unchanged. Normal retrieval excludes holdouts. The nontraining draft ledger never becomes an authentic writing corpus. Overlap now also identifies complete-sentence candidates, high lexical similarity and recent structural/opening repetition. These do not provide automated semantic understanding or prove originality.

The four new end-to-end requests, attributed research packets, drafts and actual check output are in validation/reference-optimization/. Updated manual evaluations are in validation/REVIEW.md. See the current optimization section in docs/IMPLEMENTATION_REPORT.md for final test results. The older validation artifacts remain historical test evidence.
