#!/usr/bin/env python3
"""
Generate sitemap.xml listing every indexable page as a clean (extensionless) URL.
Scans the repo for *.html (root + blog/) so new pages (e.g. new per-state pages) are picked up.
Run after build-largest-list.py; also wired into the daily GitHub Action.
"""
import os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.peterlohmann.com"

# Pages that should not be indexed / listed.
EXCLUDE = {
    "index-bely.html", "index-bodoni.html", "index-sample.html",  # old mockups
    "404.html",
    "largest-pm-companies-coming-soon.html",                       # pre-launch teaser (swap-in only)
    "products.html", "about.html", "blog-index.html",              # legacy-URL redirect stubs
    "newsletter-tues-opt-out.html", "crane-promo-opt-out.html", "subscribed.html",  # noindex utility pages
}
# blog/ redirect stubs to skip (old slug -> refreshed post)
BLOG_EXCLUDE = {"how-to-design-processes-people-actually-use.html"}

def clean_url(rel):
    if rel == "index.html":
        return SITE + "/"
    return SITE + "/" + rel[:-5]   # strip ".html"

urls = []
for f in sorted(glob.glob(os.path.join(HERE, "*.html"))):
    b = os.path.basename(f)
    if b in EXCLUDE:
        continue
    urls.append(clean_url(b))
for f in sorted(glob.glob(os.path.join(HERE, "blog", "*.html"))):
    if os.path.basename(f) in BLOG_EXCLUDE:
        continue
    urls.append(clean_url("blog/" + os.path.basename(f)))
if os.path.exists(os.path.join(HERE, "report", "index.html")):
    urls.append(SITE + "/report/")

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    lines.append(f"  <url><loc>{u}</loc></url>")
lines.append("</urlset>")

with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print(f"wrote sitemap.xml with {len(urls)} URLs")
