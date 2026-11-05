#!/usr/bin/env python3
"""Lightweight, non-classifying Corey profile editorial checks; standard library."""
import argparse
from pathlib import Path
import re
import sys

DEFAULT_RANGES = {
  'short': (12.3, 19.5, 41.7),
  'long': (80.0, 143.0, 365.6),
  'quote': (14.6, 57.0, 136.6),
  'thread': (32.9, 42.5, 48.0),
  'article': (981.7, 1698.0, 2232.8),
}
GENERIC = ['in today\'s fast-paced world','unlock your potential','seamless solutions','revolutionize your','game-changer','in the ever-evolving landscape','it\'s important to note']
CLAIMS = [r'\bI (?:made|earned|generated|closed|sold|built|spent|charge|have)\b',r'\bmy client(?:s)?\b',r'\bwe (?:saved|earned|made|closed)\b',r'\b\$\d+(?:[.,]\d+)?\s*(?:k|m|million|thousand)?\b']

def main():
 ap=argparse.ArgumentParser(description='Heuristic-only checks: not a voice score, plagiarism pass, or fact verifier.')
 ap.add_argument('--draft-file',required=True); ap.add_argument('--format',choices=DEFAULT_RANGES,required=True)
 ap.add_argument('--profile',required=False,help='Optional path to readable Corey voice-profile YAML')
 a=ap.parse_args()
 if a.profile and not Path(a.profile).is_file():
  ap.error('Profile file does not exist')
 text=Path(a.draft_file).read_text(encoding='utf8')
 tokens=re.findall(r"[A-Za-z0-9']+",text)
 words=len(tokens);lo,mid,hi=DEFAULT_RANGES[a.format]
 flags=[]
 if words<lo or words>hi:flags.append(f'Length outside sampled p10-p90 for {a.format} ({lo:g}-{hi:g} words; not a strict rule)')
 if '—' in text: flags.append('Typographic em dash: absent from measured reference posts')
 if re.search(r'(?:^|\s)#[A-Za-z]+',text):flags.append('Hashtag: rare or absent for most measured formats')
 if re.search(r'\?\s*$',text.strip()) and a.format in ('long','short'):flags.append('Question ending: unusual in reference posts')
 for phrase in GENERIC:
  if phrase in text.lower():flags.append('Generic AI-style phrase to review: '+repr(phrase))
 if len(re.findall(r'(?i)\b(?:it\'s not|this isn\'t)\b.{0,70}\b(?:it\'s|it is)\b',text))>1:
  flags.append('Repeated negation-flip constructions: revise if templated')
 claims=[pattern for pattern in CLAIMS if re.search(pattern,text,flags=re.I)]
 if claims: flags.append('First-person or numerical claim detected: verify source/approval manually ('+str(len(claims))+' pattern groups)')
 print('COREY EDITORIAL HEURISTICS | format='+a.format+' | words='+str(words)+' | reference median='+str(mid))
 if flags:
  for f in flags:print('REVIEW:',f)
 else: print('No heuristic issues detected; manual fact/originality/voice review still required.')
 print('Always run voice-clone/scripts/retrieve.py overlap separately.')
 return 0

if __name__=='__main__':sys.exit(main())
