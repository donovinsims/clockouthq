"""Explainable, read-only annotations for reference selection; no model or API."""
import math
import re

PATTERNS = ('walkthrough', 'explanation', 'demonstration', 'story', 'argument', 'cta')
CATEGORY_PATTERNS = {
    'practical_education': ('walkthrough', 'explanation'),
    'agents_tools_builds': ('walkthrough', 'demonstration'),
    'business_operations': ('explanation', 'argument', 'demonstration'),
    'founder_journey': ('story',),
}
METRICS = ('views', 'likes', 'reposts', 'replies_n', 'quotes', 'bookmarks')


def positive(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value > 0


def patterns(text):
    """Observable signals, not authoritative rhetorical or quality classifications."""
    result = []
    numbered = re.findall(r'^\s*\d+[.)]\s*(.+)', text, re.M)
    action = r'\b(?:ask|give|open|create|upload|build|run|check|test|connect|point|make|use|set|choose|map|record|feed|generate|list|write|turn|send|review|compare|find|define|copy|identify|audit|optimize|automate|clean|collect|supply)\b'
    if sum(bool(re.search(action, line[:90], re.I)) for line in numbered) >= 2:
        result.append('walkthrough')
    if re.search(r"\b(?:here.s how|how to|for example|here.s the|because|means that)\b", text, re.I):
        result.append('explanation')
    if re.search(r'\b(?:trigger|input|output|workflow|agent|bot|automation|demo|skill)\b', text, re.I):
        result.append('demonstration')
    opening = text.lstrip()[:400]
    hypothetical = re.match(r"(?:if I|if we|imagine|suppose)\b", opening, re.I)
    prompt_template = re.search(r'\b(?:exact prompt|paste this|bot description|template)\b', opening[:160], re.I)
    if not hypothetical and not prompt_template and re.search(r"\b(?:I|we)\s+(?:was|were|worked|spent|started|built|met|visited|learned|grew|played|graduated|left|used to|tested|underpriced|had)\b", opening, re.I):
        result.append('story')
    if re.search(r"\b(?:instead|but|rather than|stop|don't|not AI|the problem)\b", text, re.I):
        result.append('argument')
    if re.search(r'\b(?:download|watch|join|subscribe|bookmark|link|DM|reply)\b', text.strip().split('\n')[-1], re.I):
        result.append('cta')
    return result


def category_compatible(text, category):
    """Avoid obvious sales-coaching menus in instructional retrieval only.

    The full library remains available through unrestricted search. This gate
    cannot determine every semantic fit; the editor still inspects each source.
    """
    if category in ('practical_education', 'agents_tools_builds', 'business_operations'):
        opening = text[:400]
        if re.search(r'AI (?:consulting clients|services free course|services businesses)|\b(?:MRR|retainers?|lead magnet|meetup|workshop)\b|\b(?:sell|selling|charge|charging)\b', opening, re.I):
            return False
        if re.search(r'^\s*\d+ AI services\b|^Pick your first AI service\b', opening, re.I):
            return False
    return True


def performance(post):
    raw = {k: post.get(k) for k in METRICS}
    views = raw['views'] if positive(raw['views']) else None
    # The legacy normalized corpus uses zero for some absent fields. Preserve it
    # in raw_metrics, but never turn an ambiguous zero into an exposure estimate.
    ratios = {k + '_per_view': raw[k] / views if views and positive(raw[k]) else None
              for k in METRICS if k != 'views'}
    comparable = bool(views and positive(post.get('perf'))
                      and post.get('perf_basis') == post.get('format')
                      and post.get('tier') != 'unranked')
    return {
        'raw_metrics': raw, 'views_for_ratios': views,
        'views_status': 'positive_snapshot' if views else 'unknown_or_ambiguous_zero',
        'ratios': ratios, 'ratios_definition': 'individual count / views; fractions, not percentages or unique-person engagement rates',
        'stored_relative_performance': post.get('perf'),
        'stored_baseline': post.get('baseline'), 'stored_basis': post.get('perf_basis'),
        'comparable_within_format': comparable,
        'limitations': 'Historical uneven snapshots; capture age often unknown. Ratios do not correct all exposure differences. Zero-valued legacy numerators may be missing. No causal or virality inference.',
    }


def techniques(post):
    lines = [line.strip() for line in post['text'].splitlines() if line.strip()]
    stats = post.get('stats', {})
    return {
        'signals': patterns(post['text']),
        'opening_shape': stats.get('opener', 'inspect source opening'),
        'ending_shape': stats.get('ender', 'inspect source ending'),
        'paragraph_blocks': len(re.split(r'\n\s*\n', post['text'].strip())),
        'numbered_step_lines': len(re.findall(r'^\s*\d+[.)]', post['text'], re.M)),
        'short_line_count_under_8_words': sum(len(line.split()) < 8 for line in lines),
        'editor_task': 'Inspect hook, rhythm, progression, specificity, demonstration and ending; extract construction, then use a fresh Donovin angle. These signals are not a semantic analysis.',
    }


def select(scored, k=4, category=None, pattern=None, mode='balanced'):
    """Format is filtered upstream. Structure, source completeness, then topic.

    Performance only selects a stronger example within a relevant shortlist;
    everyday and contrasting examples retain slots. No blended virality score.
    """
    wanted = (pattern,) if pattern else CATEGORY_PATTERNS.get(category, ())
    candidates, seen = [], set()
    for similarity, post in scored:
        identity = (post.get('_reference_author'), post['id'])
        if identity in seen:
            continue
        seen.add(identity)
        tags = patterns(post['text'])
        matches = [tag for tag in wanted if tag in tags]
        if not category_compatible(post['text'], category):
            continue
        if pattern and pattern not in tags:
            continue
        if category == 'founder_journey' and 'story' not in tags:
            continue
        if similarity <= 0 and not matches:
            continue
        candidates.append({'post': post, 'topic_similarity': similarity,
                           'matching_patterns': matches, 'patterns': tags,
                           'complete_text': not post['text'].rstrip().endswith(('…', '...'))})
    candidates.sort(key=lambda c: (bool(c['matching_patterns']), c['complete_text'],
                                   c['topic_similarity'], c['post'].get('date') or ''), reverse=True)
    shortlist = candidates[:max(12, k * 3)]
    chosen = []

    def add(candidate, reason):
        if candidate not in chosen and len(chosen) < k:
            candidate['selection_reason'] = reason
            chosen.append(candidate)

    def best(pool):
        eligible = [c for c in pool if performance(c['post'])['comparable_within_format']]
        # Without a single format, retain relevance first: format-relative values
        # across mixed formats are not treated as interchangeable quality scores.
        if len({c['post'].get('format') for c in eligible}) > 1:
            return eligible
        return sorted(eligible, key=lambda c: c['post']['perf'], reverse=True)

    if mode == 'best':
        for c in best(shortlist):
            add(c, 'comparable historical performance within relevant shortlist')
        return chosen
    if mode == 'representative':
        for c in candidates:
            if c['post'].get('tier') == 'typical':
                add(c, 'representative everyday reference')
        return chosen
    if mode == 'balanced':
        # Reserve one stronger slot only when the relevant shortlist supports it.
        relevant_top = [c for c in shortlist if c['post'].get('tier') == 'top']
        stronger = [c for c in relevant_top if performance(c['post'])['comparable_within_format']]
        if stronger:
            add(stronger[0], 'one stronger relevant historical reference')
        for c in shortlist:
            if c['post'].get('tier') == 'typical' and len(chosen) < min(k, 3):
                add(c, 'representative everyday reference')
        if k >= 4:
            weaker = next((c for c in shortlist if c['post'].get('tier') == 'weak'), None)
            if weaker:
                add(weaker, 'relevant lower-performing contrast; inspect differences, do not infer cause')
    for c in candidates:
        add(c, 'structural/topic relevance; performance not required')
    return chosen


def example(candidate):
    post = candidate['post']
    author = post.get('_reference_author', post.get('author_id', 'unknown'))
    url = post.get('source_url')
    derived = False
    if not url and author == 'corey-ganim':
        url = 'https://x.com/coreyganim/status/' + post['id']
        derived = True
    return {'author_id': author, 'id': post['id'], 'source_url': url,
            'source_url_origin': 'derived from preserved author and ID' if derived else 'source record',
            'date': post.get('date'), 'format': post.get('format'), 'tier': post.get('tier'),
            'text': post['text'], 'topic_similarity': candidate['topic_similarity'],
            'selection_reason': candidate['selection_reason'],
            'source_quality': 'no terminal truncation marker detected' if candidate['complete_text'] else 'possible excerpt; inspect full archive before using structure',
            'matching_patterns': candidate['matching_patterns'],
            'techniques': techniques(post), 'performance': performance(post),
            'use': 'STYLE AND STRUCTURE ONLY; no identity, anecdotes, claims, positions or offers transferred'}
