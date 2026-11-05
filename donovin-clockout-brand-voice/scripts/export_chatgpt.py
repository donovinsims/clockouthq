#!/usr/bin/env python3
"""Build a curated portable context file; never include internal source snapshots."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    'Donovin_Sims_Brand_Profile/03_Donovin_Sims_Project_Instructions.md',
    'Donovin_Sims_Brand_Profile/01_Donovin_Sims_Brand_Voice_and_Bio.md',
    'Donovin_Sims_Brand_Profile/02_Donovin_Sims_Ideal_Customer_Profile.md',
    'voice-clone/profiles/donovin-sims/facts.md',
    'voice-clone/profiles/donovin-sims/positions.md',
    'voice-clone/profiles/donovin-sims/voice-dna.md',
    'voice-clone/profiles/donovin-sims/lexicon.md',
    'voice-clone/profiles/donovin-sims/hooks.md',
    'voice-clone/profiles/donovin-sims/top-posts.md',
    'content-strategy.json',
    'EDITORIAL_QUALITY_CHECKLIST.md',
    'BRIEF_TEMPLATE.md',
    'integrations/voice-apply/SKILL.md',
]


def build():
    intro = ('# Donovin Sims — portable ChatGPT context\n\n'
             'Generated from the active project. All required identity/style sections are embedded below. '
             'Local links are provenance labels, not attached files. Corey references are attributed '
             'mechanics only. No complete reference corpus is included. If execution or source material '
             'is unavailable, do not claim automated originality or current tool verification. '
             'Deliver drafts for Donovin review. For actual source retrieval, attach a topic-specific '
             'research packet produced by retrieve.py brief, or attach the existing original Corey '
             'corpus.jsonl as an attributed reference file when file analysis is available. Exclude '
             'holdouts, select 3-6 useful examples, and never paste the whole corpus into a prompt. '
             'A text-only session cannot claim local script checks.\n\n')
    return intro + '\n\n'.join(f'---\n\nSource section: `{name}`\n\n' +
                                (ROOT / name).read_text(encoding='utf8') for name in FILES)


def main():
    output = ROOT / 'exports/CHATGPT_CONTEXT.md'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build(), encoding='utf8')
    print(f'Wrote {output} from {len(FILES)} curated files; internal snapshots excluded.')


if __name__ == '__main__':
    main()
