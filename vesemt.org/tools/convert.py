#!/usr/bin/env python3
"""Convertit un article WordPress (https://vesemt.org/?p=ID) en article statique VESEMT.

Usage : python3 tools/convert.py <pID> [--slug override]
"""
import html, json, os, re, sys, urllib.request, urllib.parse
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(ROOT, "images")
ARTICLES = os.path.join(ROOT, "articles")
REGISTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "registry.json")
SITE = "https://axxam.net/vesemt.org"

MONTHS = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]

NAV = """        <nav>
            <ul>
                <li><a href="../index.html">Accueil</a></li>
                <li><a href="../qui-sommes-nous.html">Qui sommes nous ?</a></li>
                <li><a href="../elections-municipales-2026.html">Elections Municipales 2026</a></li>
                <li><a href="../contacter-reseaux.html">Contacter- réseaux</a></li>
                <li><a href="../politique-confidentialite.html">Politique de confidentialité</a></li>
            </ul>
        </nav>"""

# ---------- slug ----------
def slugify(t):
    t = t.lower()
    for a, b in [("à","a"),("â","a"),("ä","a"),("á","a"),("é","e"),("è","e"),("ê","e"),("ë","e"),
                 ("î","i"),("ï","i"),("ô","o"),("ö","o"),("ù","u"),("û","u"),("ü","u"),
                 ("ç","c"),("œ","oe"),("æ","ae"),("’",""),("'",""),('"',""),("“",""),("”",""),
                 ("…",""),(".",""),(",",""),(":",""),(";",""),("!",""),("?",""),("&","et")]:
        t = t.replace(a, b)
    t = re.sub(r"\s+", "-", t)
    t = re.sub(r"[^a-z0-9\-]+", "", t)
    t = re.sub(r"-+", "-", t).strip("-")
    return t

# ---------- DOM minimal ----------
class Node:
    __slots__ = ("tag", "attrs", "children", "parent")
    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = attrs
        self.children = []
        self.parent = None

class DomBuilder(HTMLParser):
    VOID = {"img", "br", "hr", "input", "meta", "link", "source", "area", "wbr"}
    DROP = {"script", "style", "svg", "noscript", "template", "head"}
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.root = Node("root", {})
        self.stack = [self.root]
    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag in self.DROP:
            self.stack.append(Node("#drop", {}))
            return
        node = Node(tag, a)
        self.stack[-1].children.append(node)
        node.parent = self.stack[-1]
        if tag not in self.VOID:
            self.stack.append(node)
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID and self.stack and self.stack[-1].tag == tag:
            self.stack.pop()
    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break
    def handle_data(self, data):
        self.stack[-1].children.append(data)
    def handle_entityref(self, name):
        self.stack[-1].children.append(html.unescape("&" + name + ";"))
    def handle_charref(self, name):
        self.stack[-1].children.append(html.unescape("&#" + name + ";"))

# ---------- nettoyage / rendu ----------
BLOCK_TAGS = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li", "blockquote",
              "figure", "figcaption", "pre", "table", "tr", "td", "th", "section", "article", "hr"}

def is_block(node):
    if isinstance(node, str):
        return False
    return node.tag in BLOCK_TAGS

def contains_block(node):
    """Le noeud contient-il un descendant de type bloc (hors lui-même) ?"""
    if isinstance(node, str):
        return False
    return any(is_block(c) or contains_block(c) for c in node.children)
INLINE = {"a", "strong", "em", "b", "i", "u", "span", "code", "br", "img", "sub", "sup", "mark"}

def render(node, downloads, slug):
    """Rend un noeud DOM en HTML propre. downloads: dict basename -> (url, alt)."""
    if isinstance(node, str):
        return [html.escape(re.sub(r"\s+", " ", node))]
    if node.tag in ("#drop", "root"):
        out = []
        for c in node.children:
            out.extend(render(c, downloads, slug))
        return out
    if node.tag in ("script", "style", "svg", "noscript", "template"):
        return []
    if node.tag == "img":
        return [render_img(node, downloads, slug)]
    if node.tag == "br":
        return ["<br>"]
    if node.tag == "hr":
        return ["<hr>"]
    if node.tag == "a":
        return [render_a(node)]
    if node.tag == "span":
        out = []
        for c in node.children:
            out.extend(render(c, downloads, slug))
        return out
    if node.tag in ("strong", "b"):
        inner = concat(render_children(node, downloads, slug))
        return [f"<strong>{inner}</strong>"] if inner else []
    if node.tag in ("em", "i"):
        inner = concat(render_children(node, downloads, slug))
        return [f"<em>{inner}</em>"] if inner else []
    if node.tag in ("code", "sub", "sup", "mark", "u"):
        inner = concat(render_children(node, downloads, slug))
        return [f"<{node.tag}>{inner}</{node.tag}>"] if inner else []
    if node.tag in ("h1","h2","h3","h4"):
        inner = concat(render_children(node, downloads, slug))
        inner = re.sub(r"^(#+\s*)+", "", inner)
        tag = "h2" if node.tag == "h1" else node.tag
        return [f"<{tag}>{inner}</{tag}>"] if inner else []
    if node.tag == "blockquote":
        inner = concat(render_children(node, downloads, slug))
        if not inner.strip():
            return []
        if re.match(r"^\s*<(p|h[1-6]|ul|ol|blockquote|div|table|figure|pre)\b", inner):
            return [f"<blockquote>{inner}</blockquote>"]
        return [f"<blockquote><p>{inner}</p></blockquote>"]
    if node.tag in ("ul", "ol"):
        lis = []
        for c in node.children:
            if isinstance(c, Node) and c.tag == "li":
                inner = concat(render_children(c, downloads, slug))
                lis.append(f"<li>{inner}</li>")
        if lis:
            return [f"<{node.tag}>{''.join(lis)}</{node.tag}>"]
        return []
    if node.tag == "li":
        inner = concat(render_children(node, downloads, slug))
        return [f"<li>{inner}</li>"] if inner else []
    if node.tag in ("p", "div", "figure", "figcaption", "section", "td", "th", "tr", "pre"):
        inner = concat(render_children(node, downloads, slug))
        if node.tag == "div" and not contains_block(node):
            return [f"<p>{inner}</p>"] if inner.strip() else []
        if node.tag == "div":
            return [inner] if inner.strip() else []
        if node.tag == "figure":
            return [f"<figure>{inner}</figure>"] if inner.strip() else []
        if node.tag == "p":
            return [f"<p>{inner}</p>"] if inner.strip() else []
        if node.tag == "figcaption":
            return [f"<figcaption>{inner}</figcaption>"] if inner.strip() else []
        return [inner] if inner.strip() else []
    # inconnu : transparent
    out = []
    for c in node.children:
        out.extend(render(c, downloads, slug))
    return out

def render_children(node, downloads, slug):
    out = []
    for c in node.children:
        out.extend(render(c, downloads, slug))
    return out

def concat(parts):
    return "".join(parts)

def render_img(node, downloads, slug):
    src = node.attrs.get("src", "")
    alt = html.unescape(node.attrs.get("alt", ""))
    # emoji Facebook -> texte (le caractère unicode)
    if "fbcdn" in src and "emoji" in src:
        return html.escape(alt) if alt else ""
    if "wp-content/uploads" in src:
        name = os.path.basename(urllib.parse.urlparse(src).path)
        name = re.sub(r"×", "x", name)
        name = re.sub(r"[^\w.\-]", "-", name)
        name = re.sub(r"-+", "-", name).strip("-")
        name = re.sub(r"\.[a-zA-Z0-9]+$", ".jpg", name)
        key = f"{slug}-{name}"
        downloads[key] = (src, alt)
        return f'<img src="../images/{key}" alt="{html.escape(alt)}">'
    if src.startswith("http"):
        return f'<img src="{html.escape(src)}" alt="{html.escape(alt)}">'
    return ""

def render_a(node):
    href = node.attrs.get("href", "")
    text = "".join(c if isinstance(c, str) else text_of(c) for c in node.children)
    text = html.unescape(text).strip()
    # liens Facebook redirect
    if "l.facebook.com" in href:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(href).query)
        href = q.get("u", [""])[0]
    # supprimer les paramètres de tracking (Facebook, etc.)
    u = urllib.parse.urlparse(href)
    if u.netloc and ("facebook.com" in u.netloc or "fbcdn" in u.netloc):
        href = urllib.parse.urlunparse((u.scheme, u.netloc, u.path, "", "", ""))
    else:
        q = urllib.parse.parse_qs(u.query)
        q.pop("fbclid", None)
        q = {k: v[0] for k, v in q.items() if k != "__tn__" and not k.startswith("__cft__") and not k.startswith("__rdc")}
        if q:
            href = urllib.parse.urlunparse((u.scheme, u.netloc, u.path, "", urllib.parse.urlencode(q), ""))
        else:
            href = urllib.parse.urlunparse((u.scheme, u.netloc, u.path, "", "", ""))
    if "vesemt.org" in href and "?p=" in href:
        p = re.search(r"\?p=(\d+)", href)
        if p:
            href = f"[[p:{p.group(1)}]]"
    if not text:
        text = href
    if href.startswith("[[p:") or href.startswith("http") or href.startswith("mailto:"):
        return f'<a href="{html.escape(href)}">{html.escape(text)}</a>'
    return html.escape(text)

def text_of(node):
    if isinstance(node, str):
        return node
    if node.tag == "img":
        alt = html.unescape(node.attrs.get("alt", ""))
        return alt if "fbcdn" in node.attrs.get("src", "") and "emoji" in node.attrs.get("src", "") else ""
    return "".join(text_of(c) for c in node.children)

def clean_spaces(s):
    s = re.sub(r"[\t\u00a0]+", " ", s)
    s = re.sub(r" +\n", "\n", s)
    s = re.sub(r"\n +", "\n", s)
    s = re.sub(r" ?<br> ?", " ", s)
    s = re.sub(r"<p>\s*</p>", "", s)
    return s.strip()

# ---------- extraction WP ----------
def fetch_article(p):
    url = f"https://vesemt.org/?p={p}"
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read().decode("utf-8", "replace")

def extract(h, p):
    m = re.search(r'<h1 class="cm-entry-title">(.*?)</h1>', h, re.S)
    title = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else None
    if title:
        title = re.sub(r"\s*#+\s*", " ", title)
        title = re.sub(r"\s{2,}", " ", title).strip()
    if not title:
        m = re.search(r"<title>(.*?)</title>", h, re.S)
        if m:
            title = html.unescape(m.group(1)).split("–")[0].split("&#8211;")[0].strip()
            title = re.sub(r"\s*#+\s*", " ", title)
            title = re.sub(r"\s{2,}", " ", title).strip()
    m = re.search(r'datetime="([^"]+)"', h)
    iso = m.group(1)[:10] if m else None
    m = re.search(r'<img[^>]*attachment-colormag-featured-image[^>]*>', h)
    feat = None
    if m:
        tag = m.group(0)
        ms = re.search(r'srcset="([^"]+)"', tag)
        if ms:
            cands = [x.split(" ")[0] for x in ms.group(1).split(",")]
            sized = [u for u in cands if re.search(r"\d+w$", u)]
            if sized:
                feat = max(sized, key=lambda u: int(re.search(r"(\d+)w", u).group(1)))
            else:
                feat = cands[0] if cands else None
        if not feat:
            ms = re.search(r'src="([^"]+)"', tag)
            feat = ms.group(1) if ms else None

    def capture(div_open):
        """Capture depuis <div class=...> jusqu'à son </div> correspondant."""
        o = h.find(div_open)
        if o < 0:
            return ""
        j = o
        depth = 0
        while j < len(h):
            nxt_o = h.find("<div", j)
            nxt_c = h.find("</div>", j)
            if nxt_o == -1 and nxt_c == -1:
                break
            if nxt_c != -1 and (nxt_o == -1 or nxt_c < nxt_o):
                depth -= 1
                j = nxt_c + 6
                if depth == 0:
                    return h[o:nxt_c + 6]
            else:
                depth += 1
                j = nxt_o + 4
        return h[o:]

    body = capture('<div class="cm-entry-summary">')
    if not body:
        body = capture('<div class="cm-post-content">')
    k = body.find('<footer')
    if k > 0:
        body = body[:k]
    return {"title": title, "iso": iso, "featured": feat, "body": body}

def fmt_date(iso):
    if not iso:
        return ""
    y, m, d = iso.split("-")
    return f"{MONTHS[int(m)-1]} {int(d)}, {y}"

def excerpt_from(body_html):
    txt = re.sub(r"<[^>]+>", " ", body_html)
    txt = html.unescape(txt)
    txt = re.sub(r"\s+", " ", txt).strip()
    # retirer URLs et mots composés uniquement d'émojis
    txt = re.sub(r"https?://\S+", "", txt)
    EMO = re.compile(r"^[^\w\s\u00c0-\u024f]|[^\w\s\u00c0-\u024f]$")
    words = [w for w in txt.split(" ") if not EMO.match(w.strip())]
    txt = " ".join(words).strip()
    if len(txt) <= 155:
        return txt
    cut = txt[:155]
    i = max(cut.rfind("."), cut.rfind("!"), cut.rfind("?"), cut.rfind("…"))
    if i > 80:
        cut = cut[: i + 1]
    cut = cut.rstrip(" ,;:")
    return cut if cut.endswith("…") else cut + "…"

# ---------- image ----------
def download_image(url, dest, maxw=800, quality=85):
    u = urllib.parse.urlsplit(url)
    safe_path = urllib.parse.quote(u.path, safe="/%")
    url = urllib.parse.urlunsplit((u.scheme, u.netloc, safe_path, u.query, u.fragment))
    with urllib.request.urlopen(url, timeout=30) as r:
        data = r.read()
    tmp = dest + ".tmp"
    open(tmp, "wb").write(data)
    try:
        from PIL import Image
        im = Image.open(tmp)
        if im.mode == "RGBA":
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[-1])
            im = bg
        else:
            im = im.convert("RGB")
        if im.width > maxw:
            im = im.resize((maxw, max(1, round(im.height * maxw / im.width))), Image.LANCZOS)
        im.save(dest, "JPEG", quality=quality, optimize=True)
    except Exception as e:
        print(f"  ! conversion image échouée ({e}) : copie brute")
        import shutil
        shutil.move(tmp, dest)
        return
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)

# ---------- gabarit ----------
def make_article(slug, meta, body_html, image_rel, prev_link, next_link, og_rel=None):
    url = f"{SITE}/articles/{slug}.html"
    og_rel = og_rel or image_rel or "Logo.jpg"
    img_url = f"{SITE}/images/{og_rel}"
    desc = meta["excerpt"]
    date_disp = fmt_date(meta["iso"])
    iso = meta["iso"] or ""
    tags = "".join(f'<a href="#">{html.escape(t)}</a> ' for t in meta.get("tags", []))
    nav = f"""                <nav class="article-navigation">
                    <div class="nav-previous">
                        <span class="nav-label">Article précédent</span>
                        <a href="{prev_link}" class="nav-title">Article précédent</a>
                    </div>
                    <div class="nav-next">
                        <span class="nav-label">Article suivant</span>
                        <a href="{next_link}" class="nav-title">Article suivant</a>
                    </div>
                </nav>"""
    img_block = f'''                    <div class="article-image">
                        <img src="../images/{image_rel}" alt="{html.escape(meta["title"])}">
                    </div>''' if image_rel else ""
    title_esc = html.escape(meta["title"])
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_esc} – VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE</title>
    <meta name="description" content="{html.escape(desc)}">
    <meta name="author" content="Le Plombier">
    <meta property="og:title" content="{title_esc}">
    <meta property="og:description" content="{html.escape(desc)}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{img_url}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title_esc}">
    <meta name="twitter:description" content="{html.escape(desc)}">
    <meta name="twitter:image" content="{img_url}">
    <link rel="stylesheet" href="../vesemt-css/style.css">
    <link rel="stylesheet" href="../vesemt-css/article.css">
</head>
<body>
    <header>
        <div class="header-content">
            <h1 class="site-title">
                <a href="../index.html">VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE</a>
            </h1>
            <p class="site-description">Comité Populaire</p>
        </div>
{NAV}
    </header>

    <main>
        <div class="container">
            <article class="article-full">
                <header class="article-header">
                    <h1 class="article-title">{title_esc}</h1>
                    <div class="article-meta">
                        <span class="article-date">
                            <time datetime="{iso}">{date_disp}</time>
                        </span>
                        <span class="article-author">Par Le Plombier</span>
                    </div>
{img_block}
                </header>

                <div class="article-content">
{body_html}
                </div>

                <div class="article-footer">
                    <div class="article-tags">
                        <span class="tags-label">Tags :</span>
                        {tags}
                    </div>

                    <div class="article-share">
                        <h3>Partager cet article</h3>
                        <div class="share-buttons">
                            <a href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" rel="noopener" class="share-button share-facebook">
                                <span>Facebook</span>
                            </a>
                            <a href="https://twitter.com/intent/tweet?text={urllib.parse.quote(meta["title"])}&url={url}" target="_blank" rel="noopener" class="share-button share-twitter">
                                <span>Twitter</span>
                            </a>
                            <a href="https://www.linkedin.com/shareArticle?mini=true&url={url}&title={urllib.parse.quote(meta["title"])}" target="_blank" rel="noopener" class="share-button share-linkedin">
                                <span>LinkedIn</span>
                            </a>
                            <a href="mailto:?subject={urllib.parse.quote(meta["title"])}&body=Je vous recommande cet article : {url}" class="share-button share-email">
                                <span>Email</span>
                            </a>
                        </div>
                    </div>

                    <div class="article-call-to-action">
                        <h3>Agissez maintenant</h3>
                        <p>Rejoignez VESEMT pour participer à la vie démocratique locale et défendre les intérêts des habitants de Saint-Pierre-des-Corps.</p>
                    </div>
                </div>

                <div class="article-comments">
                    <h3>Commentaires</h3>
                    <div class="fb-comments" data-href="{url}" data-width="100%" data-numposts="10"></div>
{nav}
</div></article>
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
                    <li><a href="../qui-sommes-nous.html">Qui sommes nous ?</a></li>
                    <li><a href="../contacter-reseaux.html">Contacter- réseaux</a></li>
                    <li><a href="../politique-confidentialite.html">Politique de confidentialité</a></li>
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

    <!-- Facebook Comments SDK -->
    <div id="fb-root"></div>
    <script async defer crossorigin="anonymous" src="https://connect.facebook.net/fr_FR/sdk.js#xfbml=1&version=v18.0"></script>
</body>
</html>
"""

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage : python3 tools/convert.py <pID> [--slug X] [--force]")
        return 1
    p = args[0]
    force = "--force" in args
    slug_override = None
    if "--slug" in args:
        slug_override = args[args.index("--slug") + 1]

    print(f"== Conversion p={p} ==")
    h = fetch_article(p)
    info = extract(h, p)
    print(f"  titre : {info['title']}")
    print(f"  date  : {info['iso']}")
    print(f"  image : {info['featured']}")

    slug = slug_override or slugify(info["title"] or f"article-{p}")
    dest = os.path.join(ARTICLES, slug + ".html")
    if os.path.exists(dest) and not force:
        print(f"  ! {slug}.html existe déjà — abandon.")
        return 1
    if os.path.exists(dest):
        print(f"  {slug}.html existant — régénération (--force).")

    # rendu du contenu
    builder = DomBuilder()
    builder.feed(info["body"])
    downloads = {}
    parts = render(builder.root, downloads, slug)
    body_html = clean_spaces("\n".join(parts))

    excerpt = excerpt_from(body_html)

    # image à la une
    image_rel = ""
    if info["featured"]:
        image_rel = f"{slug}-800x445.jpg"
        img_dest = os.path.join(IMAGES, image_rel)
        print(f"  image une -> {image_rel}")
        download_image(info["featured"], img_dest)
    else:
        image_rel = "Logo.jpg"
        print("  pas d'image à la une -> Logo.jpg")

    # résoudre les images de contenu (hors image à la une)
    og_rel = image_rel
    for key, (url, alt) in downloads.items():
        if url == info["featured"]:
            body_html = body_html.replace(f'../images/{key}', f'../images/{image_rel}')
            continue
        if og_rel == "Logo.jpg" and os.path.exists(os.path.join(IMAGES, key)):
            og_rel = key
        dl = os.path.join(IMAGES, key)
        if not os.path.exists(dl):
            print(f"  image contenu : {key}")
            download_image(url, dl)

    # nettoyage final : paragraphes vides, retournés, balises imbriquées identiques
    body_html = re.sub(r"<p>\s*</p>", "", body_html)
    body_html = re.sub(r"<p><p>", "<p>", body_html)
    body_html = re.sub(r"</p></p>", "</p>", body_html)
    for _ in range(3):
        body_html = re.sub(r"<(strong|em)>\s*<\1>", r"<\1>", body_html)
        body_html = re.sub(r"</(strong|em)>\s*</\1>", r"</\1>", body_html)
        body_html = re.sub(r"<blockquote>\s*<p>\s*<(h[1-6]|ul|ol|p|blockquote)", r"<blockquote><\1", body_html)
        body_html = re.sub(r"</(h[1-6]|ul|ol|p|blockquote)>\s*</p>\s*</blockquote>", r"</\1></blockquote>", body_html)
    body_html = re.sub(r"\n{3,}", "\n\n", body_html).strip()

    # écriture
    os.makedirs(ARTICLES, exist_ok=True)
    html_out = make_article(slug, {"title": info["title"], "excerpt": excerpt, "iso": info["iso"], "tags": []},
                            body_html, image_rel, "#", "#", og_rel)
    open(dest, "w", encoding="utf-8").write(html_out)
    smap_path = os.path.join(os.path.dirname(__file__), "slugmap.json")
    smap = json.load(open(smap_path)) if os.path.exists(smap_path) else {}
    smap[p] = slug
    json.dump(smap, open(smap_path, "w"), ensure_ascii=False, indent=2)
    print(f"  -> articles/{slug}.html")
    print(f"  extrait : {excerpt}")
    print("\nREVUE : vérifier le contenu ci-dessous avant intégration.")
    print("----")
    print(body_html[:2500])
    print("----")

if __name__ == "__main__":
    sys.exit(main())
