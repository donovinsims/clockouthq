#!/usr/bin/env python3
"""Retrieve the most relevant real posts from a creator's corpus, or check a draft for copying.

  python retrieve.py search  CORPUS.jsonl "contrarian take on AI agents" [-k 8] [--tier top] [--format short] [--include-holdout]
  python retrieve.py overlap CORPUS.jsonl --draft "text..." | --draft-file draft.txt

search: TF-IDF similarity over post text. Holdout posts are excluded unless asked (keeps the blind test clean).
overlap: finds the longest run of words a draft shares with any real post. 8+ words in a row means copying.
Pure standard library.
"""
import argparse, json, math, re, sys
from collections import Counter

STOP = set("a an and are as at be but by for from has have i in is it its of on or that the this to was we with you your".split())
tok = lambda t: [w for w in re.findall(r"[a-z0-9']+", t.lower())]


def load(path):
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


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
    best, best_i, prev = 0, 0, [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best: best, best_i = cur[j], i
        prev = cur
    return best, a[best_i - best:best_i]


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("corpus"); s.add_argument("query")
    s.add_argument("-k", type=int, default=8); s.add_argument("--tier"); s.add_argument("--format")
    s.add_argument("--include-holdout", action="store_true")
    o = sub.add_parser("overlap"); o.add_argument("corpus"); o.add_argument("--draft"); o.add_argument("--draft-file")
    a = ap.parse_args()
    posts = load(a.corpus)

    if a.cmd == "search":
        pool = posts if a.include_holdout else [p for p in posts if not p.get("holdout")]
        for score, p in search(pool, a.query, a.k, a.tier, a.format):
            print(f"--- id={p['id']} sim={score:.2f} tier={p.get('tier')} format={p.get('format')} perf={p.get('perf')}x ({p.get('perf_basis','')})")
            print(p["text"]); print()
    else:
        draft = a.draft or open(a.draft_file, encoding="utf-8").read()
        dw = tok(draft)
        worst = (0, [], None)
        for p in posts:
            n, run = longest_run(dw, tok(p["text"]))
            if n > worst[0]: worst = (n, run, p)
        n, run, p = worst
        grams = lambda w: {tuple(w[i:i + 5]) for i in range(len(w) - 4)}
        dg = grams(dw)
        shared = len(dg & set().union(*[grams(tok(q["text"])) for q in posts])) if dg else 0
        print(f"Longest shared run: {n} words" + (f' -> "{" ".join(run)}" (post {p["id"]})' if n else ""))
        print(f"5-word sequences copied from corpus: {shared} of {len(dg)}")
        print("FLAG: rewrite, this is copying." if n >= 8 or (dg and shared / len(dg) > 0.15) else "OK: original enough.")


if __name__ == "__main__":
    main()
