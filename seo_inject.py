#!/usr/bin/env python3
"""
One-time helper: add canonical + Open Graph + Twitter tags to the hand-written pages and blog posts
(the generated Top 40 / state / blog-index templates are handled in their own generators). Idempotent:
skips any file that already has a canonical tag. Also adds Person JSON-LD to the home page and
BlogPosting JSON-LD to each blog post.
"""
import os, re, glob, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.peterlohmann.com"
OG_DEFAULT = SITE + "/images/og-default.png"

STATIC = ["index.html","contact.html","newsletter.html","podcast.html","products.html",
          "peterbot.html","featured.html","financial-interest-disclosure.html","blog.html"]

def clean_url(rel):
    return SITE + "/" if rel == "index.html" else SITE + "/" + rel[:-5]

def title_of(h):
    m = re.search(r"<title>(.*?)</title>", h, re.S)
    return m.group(1).strip() if m else "Peter Lohmann"

def desc_of(h):
    m = re.search(r'<meta name="description" content="([^"]*)"', h)
    return m.group(1) if m else ""

def insert_after_desc(h, block):
    # lambda replacement so backslashes in `block` (e.g. JSON-LD) are treated literally
    if re.search(r'<meta name="description"[^>]*>', h):
        return re.sub(r'<meta name="description"[^>]*>', lambda m: m.group(0) + "\n" + block, h, count=1)
    return re.sub(r"</title>", lambda m: m.group(0) + "\n" + block, h, count=1)

def og_block(url, title, desc, og_type="website", image=OG_DEFAULT):
    t = [f'<link rel="canonical" href="{url}" />',
         f'<meta property="og:type" content="{og_type}" />',
         f'<meta property="og:title" content="{html.escape(title, quote=True)}" />']
    if desc:
        t.append(f'<meta property="og:description" content="{desc}" />')
    t += [f'<meta property="og:url" content="{url}" />',
          f'<meta property="og:image" content="{image}" />',
          '<meta property="og:site_name" content="Peter Lohmann" />',
          '<meta name="twitter:card" content="summary_large_image" />']
    return "\n".join(t)

PERSON_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Person","name":"Peter Lohmann","url":"%s/","image":"%s","jobTitle":"Property management operator, writer, and podcaster","worksFor":{"@type":"Organization","name":"RL Property Management"},"sameAs":["https://www.linkedin.com/in/pslohmann/","https://www.youtube.com/@peterlohmann","https://x.com/pslohmann","https://www.facebook.com/lohmann","https://www.instagram.com/peterlohmann_media/"]}
</script>''' % (SITE, OG_DEFAULT)

def do_static():
    n = 0
    for rel in STATIC:
        p = os.path.join(HERE, rel)
        if not os.path.exists(p):
            continue
        h = open(p, encoding="utf-8").read()
        if 'rel="canonical"' in h:
            continue
        url = clean_url(rel)
        block = og_block(url, title_of(h), desc_of(h))
        if rel == "index.html":
            block += "\n" + PERSON_LD
        open(p, "w", encoding="utf-8").write(insert_after_desc(h, block))
        n += 1
    return n

def blog_cover(h):
    m = re.search(r'\.\./images/blog/([^"]+?--cover\.webp)', h) or re.search(r'\.\./images/blog/([^"]+\.webp)', h)
    return SITE + "/images/blog/" + m.group(1) if m else OG_DEFAULT

def blog_date_iso(h):
    m = re.search(r'class="article-meta">\s*([A-Z][a-z]{2} \d{1,2}, \d{4})', h)
    if not m:
        return None
    try:
        return datetime.datetime.strptime(m.group(1), "%b %d, %Y").date().isoformat()
    except ValueError:
        return None

def do_blog():
    n = 0
    for p in sorted(glob.glob(os.path.join(HERE, "blog", "*.html"))):
        rel = "blog/" + os.path.basename(p)
        h = open(p, encoding="utf-8").read()
        if 'rel="canonical"' in h:
            continue
        url = clean_url(rel)
        title = title_of(h)
        desc = desc_of(h)
        cover = blog_cover(h)
        block = og_block(url, title, desc, og_type="article", image=cover)
        # BlogPosting JSON-LD
        headline = title.replace(" &middot; Peter Lohmann", "").replace(" · Peter Lohmann", "")
        iso = blog_date_iso(h)
        ld = {"@context": "https://schema.org", "@type": "BlogPosting",
              "headline": html.unescape(headline), "image": cover, "url": url,
              "author": {"@type": "Person", "name": "Peter Lohmann", "url": SITE + "/"},
              "publisher": {"@type": "Person", "name": "Peter Lohmann"},
              "mainEntityOfPage": url}
        if iso:
            ld["datePublished"] = iso
        import json
        block += '\n<script type="application/ld+json">' + json.dumps(ld, separators=(",", ":"), ensure_ascii=False) + "</script>"
        open(p, "w", encoding="utf-8").write(insert_after_desc(h, block))
        n += 1
    return n

if __name__ == "__main__":
    s = do_static(); b = do_blog()
    print(f"static pages tagged: {s}   blog posts tagged: {b}")
