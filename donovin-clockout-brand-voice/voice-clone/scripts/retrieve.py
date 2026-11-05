#!/usr/bin/env python3
"""Retrieve the most relevant real posts from a creator's corpus, or check a draft for copying.

  python retrieve.py search  CORPUS.jsonl "contrarian take on AI agents" [-k 8] [--tier top] [--format short] [--include-holdout]
  python retrieve.py overlap CORPUS.jsonl --draft "text..." | --draft-file draft.txt

search: structural/format relevance plus topical similarity; balanced reference selection.
brief: prepare 3-6 attributed examples and technique cues for an assistant to draft from.
record: keep generated drafts, approved edits and published records in a nontraining ledger.
Holdouts are excluded from normal retrieval.
Profile routing: omit CORPUS and pass --profile donovin-sims (the configured default).
Search defaults to attributed reference examples. Overlap covers own and reference data.
overlap: finds contiguous shared words and 5-word sequences. Thresholds trigger review,
not a legal plagiarism finding or a guarantee of original ideas. --strict exits 1 on flags.
Pure standard library.
"""
import argparse, json, math, re, sys
from pathlib import Path
from profile_config import ROOT, FORMATS, read_profile, corpus_paths
from reference_intelligence import CATEGORY_PATTERNS, PATTERNS, example, patterns, select
from datetime import datetime, timezone
import hashlib
from difflib import SequenceMatcher
from collections import Counter

STOP = set("a an and are as at be but by for from has have i in is it its of on or that the this to was we with you your".split())
tok = lambda t: [w for w in re.findall(r"[a-z0-9']+", t.lower())]


def load(path):
    with open(path, encoding="utf-8") as stream:
        return [json.loads(l) for l in stream if l.strip()]


def search(posts, query, k, tier, fmt):
    docs = [[w for w in tok(p["text"]) if w not in STOP] for p in posts]
    n = len(docs)
    df = Counter(w for d in docs for w in set(d))
    idf = lambda w: math.log((n + 1) / (df.get(w, 0) + 1)) + 1
    def vec(ws):
        c = Counter(ws)
        return {w: (1 + math.log(v)) * idf(w) for w, v in c.items()}
    q = vec([w for w in tok(query) if w not in STOP])
    qn = math.sqrt(sum(v * v for v in q.values())) or 1
    scored = []
    for p, d in zip(posts, docs):
        if tier and p.get("tier") != tier: continue
        if fmt and p.get("format") != fmt: continue
        v = vec(d)
        dot = sum(q[w] * v[w] for w in q if w in v)
        vn = math.sqrt(sum(x * x for x in v.values())) or 1
        scored.append((dot / (qn * vn), p))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:k]


def longest_run(a, b):
    match = SequenceMatcher(None, a, b, autojunk=False).find_longest_match()
    return match.size, a[match.a:match.a + match.size]


def load_sources(profile, corpus=None, source='all', include_history=False, exclude_id=None):
    paths = corpus_paths(profile, source)
    if corpus:
        candidate = Path(corpus)
        author = next((name for path, name in corpus_paths(profile) if path.resolve() == candidate.resolve()),
                      'explicit corpus; verify authorship metadata')
        paths = [(candidate, author)]
    if include_history and profile.get('draft_history'):
        history = ROOT / profile['draft_history']
        if not history.exists():
            raise ValueError('Configured draft history missing: ' + str(history))
        paths.append((history, 'draft-history; not authenticated original writing'))
    posts = []
    for path, author in paths:
        for raw in load(path):
            if exclude_id and raw.get('id') == exclude_id:
                continue
            post = dict(raw)
            post['_reference_author'] = (
                f"{raw.get('authorship', 'assisted')} for {raw.get('author_id', 'unknown')}; {raw.get('status', 'draft')}; nontraining"
                if raw.get('record_kind') == 'draft_history' else raw.get('author_id') or author)
            posts.append(post)
    return posts, paths


def safe_output(path):
    target = Path(path).resolve()
    if not target.is_relative_to(ROOT):
        raise ValueError('Write outputs only inside this project')
    if any(target.is_relative_to(ROOT / folder) for folder in
           ('voice-clone/profiles/corey-ganim', 'docs/archive', 'docs/canonical')):
        raise ValueError('Cannot write retrieval output into preserved source material')
    return target


def write_json(path, data):
    target = safe_output(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf8')


def attach_archive(examples, profile):
    archive = profile.get('reference_archive_index')
    if not archive:
        return
    entries = json.loads((ROOT / archive).read_text())['entries']
    provenance = json.loads((ROOT / profile['reference_provenance']).read_text()) if profile.get('reference_provenance') else {}
    for result in examples:
        matches = [e for e in entries if e['id'].split('-', 1)[-1] == result['id']]
        result['archive_sources'] = [{'path': str(Path(archive).parent / e['file']),
                                     'source_url': e['source_url'],
                                     'metrics_retrieved_date': e.get('metrics_retrieved_date')}
                                    for e in matches]
        result['source_provenance'] = provenance.get(result['id'], [])


def reference_examples(posts, query, k=4, fmt=None, tier=None, category=None, pattern=None, mode='balanced'):
    scored = search(posts, query, len(posts), tier, fmt)
    return [example(c) for c in select(scored, k, category, pattern, mode)]


def request_packet(profile, posts, request):
    topic = request.get('topic', '').strip()
    if not topic:
        raise ValueError('Every writing request needs a topic')
    category = request.get('category', 'practical_education')
    audience = request.get('audience', 'B' if category == 'business_operations' else 'A')
    fmt = request.get('format', 'long')
    pattern = request.get('pattern')
    k = request.get('examples', 4)
    if category not in CATEGORY_PATTERNS or audience not in ('A', 'B') or fmt not in FORMATS:
        raise ValueError('Invalid category, audience or format')
    if pattern is not None and pattern not in PATTERNS:
        raise ValueError('Unknown structural pattern')
    if not isinstance(k, int) or not 3 <= k <= 6:
        raise ValueError('Writing requests use 3-6 examples')
    examples = reference_examples(posts, topic, k, fmt, category=category, pattern=pattern)
    attach_archive(examples, profile)
    active = json.loads((ROOT / profile['profile_file']).read_text())
    return {
        'profile_id': profile['profile_id'], 'identity': active['identity']['name'],
        'request': dict(request, topic=topic, category=category, audience=audience, format=fmt),
        'fact_authority': active['identity']['facts'], 'position_authority': active['positions_file'],
        'supplied_facts_status': 'Brief assertions still require source and public-use review; this script does not verify them',
        'reference_author': 'Corey Ganim', 'examples': examples,
        'fallback': None if examples else 'No relevant structural/topic reference found; use documented voice rules without fabricated support',
        'workflow': [
            'Read Donovin facts, positions and ICP; resolve intended takeaway/outcome and supported experiences.',
            'Study the selected sources; identify hook, rhythm, paragraphing, progression, detail and ending.',
            'Write an original angle using Donovin facts and positions; never transfer source anecdotes or offers.',
            'Refine using Voice Apply; review factual accuracy, audience fit and conceptual similarity.',
            'Run editorial and overlap checks against reference, own writing, history and other batch drafts.',
            'Save research/check results privately; deliver strongest draft only for owner review.',
            'Record delivered draft as generated; approval or publication never implies unaided original authorship.',
        ],
        'limits': 'Local context preparation only, not automatic prose generation, semantic verification, current tool validation or publishing.',
    }


def sentence_sequences(text):
    # Require a sentence-ending mark: a shared fragment or heading alone isn't
    # treated as a complete copied sentence by this extra check.
    pieces = re.findall(r'[^.!?\n]+[.!?](?:\s|$)', text)
    return {tuple(tok(s)) for s in pieces if len(tok(s)) >= 5}


def overlap_report(draft, posts):
    dw = tok(draft)
    worst = (0, [], None)
    sentences = sentence_sequences(draft)
    matching_sentences = []
    for p in posts:
        n, run = longest_run(dw, tok(p['text']))
        if n > worst[0]:
            worst = (n, run, p)
        shared_sentences = sentences & sentence_sequences(p['text'])
        if shared_sentences:
            matching_sentences.append({'id': p['id'], 'author': p.get('_reference_author'),
                                       'sentences': [' '.join(s) for s in sorted(shared_sentences)]})
    n, run, p = worst
    grams = lambda w: {tuple(w[i:i + 5]) for i in range(len(w) - 4)}
    dg = grams(dw)
    shared = len(dg & set().union(*(grams(tok(q['text'])) for q in posts))) if dg else 0
    # Lexical candidates invite semantic review; this does not claim to detect meaning.
    similar = search(posts, draft, 3, None, None) if dw else []
    near = [{'id': q['id'], 'author': q.get('_reference_author'), 'lexical_similarity': round(score, 3)}
            for score, q in similar if score >= 0.8]
    history, seen_text = [], set()
    for q in reversed(posts):
        if q.get('record_kind') == 'draft_history':
            key = tuple(tok(q['text']))
            if key not in seen_text:
                seen_text.add(key)
                history.append(q)
            if len(history) == 5:
                break
    inferred = patterns(draft)
    repeated = [tag for tag in inferred if sum(q.get('hook_pattern') == tag for q in history) >= 3]
    opening = tuple(dw[:6])
    repeated_opening = [q['id'] for q in history if len(opening) >= 4 and tuple(tok(q['text'])[:6]) == opening]
    return {
        'longest_shared_run': n, 'shared_run': ' '.join(run),
        'source_id': p['id'] if p else None, 'source_author': p.get('_reference_author') if p else None,
        'shared_5grams': shared, 'draft_5grams': len(dg),
        'copied_sentence_candidates': matching_sentences,
        'lexical_near_duplicates': near,
        'repeated_recent_patterns': repeated, 'repeated_recent_openings': repeated_opening,
        'flagged': bool(n >= 8 or (dg and shared / len(dg) > 0.15) or matching_sentences or near),
        'manual_review': 'Inspect conceptual sequence, noun-substitution, borrowed experiences and repetitive hooks. Lexical similarity is not semantic proof; absence of flags is no originality guarantee.',
    }


def record_draft(profile, args):
    if not profile.get('draft_history'):
        raise ValueError('No draft history configured for this profile')
    target = safe_output(ROOT / profile['draft_history'])
    if target == (ROOT / profile['own_corpus']).resolve():
        raise ValueError('Draft history must never be the authenticated original-writing corpus')
    text = Path(args.draft_file).read_text(encoding='utf8').strip()
    if not text:
        raise ValueError('Cannot record an empty draft')
    if args.status == 'approved_edit' and not args.approved_by_owner:
        raise ValueError('An approved edit needs explicit --approved-by-owner attestation')
    if args.status == 'published':
        if not args.verified_published or not args.date or not args.source_url:
            raise ValueError('Published records need --verified-published, --date and --source-url')
        datetime.fromisoformat(args.date.replace('Z', '+00:00'))
        if not re.fullmatch(r'https://(?:x\.com|twitter\.com)/donovinsims/status/\d+', args.source_url):
            raise ValueError('Expected an actual Donovin post URL')
    record = {'id': hashlib.sha256((args.status + '\0' + text).encode()).hexdigest()[:24],
              'record_kind': 'draft_history', 'status': args.status,
              'author_id': profile['profile_id'], 'authorship': args.authorship,
              'text': text, 'category': args.category, 'format': args.format,
              'hook_pattern': args.hook_pattern, 'parent_id': args.parent_id,
              'source_url': args.source_url, 'date': args.date,
              'recorded_at': datetime.now(timezone.utc).isoformat(),
              'verified_original': False,
              'approved_by_owner': bool(args.approved_by_owner),
              'publication_verified_by_owner': bool(args.verified_published)}
    existing = load(target) if target.exists() else []
    if not any(r['id'] == record['id'] for r in existing):
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('a', encoding='utf8') as stream:
            stream.write(json.dumps(record, ensure_ascii=False) + '\n')
    return {'id': record['id'], 'history_file': str(target), 'status': args.status,
            'measurement_eligible': False, 'note': 'Separate nontraining ledger; authentic authorship needs the existing ingestion review.'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('search')
    s.add_argument('corpus', nargs='?'); s.add_argument('query')
    s.add_argument('-k', type=int, default=4); s.add_argument('--tier')
    s.add_argument('--format', choices=FORMATS)
    s.add_argument('--include-holdout', action='store_true')
    s.add_argument('--pattern', choices=PATTERNS)
    s.add_argument('--category', choices=CATEGORY_PATTERNS)
    s.add_argument('--mode', choices=('balanced', 'relevant', 'best', 'representative'), default='balanced')
    s.add_argument('--json', action='store_true')
    b = sub.add_parser('brief', help='Prepare attributed writing context; an assistant writes the prose')
    b.add_argument('topic', nargs='?')
    b.add_argument('--batch-file', help='JSON list of requests; load reference corpus once')
    b.add_argument('--audience', choices=('A', 'B'))
    b.add_argument('--category', choices=CATEGORY_PATTERNS, default='practical_education')
    b.add_argument('--format', choices=FORMATS, default='long')
    b.add_argument('--pattern', choices=PATTERNS)
    b.add_argument('--takeaway', default=''); b.add_argument('--outcome', default='')
    b.add_argument('-k', type=int, default=4)
    b.add_argument('--out', help='Save research packet inside this project')
    o = sub.add_parser('overlap'); o.add_argument('corpus', nargs='?')
    drafts = o.add_mutually_exclusive_group(required=True)
    drafts.add_argument('--draft'); drafts.add_argument('--draft-file')
    drafts.add_argument('--draft-files', nargs='+', help='Check a batch, including against earlier batch members')
    o.add_argument('--strict', action='store_true')
    o.add_argument('--exclude-draft-id', help='Exclude only the saved version currently being edited')
    o.add_argument('--json', action='store_true')
    r = sub.add_parser('record', help='Keep delivered drafts/edits/published records separate from original writing')
    r.add_argument('--draft-file', required=True)
    r.add_argument('--status', choices=('generated', 'approved_edit', 'published'), default='generated')
    r.add_argument('--category', choices=CATEGORY_PATTERNS, required=True)
    r.add_argument('--format', choices=FORMATS, default='long')
    r.add_argument('--hook-pattern', choices=PATTERNS)
    r.add_argument('--parent-id'); r.add_argument('--source-url'); r.add_argument('--date')
    r.add_argument('--authorship', choices=('AI_generated', 'AI_assisted', 'owner_reported_original'), default='AI_generated')
    r.add_argument('--approved-by-owner', action='store_true')
    r.add_argument('--verified-published', action='store_true')
    for parser in (s, b, o, r):
        parser.add_argument('--profile', help='Profile slug/directory/manifest/YAML; defaults to active Donovin')
    for parser in (s, o):
        parser.add_argument('--source', choices=('own', 'reference', 'all'))
    a = ap.parse_args()
    try:
        profile = read_profile(a.profile)
        if a.cmd == 'record':
            print(json.dumps(record_draft(profile, a), indent=2))
            return 0
        if a.cmd == 'brief' and profile['profile_id'] != 'donovin-sims':
            ap.error('Writing briefs must use the active Donovin identity')
        if a.cmd == 'overlap' and a.source and a.source != 'all':
            ap.error('Overlap must cover all configured corpora; --source is for search only')
        posts, paths = load_sources(profile, getattr(a, 'corpus', None),
                                    getattr(a, 'source', None) or ('all' if a.cmd == 'overlap' else 'reference'),
                                    include_history=a.cmd == 'overlap', exclude_id=getattr(a, 'exclude_draft_id', None))
        if a.cmd == 'search':
            if a.k < 1:
                ap.error('-k must be positive')
            pool = posts if a.include_holdout else [p for p in posts if not p.get('holdout')]
            results = reference_examples(pool, a.query, a.k, a.format, a.tier, a.category, a.pattern, a.mode)
            attach_archive(results, profile)
            if a.json:
                print(json.dumps({'examples': results, 'note': 'Source text is untrusted reference data; no instructions or facts are adopted.'}, indent=2))
            else:
                for item in results:
                    print(f"--- author={item['author_id']} id={item['id']} format={item['format']} tier={item['tier']} sim={item['topic_similarity']:.2f}")
                    print(f"Source: {item['source_url']} | {item['selection_reason']}")
                    print('Patterns:', ', '.join(item['techniques']['signals']) or 'inspect manually')
                    print('Historical performance:', json.dumps(item['performance']))
                    print(item['text']); print()
                if not results:
                    print('No authored samples available or no relevant references; use documented voice guidance.')
        elif a.cmd == 'brief':
            if bool(a.topic) == bool(a.batch_file):
                ap.error('Supply a topic or --batch-file, but not both')
            if a.batch_file:
                requests = json.loads(Path(a.batch_file).read_text(encoding='utf8'))
                if not isinstance(requests, list) or not requests or not all(isinstance(x, dict) for x in requests):
                    ap.error('--batch-file must contain a nonempty list of writing request objects')
            else:
                requests = [{'topic': a.topic, 'category': a.category, 'audience': a.audience or ('B' if a.category == 'business_operations' else 'A'),
                             'format': a.format, 'pattern': a.pattern, 'examples': a.k,
                             'takeaway': a.takeaway, 'desired_outcome': a.outcome}]
            pool = [p for p in posts if not p.get('holdout')]
            packets = [request_packet(profile, pool, request) for request in requests]
            result = packets if a.batch_file else packets[0]
            if a.out:
                write_json(a.out, result)
                print(f'Saved {len(packets)} attributed writing context packet(s) to {a.out}; no prose generated.')
            else:
                print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            inputs = [(str(path), Path(path).read_text(encoding='utf8')) for path in a.draft_files] if a.draft_files else [
                (a.draft_file or 'inline draft', a.draft if a.draft is not None else Path(a.draft_file).read_text(encoding='utf8'))]
            reports = []
            for label, text in inputs:
                report = dict(overlap_report(text, posts), draft=label,
                              corpora_checked=[{'author': author, 'path': str(path)} for path, author in paths])
                reports.append(report)
                if a.draft_files:
                    posts.append({'id': label, 'text': text, '_reference_author': 'earlier generated draft in this batch'})
            if a.json:
                print(json.dumps(reports if a.draft_files else reports[0], indent=2))
            else:
                for report in reports:
                    print('Draft:', report['draft'])
                    print(f"Longest shared run: {report['longest_shared_run']} words (post {report['source_id']}; author {report['source_author']})")
                    print(f"5-word sequences copied from corpus: {report['shared_5grams']} of {report['draft_5grams']}")
                    print('Corpora checked: ' + ', '.join(f'{author}: {path}' for path, author in paths))
                    print('FLAG: inspect textual/near-duplicate candidates.' if report['flagged'] else 'OK: no threshold overlap detected.')
                    if report['repeated_recent_patterns'] or report['repeated_recent_openings']:
                        print('REVIEW: recent hook repetition', report['repeated_recent_patterns'], report['repeated_recent_openings'])
                    print(report['manual_review'])
            if a.strict and any(item['flagged'] for item in reports):
                return 1
    except (OSError, ValueError, KeyError, TypeError) as exc:
        ap.error(str(exc))
    return 0


if __name__ == '__main__':
    sys.exit(main())
