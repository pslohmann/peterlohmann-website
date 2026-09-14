#!/usr/bin/env python3
"""
Social share images for blog posts: images/blog/<slug>--og.jpg at 1200x630.

Why: LinkedIn, Facebook and X show a large preview card only for a roughly
1.91:1 image, and LinkedIn's WebP support is unreliable. Blog covers come in
every shape (square, portrait, 4:3, 16:9) and are WebP, so shares were cropped
badly or showed no image at all.

How each image is fitted:
  - already close to widescreen (aspect 1.6 to 2.2): centre-cropped to fill
  - anything else: the whole image is placed, uncropped, on a softened,
    blurred copy of itself, so no faces or text get cut off

It then points each post's og:image at the JPG and adds width/height tags, so
LinkedIn renders the card on the very first share.

Safe to re-run: it regenerates only when the source cover is newer than the
JPG, and rewrites tags only when they differ.

    python3 make-og-share-images.py            # all posts
    python3 make-og-share-images.py <slug>     # one post
"""
import glob, json, os, re, sys
from PIL import Image, ImageFilter, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.peterlohmann.com"
W, H = 1200, 630
TARGET = W / H

def fit(src):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    r = w / h
    if 1.6 <= r <= 2.2:
        # fill: crop the overflow from the centre
        if r > TARGET:
            nw = round(h * TARGET); x = (w - nw) // 2
            im = im.crop((x, 0, x + nw, h))
        else:
            nh = round(w / TARGET); y = (h - nh) // 2
            im = im.crop((0, y, w, y + nh))
        return im.resize((W, H), Image.LANCZOS)
    # contain: whole image over a blurred, softened fill of itself
    bg_scale = max(W / w, H / h)
    bg = im.resize((round(w * bg_scale), round(h * bg_scale)), Image.LANCZOS)
    bx = (bg.width - W) // 2; by = (bg.height - H) // 2
    bg = bg.crop((bx, by, bx + W, by + H)).filter(ImageFilter.GaussianBlur(28))
    bg = ImageEnhance.Brightness(bg).enhance(0.72)
    fg_scale = min(W / w, H / h)
    fg = im.resize((round(w * fg_scale), round(h * fg_scale)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    return bg

OG_RE = re.compile(r'<meta property="og:image" content="([^"]*)" />')
SOURCES = os.path.join(HERE, "data", "og-share-sources.json")

def load_sources():
    try:
        return json.load(open(SOURCES))
    except (OSError, ValueError):
        return {}

def process(post, sources):
    slug = os.path.basename(post)[:-5]
    h = open(post, encoding="utf-8").read()
    if 'http-equiv="refresh"' in h:
        return None
    m = OG_RE.search(h)
    if not m:
        return None
    cur = m.group(1)
    og_url = f"{SITE}/images/blog/{slug}--og.jpg"
    # The source is whatever image the post chose for sharing before this script
    # touched it (usually the cover, sometimes a 16:9 card or a chart). It is
    # remembered in data/og-share-sources.json so re-runs keep that choice.
    if slug in sources:
        src_rel = sources[slug]
    elif cur != og_url:
        src_rel = cur.replace(SITE + "/", "").split("?")[0]
    else:
        return f"  ! {slug}: already points at its share image but no source is recorded"
    src = os.path.join(HERE, src_rel)
    if not os.path.exists(src):
        return f"  ! {slug}: source image {src_rel} not found, left as is"
    sources[slug] = src_rel
    out = os.path.join(HERE, "images", "blog", f"{slug}--og.jpg")
    made = False
    if not os.path.exists(out) or os.path.getmtime(src) > os.path.getmtime(out):
        fit(src).save(out, "JPEG", quality=84, optimize=True, progressive=True)
        made = True
    new = h
    if cur != og_url:
        new = new.replace(m.group(0), f'<meta property="og:image" content="{og_url}" />', 1)
    if 'property="og:image:width"' not in new:
        new = new.replace(f'<meta property="og:image" content="{og_url}" />',
                          f'<meta property="og:image" content="{og_url}" />\n'
                          f'<meta property="og:image:width" content="{W}" />\n'
                          f'<meta property="og:image:height" content="{H}" />', 1)
    if new != h:
        open(post, "w", encoding="utf-8").write(new)
    return f"  {slug}: {'image made' if made else 'image current'}{', tags updated' if new != h else ''}"

if __name__ == "__main__":
    posts = ([os.path.join(HERE, "blog", a + ".html") for a in sys.argv[1:]]
             or sorted(glob.glob(os.path.join(HERE, "blog", "*.html"))))
    sources = load_sources()
    for p in posts:
        r = process(p, sources)
        if r: print(r)
    json.dump(dict(sorted(sources.items())), open(SOURCES, "w"), indent=1)
