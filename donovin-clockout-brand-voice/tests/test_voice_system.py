import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'voice-clone/scripts'))
import ingest
import retrieve
from profile_config import read_profile, corpus_paths, format_baseline


def run_script(path, *args, cwd=ROOT):
    return subprocess.run([sys.executable, str(ROOT / path), *map(str, args)],
                          cwd=cwd, text=True, capture_output=True)


class VoiceSystemTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=ROOT / 'validation')
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)

    def sample(self, **changes):
        data = {'id': 'fixture-1', 'date': '2026-10-01',
                'text': 'A synthetic fixture explains a bounded task with a clear check.',
                'author_id': 'donovin-sims', 'verified_original': True,
                'source_url': 'https://example.invalid/fixture', 'views': 0}
        data.update(changes)
        return data

    def ingest_records(self, records, *args):
        raw = self.work / 'raw.json'
        raw.write_text(json.dumps(records))
        out = self.work / 'donovin-sims/data'
        result = run_script('voice-clone/scripts/ingest.py', raw, '--out', out,
                            '--author-id', 'donovin-sims', *args)
        return result, out

    def test_default_identity_and_separate_corpora(self):
        profile = read_profile()
        self.assertEqual(profile['profile_id'], 'donovin-sims')
        sources = corpus_paths(profile)
        self.assertEqual([a for _, a in sources], ['donovin-sims', 'corey-ganim'])
        self.assertEqual(retrieve.load(sources[0][0]), [])

    def test_own_stats_not_fabricated(self):
        baseline, author, count = format_baseline(read_profile(), 'long')
        self.assertEqual(author, 'Corey Ganim reference')
        self.assertEqual(count, 222)
        self.assertEqual(baseline['median'], 143)

    def test_profile_changes_actual_baseline(self):
        fake = {'own_stats': str(self.work / 'own.json'), 'profile_id': 'fixture', 'reference_stats': None}
        Path(fake['own_stats']).write_text(json.dumps({'by_format': {'short': {'posts': 5,
            'words': {'p10': 1, 'median': 2, 'p90': 3}}}}))
        self.assertEqual(format_baseline(fake, 'short'), ({'p10': 1, 'median': 2, 'p90': 3}, 'fixture', 5))

    def test_editorial_uses_yaml_path_and_flags_claim(self):
        draft = self.work / 'draft.txt'
        draft.write_text('I made $500 with my client. What do you think?')
        result = run_script('scripts/check_draft.py', '--draft-file', draft, '--format', 'short',
                            '--profile', ROOT / 'voice-clone/profiles/donovin-sims/donovin-voice-profile.yaml', '--json')
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data['profile_id'], 'donovin-sims')
        self.assertTrue(any('claim' in f.lower() for f in data['flags']))
        self.assertTrue(any('Question ending' in f for f in data['flags']))

    def test_invalid_profile_fails_clearly(self):
        result = run_script('scripts/check_draft.py', '--draft-file', 'validation/drafts/01-education.txt',
                            '--format', 'long', '--profile', 'does-not-exist')
        self.assertEqual(result.returncode, 2)

    def test_retrieval_legacy_and_profile_route(self):
        for args in [('search', ROOT / 'voice-clone/profiles/corey-ganim/data/corpus.jsonl', 'workflow', '-k', '1'),
                     ('search', 'workflow', '--profile', 'donovin-sims', '-k', '1')]:
            result = run_script('voice-clone/scripts/retrieve.py', *args)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('author=', result.stdout)

    def test_empty_own_search_and_cwd_independence(self):
        result = run_script('voice-clone/scripts/retrieve.py', 'search', 'workflow', '--source', 'own', cwd=self.work)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('No authored samples', result.stdout)

    def test_holdouts_excluded_from_normal_search(self):
        corpus = self.work / 'corpus.jsonl'
        corpus.write_text('\n'.join(json.dumps(p) for p in [
            {'id': 'hidden', 'text': 'unique hidden answer', 'holdout': True},
            {'id': 'visible', 'text': 'ordinary visible answer example', 'holdout': False}]))
        result = run_script('voice-clone/scripts/retrieve.py', 'search', corpus, 'answer')
        self.assertNotIn('id=hidden', result.stdout)
        self.assertIn('id=visible', result.stdout)

    def test_overlap_flag_and_empty_corpus(self):
        corpus = self.work / 'corpus.jsonl'
        text = 'one two three four five six seven eight nine ten'
        corpus.write_text(json.dumps({'id': 'fixture', 'text': text}) + '\n')
        result = run_script('voice-clone/scripts/retrieve.py', 'overlap', corpus, '--draft', text, '--strict')
        self.assertEqual(result.returncode, 1)
        self.assertIn('FLAG:', result.stdout)
        corpus.write_text('')
        result = run_script('voice-clone/scripts/retrieve.py', 'overlap', corpus, '--draft', 'unrelated text', '--strict')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_overlap_requires_one_draft(self):
        for extra in [[], ['--draft', 'a', '--draft-file', 'b']]:
            result = run_script('voice-clone/scripts/retrieve.py', 'overlap', *extra)
            self.assertEqual(result.returncode, 2)

    def test_profile_overlap_covers_both_authors(self):
        text = 'one two three four five six seven eight nine ten'
        own = self.work / 'own.jsonl'
        ref = self.work / 'ref.jsonl'
        own.write_text(json.dumps({'id': 'own', 'text': 'Unrelated example for one source.'}) + '\n')
        ref.write_text(json.dumps({'id': 'ref', 'text': text}) + '\n')
        profile = dict(read_profile())
        profile['own_corpus'] = str(own)
        profile['reference_corpora'] = [{'author_id': 'corey-ganim', 'path': str(ref)}]
        manifest = self.work / 'manifest.json'
        manifest.write_text(json.dumps(profile))
        result = run_script('voice-clone/scripts/retrieve.py', 'overlap', '--profile', manifest,
                            '--draft', text, '--strict')
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn('donovin-sims:', result.stdout)
        self.assertIn('corey-ganim:', result.stdout)

    def test_ingest_rejects_mixed_missing_and_generated(self):
        for changes in [{'author_id': 'corey-ganim'}, {'verified_original': False},
                        {'source_url': ''}, {'generated': True}, {'date': 'bad-date'}]:
            result, out = self.ingest_records([self.sample(**changes)])
            self.assertEqual(result.returncode, 2, result.stdout)
            self.assertFalse(out.exists())

    def test_ingest_deduplicates_and_unknown_metrics_unranked(self):
        result, out = self.ingest_records([self.sample(), self.sample()])
        self.assertEqual(result.returncode, 0, result.stderr)
        posts = retrieve.load(out / 'corpus.jsonl')
        self.assertEqual(len(posts), 1)
        self.assertIsNone(posts[0]['perf'])
        self.assertEqual(posts[0]['tier'], 'unranked')
        stats = json.loads((out / 'stats.json').read_text())
        self.assertEqual(stats['author_id'], 'donovin-sims')
        self.assertEqual(stats['by_format'], {})

    def test_cross_author_merge_rejected(self):
        old = self.work / 'old.jsonl'
        old.write_text(json.dumps(self.sample(author_id='corey-ganim')) + '\n')
        result, out = self.ingest_records([self.sample()], '--merge', old)
        self.assertEqual(result.returncode, 2)
        self.assertFalse(out.exists())

    def test_holdout_and_per_format_measurement(self):
        records = [self.sample(id=str(i), text=f'Example {i} is a synthetic fixture with a bounded task and clear review.')
                   for i in range(35)]
        result, out = self.ingest_records(records)
        self.assertEqual(result.returncode, 0, result.stderr)
        posts = retrieve.load(out / 'corpus.jsonl')
        held = {p['id'] for p in posts if p['holdout']}
        self.assertEqual(len(held), 10)
        stats = json.loads((out / 'stats.json').read_text())
        self.assertEqual(stats['posts_measured'], 25)
        self.assertEqual(stats['by_format']['short']['posts'], 25)
        result, _ = self.ingest_records([self.sample(id='new')], '--merge', out / 'corpus.jsonl')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p['id'] for p in retrieve.load(out / 'corpus.jsonl') if p['holdout']}, held)

    def test_missing_id_is_stable_in_generic_normalizer(self):
        value = {'text': 'Stable synthetic text without a source identifier.'}
        self.assertEqual(ingest.normalize(value)['id'], ingest.normalize(value)['id'])

    def test_strategy_allocation_and_instruction_copies(self):
        plan = json.loads((ROOT / 'validation/20-post-plan.json').read_text())
        from collections import Counter
        self.assertEqual(dict(Counter(p['category'] for p in plan['posts'])), plan['allocation'])
        self.assertEqual(sum(json.loads((ROOT / 'content-strategy.json').read_text())['mix'].values()), 100)
        brand = ROOT / 'Donovin_Sims_Brand_Profile'
        self.assertEqual((brand / '03_Donovin_Sims_Project_Instructions.md').read_bytes(),
                         (brand / '03_Donovin_Sims_Project_Instructions.txt').read_bytes())


if __name__ == '__main__':
    unittest.main()
