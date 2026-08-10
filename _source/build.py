import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_source")
PAGES = os.path.join(SRC, "pages")

META_RE = re.compile(r"^\s*<!--meta\s*(\{.*?\})\s*-->", re.S)
COMMENT_RE = re.compile(r"[ \t]*<!--(?!\[if).*?-->[ \t]*", re.S)
BLANKS_RE = re.compile(r"\n[ \t]*\n[ \t]*\n+")


def strip_comments(html):
    html = COMMENT_RE.sub("", html)
    return BLANKS_RE.sub("\n\n", html)


def build_page(slug, template):
    path = os.path.join(PAGES, slug + ".html")
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()

    match = META_RE.match(raw)
    if not match:
        raise SystemExit("Bloc <!--meta ...--> manquant dans " + path)

    meta = json.loads(match.group(1))
    body = strip_comments(raw[match.end():]).strip()

    out = template
    out = out.replace("{{TITLE}}", meta["title"])
    out = out.replace("{{DESC}}", meta["desc"])
    out = out.replace("{{KEYWORDS}}", meta.get("keywords", ""))
    out = out.replace("{{SLUG}}", "" if slug == "index" else slug + ".html")
    out = out.replace("{{OGTYPE}}", meta.get("ogtype", "website"))
    out = out.replace("{{OGIMG}}", meta.get("ogimg", "salle-des-marches.png"))
    out = out.replace("{{JSONLD}}", meta.get("jsonld", ""))
    out = out.replace("{{BODY}}", body)

    nav = meta.get("nav")
    if nav:
        out = out.replace(
            'data-nav="%s">' % nav, 'data-nav="%s" aria-current="page">' % nav
        )

    out = strip_comments(out)

    dest = os.path.join(ROOT, slug + ".html")
    with open(dest, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out)
    return dest


def main():
    with open(os.path.join(SRC, "template.html"), encoding="utf-8") as fh:
        template = fh.read()

    slugs = sorted(f[:-5] for f in os.listdir(PAGES) if f.endswith(".html"))
    if not slugs:
        raise SystemExit("Aucune page dans " + PAGES)

    for slug in slugs:
        dest = build_page(slug, template)
        print("  ok  " + os.path.basename(dest))

    print("\n%d pages generees." % len(slugs))


if __name__ == "__main__":
    sys.exit(main())
