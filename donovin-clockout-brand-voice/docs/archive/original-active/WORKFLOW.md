# End-to-end Writing Workflow

1. **Brief:** Choose one audience, format, factual angle, target action and any confirmed claims. Use `BRIEF_TEMPLATE.md`.
2. **Retrieve:** Read the YAML profile plus `voice-dna.md`, `lexicon.md` and `positions.md`; retrieve 5–8 relevant non-holdout posts using the original `retrieve.py` script.
3. **Write:** Follow `integrations/voice-apply/SKILL.md`: create three different angles, evaluate, then produce one preferred original draft. Avoid dressing the draft in the author's personal history unless sourced.
4. **Review:** Use the editorial checklist, the upstream AI-tells list *only* for investigation, and the `scripts/check_draft.py` CLI for heuristic flags. Keep attested Corey language intact.
5. **Validate:** Run original corpus overlap and manually check sources, authorization and factual claims. Redraft if any meaningful duplication or invented fact appears.
6. **Learn:** Record the final approved edit, its rationale, post date/format, and reliable outcome measures. Do not retrain on unapproved AI drafts. Use `integrations/voice-analyze/SKILL.md` when enough new original samples justify recalibration.

## Example local commands (run from ZIP extraction root)

```bash
python voice-clone/scripts/retrieve.py search voice-clone/profiles/corey-ganim/data/corpus.jsonl "AI assessments local clients" -k 8
python scripts/check_draft.py --draft-file your-draft.txt --format long --profile voice-clone/profiles/corey-ganim/corey-voice-profile.yaml
python voice-clone/scripts/retrieve.py overlap voice-clone/profiles/corey-ganim/data/corpus.jsonl --draft-file your-draft.txt
```

`check_draft.py` runs offline with Python standard library, reads the YAML profile only as a file existence check, and **does not certify factual accuracy, human authorship or voice fidelity**. The original overlap script is the more important copying check.
