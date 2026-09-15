#!/usr/bin/env python3
"""
Cover and card image for the 2026 PM franchise post (1200x675, used for both).

The motif comes from the post's first chart: four franchise systems' outlet counts over
time, where the two big systems level off and the two small ones keep climbing. Drawn as
abstract lines on a card with no numbers or labels, so it never reads as the data itself.

Writes images/blog/property-management-franchises-2026--cover.webp and --card.webp
"""
from PIL import Image, ImageDraw

SLUG = "property-management-franchises-2026"
W, H = 1200, 675
BG, CARD, LINE, GRID = (246, 249, 252), (255, 255, 255), (220, 228, 236), (234, 239, 244)
SERIES = [  # colours match the post's own charts; y values are shape only, not data
    ((44, 124, 176), [0.62, 0.58, 0.52, 0.44, 0.35, 0.27, 0.26]),   # levels off
    ((224, 112, 60), [0.74, 0.66, 0.53, 0.49, 0.48, 0.40, 0.39]),   # levels off
    ((232, 164, 31), [0.84, 0.83, 0.82, 0.81, 0.79, 0.77, 0.76]),   # slow climb
    ((31, 170, 122), [0.91, 0.91, 0.90, 0.88, 0.87, 0.86, 0.81]),   # late climb, stays below the yellow line (76 < 91)
]

def render(scale=2):
    w, h = W * scale, H * scale
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    pad = 60 * scale
    card = (pad, pad, w - pad, h - pad)
    d.rounded_rectangle(card, radius=22 * scale, fill=CARD, outline=LINE, width=2 * scale)
    l, t, r, b = card[0] + 70 * scale, card[1] + 60 * scale, card[2] - 90 * scale, card[3] - 60 * scale
    for i in range(5):                                   # faint horizontal grid
        y = t + (b - t) * i / 4
        d.line((l, y, r, y), fill=GRID, width=2 * scale)
    for colour, ys in SERIES:
        pts = [(l + (r - l) * i / (len(ys) - 1), t + (b - t) * y) for i, y in enumerate(ys)]
        d.line(pts, fill=colour, width=9 * scale, joint="curve")
        for x, y in pts:                                 # hollow markers, like the source chart
            rr = 10 * scale
            d.ellipse((x - rr, y - rr, x + rr, y + rr), fill=CARD, outline=colour, width=5 * scale)
    return im.resize((W, H), Image.LANCZOS)

if __name__ == "__main__":
    img = render()
    for kind in ("cover", "card"):
        out = f"images/blog/{SLUG}--{kind}.webp"
        img.save(out, "WEBP", quality=88, method=6)
        print("  wrote", out, img.size)
