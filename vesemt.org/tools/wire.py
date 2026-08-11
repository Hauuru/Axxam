#!/usr/bin/env python3
"""wire.py — intégration des articles dans le site statique VESEMT.

1.  Construit la liste maîtresse des articles (articles/*.html).
2.  Résout les placeholders [[p:N]] -> ../articles/<slug>.html (slugmap.json).
3.  Réécrit la navigation (5 liens) sur toutes les pages racine et articles.
4.  Chaîne la navigation précédent/suivant de chaque article.
5.  Régénère index.html (bandeau + liste de tous les articles).
6.  Régénère sitemap.xml.

Usage : python3 tools/wire.py
"""
import html
import json
import os
import re
import glob
import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES = os.path.join(BASE, "articles")
ROOT = BASE
SITE = "https://axxam.net/vesemt.org"

NAV_LINKS = [
    ("index.html", "Accueil"),
    ("qui-sommes-nous.html", "Qui sommes nous ?"),
    ("elections-municipales-2026.html", "Elections Municipales 2026"),
    ("contacter-reseaux.html", "Contacter- réseaux"),
    ("politique-confidentialite.html", "Politique de confidentialité"),
]


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def find_articles():
    items = []
    for path in glob.glob(os.path.join(ARTICLES, "*.html")):
        src = read(path)
        name = os.path.basename(path)
        og_title = re.search(r'<meta property="og:title" content="(.*?)">', src, re.S)
        desc = re.search(r'<meta name="description" content="(.*?)">', src, re.S)
        iso = re.search(r'<time datetime="([0-9-]+)"', src)
        og_img = re.search(r'<meta property="og:image" content="(.*?)">', src)
        items.append({
            "file": name,
            "slug": name[:-5],
            "title": html.unescape(og_title.group(1)).strip() if og_title else name[:-5],
            "desc": html.unescape(desc.group(1)).strip() if desc else "",
            "iso": iso.group(1) if iso else "0000-00-00",
            "img": og_img.group(1).rsplit("/", 1)[-1] if og_img else "Logo.jpg",
        })
    items.sort(key=lambda a: a["iso"], reverse=True)
    return items


def make_nav(prefix, active_file=None):
    lis = []
    for page, label in NAV_LINKS:
        active = ' class="active"' if page == active_file else ""
        lis.append(f'                <li><a href="{prefix}{page}"{active}>{label}</a></li>')
    return ("        <nav>\n            <ul>\n" + "\n".join(lis) +
            "\n            </ul>\n        </nav>")


def rewrite_nav(path, active_file=None):
    src = read(path)
    prefix = "../" if path.startswith(ARTICLES) else ""
    nav = make_nav(prefix, active_file)
    new = re.sub(r"<nav>\s*<ul>.*?</ul>\s*</nav>", nav, src, flags=re.S)
    if new != src:
        write(path, new)
        return True
    return False


def resolve_placeholders(path, slugmap):
    src = read(path)
    n = 0
    def repl(m):
        nonlocal n
        pid = m.group(1)
        if pid in slugmap:
            n += 1
            return f"../articles/{slugmap[pid]}.html"
        return m.group(0)
    new = re.sub(r"\[\[p:(\d+)\]\]", repl, src)
    new = re.sub(r"(?<=>)#+\s+", "", new)
    if new != src:
        write(path, new)
    return n, len(re.findall(r"\[\[p:(\d+)\]\]", src))


def rewrite_article_nav(path, prev, nxt):
    src = read(path)
    if prev:
        prev_block = (f'                <div class="nav-previous">\n'
                      f'                    <span class="nav-label">Article précédent</span>\n'
                      f'                    <a href="../articles/{prev["file"]}" class="nav-title">{html.escape(prev["title"])}</a>\n'
                      f'                </div>')
    else:
        prev_block = ('                <div class="nav-previous">\n'
                      '                    <span class="nav-label">Article précédent</span>\n'
                      '                    <span class="nav-title">Article précédent</span>\n'
                      '                </div>')
    if nxt:
        nxt_block = (f'                <div class="nav-next">\n'
                     f'                    <span class="nav-label">Article suivant</span>\n'
                     f'                    <a href="../articles/{nxt["file"]}" class="nav-title">{html.escape(nxt["title"])}</a>\n'
                     f'                </div>')
    else:
        nxt_block = ('                <div class="nav-next">\n'
                     '                    <span class="nav-label">Article suivant</span>\n'
                     '                    <span class="nav-title">Article suivant</span>\n'
                     '                </div>')
    block = ('                <nav class="article-navigation">\n' +
             prev_block + "\n" + nxt_block + '\n                </nav>')
    new = re.sub(r"<nav class=\"article-navigation\">.*?</nav>", block, src, flags=re.S)
    if new != src:
        write(path, new)
        return True
    return False


def fmt_date_short(iso):
    if not iso or iso.startswith("0000"):
        return ""
    MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin",
              "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m) - 1]} {y}"


def build_index(articles, header):
    rows = []
    for a in articles:
        title = html.escape(a["title"])
        desc = html.escape(a["desc"])
        if len(desc) > 120:
            cut = desc[:120]
            i = max(cut.rfind(" "), 60)
            desc = cut[:i].rstrip(" ,;:") + "…"
        date = fmt_date_short(a["iso"])
        rows.append(f'                <li class="list-item">\n'
                    f'                    <span class="list-date">{date}</span>\n'
                    f'                    <a class="list-title" href="articles/{a["file"]}">{title}</a>\n'
                    f'                    <span class="list-excerpt">{desc}</span>\n'
                    f'                </li>')
    body = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accueil – VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE</title>
    <meta name="description" content="VESEMT est un comité populaire et bienveillant engagé pour la solidarité et la démocratie en métropole tourangelle. Découvrez nos actions et nos analyses.">
    <meta name="author" content="VESEMT">
    <meta property="og:title" content="Accueil">
    <meta property="og:description" content="VESEMT est un comité populaire et bienveillant engagé pour la solidarité et la démocratie en métropole tourangelle.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://axxam.net/vesemt.org/index.html">
    <meta property="og:image" content="https://axxam.net/vesemt.org/images/New-bandeau-SITE.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Accueil">
    <meta name="twitter:description" content="VESEMT est un comité populaire et bienveillant engagé pour la solidarité et la démocratie en métropole tourangelle.">
    <meta name="twitter:image" content="https://axxam.net/vesemt.org/images/New-bandeau-SITE.jpg">
    <link rel="stylesheet" href="vesemt-css/style.css">
    <style>
        .agent-cta {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-top: 14px;
            padding: 11px 20px;
            background: #F44336;
            color: #fff;
            border-radius: 999px;
            font-weight: 700;
            font-size: 15px;
            text-decoration: none;
            transition: background 0.15s;
        }}
        .agent-cta:hover {{ background: #c0392b; }}
    </style>
</head>
<body>
{header}
<div class="hero-banner">
        <img src="images/New-bandeau-SITE.jpg" alt="VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE">
    </div>

    <main>
        <div class="container">
            <div class="page-header">
                <h1>Bienvenue sur VESEMT</h1>
                <p class="page-intro">Un comité populaire et bienveillant engagé pour la solidarité et la démocratie en métropole tourangelle</p>
                <a class="agent-cta" href="agent.html">💬 Questionner nos articles</a>
            </div>

            <section class="articles-list">
                <h2>Nos actualités</h2>
                <p class="list-intro">Tous nos articles, du plus récent au plus ancien.</p>
                <ul class="article-index">
{chr(10).join(rows)}
                </ul>
            </section>
        </div>
    </main>

<footer>
        <div class="footer-content">
            <div class="footer-section">
                <h3>À propos</h3>
                <p>VESEMT est un collectif citoyen engagé pour la solidarité et la démocratie en métropole tourangelle.</p>
            </div>
            <div class="footer-section">
                <h3>Liens utiles</h3>
                <ul>
                    <li><a href="qui-sommes-nous.html">Qui sommes nous ?</a></li>
                    <li><a href="contacter-reseaux.html">Contacter- réseaux</a></li>
                    <li><a href="politique-confidentialite.html">Politique de confidentialité</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Newsletter</h3>
                <p>Recevez nos actualités</p>
                <form class="newsletter-form" action="https://app.brevo.com/form.php" method="POST">
                    <input type="email" name="email" placeholder="Votre email" required>
                    <button type="submit">S'inscrire</button>
                </form>
            </div>
            <div class="footer-section">
                <h3>Suivez-nous</h3>
                <div class="social-links">
                    <a href="https://www.facebook.com/vesemt" target="_blank" rel="noopener">Facebook</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 VESEMT - Tous droits réservés</p>
                        <p class="footer-credits">🌱 Créé avec passion par Le Plombier, Marco, Calcifere et Hauuru</p>
        </div>
    </footer>
</body>
</html>"""
    return body


def build_sitemap(pages, articles):
    today = datetime.date.today().isoformat()
    urls = []
    for page in pages:
        priority = "1.0" if page == "index.html" else "0.8"
        urls.append((SITE + "/" + page, today, priority))
    for a in articles:
        urls.append((SITE + "/articles/" + a["file"], today, "0.7"))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod, prio in urls:
        lines.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>{prio}</priority>\n  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main():
    slugmap_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "slugmap.json")
    slugmap = json.load(open(slugmap_path)) if os.path.exists(slugmap_path) else {}

    idx_path = os.path.join(ROOT, "index.html")

    articles = find_articles()
    print(f"== {len(articles)} articles détectés ==")

    # 1. résolution des placeholders
    for a in articles:
        path = os.path.join(ARTICLES, a["file"])
        done, total = resolve_placeholders(path, slugmap)
        if total:
            print(f"  [{a['file']}] placeholders {done}/{total} résolus")

    # 2. navigation 5 liens sur toutes les pages
    for page in glob.glob(os.path.join(ROOT, "*.html")):
        if os.path.basename(page) == "index.html":
            continue
        if rewrite_nav(page, os.path.basename(page)):
            print(f"  nav -> {os.path.basename(page)}")
    for a in articles:
        if rewrite_nav(os.path.join(ARTICLES, a["file"])):
            print(f"  nav -> articles/{a['file']}")

    # 3. précédent/suivant
    for i, a in enumerate(articles):
        prev = articles[i + 1] if i + 1 < len(articles) else None
        nxt = articles[i - 1] if i - 1 >= 0 else None
        if rewrite_article_nav(os.path.join(ARTICLES, a["file"]), prev, nxt):
            print(f"  prev/next -> {a['file']}")

    # 4. index
    header = ('    <header>\n'
              '        <div class="header-content">\n'
              '            <h1 class="site-title">\n'
              '                <a href="index.html">VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE</a>\n'
              '            </h1>\n'
              '            <p class="site-description">Comité Populaire bienveillant</p>\n'
              '        </div>\n' +
              make_nav("", "index.html") +
              '\n    </header>')
    write(idx_path, build_index(articles, header))
    print(f"  index.html régénéré ({len(articles)} articles listés)")

    # 5. sitemap
    pages = [os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "*.html"))]
    pages = [p for p in pages if p not in
             {"dossiers-metropolitains.html", "saint-pierre-des-corps.html",
              "le-quotidien-le-vrai.html", "vesemt-localement.html",
              "author-le-plombier.html"}]
    pages.sort()
    write(os.path.join(ROOT, "sitemap.xml"), build_sitemap(pages, articles))
    print(f"  sitemap.xml régénéré ({len(pages)} pages + {len(articles)} articles)")


if __name__ == "__main__":
    main()
