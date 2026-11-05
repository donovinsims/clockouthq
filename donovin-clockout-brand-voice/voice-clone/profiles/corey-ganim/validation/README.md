# Initial voice validation

## Completed checks
- Corpus: 405 unique originals, 10 holdouts (not used for measurements/retrieval).
- Cold-generation diagnostic: three unguided generic control posts documented in `../validation-notes.md`.
- Overlap: ten synthetic candidates checked against the original corpus with `retrieve.py overlap`.

| Candidate | Format | Overlap result |
|---|---|---|
| 01 | long | pass (longest 3 words) |
| 02 | long | pass (longest 5 words) |
| 03 | short | pass (longest 5 words) |
| 04 | quote | pass (longest 5 words) |
| 05 | quote | pass (longest 2 words) |
| 06 | short | pass (longest 3 words) |
| 07 | long | pass (longest 5 words) |
| 08 | long | pass (longest 4 words) |
| 09 | long | pass (longest 4 words) |
| 10 | long | pass (longest 4 words) |

## Not done
- **Independent blind test:** not completed. It requires a creator, a regular reader, or a separate judge without access to the voice profile. Do not claim the pack is indistinguishable from the creator.
- **Engagement validation:** impossible until newly drafted posts have been published and view/engagement metrics observed over time.
- **Creator authorization and edits:** not supplied. No approval or authorship by the creator can be inferred.
- **Replies:** the supplied latest export contains no replies and the spreadsheet replies were excluded from the original-post corpus. A reply-specific voice model needs its own source samples.
