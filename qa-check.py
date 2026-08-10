#!/usr/bin/env python3
"""
Pre-launch QA sweep: scan every page for broken internal links and missing local images.
Read-only. Run before publishing (and again after any big batch of edits):  python3 qa-check.py
Skips external links (http/mailto/tel) and obvious JS fragments. Treats extensionless internal
links as OK if the .html file exists (GitHub Pages serves both).
"""
import glob, re, os

ROOT = os.getcwd()
files = glob.glob("*.html") + glob.glob("blog/*.html") + glob.glob("report/index.html")

def resolve(src_file, ref):
    ref = ref.split('#')[0].split('?')[0].strip()
    if not ref or "'" in ref or "+" in ref or "{" in ref:   # skip JS fragments / templates
        return None
    if ref.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', 'data:', '//')):
        return None
    base = ROOT if ref.startswith('/') else os.path.dirname(os.path.join(ROOT, src_file))
    return os.path.normpath(os.path.join(base, ref.lstrip('/')))

broken_links, missing_imgs = [], []
for f in files:
    h = open(f, encoding="utf-8").read()
    # strip <script> blocks so JS string-building isn't mistaken for links
    h_nojs = re.sub(r'<script\b.*?</script>', '', h, flags=re.S)
    for m in re.finditer(r'<a[^>]+href="([^"]+)"', h_nojs):
        p = resolve(f, m.group(1))
        if p and not (os.path.exists(p) or os.path.exists(p + '.html') or os.path.isdir(p)):
            broken_links.append((f, m.group(1)))
    for m in re.finditer(r'<(?:img|source)[^>]+src="([^"]+)"', h_nojs):
        p = resolve(f, m.group(1))
        if p and not os.path.exists(p):
            missing_imgs.append((f, m.group(1)))

print(f"QA sweep: scanned {len(files)} pages.")
print(f"\nBroken internal links: {len(broken_links)}")
for f, r in broken_links: print(f"  {f}  ->  {r}")
print(f"\nMissing local images: {len(set(missing_imgs))}")
for f, r in sorted(set(missing_imgs)): print(f"  {f}  ->  {r}")
if not broken_links and not missing_imgs:
    print("\nAll clean.")
