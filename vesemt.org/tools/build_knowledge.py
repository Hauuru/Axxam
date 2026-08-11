#!/usr/bin/env python3
"""Génère la base de connaissance de l'agent conversationnel VESEMT.

Usage : python3 tools/build_knowledge.py [--max-chars N]

Parse chaque article de articles/*.html et écrit vesemt-knowledge.js
(un objet window.VESEMT_ARTICLES), trié par date décroissante.

À exécuter après chaque nouvelle conversion (voir documentation/CONVERSION-METHODE.md).
"""
import html, json, os, re, sys, glob
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES = os.path.join(ROOT, "articles")
OUT = os.path.join(ROOT, "vesemt-knowledge.js")
SITE = "https://axxam.net/vesemt.org"


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


BLOCK = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li",
         "blockquote", "figure", "figcaption", "pre", "table", "tr", "td",
         "th", "section", "article", "hr", "br"}


def to_text(node, out):
    """Convertit un noeud DOM en texte brut (sauts de ligne aux frontières de blocs)."""
    if isinstance(node, str):
        out.append(re.sub(r"\s+", " ", node))
        return
    tag = node.tag
    if tag in ("#drop",) or tag in DomBuilder.DROP:
        return
    if tag == "img":
        alt = node.attrs.get("alt", "").strip()
        if alt:
            out.append(f"[Image : {alt}]")
        return
    if tag in BLOCK and out and not out[-1].endswith("\n"):
        out.append("\n")
    for c in node.children:
        to_text(c, out)
    if tag in BLOCK and not out[-1].endswith("\n"):
        out.append("\n")


def children(node):
    return [c for c in node.children if not isinstance(c, str)]


def find(node, tag, cls=None):
    """Premier descendant de la balise (optionnellement avec une classe)."""
    if node.tag == tag and (cls is None or node.attrs.get("class", "") == cls):
        return node
    for c in children(node):
        r = find(c, tag, cls)
        if r:
            return r
    return None


def find_any(node, predicate):
    """Premier descendant satisfaisant predicate(node)."""
    if predicate(node):
        return node
    for c in children(node):
        r = find_any(c, predicate)
        if r:
            return r
    return None


def meta_content(node, name):
    for c in children(node):
        if c.tag == "meta" and c.attrs.get("name") == name:
            return c.attrs.get("content", "").strip()
        r = meta_content(c, name)
        if r:
            return r
    return ""


def clean_text(raw):
    return re.sub(r"[ \t]+", " ", re.sub(r"\n{3,}", "\n\n", raw)).strip()


def text_of(node):
    out = []
    to_text(node, out)
    return clean_text("".join(out))


def extract_tags(text):
    """Hashtags éventuels en fin d'article (ex. #VESEMT #TMVL)."""
    tags = re.findall(r"#([A-Za-z0-9À-ÿ_]+)", text)
    seen, out = set(), []
    for t in tags:
        if t.lower() not in seen:
            seen.add(t.lower())
            out.append(t)
    return out


def build_article(path):
    builder = DomBuilder()
    builder.feed(open(path, encoding="utf-8").read())

    h1 = find(builder.root, "h1", "article-title")
    title = text_of(h1).rstrip(".") if h1 else ""
    if not title:
        m = re.search(r"<title>(.*?)\s*– VIVRE", open(path, encoding="utf-8").read(), re.S)
        title = clean_text(m.group(1)) if m else os.path.basename(path)

    time_node = find(builder.root, "time")
    iso = time_node.attrs.get("datetime", "") if time_node else ""

    author = ""
    author_span = find_any(builder.root, lambda n: n.tag == "span" and "article-author" in n.attrs.get("class", ""))
    if author_span:
        author = text_of(author_span)

    excerpt = meta_content(builder.root, "description")

    content = find(builder.root, "div", "article-content")
    body = text_of(content) if content else ""
    tags = extract_tags(body)

    slug = os.path.basename(path)[:-5]
    return {
        "slug": slug,
        "title": title,
        "iso": iso,
        "author": author,
        "excerpt": excerpt,
        "tags": tags,
        "text": body,
        "url": f"{SITE}/articles/{slug}.html",
    }


def main():
    max_chars = None
    if "--max-chars" in sys.argv:
        max_chars = int(sys.argv[sys.argv.index("--max-chars") + 1])

    articles = []
    for f in sorted(glob.glob(os.path.join(ARTICLES, "*.html"))):
        try:
            articles.append(build_article(f))
        except Exception as e:
            print(f"  ! {os.path.basename(f)} : {e}")

    articles.sort(key=lambda a: a["iso"] or "0000-00-00", reverse=True)

    if max_chars:
        for a in articles:
            if len(a["text"]) > max_chars:
                a["text"] = a["text"][:max_chars].rstrip() + " […]"

    js = "/* Généré par tools/build_knowledge.py — ne pas modifier à la main. */\n"
    js += "window.VESEMT_ARTICLES = " + json.dumps(articles, ensure_ascii=False, indent=1) + ";\n"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(js)

    words = sum(len(a["text"].split()) for a in articles)
    print(f"-> vesemt-knowledge.js : {len(articles)} articles, {words} mots, "
          f"{os.path.getsize(OUT)//1024} Ko")


if __name__ == "__main__":
    main()
