#!/usr/bin/env python3
"""Normalize scraped X posts, score each against the creator's OWN baseline,
and measure the voice.

Usage:
  python ingest.py RAW.json|RAW.csv --out profiles/NAME/data [--holdout 10] [--seed 7]
                   [--tag-all thread|article|long] [--merge profiles/NAME/data/corpus.jsonl]

Outputs in --out: corpus.jsonl, replies.jsonl, stats.json, stats.md, ingest-report.txt
Pure standard library. Field names are auto-detected (Scrape Creators, X API, CSV exports).
"""
import argparse, csv, json, math, random, re, statistics as st, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ALIASES = {
    "id": ["id", "id_str", "rest_id", "tweet_id", "post_id"],
    "text": ["full_text", "text", "content", "tweet", "body", "note_tweet_text"],
    "date": ["created_at", "date", "timestamp", "posted_at", "time", "created"],
    "likes": ["favorite_count", "likes", "like_count", "favorites"],
    "reposts": ["retweet_count", "reposts", "repost_count", "retweets"],
    "replies": ["reply_count", "replies", "reply_counts"],
    "quotes": ["quote_count", "quotes"],
    "bookmarks": ["bookmark_count", "bookmarks"],
    "views": ["views", "view_count", "impressions", "impression_count", "views_count"],
}
STOP = set("""a about after all also am an and any are as at be because been but by can could did do does
for from had has have he her him his how i if in into is it its just me more my no not of on one or our
out so some than that the their them then there these they this to up us was we were what when which who
will with would you your""".split())
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\U0001F000-\U0001F2FF]")
URL = re.compile(r"https?://\S+")


def flatten(d):
    out = dict(d)
    for k in ("legacy", "tweet", "core"):
        if isinstance(d.get(k), dict):
            for kk, vv in d[k].items():
                out.setdefault(kk, vv)
    return out


def find_list(obj):
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict):
        for k in ("tweets", "posts", "data", "results", "items", "timeline"):
            if k in obj:
                r = find_list(obj[k])
                if r:
                    return r
        for v in obj.values():
            if isinstance(v, list) and v and isinstance(v[0], dict):
                return v
    return []


def load(path):
    p = Path(path)
    if p.suffix.lower() == ".csv":
        with open(p, newline="", encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))
    txt = p.read_text(encoding="utf-8")
    try:
        return find_list(json.loads(txt))
    except json.JSONDecodeError:
        return [json.loads(l) for l in txt.splitlines() if l.strip()]  # jsonl


def pick(d, key):
    for a in ALIASES[key]:
        if a in d and d[a] not in (None, ""):
            v = d[a]
            if isinstance(v, dict):
                v = v.get("count") or v.get("value") or 0
            return v
    return None


def num(v):
    try:
        return float(str(v).replace(",", ""))
    except (TypeError, ValueError):
        return 0.0


def parse_date(v):
    if v is None:
        return None
    s = str(v).strip()
    if re.fullmatch(r"\d{10,13}", s):
        n = int(s)
        return datetime.fromtimestamp(n / 1000 if n > 1e11 else n, tz=timezone.utc)
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except ValueError:
        pass
    for fmt in ("%a %b %d %H:%M:%S %z %Y", "%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(s.replace("Z", "+0000"), fmt)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    return None


def normalize(raw):
    d = flatten(raw)
    text = pick(d, "text")
    if not text:
        return None
    text = str(text).replace("\r\n", "\n").strip()
    is_rt = bool(d.get("is_retweet") or d.get("retweeted_status") or text.startswith("RT @"))
    is_reply = bool(d.get("in_reply_to_status_id") or d.get("in_reply_to_status_id_str")
                    or d.get("is_reply") or d.get("in_reply_to_screen_name") or text.startswith("@"))
    is_quote = bool(d.get("is_quote_status") or d.get("is_quote") or d.get("quoted_status"))
    dt = parse_date(pick(d, "date"))
    return {
        "id": str(pick(d, "id") or hash(text)),
        "date": dt.isoformat() if dt else None,
        "text": text,
        "likes": num(pick(d, "likes")), "reposts": num(pick(d, "reposts")),
        "replies_n": num(pick(d, "replies")), "quotes": num(pick(d, "quotes")),
        "bookmarks": num(pick(d, "bookmarks")), "views": num(pick(d, "views")),
        "is_retweet": is_rt, "is_reply": is_reply, "is_quote": is_quote,
        "format": d.get("format"),
    }


def drop_reason(p):
    t = URL.sub("", p["text"]).strip()
    low = p["text"].lower()
    if p["is_retweet"]: return "retweet"
    if len(t) < 15: return "link drop or too short"
    if re.search(r"giveaway|rt to win|retweet to win|comment .* to win", low): return "giveaway"
    return None


def words(t):
    return [w for w in (x.strip(".-") for x in re.findall(r"[A-Za-z0-9'$%@#.\-]+", t)) if w]


def sentences(t):
    parts = re.split(r"(?<=[.!?])\s+|\n+", t)
    return [s for s in parts if s.strip()]


def opener(t):
    first = t.strip().split("\n")[0].strip()
    if re.match(r"^[\$#]?\d", first): return "number"
    if first.endswith("?"): return "question"
    if first[:1] in "\"“'": return "quote"
    if re.match(r"^(i|i'm|i’ve|i've|my)\b", first.lower()): return "I-statement"
    if re.match(r"^(you|your|if you)\b", first.lower()): return "you-statement"
    if re.match(r"^(stop|don't|do|never|start|write|build|use|try|read)\b", first.lower()): return "command"
    return "statement"


def ender(t):
    last = t.strip().split("\n")[-1].strip()
    if last.endswith("?"): return "question"
    if re.search(r"\b(follow|repost|retweet|rt|dm|subscribe|comment|reply|bookmark|link in)\b", last.lower()):
        return "call-to-action"
    if EMOJI.search(last[-3:] if last else ""): return "emoji"
    if last and last[-1] not in ".!?\"”)": return "no-terminal-punctuation"
    return "statement"


def post_stats(t):
    w = words(t)
    s = sentences(t)
    sl = [len(words(x)) for x in s] or [0]
    return {
        "words": len(w), "avg_sentence": round(sum(sl) / len(sl), 1),
        "lines": t.count("\n") + 1, "blank_lines": t.count("\n\n"),
        "opener": opener(t), "ender": ender(t),
        "lower_start": t[:1].islower(), "em_dash": t.count("—"), "ellipsis": t.count("...") + t.count("…"),
        "exclaim": t.count("!"), "paren": t.count("("), "colon": t.count(":"),
        "hashtags": len(re.findall(r"#\w+", t)), "links": len(URL.findall(t)),
        "mentions": len(re.findall(r"@\w+", t)), "emoji": len(EMOJI.findall(t)),
        "caps_words": sum(1 for x in w if len(x) > 2 and x.isupper()),
        "contractions": len(re.findall(r"\b\w+['’](t|s|re|ve|ll|d|m)\b", t.lower())),
    }


def pct(vals, p):
    vals = sorted(vals)
    if not vals: return 0
    k = (len(vals) - 1) * p / 100
    f, c = math.floor(k), math.ceil(k)
    return round(vals[f] + (vals[c] - vals[f]) * (k - f), 1)


def measure(base):
    S = [p["stats"] for p in base]
    n = len(S)
    share = lambda k: round(100 * sum(1 for s in S if s[k]) / n)
    allw = [w.lower() for p in base for w in words(p["text"])]
    groups = {"I": {"i", "i'm", "i've", "i'll", "my", "me"}, "we": {"we", "we're", "our", "us"}, "you": {"you", "your", "you're"}}
    return {
        "posts": n,
        "words": {"p10": pct([s["words"] for s in S], 10), "median": pct([s["words"] for s in S], 50), "p90": pct([s["words"] for s in S], 90)},
        "avg_sentence_len": {"p10": pct([s["avg_sentence"] for s in S], 10), "median": pct([s["avg_sentence"] for s in S], 50), "p90": pct([s["avg_sentence"] for s in S], 90)},
        "lines_per_post": {"median": pct([s["lines"] for s in S], 50), "p90": pct([s["lines"] for s in S], 90)},
        "openers_pct": {k: round(100 * c / n) for k, c in Counter(s["opener"] for s in S).most_common()},
        "enders_pct": {k: round(100 * c / n) for k, c in Counter(s["ender"] for s in S).most_common()},
        "pct_posts_with": {k: share(k) for k in ("lower_start", "em_dash", "ellipsis", "exclaim", "paren", "colon", "hashtags", "links", "mentions", "emoji", "caps_words", "contractions")},
        "pronoun_counts": {k: sum(1 for w in allw if w in v) for k, v in groups.items()},
    }


def vocab(base):
    docs = [set(w.lower() for w in words(p["text"])) for p in base]
    df = Counter(w for d in docs for w in d if w not in STOP and len(w) > 2 and not w.startswith(("http", "@")))
    tri = Counter()
    for p in base:
        ws = [w.lower() for w in words(p["text"])]
        tri.update({" ".join(ws[i:i + 3]) for i in range(len(ws) - 2)
                    if not all(x in STOP for x in ws[i:i + 3])})
    floor = 3 if len(base) >= 30 else 2
    return {"top_words_by_posts": df.most_common(40),
            "top_trigrams_by_posts": [(k, c) for k, c in tri.most_common(60) if c >= floor][:25]}


def metric_fn(posts):
    has_views = sum(1 for p in posts if p["views"] > 0) > len(posts) / 2
    if has_views:
        return "views", lambda p: p["views"]
    return "weighted engagement", lambda p: p["likes"] + 2 * p["reposts"] + 2 * p["replies_n"] + p["quotes"] + p["bookmarks"]


def score(posts):
    """Score each post against the creator's own baseline FOR ITS FORMAT.
    A format with 10+ posts gets its own baseline and tiers. A smaller format (often threads or
    articles) is scored roughly against all posts and left 'unranked', because comparing a thread
    post to a short post isn't a fair test."""
    name, f = metric_fn(posts)
    for p in posts:
        p["metric"] = f(p)
    valid = [p for p in posts if p["metric"] > 0]
    counts = Counter(p["format"] for p in valid)
    for p in posts:
        own = counts[p["format"]] >= 10
        p["group"] = p["format"] if own else "all"
        p["perf_basis"] = p["format"] if own else "all posts (rough)"
    groups = {}
    for p in valid:
        groups.setdefault(p["group"], []).append(p)
    for g, ps in groups.items():
        ref = valid if g == "all" else ps
        dated = [q for q in ref if q["date"]]
        gmed = st.median([q["metric"] for q in ref]) or 1
        for p in ps:
            base = None
            if p["date"] and len(dated) >= 20:
                d0 = datetime.fromisoformat(p["date"])
                near = [q["metric"] for q in dated if q is not p
                        and abs((datetime.fromisoformat(q["date"]) - d0).days) <= 45]
                if len(near) >= 10:
                    base = st.median(near)
            p["baseline"] = base or gmed
            p["perf"] = round(p["metric"] / (p["baseline"] or 1), 2)
        if g == "all":
            for p in ps:
                p["tier"] = "unranked"
            continue
        ranked = sorted(ps, key=lambda p: p["perf"], reverse=True)
        n = len(ranked)
        top_n, weak_n = max(1, round(n * 0.12)), max(1, round(n * 0.10))
        top_ids = {id(p) for p in ranked[:top_n]}
        weak_ids = {id(p) for p in ranked[-weak_n:] if p["perf"] < 0.7}
        for p in ps:
            p["tier"] = "top" if id(p) in top_ids else "weak" if id(p) in weak_ids else "typical"
    for p in posts:
        if p["metric"] <= 0:
            p["perf"] = None
            p["baseline"] = None
            p["tier"] = "unranked"
            p["perf_basis"] = "missing view metric"
    return name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw"); ap.add_argument("--out", required=True)
    ap.add_argument("--holdout", type=int, default=10); ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--tag-all", default=None, help="force format tag: thread, article, long")
    ap.add_argument("--merge", default=None, help="existing corpus.jsonl to merge into")
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)

    raw = load(a.raw)
    norm = [x for x in (normalize(r) for r in raw if isinstance(r, dict)) if x]
    kept, replies, dropped = [], [], Counter()
    for p in norm:
        r = drop_reason(p)
        if r: dropped[r] += 1; continue
        if p["is_reply"]: replies.append(p); continue
        p["format"] = a.tag_all or p.get("format") or ("quote" if p["is_quote"] else "long" if len(p["text"]) > 280 else "short")
        kept.append(p)

    held = set()
    if a.merge and Path(a.merge).exists():
        old = [json.loads(l) for l in open(a.merge, encoding="utf-8") if l.strip()]
        held = {o["id"] for o in old if o.get("holdout")}
        have = {o["id"] for o in kept}
        kept += [o for o in old if o["id"] not in have]
    seen, uniq = set(), []
    for p in kept:
        if p["id"] in seen: continue
        seen.add(p["id"]); uniq.append(p)
    kept = uniq
    if not kept:
        sys.exit("No usable posts found. Check the file format and field names.")

    metric_name = score(kept)
    pool = [p for p in kept if p["id"] not in held]
    if not held and a.holdout and len(kept) >= 30:
        random.Random(a.seed).shuffle(pool)
        held = {p["id"] for p in pool[:a.holdout]}
    for p in kept:
        p["holdout"] = p["id"] in held
        p["stats"] = post_stats(p["text"])

    with open(out / "corpus.jsonl", "w", encoding="utf-8") as f:
        for p in sorted(kept, key=lambda x: x["date"] or ""):
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    with open(out / "replies.jsonl", "w", encoding="utf-8") as f:
        for p in replies: f.write(json.dumps(p, ensure_ascii=False) + "\n")

    # Voice measurements: everything except holdout, originals only, measured PER FORMAT.
    # Formats differ a lot (a 15-word post vs a 1,500-word article), so blended numbers mislead.
    base = [p for p in kept if not p["holdout"]]
    by_fmt = {}
    for p in base:
        by_fmt.setdefault(p["format"], []).append(p)
    MIN_FMT = 5
    stats = {
        "posts_measured": len(base), "holdout": len(held), "replies_separated": len(replies), "dropped": dict(dropped),
        "performance_metric": metric_name,
        "formats": {k: len(v) for k, v in by_fmt.items()},
        "tiers": dict(Counter(p["tier"] for p in kept)),
        "by_format": {k: measure(v) for k, v in by_fmt.items() if len(v) >= MIN_FMT},
        "too_few_to_measure": {k: len(v) for k, v in by_fmt.items() if len(v) < MIN_FMT},
        "all_formats_blended": measure(base),
        "vocabulary_all_formats": vocab(base),
    }
    for k, v in by_fmt.items():
        if len(v) >= 30:
            stats["by_format"][k]["vocabulary"] = vocab(v)
    (out / "stats.json").write_text(json.dumps(stats, indent=1, ensure_ascii=False))

    def block(title, m):
        return [f"## {title} ({m['posts']} posts)",
                f"- Words per post (p10 / median / p90): {m['words']}",
                f"- Avg sentence length (p10 / median / p90): {m['avg_sentence_len']}",
                f"- Lines per post (median / p90): {m['lines_per_post']}",
                f"- Openers %: {m['openers_pct']}", f"- Enders %: {m['enders_pct']}",
                f"- % of posts containing: {m['pct_posts_with']}", f"- Pronoun counts: {m['pronoun_counts']}", ""]

    md = [f"# Voice measurements ({len(base)} posts measured, {len(held)} held out)", "",
          f"Performance metric: {metric_name}, scored against the creator's own baseline for each format (+-45 days). Formats with under 10 posts are scored roughly against all posts and left unranked.",
          f"Formats: {stats['formats']}  |  Tiers: {stats['tiers']}  |  Dropped: {dict(dropped)}  |  Replies separated: {len(replies)}", "",
          "Use the per-format sections for rhythm and shape. Formats differ a lot, so the blended section at the bottom is reference only.", ""]
    for k, m in stats["by_format"].items():
        md += block(f"Format: {k}", m)
        if "vocabulary" in m:
            md += [f"Top words in {k} (by number of posts): " + ", ".join(f"{w} ({c})" for w, c in m["vocabulary"]["top_words_by_posts"][:25]), ""]
    if stats["too_few_to_measure"]:
        md += [f"Too few to measure (under {MIN_FMT} posts): {stats['too_few_to_measure']}. Read these directly instead of trusting numbers.", ""]
    v = stats["vocabulary_all_formats"]
    md += ["## Vocabulary (all formats)", "Top words (by number of posts): " + ", ".join(f"{w} ({c})" for w, c in v["top_words_by_posts"]), "",
           "Recurring 3-word phrases: " + (", ".join(f"{w} ({c})" for w, c in v["top_trigrams_by_posts"]) or "none"), ""]
    md += block("All formats blended (reference only, don't use for rhythm)", stats["all_formats_blended"])
    (out / "stats.md").write_text("\n".join(md))
    basis = Counter(p["perf_basis"] for p in kept)
    stats["perf_basis"] = dict(basis)
    (out / "stats.json").write_text(json.dumps(stats, indent=1, ensure_ascii=False))
    rep = (f"Performance baselines: {dict(basis)} (anything marked 'all posts (rough)' is unranked; treat its perf as directional only)\n"
           f"Raw records: {len(raw)} | usable originals kept: {len(kept)} | replies: {len(replies)} | dropped: {dict(dropped)}\n"
           f"Dated posts: {sum(1 for p in kept if p['date'])} | holdout: {len(held)} | metric: {metric_name}\n")
    if len(kept) < 100: rep += "WARNING: fewer than 100 originals. Profile will be thin.\n"
    (out / "ingest-report.txt").write_text(rep)
    print(rep + f"Wrote {out}/corpus.jsonl, replies.jsonl, stats.json, stats.md")


if __name__ == "__main__":
    main()
