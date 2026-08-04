#!/usr/bin/env python3
"""Construit registry.json à partir des articles statiques existants.

Chaque entrée : slug, title, iso, excerpt, image, file.
Source de vérité pour l'intégration (index, sitemap, prev/next, liens ?p=).
"""
import json, os, re, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES = os.path.join(ROOT, "articles")
REGISTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "registry.json")

def extract(f):
    p = os.path.join(ARTICLES, f)
    h = open(p, encoding="utf-8").read()
    slug = f[:-5]
    t = re.search(r'<h1 class="article-title">(.*?)</h1>', h, re.S)
    title = H.unescape(re.sub(r"<[^>]+>", "", t.group(1))).strip() if t else None
    if not title:
        t = re.search(r'<title>(.*?)</title>', h, re.S)
        title = H.unescape(t.group(1)).split("–")[0].strip() if t else slug
    d = re.search(r'<time datetime="([^"]+)"', h)
    iso = d.group(1)[:10] if d else None
    m = re.search(r'<meta name="description" content="([^"]*)"', h)
    excerpt = H.unescape(m.group(1)) if m else ""
    m = re.search(r'<meta property="og:image" content="[^"]*/([^/"]+)"', h)
    image = m.group(1) if m else ""
    return {"slug": slug, "title": title, "iso": iso, "excerpt": excerpt,
            "image": image, "file": f}

def main():
    reg = []
    for f in sorted(os.listdir(ARTICLES)):
        if f.endswith(".html"):
            reg.append(extract(f))
    json.dump(reg, open(REGISTRY, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"registry.json : {len(reg)} articles")
    for e in reg:
        print(f"  {e['iso']}  {e['slug']}")

if __name__ == "__main__":
    main()
