"""Project-local routing. Active YAML uses the JSON subset of YAML 1.2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMATS = ('short', 'long', 'quote', 'thread', 'article')


def read_profile(value=None):
    if value is None:
        value = json.loads((ROOT / 'content-strategy.json').read_text())['active_profile']
    candidate = Path(value)
    if candidate.is_file():
        manifest = candidate.parent / 'manifest.json' if candidate.suffix in ('.yaml', '.yml') else candidate
    elif candidate.is_dir():
        manifest = candidate / 'manifest.json'
    else:
        manifest = ROOT / 'voice-clone' / 'profiles' / value / 'manifest.json'
    data = json.loads(manifest.read_text(encoding='utf8'))
    if data.get('profile_id') == 'donovin-sims':
        profile = json.loads((ROOT / data['profile_file']).read_text(encoding='utf8'))
        if profile['identity']['name'] != 'Donovin Sims':
            raise ValueError('Active profile identity mismatch')
        return data
    if manifest.parent.name == 'corey-ganim':
        return {'profile_id': 'corey-ganim', 'name': 'Corey Ganim reference',
                'own_corpus': 'voice-clone/profiles/corey-ganim/data/corpus.jsonl',
                'own_stats': 'voice-clone/profiles/corey-ganim/data/stats.json',
                'reference_corpora': [], 'reference_stats': None}
    raise ValueError('Unsupported profile manifest: ' + str(manifest))


def corpus_paths(profile, source='all'):
    own = [(ROOT / profile['own_corpus'], profile['profile_id'])]
    refs = [(ROOT / r['path'], r['author_id']) for r in profile['reference_corpora']]
    if source == 'own':
        return own
    if source == 'reference':
        return refs or own
    return own + refs


def format_baseline(profile, fmt):
    paths = [(profile['own_stats'], profile['profile_id'])]
    if profile.get('reference_stats'):
        paths.append((profile['reference_stats'], 'Corey Ganim reference'))
    for path, author in paths:
        stats = json.loads((ROOT / path).read_text(encoding='utf8'))
        sample = stats.get('by_format', {}).get(fmt)
        if sample and sample.get('posts', 0) >= 5:
            return sample['words'], author, sample['posts']
    return None, None, 0
