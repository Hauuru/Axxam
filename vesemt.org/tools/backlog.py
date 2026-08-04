#!/usr/bin/env python3
"""Backlog VESEMT : flux RSS -> liste des articles à convertir, dédupliquée vs registry.json."""
import json, os, re, sys, urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "registry.json")
BACKLOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backlog.json")

ACC = {"à":"a","â":"a","ä":"a","á":"a","é":"e","è":"e","ê":"e","ë":"e","î":"i","ï":"i",
       "ô":"o","ö":"o","ù":"u","û":"u","ü":"u","ç":"c","œ":"oe","æ":"ae","ñ":"n"}

def norm(t):
    t = t.lower()
    for a, b in ACC.items():
        t = t.replace(a, b)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return t

def tokens(s):
    return set(norm(s).split())

def jaccard(a, b):
    A, B = tokens(a), tokens(b)
    if not A or not B:
        return 0.0
    return len(A & B) / len(A | B)

def fetch_rss():
    items, pg = [], 1
    while pg <= 12:
        url = f"https://vesemt.org/?feed=rss2&paged={pg}"
        try:
            with urllib.request.urlopen(url, timeout=25) as r:
                xml = r.read().decode("utf-8", "replace")
        except Exception as e:
            print(f"  arrêt à paged={pg} ({e})")
            break
        root = ET.fromstring(xml)
        cur = [it for it in root.iter("item")]
        if not cur:
            break
        for it in cur:
            title = (it.findtext("title") or "").strip()
            link = it.findtext("link") or ""
            date = it.findtext("pubDate") or ""
            m = re.search(r"\?p=(\d+)", link)
            p = int(m.group(1)) if m else None
            cats = [c for c in it.iter("category")]
            items.append({"p": p, "title": title, "date": date})
        pg += 1
    return items

def main():
    if not os.path.exists(REGISTRY):
        print("registry.json absent — lancez d'abord tools/build_registry.py")
        return 1
    reg = json.load(open(REGISTRY, encoding="utf-8"))
    reg_titles = [e["title"] for e in reg]

    print("== Récupération du flux RSS ==")
    items = fetch_rss()
    items.sort(key=lambda x: x["date"], reverse=True)
    print(f"  {len(items)} articles RSS")

    known, pending = [], []
    for it in items:
        best, best_s = None, 0.0
        for t in reg_titles:
            s = jaccard(it["title"], t)
            if s > best_s:
                best_s, best = s, t
        if best_s >= 0.5:
            it["match"] = best
            it["score"] = round(best_s, 2)
            known.append(it)
        else:
            pending.append(it)

    print(f"  déjà convertis : {len(known)}")
    for it in known:
        print(f"    p={it['p']:<4} {it['match'][:55]}")
    print(f"  EN ATTENTE : {len(pending)}")
    for i, it in enumerate(pending, 1):
        print(f"    {i:>2}. p={it['p']:<4} {it['date'][:16]}  {it['title'][:70]}")

    json.dump({"known": known, "pending": pending}, open(BACKLOG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"-> backlog.json ({len(pending)} en attente)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
