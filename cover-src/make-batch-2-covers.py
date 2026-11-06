"""Batch 2 of redrawn blog covers (Nov 2025 to Sep 2026 posts). Writes cover-src/<slug>.html.

Themes alternate by publish date across all drawn covers (see the site CLAUDE.md).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cover_kit import *

ICON.update({
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "send": '<path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4z"/>',
    "inbox": '<path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/>',
    "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
    "scales": '<path d="M12 3v18M7 21h10M4 7h16M12 3l-1 4h2z"/><path d="M7 7 4 14a3 3 0 0 0 6 0z"/><path d="M17 7l-3 7a3 3 0 0 0 6 0z"/>',
    "flame": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.29 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
    "ban": '<circle cx="12" cy="12" r="10"/><path d="m4.9 4.9 14.2 14.2"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "heartcrack": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7z"/><path d="m12 13-1-1 2-2-3-3 2-2"/>',
    "tag": '<path d="M12.6 2.6A2 2 0 0 0 11.2 2H4a2 2 0 0 0-2 2v7.2a2 2 0 0 0 .6 1.4l8.7 8.7a2.4 2.4 0 0 0 3.4 0l6.6-6.6a2.4 2.4 0 0 0 0-3.4z"/><circle cx="7.5" cy="7.5" r="1.2"/>',
    "filter": '<path d="M22 3H2l8 9.46V19l4 2v-8.54z"/>',
    "folder": '<path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/>',
    "archive": '<rect x="2" y="3" width="20" height="5" rx="1"/><path d="M4 8v11a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8M10 12h4"/>',
    "reply": '<path d="M9 17 4 12l5-5"/><path d="M20 18v-2a4 4 0 0 0-4-4H4"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "bank": '<path d="M3 21h18M3 10h18M5 6l7-3 7 3M4 10v11M20 10v11M8 14v3M12 14v3M16 14v3"/>',
    "undo": '<path d="M3 7v6h6"/><path d="M21 17a9 9 0 0 0-9-9 9 9 0 0 0-6 2.3L3 13"/>',
    "wifi": '<path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/>',
    "cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9z"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
    "code": '<path d="M8 7 3 12l5 5M16 7l5 5-5 5"/>',
    "news": '<path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/><path d="M18 14h-8M15 18h-5M10 6h8v4h-8z"/>',
    "bot": '<rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4M8 16h.01M16 16h.01"/>',
    "flow": '<rect x="3" y="3" width="6" height="6" rx="1"/><rect x="15" y="15" width="6" height="6" rx="1"/><path d="M6 9v3a3 3 0 0 0 3 3h6"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1"/>',
    "headset": '<path d="M3 14v-3a9 9 0 0 1 18 0v3"/><path d="M21 16a2 2 0 0 1-2 2h-1v-6h1a2 2 0 0 1 2 2zM3 16a2 2 0 0 0 2 2h1v-6H5a2 2 0 0 0-2 2z"/><path d="M18 18a4 4 0 0 1-4 3h-2"/>',
    "pin2": '<path d="M12 17v5M9 10.76V6h6v4.76l2 3.24H7z"/><path d="M8 2h8"/>',
})

def line(d, light=False, dash=True, op=None):
    c = "#5f7a8f" if light else BAR
    o = op or (".6" if light else ".5")
    da = ' stroke-dasharray="3 9"' if dash else ""
    return f'<path d="{d}" stroke="{c}" stroke-opacity="{o}" stroke-width="2.5"{da}/>'

def card(x, y, w, h, light, rx=18, fill=None):
    f = fill or (NAVY2 if light else NAVY)
    if light:
        return f'<g filter="url(#lift)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}"/></g>'
    return f'<g filter="url(#rim)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}" stroke="{EDGE}" stroke-width="1.5"/></g>'

def bars(x, y, widths, gap=24, op=(".8", ".45")):
    out = []
    for i, w in enumerate(widths):
        out.append(f'<rect x="{x}" y="{y + i * gap}" width="{w}" height="{11 if i == 0 else 9}" rx="5" fill="{BAR}" fill-opacity="{op[0] if i == 0 else op[1]}"/>')
    return "".join(out)

def glow_orange(cx, cy, r):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#glowO)"/>'

def hero(cx, cy, r, name, isize=None, ring=True):
    s = [glow_orange(cx, cy, r * 2.2)]
    if ring:
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 20}" stroke="{ORANGE}" stroke-opacity=".4" stroke-width="2"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ORANGE}" filter="url(#soft)"/>')
    s.append(icon(name, cx, cy, isize or r * 1.05, width=1.9))
    return "".join(s)

# ---------------------------------------------------------------- covers
def newsletter():          # Nov 17, 2025 (LIGHT)
    L = True; b = []
    b.append(line("M330 150 C 420 90 470 140 470 200", L)); b.append(line("M330 526 C 420 586 470 536 470 476", L))
    b.append(line("M870 150 C 780 90 730 140 730 200", L)); b.append(line("M870 526 C 780 586 730 536 730 476", L))
    b.append(glow_orange(600, 338, 320))
    b.append(card(440, 112, 320, 452, L, rx=22))
    b.append(f'<path d="M440 134a22 22 0 0 1 22-22h276a22 22 0 0 1 22 22v58H440z" fill="{ORANGE}"/>')
    b.append(icon("mail", 600, 152, 40, width=1.9))
    b.append(bars(478, 226, [220, 244, 200, 230], gap=26))
    b.append(f'<path d="M482 440 L530 412 L578 426 L626 384 L674 398 L722 356" stroke="{BLUE}" stroke-width="6" filter="url(#soft)"/>')
    b.append(f'<path d="M478 470H722" stroke="#fff" stroke-opacity=".12" stroke-width="2"/>')
    b.append(bars(478, 498, [170, 120], gap=24))
    for cx, cy, n in ((270, 150, "users"), (270, 526, "inbox"), (930, 526, "bell")):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="64" stroke="{BLUE}" stroke-opacity=".3" stroke-width="2"/>')
        b.append(disc(cx, cy, 52, BLUE, n, isize=46))
    b.append(hero(930, 150, 58, "send", isize=56))
    return page(LIGHT, "\n".join(b))

def owner_leads():         # Dec 5, 2025 (DARK)
    L = False; b = []
    b.append('<circle cx="600" cy="360" r="330" fill="url(#glowB)" opacity=".5"/>')
    b.append(card(190, 120, 820, 440, L, rx=24))
    vals = [17, 23, 26, 15, 14, 6, 5, 2, 1]
    x0, base, bw, gap = 250, 500, 62, 20
    for i, v in enumerate(vals):
        h = v * 12.5
        col = ORANGE if i < 3 else BLUE
        b.append(f'<rect x="{x0 + i * (bw + gap)}" y="{base - h:.0f}" width="{bw}" height="{h:.0f}" rx="10" fill="{col}" filter="url(#soft)"/>')
    b.append(f'<path d="M230 {base + 14}H970" stroke="#fff" stroke-opacity=".18" stroke-width="2"/>')
    b.append(hero(1010, 120, 54, "clock", isize=50, ring=False))
    b.append(disc(190, 120, 48, BLUE, "users", isize=44))
    return page(DARK, "\n".join(b))

def role_design():         # Dec 16, 2025 (LIGHT)
    L = True; b = []
    b.append(glow_orange(600, 170, 220))
    roles = [("key", 210), ("wrench", 470), ("dollar", 730), ("users", 990)]
    for i, (n, cx) in enumerate(roles):
        hot = i == 1
        b.append(f'<path d="M600 250 V320 H{cx} V392" stroke="{ORANGE if hot else "#5f7a8f"}" stroke-opacity="{".9" if hot else ".55"}" stroke-width="{4 if hot else 2.5}"{"" if hot else " stroke-dasharray=\"3 9\""}/>')
    b.append(card(470, 92, 260, 158, L, rx=22))
    b.append(disc(540, 171, 40, ORANGE, "user", glow="soft", isize=40))
    b.append(bars(600, 150, [96, 70], gap=26))
    for i, (n, cx) in enumerate(roles):
        b.append(card(cx - 110, 392, 220, 170, L, rx=20))
        b.append(disc(cx, 450, 36, ORANGE if i == 1 else BLUE, n, glow="soft" if i == 1 else None, isize=36))
        b.append(f'<rect x="{cx - 70}" y="508" width="140" height="10" rx="5" fill="{BAR}" fill-opacity=".8"/>')
        b.append(f'<rect x="{cx - 46}" y="530" width="92" height="8" rx="4" fill="{BAR}" fill-opacity=".45"/>')
    return page(LIGHT, "\n".join(b))

def tapeworm():            # Feb 11, 2026 (DARK)
    L = False; b = []
    # the margin: a big coin with bites taken out of it
    b.append(glow_orange(820, 330, 320))
    b.append('<defs><mask id="bite"><rect width="1200" height="675" fill="#fff"/>'
             '<circle cx="642" cy="268" r="58" fill="#000"/><circle cx="636" cy="360" r="54" fill="#000"/><circle cx="664" cy="446" r="46" fill="#000"/></mask></defs>')
    b.append(f'<g mask="url(#bite)"><circle cx="820" cy="330" r="200" fill="{ORANGE}"/><circle cx="820" cy="330" r="160" stroke="#fff" stroke-opacity=".35" stroke-width="4"/></g>')
    b.append(icon("dollar", 838, 330, 170, width=1.6))
    # a chain of software tiles snaking in to feed on it
    pts = [(110, 520, "cloud"), (222, 430, "card"), (330, 360, "phone"), (440, 400, "chart"), (548, 340, "mail")]
    d = "M" + " L".join(f"{x} {y}" for x, y, _ in pts)
    b.append(f'<path d="{d}" stroke="{BAR}" stroke-opacity=".4" stroke-width="3" stroke-dasharray="3 9"/>')
    for x, y, n in pts:
        hot = n in ("card", "chart")
        b.append(f'<rect x="{x - 46}" y="{y - 46}" width="92" height="92" rx="20" fill="{BLUE if hot else NAVY}" stroke="{EDGE}" stroke-width="1.5" filter="url(#rim)"/>')
        b.append(icon(n, x, y, 44, width=2))
    return page(DARK, "\n".join(b))

def agent_steps():         # Feb 16, 2026 (LIGHT)
    L = True; b = []
    b.append(line("M290 338 H470", L, dash=False, op=".7")); b.append(line("M650 338 H800", L, dash=False, op=".7"))
    b.append(f'<path d="M462 330l12 8-12 8M790 330l12 8-12 8" stroke="#5f7a8f" stroke-opacity=".7" stroke-width="2.5"/>')
    b.append(f'<circle cx="210" cy="338" r="80" fill="{NAVY2}" filter="url(#lift)"/>')
    b.append(icon("gear", 210, 338, 76, width=1.9))
    b.append(f'<circle cx="560" cy="338" r="98" fill="{BLUE}" filter="url(#lift)"/>')
    b.append(icon("flow", 560, 338, 92, width=1.9))
    b.append(hero(960, 338, 128, "bot", isize=128))
    b.append(f'<path d="{SPARKLE}" transform="translate(1060 214) scale(.6)" fill="{ORANGE}"/>')
    return page(LIGHT, "\n".join(b))

def company_structure():   # Mar 5, 2026 (DARK)
    L = False; b = []
    b.append('<circle cx="600" cy="338" r="330" fill="url(#glowB)" opacity=".5"/>')
    tiles = [(330, 96, "building"), (612, 96, "house"), (330, 352, "users"), (612, 352, "gear")]
    for x, y, n in tiles:
        b.append(card(x, y, 258, 228, L, rx=24))
        b.append(disc(x + 129, y + 100, 52, BLUE, n, isize=50))
        b.append(f'<rect x="{x + 69}" y="{y + 176}" width="120" height="10" rx="5" fill="{BAR}" fill-opacity=".7"/>')
    b.append(hero(600, 338, 58, "headset", isize=56))
    return page(DARK, "\n".join(b))

def ftc_letters():         # Mar 23, 2026 (LIGHT)
    L = True; b = []
    b.append(glow_orange(600, 330, 300))
    # 13 software tiles in an arc above and around the letter
    import math
    for i in range(13):
        a = math.radians(200 + i * (140 / 12))
        x, y = 600 + 440 * math.cos(a), 420 + 330 * math.sin(a)
        b.append(f'<rect x="{x - 30:.0f}" y="{y - 30:.0f}" width="60" height="60" rx="14" fill="{BLUE if i % 3 else NAVY2}" filter="url(#lift)"/>')
        b.append(icon("code", x, y, 28, width=2.2))
    b.append(card(420, 250, 360, 250, L, rx=22))
    b.append(f'<path d="M420 272 L600 392 L780 272" stroke="#fff" stroke-opacity=".5" stroke-width="4"/>')
    b.append(f'<circle cx="760" cy="262" r="60" fill="{ORANGE}" filter="url(#soft)"/>')
    b.append(icon("alert", 760, 262, 62, width=2.6))
    return page(LIGHT, "\n".join(b))

def rpu():                 # Mar 31, 2026 (DARK)
    L = False; b = []
    vals = [1.5, 20, 14, 38, 21, 7]
    x0, base, bw, gap = 250, 560, 92, 34
    b.append('<circle cx="560" cy="420" r="340" fill="url(#glowB)" opacity=".5"/>')
    for i, v in enumerate(vals):
        h = v * 9.5
        col = ORANGE if i == 3 else BLUE
        b.append(f'<rect x="{x0 + i * (bw + gap)}" y="{base - h:.0f}" width="{bw}" height="{h:.0f}" rx="12" fill="{col}" filter="url(#soft)"/>')
    b.append(f'<path d="M220 {base + 16}H1000" stroke="#fff" stroke-opacity=".2" stroke-width="2"/>')
    b.append(hero(668, 120, 62, "dollar", isize=58))
    b.append(disc(758, 64, 36, BLUE, "house", isize=34))
    return page(DARK, "\n".join(b))

def esa():                 # Apr 8, 2026 (LIGHT)
    L = True; b = []
    b.append(line("M330 338 H470", L, dash=True)); b.append(line("M730 338 H870", L, dash=True))
    b.append(f'<circle cx="600" cy="338" r="150" fill="{NAVY2}" filter="url(#lift)"/>')
    b.append(f'<circle cx="600" cy="338" r="172" stroke="{NAVY2}" stroke-opacity=".25" stroke-width="2"/>')
    b.append(icon("scales", 600, 330, 170, width=1.5))
    b.append(f'<circle cx="250" cy="338" r="92" fill="{BLUE}" filter="url(#lift)"/>')
    b.append(icon("house", 250, 338, 88, width=1.9))
    b.append(glow_orange(950, 338, 200))
    b.append(f'<circle cx="950" cy="338" r="92" fill="{ORANGE}" filter="url(#soft)"/>')
    # paw print
    b.append('<g fill="#fff"><ellipse cx="950" cy="362" rx="30" ry="25"/><ellipse cx="914" cy="322" rx="12" ry="15"/><ellipse cx="938" cy="302" rx="12" ry="16"/><ellipse cx="964" cy="302" rx="12" ry="16"/><ellipse cx="988" cy="322" rx="12" ry="15"/></g>')
    return page(LIGHT, "\n".join(b))

def accounting():          # Apr 17, 2026 (DARK)
    L = False; b = []
    b.append('<circle cx="560" cy="340" r="320" fill="url(#glowB)" opacity=".5"/>')
    b.append(card(400, 90, 340, 496, L, rx=30))
    b.append(f'<rect x="436" y="126" width="268" height="96" rx="14" fill="#1b3446"/>')
    b.append(f'<rect x="560" y="164" width="120" height="22" rx="8" fill="{BAR}" fill-opacity=".8"/>')
    for r_ in range(4):
        for c in range(4):
            x, y = 436 + c * 70, 252 + r_ * 80
            col = ORANGE if (r_, c) == (3, 3) else (BLUE if c == 3 else "#3b5a70")
            b.append(f'<rect x="{x}" y="{y}" width="58" height="62" rx="12" fill="{col}"/>')
    b.append(hero(760, 110, 64, "flame", isize=60))
    b.append(line("M740 420 C 820 420 840 470 900 470"))
    b.append(f'<rect x="896" y="410" width="200" height="120" rx="18" fill="{NAVY}" stroke="{EDGE}" stroke-width="1.5" filter="url(#rim)"/>')
    for i in range(3):
        y = 438 + i * 30
        b.append(f'<rect x="922" y="{y}" width="{[110, 90, 120][i]}" height="9" rx="4.5" fill="{BAR}" fill-opacity=".55"/>')
        b.append(disc(1066, y + 4, 11, ORANGE if i == 1 else BLUE, "x" if i == 1 else "check", isize=12))
    return page(DARK, "\n".join(b))

def google_reviews():      # May 5, 2026 (LIGHT)
    L = True; b = []
    b.append(card(300, 90, 600, 150, L, rx=26))
    for i in range(5):
        cx = 380 + i * 110
        b.append(f'<g transform="translate({cx - 34} 131) scale(2.85)"><path d="{ICON["star"][9:-3]}" fill="{ORANGE if i < 4 else "none"}" stroke="{ORANGE}" stroke-width="1.6"/></g>')
    for i, (x, y) in enumerate(((180, 300), (470, 300), (760, 300))):
        hot = i == 1
        b.append(card(x, y, 260, 250, L, rx=22))
        b.append(disc(x + 56, y + 58, 30, BLUE, "user", isize=30))
        b.append(bars(x + 100, y + 48, [120, 90], gap=24))
        b.append(bars(x + 36, y + 120, [188, 160, 176], gap=30, op=(".45", ".45")))
        if hot:
            b.append(glow_orange(x + 130, y + 125, 170))
            b.append(f'<circle cx="{x + 130}" cy="{y + 125}" r="70" fill="{ORANGE}" filter="url(#soft)"/>')
            b.append(icon("ban", x + 130, y + 125, 86, width=2.2))
    return page(LIGHT, "\n".join(b))

def zillow_squeeze():      # May 11, 2026 (DARK)
    L = False; b = []
    b.append('<circle cx="600" cy="338" r="330" fill="url(#glowB)" opacity=".5"/>')
    b.append(card(400, 110, 400, 460, L, rx=24))
    b.append(f'<rect x="424" y="134" width="352" height="200" rx="14" fill="#1b3446"/>')
    b.append(icon("house", 600, 234, 120, color="#9fb6c6", width=1.4))
    b.append(bars(432, 364, [260, 200, 230], gap=28))
    b.append(f'<rect x="432" y="470" width="150" height="54" rx="27" fill="{BLUE}"/>')
    b.append(f'<rect x="600" y="470" width="168" height="54" rx="27" fill="#3b5a70"/>')
    b.append(icon("phone", 507, 497, 26, width=2.2)); b.append(icon("mail", 684, 497, 26, width=2.2))
    # phone number taken away, features behind a paywall
    b.append(line("M400 300 C 330 300 300 230 250 230"))
    b.append(disc(220, 230, 54, BLUE, "phone", isize=48))
    b.append(f'<path d="M180 270 L260 190" stroke="{ORANGE}" stroke-width="7"/>')
    b.append(line("M800 420 C 870 420 900 470 950 470"))
    b.append(hero(980, 470, 60, "lock", isize=56))
    b.append(disc(1050, 400, 26, BLUE, "dollar", isize=26))
    return page(DARK, "\n".join(b))

def ai_news():             # Jun 22, 2026 (LIGHT)
    L = True; b = []
    b.append(card(340, 92, 520, 490, L, rx=26))
    b.append(icon("news", 420, 160, 60, width=1.8))
    b.append(bars(476, 140, [300, 220], gap=30))
    b.append(f'<rect x="380" y="226" width="440" height="140" rx="14" fill="#1b3446"/>')
    b.append(f'<path d="{SPARKLE}" transform="translate(600 296) scale(1.2)" fill="{BLUE}"/>')
    for i in range(2):
        y = 410 + i * 76
        b.append(glow_orange(410, y + 12, 70))
        b.append(f'<circle cx="410" cy="{y + 12}" r="26" fill="{ORANGE}" filter="url(#soft)"/>')
        b.append(f'<text x="410" y="{y + 22}" text-anchor="middle" fill="#fff" font-size="28" font-weight="800">{i + 1}</text>')
        b.append(bars(456, y + 2, [[300, 220][i], [220, 260][i]], gap=22))
    b.append(disc(880, 120, 52, BLUE, "search", isize=48))
    b.append(disc(320, 560, 44, BLUE, "check", isize=42))
    return page(LIGHT, "\n".join(b))

def iphone():              # Jun 29, 2026 (DARK)
    L = False; b = []
    b.append(glow_orange(600, 338, 300))
    b.append(f'<g filter="url(#rim)"><rect x="470" y="70" width="260" height="535" rx="42" fill="{NAVY}" stroke="{EDGE}" stroke-width="2"/></g>')
    b.append(f'<rect x="490" y="92" width="220" height="490" rx="30" fill="#1b3446"/>')
    b.append(f'<rect x="562" y="104" width="76" height="20" rx="10" fill="{NAVY}"/>')
    b.append(f'<circle cx="600" cy="338" r="84" fill="{ORANGE}" filter="url(#soft)"/>')
    b.append(icon("heartcrack", 600, 340, 92, width=1.9))
    # notifications drifting away
    for x, y, n, o in ((250, 170, "bell", 1), (930, 140, "mail", 1), (180, 430, "chart", .7), (980, 420, "users", .8), (330, 560, "phone", .55), (870, 580, "bell", .5)):
        b.append(f'<g opacity="{o}"><rect x="{x - 62}" y="{y - 30}" width="124" height="60" rx="18" fill="{NAVY}" stroke="{EDGE}" stroke-width="1.5"/>')
        b.append(disc(x - 30, y, 18, BLUE, n, isize=20))
        b.append(f'<rect x="{x - 4}" y="{y - 8}" width="52" height="8" rx="4" fill="{BAR}" fill-opacity=".7"/><rect x="{x - 4}" y="{y + 6}" width="36" height="7" rx="3.5" fill="{BAR}" fill-opacity=".4"/></g>')
    return page(DARK, "\n".join(b))

def email_systems():       # Jul 20, 2026 (LIGHT)
    L = True; b = []
    names = ["mail", "tag", "filter", "clock", "users", "check", "reply", "inbox", "folder", "bell", "archive", "send", "pin2", "calendar", "star"]
    b.append(glow_orange(600, 338, 260))
    for i, n in enumerate(names):
        r_, c = divmod(i, 5)
        x, y = 268 + c * 146, 132 + r_ * 146
        hot = n == "inbox"
        if hot:
            b.append(f'<rect x="{x - 8}" y="{y - 8}" width="136" height="136" rx="30" fill="{ORANGE}" filter="url(#soft)"/>')
            b.append(icon(n, x + 60, y + 60, 64, width=2))
        else:
            b.append(f'<rect x="{x}" y="{y}" width="120" height="120" rx="26" fill="{BLUE if (r_ + c) % 2 else NAVY2}" filter="url(#lift)"/>')
            b.append(icon(n, x + 60, y + 60, 50, width=2))
    return page(LIGHT, "\n".join(b))

def ach():                 # Aug 7, 2026 (DARK)
    L = False; b = []
    b.append('<circle cx="560" cy="338" r="330" fill="url(#glowB)" opacity=".45"/>')
    b.append(f'<circle cx="190" cy="338" r="96" fill="{BLUE}"/>')
    b.append(f'<circle cx="190" cy="338" r="116" stroke="{BLUE}" stroke-opacity=".35" stroke-width="2"/>')
    b.append(icon("bank", 190, 336, 96, width=1.9))
    rows = [(170, 150, BLUE), (260, 270, BLUE), (450, 390, BLUE), (640, 510, ORANGE)]
    for i, (w, y, col) in enumerate(rows):
        b.append(line(f"M290 338 C 330 338 330 {y} 360 {y}", op=".35"))
        b.append(f'<rect x="360" y="{y - 20}" width="{w}" height="40" rx="20" fill="{col}" filter="url(#soft)"/>')
        b.append(disc(360 + w + 40, y, 26, NAVY, "undo", isize=28))
        b.append(f'<circle cx="{360 + w + 40}" cy="{y}" r="26" stroke="{EDGE}" stroke-width="1.5"/>')
    b.append(disc(1080, 110, 40, NAVY, "clock", isize=40))
    return page(DARK, "\n".join(b))

def process_design():      # Aug 12, 2026 (LIGHT)
    L = True; b = []
    import random
    rnd = random.Random(7)
    pts = [(rnd.uniform(110, 520), rnd.uniform(130, 545)) for _ in range(26)]
    d = f"M{pts[0][0]:.0f} {pts[0][1]:.0f}"
    for (x1, y1), (x2, y2) in zip(pts[1::2], pts[2::2]):
        d += f" S {x1:.0f} {y1:.0f} {x2:.0f} {y2:.0f}"
    d += " C 560 300 590 330 630 338"
    b.append(f'<path d="{d}" stroke="#5f7a8f" stroke-opacity=".75" stroke-width="3"/>')
    b.append(glow_orange(860, 338, 260))
    b.append(card(640, 110, 420, 456, L, rx=26))
    for i in range(4):
        y = 170 + i * 98
        b.append(f'<rect x="684" y="{y}" width="56" height="56" rx="14" fill="{ORANGE}" filter="url(#soft)"/>')
        b.append(icon("check", 712, y + 28, 34, width=2.6))
        b.append(f'<rect x="768" y="{y + 14}" width="{[220, 180, 240, 160][i]}" height="11" rx="5.5" fill="{BAR}" fill-opacity=".85"/>')
        b.append(f'<rect x="768" y="{y + 36}" width="{[150, 190, 120, 170][i]}" height="8" rx="4" fill="{BAR}" fill-opacity=".45"/>')
    return page(LIGHT, "\n".join(b))

def group_rate():          # Sep 29, 2026 (LIGHT)
    L = True; b = []
    b.append(glow_orange(600, 200, 260))
    for i, (r_, op) in enumerate(((70, 1), (130, .8), (190, .6))):
        b.append(f'<path d="M{600 - r_ * .8:.0f} {214 - r_ * .35:.0f} A {r_} {r_} 0 0 1 {600 + r_ * .8:.0f} {214 - r_ * .35:.0f}" stroke="{ORANGE}" stroke-opacity="{op}" stroke-width="16" filter="url(#soft)"/>')
    b.append(f'<circle cx="600" cy="226" r="16" fill="{ORANGE}" filter="url(#soft)"/>')
    b.append(card(430, 272, 340, 330, L, rx=18))
    for r_ in range(4):
        for c in range(4):
            x, y = 466 + c * 72, 304 + r_ * 66
            if r_ == 3 and c in (1, 2):
                continue
            b.append(f'<rect x="{x}" y="{y}" width="52" height="42" rx="8" fill="{BLUE if (r_ * 4 + c) % 3 == 0 else "#ffffff"}" fill-opacity="{1 if (r_ * 4 + c) % 3 == 0 else .14}"/>')
    b.append(f'<rect x="548" y="502" width="104" height="100" rx="10" fill="#1b3446"/>')
    b.append(line("M430 470 C 360 470 330 420 290 420", L)); b.append(line("M770 470 C 840 470 870 420 910 420", L))
    b.append(disc(240, 420, 54, BLUE, "dollar", isize=48))
    b.append(disc(960, 420, 54, BLUE, "users", isize=50))
    return page(LIGHT, "\n".join(b))

PAGES = {
    "why-i-started-my-property-management-newsletter": newsletter,
    "owner-leads-property-management-sales-data": owner_leads,
    "role-design-property-management": role_design,
    "tapeworm-vendors-property-management": tapeworm,
    "openclaw-ai-agent-property-management": agent_steps,
    "property-management-company-structure": company_structure,
    "ftc-warning-letter-13-pm-software-companies": ftc_letters,
    "revenue-per-unit-property-management": rpu,
    "federal-esa-lawsuit-property-managers": esa,
    "mad-about-pm-accounting-software": accounting,
    "google-review-policy-update-property-management": google_reviews,
    "zillow-removes-phone-numbers-rental-listings": zillow_squeeze,
    "ai-news-rule-property-management-vendors": ai_news,
    "im-breaking-up-with-my-iphone-and-you-should-too": iphone,
    "email-systems-that-scale-property-management": email_systems,
    "ach-rules-every-property-manager-should-understand": ach,
    "how-to-design-a-process-people-actually-want-to-use": process_design,
    "group-rate-internet-property-management": group_rate,
}

if __name__ == "__main__":
    only = sys.argv[1:]
    for slug, fn in PAGES.items():
        if only and slug not in only:
            continue
        with open(os.path.join(OUT, f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(fn())
        print("wrote", slug)
