# Testing and limits

## Existing evidence
- Original voice-clone package contains 405 unique originals, 395 measured and 10 held out.
- Its earlier test created 10 *synthetic* drafts and checked textual overlap. That was **not** an independent blind study and cannot establish indistinguishability.
- It contains approximately 10 thread roots and 12 articles; replies are not adequately represented for reply-specific fidelity claims.
- Engagement snapshots omit views for some posts; missing metrics cannot be converted to zero. Correlation of post style and raw engagement does not establish causation.

## Validation now included
- The YAML profile preserves the 395-post measured-format baseline from the source stats and adds clearly labeled subjective tone values and regex-based sentence-spread *descriptors*.
- `scripts/check_draft.py` provides deterministic flags for length versus format reference range, question endings, em dash use, hashtags, generic phrases and self-reported success phrases that require proof.
- The original `retrieve.py overlap` script remains the originality check. Neither is an AI detector or a publishing clearance tool.

## Next real quality test
1. Freeze the YAML and training examples.
2. Retain the 10 held-out posts out of all prompts and retrieval.
3. Ask an independent evaluator familiar with the account to classify an anonymized, balanced set of real and newly written samples in the **same format** without exposing profile labels.
4. Log both accuracy and specific reasons; revise the profile on new training content only, then test with another clean holdout.
5. Measure conversions or engagement only after actual publishing, adjusting for topic, audience size, date and distribution.

No blind test or human evaluation was run as part of this integration.
