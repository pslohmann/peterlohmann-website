"""Five redrawn blog covers (Sep 8 to Oct 16, 2026). Writes cover-src/<slug>.html."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cover_kit import *

# 1. Sep 8: owner draw prep (DARK). A payout table where most rows pass and three get flagged.
def owner_draw():
    b = []
    b.append('<circle cx="600" cy="338" r="330" fill="url(#glowB)" opacity=".5"/>')
    b.append(f'<g filter="url(#rim)"><rect x="330" y="104" width="540" height="468" rx="20" fill="{NAVY}" stroke="{EDGE}" stroke-width="1.5"/></g>')
    b.append(f'<rect x="362" y="136" width="150" height="12" rx="6" fill="{BAR}" fill-opacity=".8"/>')
    b.append(f'<rect x="720" y="136" width="90" height="12" rx="6" fill="{BAR}" fill-opacity=".45"/>')
    flagged = {2, 5}
    widths = [170, 130, 190, 150, 120, 180, 140, 160]
    for i in range(8):
        y = 176 + i * 47
        if i in flagged:
            b.append(f'<rect x="346" y="{y - 4}" width="508" height="42" rx="10" fill="{ORANGE}" fill-opacity=".2" stroke="{ORANGE}" stroke-opacity=".6" stroke-width="1.5"/>')
        b.append(f'<rect x="366" y="{y + 12}" width="{widths[i]}" height="10" rx="5" fill="{BAR}" fill-opacity="{".9" if i in flagged else ".55"}"/>')
        b.append(f'<rect x="660" y="{y + 12}" width="96" height="10" rx="5" fill="{BAR}" fill-opacity="{".9" if i in flagged else ".4"}"/>')
        if i in flagged:
            b.append(disc(810, y + 17, 16, ORANGE, "alert", glow="soft", isize=20))
        else:
            b.append(disc(810, y + 17, 14, BLUE, "check", isize=16))
    # inputs on the left, AI on the corner, clock: done in an afternoon
    b.append(f'<path d="M232 228 C 290 228 290 260 330 270" stroke="{BAR}" stroke-opacity=".5" stroke-width="2.5" stroke-dasharray="3 9"/>')
    b.append(f'<path d="M232 448 C 290 448 290 410 330 400" stroke="{BAR}" stroke-opacity=".5" stroke-width="2.5" stroke-dasharray="3 9"/>')
    b.append(disc(190, 228, 44, BLUE, "house", isize=40))
    b.append(disc(190, 448, 44, BLUE, "dollar", isize=40))
    b.append('<circle cx="870" cy="104" r="120" fill="url(#glowO)"/>')
    b.append(f'<circle cx="870" cy="104" r="54" fill="{ORANGE}" filter="url(#soft)"/>')
    b.append(f'<path d="{SPARKLE}" transform="translate(870 104) scale(.75)" fill="#fff"/>')
    b.append(f'<path d="M870 572 C 940 600 990 540 1010 470" stroke="{BAR}" stroke-opacity=".5" stroke-width="2.5" stroke-dasharray="3 9"/>')
    b.append(f'<circle cx="1010" cy="420" r="58" stroke="{BLUE}" stroke-opacity=".35" stroke-width="2"/>')
    b.append(disc(1010, 420, 46, NAVY2, "clock", isize=42))
    return page(DARK, "\n".join(b))

# 2. Sep 15: franchises (LIGHT). The four-system chart, drawn on a navy panel with glowing lines.
def franchises():
    b = []
    b.append(f'<g filter="url(#lift)"><rect x="140" y="92" width="920" height="491" rx="24" fill="{NAVY2}"/></g>')
    l, r, t, bt = 220, 960, 170, 520
    for i in range(5):
        y = t + (bt - t) * i / 4
        b.append(f'<path d="M{l} {y:.0f}H{r}" stroke="#fff" stroke-opacity=".08" stroke-width="2"/>')
    series = [("#4a9fd6", [0.62, 0.58, 0.52, 0.44, 0.35, 0.27, 0.26]),
              (ORANGE, [0.74, 0.66, 0.53, 0.49, 0.48, 0.40, 0.39]),
              ("#E8A41F", [0.84, 0.83, 0.82, 0.81, 0.79, 0.77, 0.76]),
              ("#1FAA7A", [0.91, 0.91, 0.90, 0.88, 0.87, 0.86, 0.81])]
    for color, ys in series:
        pts = [(l + (r - l) * i / 6, t + (bt - t) * y) for i, y in enumerate(ys)]
        d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
        b.append(f'<path d="{d}" stroke="{color}" stroke-width="7" filter="url(#soft)"/>')
        for j, (x, y) in enumerate(pts):
            rr = 11 if j == 6 else 7
            b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rr}" fill="{NAVY2}" stroke="{color}" stroke-width="4"/>')
    # stickers on the panel corner: the franchise storefront and the fees
    b.append('<circle cx="150" cy="104" r="120" fill="url(#glowO)"/>')
    b.append(disc(150, 104, 52, ORANGE, "store", glow="soft", isize=46))
    b.append(disc(262, 72, 34, BLUE, "dollar", isize=30))
    return page(LIGHT, "\n".join(b))

# 3. Sep 22: PM API Report Card (DARK, words allowed). A report card with five category rows.
def api_card():
    b = []
    b.append('<circle cx="560" cy="338" r="340" fill="url(#glowB)" opacity=".55"/>')
    b.append(f'<g filter="url(#rim)"><rect x="250" y="92" width="620" height="492" rx="22" fill="{NAVY}" stroke="{EDGE}" stroke-width="1.5"/></g>')
    b.append('<text x="290" y="160" fill="#fff" font-size="38" font-weight="800" letter-spacing="-.5">PM API Report Card</text>')
    b.append(f'<rect x="290" y="182" width="72" height="5" rx="2.5" fill="{ORANGE}"/>')
    rows = [("plug", .86, BLUE), ("gear", .66, ORANGE), ("key", 1.0, BLUE), ("book", .58, ORANGE), ("dollar", .96, BLUE)]
    for i, (name, frac, color) in enumerate(rows):
        y = 238 + i * 66
        b.append(disc(316, y, 22, BLUE if color == BLUE else "#3b5a70", name, isize=22))
        b.append(f'<rect x="360" y="{y - 7}" width="460" height="14" rx="7" fill="#1b3446"/>')
        b.append(f'<rect x="360" y="{y - 7}" width="{460 * frac:.0f}" height="14" rx="7" fill="{color}" filter="url(#soft)"/>')
    b.append('<circle cx="884" cy="140" r="150" fill="url(#glowO)"/>')
    b.append(f'<circle cx="884" cy="140" r="78" fill="{ORANGE}" filter="url(#soft)"/>')
    b.append(f'<circle cx="884" cy="140" r="96" stroke="{ORANGE}" stroke-opacity=".45" stroke-width="2"/>')
    b.append('<text x="884" y="170" text-anchor="middle" fill="#fff" font-size="86" font-weight="800">A</text>')
    # the software being graded, plugged in from the right
    b.append(f'<path d="M870 420 C 930 420 950 470 1010 470" stroke="{BAR}" stroke-opacity=".5" stroke-width="2.5" stroke-dasharray="3 9"/>')
    b.append(f'<rect x="1000" y="420" width="104" height="100" rx="20" fill="{BLUE}"/>')
    b.append('<g transform="translate(1022 440) scale(2.5)" stroke="#fff" stroke-width="1.9"><path d="M8 7 3 12l5 5M16 7l5 5-5 5"/></g>')
    return page(DARK, "\n".join(b))

# 4. Oct 9: conference calendar (LIGHT). A navy calendar with marked dates and the trip around it.
def conferences():
    b = []
    b.append('<path d="M190 200 C 300 60 470 70 520 120 M680 120 C 760 60 930 70 1010 200 M1010 470 C 940 610 760 610 700 560 M500 560 C 430 610 260 610 190 470" stroke="#5f7a8f" stroke-opacity=".55" stroke-width="2.5" stroke-dasharray="3 10"/>')
    b.append('<circle cx="600" cy="338" r="300" fill="url(#glowO)"/>')
    b.append(f'<g filter="url(#lift)"><rect x="410" y="120" width="380" height="440" rx="26" fill="{NAVY2}"/></g>')
    b.append(f'<path d="M410 146a26 26 0 0 1 26-26h328a26 26 0 0 1 26 26v62H410z" fill="{ORANGE}"/>')
    for x in (500, 700):
        b.append(f'<rect x="{x - 9}" y="92" width="18" height="58" rx="9" fill="#1f2a36"/>')
    marked = {(0, 2), (1, 0), (2, 3), (3, 1)}
    for row in range(4):
        for col in range(4):
            x, y = 452 + col * 78, 240 + row * 76
            if (row, col) in marked:
                b.append(f'<rect x="{x}" y="{y}" width="56" height="56" rx="12" fill="{ORANGE}" filter="url(#soft)"/>')
                b.append(icon("check", x + 28, y + 28, 30, width=2.6))
            else:
                b.append(f'<rect x="{x}" y="{y}" width="56" height="56" rx="12" fill="#ffffff" fill-opacity=".12"/>')
    for cx, cy, name in ((190, 200, "plane"), (1010, 200, "badge"), (1010, 470, "mic"), (190, 470, "pin")):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="66" stroke="{BLUE}" stroke-opacity=".3" stroke-width="2"/>')
        b.append(disc(cx, cy, 54, BLUE, name, isize=48))
    return page(LIGHT, "\n".join(b))

# 5. Oct 16: NARPM Week (DARK). A megaphone sending out a fan of announcement cards.
def narpm():
    b = []
    for r_, op in ((170, .35), (230, .22), (290, .12)):
        b.append(f'<path d="M{330 + r_ * .55:.0f} {338 - r_ * .83:.0f} A {r_} {r_} 0 0 1 {330 + r_ * .55:.0f} {338 + r_ * .83:.0f}" stroke="{ORANGE}" stroke-opacity="{op}" stroke-width="4"/>')
    b.append('<circle cx="330" cy="338" r="250" fill="url(#glowO)"/>')
    b.append(f'<circle cx="330" cy="338" r="128" stroke="{ORANGE}" stroke-opacity=".4" stroke-width="2"/>')
    b.append(f'<circle cx="330" cy="338" r="108" fill="{ORANGE}" filter="url(#soft)"/>')
    b.append(icon("megaphone", 330, 338, 112, width=1.7))
    cards = [("chart", 640, 92), ("rocket", 700, 194), ("sparkle", 730, 296), ("users", 700, 398), ("star", 640, 500)]
    for i, (name, x, y) in enumerate(cards):
        b.append(f'<g filter="url(#rim)"><rect x="{x}" y="{y}" width="420" height="84" rx="18" fill="{NAVY}" stroke="{EDGE}" stroke-width="1.5"/></g>')
        fill = ORANGE if name == "sparkle" else BLUE
        b.append(disc(x + 46, y + 42, 26, fill, name, isize=28))
        b.append(f'<rect x="{x + 92}" y="{y + 26}" width="{[200, 240, 180, 220, 190][i]}" height="11" rx="5.5" fill="{BAR}" fill-opacity=".8"/>')
        b.append(f'<rect x="{x + 92}" y="{y + 49}" width="{[140, 120, 160, 110, 150][i]}" height="9" rx="4.5" fill="{BAR}" fill-opacity=".4"/>')
    return page(DARK, "\n".join(b))

PAGES = {
    "how-i-automated-owner-draw-prep-with-ai": owner_draw,
    "property-management-franchises-2026": franchises,
    "why-i-built-the-pm-api-report-card": api_card,
    "property-management-conference-calendar-2026-2027": conferences,
    "narpm-week-las-vegas-vendor-announcements": narpm,
}
os.makedirs(OUT, exist_ok=True)
for slug, fn in PAGES.items():
    with open(os.path.join(OUT, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(fn())
    print("wrote", slug)
