#!/usr/bin/env python3
"""Generate images/og-default.png — the social/text-share card. On-brand: white background,
two-tone "Peter Lohmann" (Peter = navy, Lohmann = accent blue) matching the site nav."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
NAVY = (31, 58, 77)      # --navy
BLUE = (44, 124, 176)    # --primary / accent
MUTED = (88, 107, 120)   # --muted slate
img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)

def font(paths, size):
    for p in paths:
        try: return ImageFont.truetype(p, size)
        except Exception: continue
    return ImageFont.load_default()

SERIF = ["/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
         "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"]
SANS = ["/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Helvetica.ttc"]
f_name = font(SERIF, 138)
f_sub = font(SANS, 40)
f_dom = font(SANS, 31)

def center_two(y, a, b, fa, ca, cb):
    wa = d.textlength(a, font=fa); wb = d.textlength(b, font=fb if False else fa)
    x = (W - (wa + wb)) / 2
    d.text((x, y), a, font=fa, fill=ca)
    d.text((x + wa, y), b, font=fa, fill=cb)

def center(y, text, f, fill):
    d.text(((W - d.textlength(text, font=f)) / 2, y), text, font=f, fill=fill)

# subtle brand accent bar across the very top
d.rectangle([0, 0, W, 8], fill=BLUE)

# name: "Peter " (navy) + "Lohmann" (blue)
center_two(196, "Peter ", "Lohmann", f_name, NAVY, BLUE)
# accent underline
uw = 132
d.rectangle([(W - uw) / 2, 372, (W + uw) / 2, 379], fill=BLUE)
# subtitle (two lines)
center(424, "Property management data, insights,", f_sub, MUTED)
center(474, "and the Largest PM Companies list", f_sub, MUTED)
# domain
center(556, "peterlohmann.com", f_dom, BLUE)

img.save("images/og-default.png", "PNG")
print("wrote images/og-default.png", img.size)
