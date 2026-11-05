# Historical Corey reference — not active Donovin identity

Use ../donovin-sims/README.md for active writing. All measurements and posts below describe Corey Ganim. Original data and source archives are preserved.

# Corey Ganim X Voice Profile

**Profile version:** 1.0, 2026-10-30. **Source:** user-supplied X exports and curated archive. **Scope:** style analysis, research-based original drafting and revision, not identity impersonation.

## Fast usage

1. Read `voice-dna.md`, `lexicon.md`, `positions.md`, then `hooks.md`.
2. For a topic, retrieve 5–8 similar real posts, with a mix of typical and top examples, before drafting:

```bash
python ../../scripts/retrieve.py search data/corpus.jsonl "local AI service business" -k 8
python ../../scripts/retrieve.py search data/corpus.jsonl "paid assessment" -k 6 --tier top --format long
```

From this folder, scripts are located at `../../scripts/` in the bundled `voice-clone/` root.

3. Draft three original variants. Pick one. Check against voice and stances. Fact-check numbers, clients and events; require approval for creator attribution.
4. Check overlap before publication:

```bash
python ../../scripts/retrieve.py overlap data/corpus.jsonl --draft-file draft.txt
```

5. For thread and article formats, consult `../../references/formats.md` and `source-archive/`. For replies, there is insufficient dedicated sample; do not assert reply fidelity.

**Files:** `data/corpus.jsonl` (searchable originals), `data/stats.md`, `data/source-audit.json`, `top-posts.md` (curated), `validation-notes.md` (initial tests and caveats), `source-archive/` (complete articles and archived threads), `learning-log.md` (ongoing evaluation).

**Caution:** X posts can contain time-sensitive or unverified personal claims. Metrics are inconsistent snapshots. No one authorized us to speak on Corey's behalf; a creator-owned publishing workflow should seek explicit permission.
