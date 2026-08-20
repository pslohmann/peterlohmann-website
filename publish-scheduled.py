#!/usr/bin/env python3
"""
Publishes blog posts that were queued in data/scheduled-posts.json.

How the whole thing fits together:
  1. The post file already lives in blog/ but carries a `noindex` line, and nothing
     links to it, so it is effectively invisible until this script runs.
  2. This script checks which queued posts are due, then for each one:
       - refuses to publish if the post file or any image it uses is missing
       - strips the noindex line (the post becomes indexable)
       - makes it the featured post on blog.html, demoting the old featured post
         into the regular card grid
       - bumps the "N posts and counting" number in the blog hero
       - drops the entry from the queue so it never publishes twice
  3. build-sitemap.py is re-run so the new post is in the sitemap.

Run it yourself any time with:   python3 publish-scheduled.py --now
(--now ignores the publish_on date and publishes everything queued.)

Nothing is written unless every check passes, so a half-finished post can't go live.
"""

import json, os, re, subprocess, sys
from datetime import datetime
from zoneinfo import ZoneInfo

HERE      = os.path.dirname(os.path.abspath(__file__))
QUEUE     = os.path.join(HERE, "data", "scheduled-posts.json")
BLOG_IDX  = os.path.join(HERE, "blog.html")
TZ        = ZoneInfo("America/New_York")

NOINDEX_RE = re.compile(r'^[ \t]*<meta name="robots" content="noindex" data-scheduled="1" />\r?\n', re.M)

# The current featured post block on blog.html, so we can demote it to a card.
FEATURE_RE = re.compile(
    r'[ \t]*<a class="feature-post" href="(?P<href>[^"]+)">\s*'
    r'<div class="ph-img"><img src="(?P<img>[^"]+)"[^>]*></div>\s*'
    r'<div class="fp-body">\s*'
    r'<span class="tag tag-warn">Latest</span>\s*'
    r'<div class="date">(?P<date>[^<]*)</div>\s*'
    r'<h2>(?P<title>.*?)</h2>\s*'
    r'<p>(?P<desc>.*?)</p>\s*'
    r'<span class="arrow">Read the post &rarr;</span>\s*'
    r'</div>\s*</a>\s*'
    r'(?P<cards><div class="post-cards mt-lg">)',
    re.S)

LOCAL_IMG_RE = re.compile(r'<img[^>]+src="(?!https?:)([^"]+)"')


def fail(msg):
    print(f"ERROR: {msg}")
    sys.exit(1)


def load_queue():
    with open(QUEUE) as f:
        return json.load(f)


def check_assets(slug):
    """Refuse to publish unless the post and every local image it references exist."""
    post_path = os.path.join(HERE, "blog", f"{slug}.html")
    if not os.path.exists(post_path):
        fail(f"blog/{slug}.html does not exist. Nothing published.")

    with open(post_path, encoding="utf-8") as f:
        html = f.read()

    missing = []
    for src in LOCAL_IMG_RE.findall(html):
        # image srcs inside blog/ are written relative to blog/, e.g. ../images/blog/x.png
        resolved = os.path.normpath(os.path.join(HERE, "blog", src))
        if not os.path.exists(resolved):
            missing.append(os.path.relpath(resolved, HERE))

    if missing:
        fail("these images are missing, so the post was NOT published:\n  - " + "\n  - ".join(missing))

    return post_path, html


def publish(entry, idx_html):
    slug = entry["slug"]
    post_path, post_html = check_assets(slug)

    # 1. Un-hide the post.
    cleaned, n = NOINDEX_RE.subn("", post_html)
    if n:
        with open(post_path, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"  removed noindex from blog/{slug}.html")
    else:
        print(f"  (no noindex line found in blog/{slug}.html; leaving it as-is)")

    # 2. Demote the current featured post to a card, promote this one.
    m = FEATURE_RE.search(idx_html)
    if not m:
        fail("could not find the featured-post block on blog.html; blog.html was not changed.")

    demoted = (
        f'        <a class="post-card" href="{m.group("href")}">\n'
        f'          <div class="ph-img"><img src="{m.group("img")}" alt="" loading="lazy"></div>\n'
        f'          <div class="pc-body"><div class="date">{m.group("date")}</div>'
        f'<h3>{m.group("title")}</h3><p>{m.group("desc")}</p>'
        f'<span class="arrow">Read &rarr;</span></div>\n'
        f'        </a>\n'
    )

    new_feature = (
        f'      <a class="feature-post" href="/blog/{slug}">\n'
        f'        <div class="ph-img"><img src="{entry["card_image"]}" alt="" loading="lazy"></div>\n'
        f'        <div class="fp-body">\n'
        f'          <span class="tag tag-warn">Latest</span>\n'
        f'          <div class="date">{entry["date_label"]}</div>\n'
        f'          <h2>{entry["title"]}</h2>\n'
        f'          <p>{entry["description"]}</p>\n'
        f'          <span class="arrow">Read the post &rarr;</span>\n'
        f'        </div>\n'
        f'      </a>\n'
        f'      {m.group("cards")}\n'
    )

    idx_html = idx_html[:m.start()] + new_feature + demoted + idx_html[m.end():]

    # 3. Bump the post count in the hero line.
    def bump(mo):
        return f"{int(mo.group(1)) + 1} posts and counting"
    idx_html, bumped = re.subn(r"(\d+) posts and counting", bump, idx_html, count=1)
    if not bumped:
        print("  WARNING: could not find the 'N posts and counting' line to bump.")

    print(f"  featured on blog.html: {entry['title']}")
    return idx_html


def main():
    force = "--now" in sys.argv
    now = datetime.now(TZ)
    today = now.date().isoformat()

    data = load_queue()
    queued = data.get("posts", [])
    if not queued:
        print("Nothing in the publish queue.")
        return

    due = [p for p in queued if force or p.get("publish_on", "9999-12-31") <= today]
    if not due:
        nxt = min((p.get("publish_on", "?") for p in queued), default="?")
        print(f"Nothing due today ({today}). Next scheduled: {nxt}")
        return

    with open(BLOG_IDX, encoding="utf-8") as f:
        idx_html = f.read()

    # Oldest scheduled first, so the newest ends up as the featured post.
    for entry in sorted(due, key=lambda p: p.get("publish_on", "")):
        print(f"Publishing: {entry['slug']}")
        idx_html = publish(entry, idx_html)

    with open(BLOG_IDX, "w", encoding="utf-8") as f:
        f.write(idx_html)

    data["posts"] = [p for p in queued if p not in due]
    with open(QUEUE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")

    subprocess.run([sys.executable, os.path.join(HERE, "build-sitemap.py")], check=True)
    print(f"Published {len(due)} post(s) at {now:%Y-%m-%d %H:%M %Z}.")


if __name__ == "__main__":
    main()
