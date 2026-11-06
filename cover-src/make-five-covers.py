"""Five redrawn blog covers in the new style. Writes cover-src/<slug>.html in the site repo."""
import os
REPO = "/Users/andrewswensen/Documents/Claude/Projects/peterlohmann-website"
OUT = os.path.join(REPO, "cover-src")

DARK = ("radial-gradient(900px 560px at 50% 50%, #24465e 0%, #1b3446 55%, #142838 100%)",
        "rgba(255,255,255,.07)")
LIGHT = ("radial-gradient(900px 560px at 50% 50%, #ffffff 0%, #f6f9fc 60%, #eef3f8 100%)",
         "rgba(31,42,54,.07)")

ICON = {
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "alert": '<path d="M12 6.5v7"/><path d="M12 17.5h.01"/>',
    "house": '<path d="M3 10.2 12 3l9 7.2V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    "dollar": '<path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "store": '<path d="M3 9l1.6-5h14.8L21 9"/><path d="M3 9h18v11H3z"/><path d="M9 20v-6h6v6"/>',
    "plug": '<path d="M9 2v6M15 2v6"/><path d="M6 8h12v4a6 6 0 0 1-12 0z"/><path d="M12 18v4"/>',
    "gear": '<circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1"/>',
    "key": '<circle cx="7.5" cy="15.5" r="4.5"/><path d="M10.7 12.3 21 2M17 6l3 3M14 9l2 2"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
    "plane": '<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "badge": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10.5" r="2"/><path d="M14.5 9h3.5M14.5 13h3.5M5.8 16.5c.6-1.4 1.8-2 3.2-2s2.6.6 3.2 2"/>',
    "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10v1a7 7 0 0 1-14 0v-1M12 18v4M8 22h8"/>',
    "megaphone": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    "chart": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
    "rocket": '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>',
    "users": '<circle cx="9" cy="7" r="4"/><path d="M3 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2M16 3.13a4 4 0 0 1 0 7.75M21 21v-2a4 4 0 0 0-3-3.85"/>',
    "sparkle": '<path d="M9.9 15.5A2 2 0 0 0 8.5 14.1L2.4 12.5a.5.5 0 0 1 0-1l6.1-1.6A2 2 0 0 0 9.9 8.5l1.6-6.1a.5.5 0 0 1 1 0l1.6 6.1a2 2 0 0 0 1.4 1.4l6.1 1.6a.5.5 0 0 1 0 1l-6.1 1.6a2 2 0 0 0-1.4 1.4l-1.6 6.1a.5.5 0 0 1-1 0z"/>',
    "star": '<path d="M12 2.5l2.9 5.9 6.6 1-4.8 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5-4.8-4.6 6.6-1z"/>',
}
SPARKLE = "M0 -38 C 4 -12 12 -4 38 0 C 12 4 4 12 0 38 C -4 12 -12 4 -38 0 C -12 -4 -4 -12 0 -38 Z"

def icon(name, cx, cy, size, color="#fff", width=2):
    s = size / 24
    return (f'<g transform="translate({cx - size/2:.1f} {cy - size/2:.1f}) scale({s:.3f})" '
            f'stroke="{color}" stroke-width="{width / s * s:.2f}" fill="none">{ICON[name]}</g>')

def disc(cx, cy, r, fill, name, glow=None, isize=None):
    g = f' filter="url(#{glow})"' if glow else ""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{g}/>'
            + icon(name, cx, cy, isize or r * 1.0))

DEFS = """<defs>
  <radialGradient id="glowO" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#E0703C" stop-opacity="{go}"/><stop offset="60%" stop-color="#E0703C" stop-opacity="{go2}"/><stop offset="100%" stop-color="#E0703C" stop-opacity="0"/></radialGradient>
  <radialGradient id="glowB" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#2C7CB0" stop-opacity="{gb}"/><stop offset="100%" stop-color="#2C7CB0" stop-opacity="0"/></radialGradient>
  <filter id="halo" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur in="SourceGraphic" stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur in="SourceGraphic" stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="lift" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#0b1a26" flood-opacity="{lift}"/></filter>
  <filter id="rim" x="-25%" y="-70%" width="150%" height="240%"><feMorphology in="SourceAlpha" operator="dilate" radius="4" result="w"/><feGaussianBlur in="w" stdDeviation="9" result="s"/><feFlood flood-color="#7FB4DD" flood-opacity="{rim}"/><feComposite in2="s" operator="in" result="h"/><feMerge><feMergeNode in="h"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>"""

def page(theme, svg_body, extra_css=""):
    bg, dot = theme
    dark = theme is DARK
    defs = DEFS.format(go=".55" if dark else ".32", go2=".13" if dark else ".08", gb=".5" if dark else ".25",
                       lift=".45" if dark else ".22", rim=".45" if dark else "0")
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="robots" content="noindex">
<style>
  html,body{{margin:0;width:1200px;height:675px;overflow:hidden;}}
  body{{background:{bg};position:relative;font-family:"Helvetica Neue",Arial,sans-serif;}}
  .dots{{position:absolute;inset:0;background-image:radial-gradient({dot} 1.2px, transparent 1.3px);background-size:28px 28px;}}
  svg{{position:absolute;inset:0;}}{extra_css}
</style></head>
<body><div class="dots"></div>
<svg width="1200" height="675" viewBox="0 0 1200 675" fill="none" stroke-linecap="round" stroke-linejoin="round">
{defs}
{svg_body}
</svg>
</body></html>
"""

NAVY, NAVY2, EDGE, BLUE, ORANGE, BAR = "#2a4a61", "#24435a", "#4c6a80", "#2C7CB0", "#E0703C", "#9fb6c6"

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
