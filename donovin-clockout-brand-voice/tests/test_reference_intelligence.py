import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'voice-clone/scripts'))
import retrieve
from reference_intelligence import performance, patterns, select, example
from profile_config import read_profile


class ReferenceIntelligenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=ROOT / 'validation')
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)

    def post(self, name, tier='typical', perf=1, **extra):
        result = {'id': name, 'text': 'Workflow example:\n1) Supply sample notes.\n2) Check the output.',
                  'format': 'long', 'views': 1000, 'likes': 100, 'perf': perf,
                  'perf_basis': 'long', 'tier': tier, '_reference_author': 'corey-ganim'}
        result.update(extra)
        return result

    def cli(self, *args):
        return subprocess.run([sys.executable, str(ROOT / 'voice-clone/scripts/retrieve.py'), *map(str, args)],
                              cwd=ROOT, text=True, capture_output=True)

    def test_balanced_keeps_everyday_and_contrast(self):
        posts = [self.post('top1', 'top', 10), self.post('top2', 'top', 8),
                 self.post('ordinary1'), self.post('ordinary2'), self.post('weak', 'weak', .4)]
        chosen = select([(1, p) for p in posts], k=4, category='practical_education')
        self.assertEqual([c['post']['tier'] for c in chosen], ['top', 'typical', 'typical', 'weak'])

    def test_structure_outranks_keyword_only(self):
        structured = self.post('structure')
        keyword = self.post('keyword', text='Workflow workflow workflow is a topic.')
        chosen = select([(1, keyword), (.1, structured)], k=1, category='practical_education', mode='relevant')
        self.assertEqual(chosen[0]['post']['id'], 'structure')

    def test_hypothetical_is_not_history_and_menu_is_not_walkthrough(self):
        self.assertNotIn('story', patterns('If I was in college I would build a study agent.'))
        self.assertNotIn('walkthrough', patterns('Services:\n1) Assessment: $999.\n2) Concierge: $1000.'))
        self.assertIn('story', patterns('I worked a summer job. That is part of my background.'))

    def test_missing_zero_views_are_unknown_not_poor_performance(self):
        for views in (None, 0):
            post = self.post('unknown', 'top', 500, views=views)
            data = performance(post)
            self.assertIsNone(data['views_for_ratios'])
            self.assertIsNone(data['ratios']['likes_per_view'])
            self.assertFalse(data['comparable_within_format'])
            self.assertEqual(select([(1, post)], mode='best'), [])

    def test_ratios_and_original_metrics_preserved(self):
        post = self.post('ratio')
        before = json.dumps(post, sort_keys=True)
        data = performance(post)
        self.assertEqual(data['ratios']['likes_per_view'], .1)
        self.assertEqual(data['raw_metrics']['views'], 1000)
        self.assertEqual(json.dumps(post, sort_keys=True), before)

    def test_best_uses_comparable_baseline_not_raw_likes(self):
        winner = self.post('winner', 'top', 5, likes=10)
        popular = self.post('popular', 'typical', 1, likes=10000)
        rough = self.post('rough', 'unranked', 999, perf_basis='all posts (rough)')
        chosen = select([(1, p) for p in (popular, rough, winner)], k=2, mode='best')
        self.assertEqual([c['post']['id'] for c in chosen], ['winner', 'popular'])

    def test_exact_format_filter_and_representative_mode(self):
        posts = [self.post('long'), self.post('short', format='short')]
        results = retrieve.reference_examples(posts, 'workflow', fmt='short', mode='representative')
        self.assertEqual([p['id'] for p in results], ['short'])

    def test_no_relevant_reference_falls_back_honestly(self):
        packet = retrieve.request_packet(read_profile(), [self.post('none', text='Unrelated plain sentence.')],
                                        {'topic': 'zyzzqx', 'category': 'founder_journey'})
        self.assertEqual(packet['examples'], [])
        self.assertIn('No relevant', packet['fallback'])

    def test_short_copied_sentence_and_reordered_near_duplicate(self):
        post = self.post('source', text='Please check the source before sending. Another unrelated section follows.')
        report = retrieve.overlap_report('Please check the source before sending. A fresh ending here.', [post])
        self.assertLess(report['longest_shared_run'], 8)
        self.assertTrue(report['copied_sentence_candidates'])
        self.assertTrue(report['flagged'])
        text = 'Alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu.'
        report = retrieve.overlap_report('Mu lambda kappa iota theta eta zeta epsilon delta gamma beta alpha.',
                                        [self.post('reordered', text=text)])
        self.assertTrue(report['lexical_near_duplicates'])

    def test_history_repetition_and_generated_not_training(self):
        history = [self.post(str(i), text='A separate task has a different description.',
                    record_kind='draft_history', hook_pattern='demonstration') for i in range(3)]
        result = retrieve.overlap_report('Give the agent a bounded job and inspect its result.', history)
        self.assertNotIn('demonstration', result['repeated_recent_patterns'])
        for i, row in enumerate(history):
            row['text'] += f' Distinct example {i}.'
        result = retrieve.overlap_report('Give the agent a bounded job and inspect its result.', history)
        self.assertIn('demonstration', result['repeated_recent_patterns'])
        draft = self.work / 'draft.txt'; draft.write_text('A generated fixture with a practical review step.')
        profile = dict(read_profile(), draft_history=str(self.work / 'history.jsonl'))
        args = argparse.Namespace(draft_file=str(draft), status='generated', approved_by_owner=False,
            verified_published=False, date=None, source_url=None, authorship='AI_generated', category='practical_education',
            format='long', hook_pattern='explanation', parent_id=None)
        with self.assertRaises(ValueError):
            retrieve.record_draft(dict(profile, draft_history=profile['own_corpus']), args)
        record = retrieve.record_draft(profile, args)
        self.assertFalse(record['measurement_eligible'])
        data = retrieve.load(self.work / 'history.jsonl')
        self.assertFalse(data[0]['verified_original'])
        self.assertEqual(data[0]['status'], 'generated')
        loaded, _ = retrieve.load_sources(profile, source='own', include_history=True)
        history_record = next(p for p in loaded if p.get('record_kind') == 'draft_history')
        self.assertIn('AI_generated for donovin-sims', history_record['_reference_author'])
        self.assertIn('nontraining', history_record['_reference_author'])
        retrieve.record_draft(profile, args)
        self.assertEqual(len(retrieve.load(self.work / 'history.jsonl')), 1)
        args.status = 'approved_edit'
        with self.assertRaises(ValueError):
            retrieve.record_draft(profile, args)
        args.approved_by_owner = True
        retrieve.record_draft(profile, args)
        self.assertEqual([x['status'] for x in retrieve.load(self.work / 'history.jsonl')], ['generated', 'approved_edit'])
        args.status = 'published'
        with self.assertRaises(ValueError):
            retrieve.record_draft(profile, args)
        args.verified_published = True; args.date = '2026-11-01'
        args.source_url = 'https://x.com/donovinsims/status/123'
        retrieve.record_draft(profile, args)
        self.assertFalse(retrieve.load(self.work / 'history.jsonl')[-1]['verified_original'])

    def test_output_cannot_overwrite_reference_or_escape_project(self):
        for path in (ROOT / 'voice-clone/profiles/corey-ganim/data/corpus.jsonl',
                     ROOT / 'docs/canonical/tree.json', ROOT.parent / 'outside-output.json'):
            with self.assertRaises(ValueError):
                retrieve.safe_output(path)

    def test_batch_context_and_attribution(self):
        requests = self.work / 'requests.json'
        requests.write_text(json.dumps([{'topic': 'workflow', 'category': 'practical_education', 'audience': 'A'},
                                       {'topic': 'operations', 'category': 'business_operations', 'audience': 'B'}]))
        output = self.work / 'packets.json'
        result = self.cli('brief', '--batch-file', requests, '--out', output)
        self.assertEqual(result.returncode, 0, result.stderr)
        packets = json.loads(output.read_text())
        self.assertEqual([p['request']['audience'] for p in packets], ['A', 'B'])
        corpus = {p['id']: p for p in retrieve.load(ROOT / read_profile()['reference_corpora'][0]['path'])}
        for packet in packets:
            self.assertEqual(packet['identity'], 'Donovin Sims')
            self.assertGreaterEqual(len(packet['examples']), 3)
            for item in packet['examples']:
                self.assertFalse(corpus[item['id']]['holdout'])
                self.assertEqual(item['text'], corpus[item['id']]['text'])
                self.assertEqual(item['author_id'], 'corey-ganim')
                self.assertIn('coreyganim/status/', item['source_url'])

    def test_batch_overlap_compares_other_batch_drafts(self):
        empty = self.work / 'empty.jsonl'; empty.write_text('')
        a = self.work / 'a.txt'; b = self.work / 'b.txt'
        a.write_text('One two three four five six seven eight nine ten.')
        b.write_text(a.read_text())
        result = self.cli('overlap', empty, '--draft-files', a, b, '--strict', '--json')
        self.assertEqual(result.returncode, 1, result.stderr)
        reports = json.loads(result.stdout)
        self.assertFalse(reports[0]['flagged'])
        self.assertTrue(reports[1]['flagged'])


if __name__ == '__main__':
    unittest.main()
