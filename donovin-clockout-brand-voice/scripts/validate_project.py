#!/usr/bin/env python3
"""Validate active routing, identity, structured data, links and preserved evidence."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'voice-clone/scripts'))
from profile_config import read_profile, corpus_paths


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    errors, checks, notes = [], [], []
    paths = [p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    count = 0
    for path in paths:
        try:
            if path.suffix == '.json':
                json.loads(path.read_text(encoding='utf8'))
                count += 1
            elif path.suffix == '.jsonl':
                for line in path.read_text(encoding='utf8').splitlines():
                    if line.strip():
                        json.loads(line)
                count += 1
        except (ValueError, OSError) as exc:
            errors.append(f'Structured data: {path.relative_to(ROOT)}: {exc}')
    checks.append(f'Parsed {count} JSON/JSONL files')
    try:
        import yaml
        ypaths = [p for p in paths if p.suffix in ('.yaml', '.yml')]
        for path in ypaths:
            yaml.safe_load(path.read_text(encoding='utf8'))
        checks.append(f'Parsed all {len(ypaths)} YAML files with existing PyYAML')
    except ImportError:
        notes.append('PyYAML unavailable: active JSON-subset YAML parsed; historical YAML not independently parsed')
    except Exception as exc:
        errors.append('YAML: ' + str(exc))

    profile = read_profile()
    for path, author in corpus_paths(profile):
        if not path.is_file():
            errors.append(f'Missing corpus for {author}: {path}')
    own = ROOT / profile['own_corpus']
    if own.read_text().strip():
        notes.append('Own samples now present: review profile counts and provenance')
    else:
        data = json.loads((ROOT / profile['own_stats']).read_text())
        if data['posts_measured'] != 0:
            errors.append('Fabricated own measurement count')
    for key in ('profile_file', 'own_stats', 'reference_stats'):
        if not (ROOT / profile[key]).is_file():
            errors.append('Missing manifest path: ' + profile[key])
    checks.append('Active Donovin identity/routing and separate corpus paths')
    history_path = profile.get('draft_history')
    if history_path:
        hp = ROOT / history_path
        if not hp.is_file() or hp.resolve() == own.resolve():
            errors.append('Draft history missing or mixed into authenticated own corpus')
        else:
            history = [json.loads(line) for line in hp.read_text().splitlines() if line.strip()]
            for row in history:
                if row.get('record_kind') != 'draft_history' or row.get('verified_original') is not False:
                    errors.append('Invalid nontraining draft-history record')
                if row.get('status') not in ('generated', 'approved_edit', 'published'):
                    errors.append('Unknown draft-history status')
                if row.get('status') == 'approved_edit' and not row.get('approved_by_owner'):
                    errors.append('Approved history lacks owner attestation')
                if row.get('status') == 'published' and not (row.get('publication_verified_by_owner') and row.get('source_url') and row.get('date')):
                    errors.append('Published history lacks reviewed evidence')
            checks.append(f'{len(history)} separate draft-history records remain nontraining')
    for key in ('reference_archive_index', 'reference_provenance'):
        if profile.get(key) and not (ROOT / profile[key]).is_file():
            errors.append('Missing reference routing: ' + profile[key])

    brand = ROOT / 'Donovin_Sims_Brand_Profile'
    bio = (brand / '01_Donovin_Sims_Brand_Voice_and_Bio.md').read_text()
    numbers = [int(n) for n in re.findall(r'^## (\d+)\.', bio, re.M)]
    if numbers != list(range(1, 15)):
        errors.append('Brand biography does not preserve all 14 sections')
    for phrase in ('Direct', 'Practical', 'Commercially grounded', 'Generous and educational',
                   'Conversational and occasionally rough', 'Confident but evidence-conscious'):
        if phrase not in bio:
            errors.append('Missing characteristic: ' + phrase)
    if (brand / '03_Donovin_Sims_Project_Instructions.md').read_bytes() != (brand / '03_Donovin_Sims_Project_Instructions.txt').read_bytes():
        errors.append('Instruction copies diverged')
    checks.append('14 biography sections, six characteristics, matching instruction copies')

    strategy = json.loads((ROOT / 'content-strategy.json').read_text())
    voice = json.loads((ROOT / profile['profile_file']).read_text())
    if strategy['mix'] != {k: v for k, v in voice['content_mix'].items() if k != 'status'}:
        errors.append('YAML/strategy mix mismatch')
    from collections import Counter
    plan = json.loads((ROOT / 'validation/20-post-plan.json').read_text())
    actual = dict(Counter(p['category'] for p in plan['posts']))
    if actual != plan['allocation'] or actual != {k: v // 5 for k, v in strategy['mix'].items()}:
        errors.append('20-post plan allocation mismatch')
    checks.append('60/20/15/5 strategy and 12/4/3/1 plan consistency')

    skip = ('docs/archive/', 'docs/canonical/', 'voice-clone/profiles/corey-ganim/',
            'integrations/ghostwriter-upstream/', 'exports/')
    active = [p for p in paths if p.suffix in ('.md', '.txt') and not any(
        str(p.relative_to(ROOT)).startswith(s) for s in skip)]
    link_count = 0
    for path in active:
        text = path.read_text(encoding='utf8')
        if re.search(r"^# Corey|\bI'm Corey Ganim\b|\bI am Corey Ganim\b", text, re.M):
            errors.append('Active identity leakage: ' + str(path.relative_to(ROOT)))
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if '://' in target or target.startswith(('#', 'mailto:')):
                continue
            target = unquote(target.split('#')[0].strip('<>'))
            if target and not (path.parent / target).exists():
                errors.append(f'Broken link: {path.relative_to(ROOT)} -> {target}')
            link_count += 1
    checks.append(f'Active identity scan and {link_count} relative Markdown links')

    baseline = json.loads((ROOT / 'docs/original-project-hashes.json').read_text())
    protected = ('voice-clone/profiles/corey-ganim/data/', 'voice-clone/profiles/corey-ganim/source-archive/',
                 'integrations/ghostwriter-upstream/')
    kept = 0
    for rel, expected in baseline.items():
        if rel.startswith(protected):
            kept += 1
            if not (ROOT / rel).is_file() or sha(ROOT / rel) != expected:
                errors.append('Historical evidence changed: ' + rel)
    checks.append(f'{kept} original corpus/archive/upstream files byte-identical')

    rb = json.loads((ROOT / 'docs/reference-readonly-baseline.json').read_text())
    ref = Path(rb['root'])
    current = {str(p.relative_to(ref)): sha(p) for p in ref.rglob('*') if p.is_file()}
    if current != rb['sha256']:
        errors.append('Read-only reference folder changed versus captured manifest')
    checks.append(f'Read-only reference integrity: {len(current)} files')

    tree = json.loads((ROOT / 'docs/canonical/tree.json').read_text())
    fetched = 0
    for entry in tree['tree']:
        path = ROOT / 'docs/canonical' / entry['path']
        if entry['type'] == 'blob' and path.is_file():
            content = path.read_bytes()
            actual = hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()
            if actual != entry['sha']:
                errors.append('Canonical snapshot hash mismatch: ' + entry['path'])
            fetched += 1
    checks.append(f'{fetched} fetched canonical files match pinned Git blob hashes')

    import export_chatgpt
    export = ROOT / 'exports/CHATGPT_CONTEXT.md'
    if not export.exists() or export.read_text() != export_chatgpt.build():
        errors.append('Portable ChatGPT export is missing or stale')
    checks.append('Portable context matches curated active inputs')
    result = {'status': 'pass' if not errors else 'fail', 'checks': checks, 'notes': notes, 'errors': errors}
    (ROOT / 'validation/project-checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
