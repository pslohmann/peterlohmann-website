#!/usr/bin/env python3
"""
Site icon set, drawn to match favicon.svg exactly: "PL" in Arial Bold, PL blue (#2C7CB0).

Writes, at the site root:
  favicon.ico            16/32/48, transparent   (browsers and RSS readers request /favicon.ico)
  apple-touch-icon.png   180x180, white ground   (iOS home screen; iOS shows transparency as black)
  icon-192.png           192x192, white ground   (Android home screen, via site.webmanifest)
  icon-512.png           512x512, white ground   (Android splash / install)

Run on a Mac (it uses the system Arial Bold):  python3 make-icons.py
"""
from PIL import Image, ImageDraw, ImageFont

FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
BLUE = (44, 124, 176, 255)

def draw(size, ground=None, scale=1.0):
    """Mirror the SVG: 256 viewBox, font-size 172, centred, baseline at y=189. `scale` < 1
    adds breathing room for the home-screen icons, which platforms crop into rounded shapes."""
    im = Image.new("RGBA", (size, size), ground or (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    k = size / 256 * scale
    font = ImageFont.truetype(FONT, round(172 * k))
    cx = size / 2
    baseline = size / 2 + (189 - 128) * k
    d.text((cx, baseline), "PL", font=font, fill=BLUE, anchor="ms")
    return im

if __name__ == "__main__":
    base = draw(256)
    base.save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    white = (255, 255, 255, 255)
    draw(180, white, 0.78).convert("RGB").save("apple-touch-icon.png", optimize=True)
    draw(192, white, 0.72).convert("RGB").save("icon-192.png", optimize=True)
    draw(512, white, 0.72).convert("RGB").save("icon-512.png", optimize=True)
    for f in ("favicon.ico", "apple-touch-icon.png", "icon-192.png", "icon-512.png"):
        print("  wrote", f, Image.open(f).size)
