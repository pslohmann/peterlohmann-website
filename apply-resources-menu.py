#!/usr/bin/env python3
"""
One-time menu change: groups Blog, Free Courses and PeterBot under a "Resources" dropdown in the
top menu, adds Free Courses to the footer, and bumps the styles.css / site.js cache version so
browsers fetch the new menu styles.

The menu is written out in full on every page and inside four page builders, so this script edits
all of them: every .html page in the repo (except _archive/ and _drafts/) plus build-blog.py,
build-podcast.py, build-largest-list.py and build-api-grader.py. The courses builder copies its
menu from blog.html, and the AI timeline's share pages copy theirs from its index page.

RUN:  python3 apply-resources-menu.py          (safe to run again; already-converted files are skipped)

build-largest-list.py keeps its menu in NAV_LINKS / FOOT_LINKS fragments, which were edited by hand
(2026-10-29), so the script reports it as not converted; that's expected.
"""
import os, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
OLD_V, NEW_V = "28", "29"
ORDER_BEFORE = ["Newsletter", "Podcast", "Largest PM Companies", "API Grader"]
GROUP = ["Blog", "Free Courses", "PeterBot"]
ORDER_AFTER = ["M&amp;A Report", "Products"]

NAV_RE = re.compile(r'(?P<open><div class="links" id="navlinks">)(?P<body>(?:\s*<a [^>]*>[^<]*</a>)+)(?P<ws>\s*)</div>')
A_RE = re.compile(r'<a href="(?P<href>[^"]+)"(?P<active> class="active")?>(?P<label>[^<]+)</a>')
FOOT_BLOG_RE = re.compile(r'(<nav class="foot-links"[^>]*>.*?)(\n?(?P<ind>[ \t]*)<a href="[^"]*blog[^"]*"[^>]*>Blog</a>)', re.S)


def new_nav(m):
    body = m.group("body")
    ind = re.match(r"\s*?\n?([ \t]*)<a", body).group(1) if "\n" in body else ""
    nl = "\n" if "\n" in body else " "
    items = {a.group("label"): a for a in A_RE.finditer(body)}
    if not all(k in items for k in ORDER_BEFORE + ["Blog", "PeterBot"] + ORDER_AFTER):
        return None

    def a(label, href=None):
        it = items.get(label)
        href = href or it.group("href")
        act = ' class="active"' if it is not None and it.group("active") else ""
        return f'<a href="{href}"{act}>{label}</a>'

    group_active = any(items[k].group("active") for k in ("Blog", "PeterBot"))
    btn_cls = "nav-group-btn active" if group_active else "nav-group-btn"
    sub = ind + "  "
    lines = [a(k) for k in ORDER_BEFORE]
    group = (f'<div class="nav-group">{nl}{sub}<a href="/blog" class="{btn_cls}" aria-haspopup="true" aria-expanded="false">Resources</a>'
             f'{nl}{sub}<div class="nav-menu" id="nav-resources">'
             f'{nl}{sub}  {a("Blog")}{nl}{sub}  <a href="/courses/">Free Courses</a>{nl}{sub}  {a("PeterBot")}'
             f'{nl}{sub}</div>{nl}{ind}</div>')
    lines.append(group)
    lines += [a(k) for k in ORDER_AFTER]
    return m.group("open") + "".join(nl + ind + x for x in lines) + m.group("ws") + "</div>"


def convert(text):
    changed = False
    if 'class="nav-group"' not in text:
        def repl(m):
            nonlocal changed
            out = new_nav(m)
            if out is None:
                return m.group(0)
            changed = True
            return out
        text = NAV_RE.sub(repl, text)
    if 'foot-links' in text and '>Free Courses</a>' not in text.split('foot-links', 1)[1][:3000]:
        def frepl(m):
            nonlocal changed
            changed = True
            sep = "\n" + m.group("ind") if m.group(2).startswith("\n") else " "
            return m.group(1) + m.group(2) + sep + '<a href="/courses/">Free Courses</a>'
        text = FOOT_BLOG_RE.sub(frepl, text)
    bumped = re.sub(r'((?:styles\.css|site\.js)\?v=)' + OLD_V + r'\b', r'\g<1>' + NEW_V, text)
    bumped = re.sub(r'(ASSET_V\s*=\s*")' + OLD_V + '"', r'\g<1>' + NEW_V + '"', bumped)
    return bumped, changed or bumped != text


def main():
    files = [f for f in glob.glob(os.path.join(HERE, "**", "*.html"), recursive=True)
             if not os.path.relpath(f, HERE).startswith(("_archive", "_drafts"))]
    files += [os.path.join(HERE, f) for f in ("build-blog.py", "build-podcast.py", "build-largest-list.py", "build-api-grader.py")]
    n = 0
    for f in sorted(files):
        s = open(f, encoding="utf-8").read()
        out, changed = convert(s)
        if changed and out != s:
            open(f, "w", encoding="utf-8").write(out)
            n += 1
    print(f"updated {n} files")
    left = [os.path.relpath(f, HERE) for f in files
            if 'id="navlinks"' in open(f, encoding="utf-8").read() and 'class="nav-group"' not in open(f, encoding="utf-8").read()]
    if left:
        print("menu NOT converted in:", ", ".join(left))


if __name__ == "__main__":
    main()
