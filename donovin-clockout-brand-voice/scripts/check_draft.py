#!/usr/bin/env python3
"""Deterministic editorial review flags, never a fact or authorship detector."""
import argparse
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'voice-clone/scripts'))
from profile_config import FORMATS, format_baseline, read_profile

GENERIC = ["in today's fast-paced world", 'unlock your potential', 'seamless solutions',
           'revolutionize your', 'game-changer', 'in the ever-evolving landscape',
           "it's important to note"]
CLAIMS = [r"\bI (?:made|earned|generated|closed|sold|built|spent|charge|have|tested|worked|played|grew|attended)\b",
          r"\bmy client(?:s)?\b", r"\bwe (?:saved|earned|made|closed)\b",
          r"\$\d+(?:[.,]\d+)?(?:\s*(?:k|m|million|thousand))?\b"]


def review(text, fmt, profile):
    words = len(re.findall(r"[A-Za-z0-9']+", text))
    baseline, author, count = format_baseline(profile, fmt)
    flags = []
    if baseline and not baseline['p10'] <= words <= baseline['p90']:
        flags.append(f"Length outside {author} sampled p10-p90 for {fmt} "
                     f"({baseline['p10']:g}-{baseline['p90']:g}); descriptive only")
    if '—' in text:
        flags.append('Typographic em dash: review against adopted style')
    if re.search(r'(?:^|\s)#[A-Za-z]+', text):
        flags.append('Hashtag: review format fit')
    if re.search(r'\?\s*$', text.strip()) and fmt in ('long', 'short'):
        flags.append('Question ending: avoid empty engagement bait')
    for phrase in GENERIC:
        if phrase in text.lower():
            flags.append('Generic phrase to review: ' + repr(phrase))
    if len(re.findall(r"(?i)\b(?:it's not|this isn't)\b.{0,70}\b(?:it's|it is)\b", text)) > 1:
        flags.append('Repeated negation-flip constructions: revise if templated')
    if any(re.search(p, text, re.I) for p in CLAIMS):
        flags.append('Personal/numerical claim: verify dated source and public-use suitability manually')
    if profile['profile_id'] == 'donovin-sims':
        if re.search(r"\b(?:I'm|I am) Corey\b|\bmy (?:AI Operator Academy|Build With AI podcast)\b", text, re.I):
            flags.append('IDENTITY: possible Corey personal-claim leakage')
        if re.search(r'\b(?:start|launch|grow) (?:your |an? )?AI (?:agency|consulting business)\b', text, re.I):
            flags.append('POSITION: possible excluded agency education')
    return {'profile_id': profile['profile_id'], 'format': fmt, 'words': words,
            'baseline_author': author, 'baseline_sample_count': count,
            'reference_median': baseline['median'] if baseline else None,
            'flags': flags, 'caveat': 'Heuristics only; manual facts, originality and voice review required.'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--draft-file', required=True)
    ap.add_argument('--format', choices=FORMATS, required=True)
    ap.add_argument('--profile', help='Profile slug, directory, manifest or adjacent YAML path')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    try:
        result = review(Path(a.draft_file).read_text(encoding='utf8'), a.format, read_profile(a.profile))
    except (OSError, ValueError, KeyError) as exc:
        ap.error(str(exc))
    if a.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"EDITORIAL REVIEW | {result['profile_id']} | {a.format} | words={result['words']}")
        print(f"Baseline: {result['baseline_author'] or 'none'}; n={result['baseline_sample_count']}; "
              f"median={result['reference_median']}")
        for flag in result['flags']:
            print('REVIEW:', flag)
        print(result['caveat'])
        print('Run voice-clone/scripts/retrieve.py overlap separately.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
