#!/usr/bin/env python3
"""
Small card thumbnails for the blog list page: images/blog/<slug>--thumb.webp, 800x450.

blog.html shows each post as a 16:9 card about 340-420px wide, but it was loading
each post's full 1200px cover (up to ~360 KB apiece, 90+ of them). The cards use
object-fit: cover, which shows the centre of the image, so each thumbnail is cut
from the centre at 16:9: the card looks exactly the same, at a fraction of the weight.
800px wide stays sharp on retina phones and laptops.

Safe to re-run: skips thumbnails that are newer than their source, then points
every post card on blog.html at its thumbnail. The featured post at the top keeps
its full-size image. publish-scheduled.py uses the thumbnail when it demotes a
featured post to a card.

    python3 make-blog-thumbs.py          # every card on blog.html
    python3 make-blog-thumbs.py <slug>   # one new post, before it is published, so the card
                                         # it later becomes already has a thumbnail
"""
import glob, os, re, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 800, 450
CARD_RE = re.compile(r'(<a class="post-card" href="/blog/([^"]+)">\s*<div class="ph-img"><img src=")([^"]+)(")')

def thumb(src, out):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    if w / h > W / H:
        nw = round(h * W / H); x = (w - nw) // 2; im = im.crop((x, 0, x + nw, h))
    else:
        nh = round(w * H / W); y = (h - nh) // 2; im = im.crop((0, y, w, y + nh))
    # never enlarge: a small source keeps its own resolution (the browser scales it anyway)
    if im.width > W:
        im = im.resize((W, H), Image.LANCZOS)
    im.save(out, "WEBP", quality=80, method=6)

def main():
    idx_path = os.path.join(HERE, "blog.html")
    html = open(idx_path, encoding="utf-8").read()
    made = repointed = 0
    def swap(m):
        nonlocal made, repointed
        slug, src = m.group(2), m.group(3)
        rel = f"images/blog/{slug}--thumb.webp"
        if src == rel:
            return m.group(0)
        src_path = os.path.join(HERE, src)
        out = os.path.join(HERE, rel)
        if not os.path.exists(src_path):
            print(f"  ! {slug}: card image {src} not found, left as is")
            return m.group(0)
        if not os.path.exists(out) or os.path.getmtime(src_path) > os.path.getmtime(out):
            thumb(src_path, out); made += 1
        repointed += 1
        return m.group(1) + rel + m.group(4)
    new = CARD_RE.sub(swap, html)
    if new != html:
        open(idx_path, "w", encoding="utf-8").write(new)
    print(f"thumbnails made: {made} | cards repointed: {repointed}")

def one(slug):
    """Thumbnail for a single post from its --card image, else its --cover image."""
    for kind in ("card", "cover"):
        found = sorted(glob.glob(os.path.join(HERE, "images", "blog", f"{slug}--{kind}.*")))
        if found:
            out = os.path.join(HERE, "images", "blog", f"{slug}--thumb.webp")
            thumb(found[0], out)
            print(f"  {slug}: thumbnail made from {os.path.basename(found[0])}")
            return
    print(f"  ! {slug}: no --card or --cover image found")

if __name__ == "__main__":
    if sys.argv[1:]:
        for a in sys.argv[1:]:
            one(a)
    else:
        main()
