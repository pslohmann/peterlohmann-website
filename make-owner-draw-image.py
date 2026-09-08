#!/usr/bin/env python3
"""
Featured image for the owner-draw automation post.

The motif comes straight out of the post: a reconciliation table where most rows
are fine to pay as-is, and the handful the script flags are highlighted. Kept
abstract on purpose, with bars instead of numbers, so the image never reads as
real account data.

Writes both sizes the blog uses:
  images/blog/how-i-automated-owner-draw-prep-with-ai--cover.webp   1200x380
  images/blog/how-i-automated-owner-draw-prep-with-ai--card.webp    1200x675
"""
from PIL import Image, ImageDraw

SLUG = "how-i-automated-owner-draw-prep-with-ai"

# Site tokens, so the image sits with the rest of the brand.
BG      = (246, 249, 252)
CARD    = (255, 255, 255)
LINE    = (220, 228, 236)
NAVY    = (31, 58, 77)
BLUE    = (44, 124, 176)
WASH    = (220, 231, 239)
MUTED   = (176, 190, 202)
AMBER   = (224, 112, 60)      # --orange
AMBER_BG = (253, 243, 232)
HEADBG  = (238, 243, 248)


def rounded(d, box, r, fill=None, outline=None, width=1):
    try:
        d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)
    except AttributeError:                      # very old Pillow
        d.rectangle(box, fill=fill, outline=outline, width=width)


def render(w, h, rows, flagged):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)

    pad = int(w * 0.055)
    card = (pad, pad, w - pad, h - pad)
    rounded(d, card, 18, fill=CARD, outline=LINE, width=2)

    inner_l, inner_r = card[0] + 1, card[2] - 1
    head_h = max(34, int((card[3] - card[1]) * 0.13))
    # header strip
    d.rectangle((inner_l, card[1] + 1, inner_r, card[1] + head_h), fill=HEADBG)
    d.line((inner_l, card[1] + head_h, inner_r, card[1] + head_h), fill=LINE, width=2)

    # two column labels, as bars rather than words
    lx = inner_l + int(w * 0.035)
    d.rounded_rectangle((lx, card[1] + head_h // 2 - 5, lx + int(w * 0.14),
                         card[1] + head_h // 2 + 5), radius=5, fill=MUTED)
    rx = inner_r - int(w * 0.035)
    d.rounded_rectangle((rx - int(w * 0.09), card[1] + head_h // 2 - 5, rx,
                         card[1] + head_h // 2 + 5), radius=5, fill=MUTED)

    body_top = card[1] + head_h + 1
    body_h = card[3] - body_top
    rh = body_h / rows

    for i in range(rows):
        y0 = body_top + i * rh
        y1 = y0 + rh
        hit = i in flagged
        if hit:
            d.rectangle((inner_l, y0, inner_r, y1), fill=AMBER_BG)
            d.rectangle((inner_l, y0, inner_l + 6, y1), fill=AMBER)   # flag rail
        if i:
            d.line((inner_l, y0, inner_r, y0), fill=LINE, width=1)

        mid = (y0 + y1) / 2
        bar_h = max(7, int(rh * 0.20))
        # property name bar, varied width so the rows read as data
        wid = int(w * (0.20 + 0.055 * ((i * 7) % 5)))
        d.rounded_rectangle((lx, mid - bar_h / 2, lx + wid, mid + bar_h / 2),
                            radius=bar_h // 2, fill=WASH if not hit else (243, 214, 194))
        # amount bar, right aligned
        awid = int(w * (0.055 + 0.018 * ((i * 3) % 4)))
        d.rounded_rectangle((rx - awid, mid - bar_h / 2, rx, mid + bar_h / 2),
                            radius=bar_h // 2, fill=AMBER if hit else BLUE)
    return img


def main():
    out = "images/blog"
    cover = render(1200, 380, rows=5, flagged={1, 3})
    cover.save(f"{out}/{SLUG}--cover.webp", "WEBP", quality=88, method=6)
    card = render(1200, 675, rows=8, flagged={2, 4, 6})
    card.save(f"{out}/{SLUG}--card.webp", "WEBP", quality=88, method=6)
    for suffix in ("cover", "card"):
        p = f"{out}/{SLUG}--{suffix}.webp"
        print(f"  wrote {p}  {Image.open(p).size}")


if __name__ == "__main__":
    main()
