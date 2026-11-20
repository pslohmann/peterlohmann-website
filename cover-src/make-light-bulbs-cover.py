"""Nov 20, 2026 cover: an electrical engineer's opinion on light bulbs (LIGHT).
A big navy A19 bulb with a warm glowing filament, sitting over a color-temperature strip
(warm 2700K to cool 5000K), with the post's other topics around it: bulb shapes, motion
sensor switches, Lever Nuts (wiring), and Caseta timers.
Writes cover-src/<slug>.html."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cover_kit import *

SLUG = "electrical-engineer-opinion-light-bulbs"
LINE = "#7d97ab"   # connector lines on a light ground (see CLAUDE.md)

ICON.update({
    "bulb": '<path d="M9 18h6M10 21.5h4"/><path d="M12 2.5a6.5 6.5 0 0 0-4 11.6c.7.6 1 1.4 1 2.3V17h6v-.6c0-.9.3-1.7 1-2.3A6.5 6.5 0 0 0 12 2.5z"/>',
    "switch": '<rect x="6" y="2.5" width="12" height="19" rx="2"/><rect x="9.5" y="6" width="5" height="12" rx="1.2"/><path d="M9.5 12h5"/>',
    "motion": '<circle cx="12" cy="13" r="2"/><path d="M8.5 9.5a5 5 0 0 1 7 0M6 7a8.5 8.5 0 0 1 12 0M9 19.5l3-4.5 3 4.5"/>',
    "wire": '<path d="M2 8h6M2 16h6"/><rect x="8" y="5" width="9" height="14" rx="2"/><path d="M11 5v-2M14 5v-2"/><path d="M17 12h5"/>',
})

def big_bulb(cx, cy):
    """An A19 bulb: glass globe, neck, and screw base, drawn as one navy piece."""
    r = 118
    gy = cy - 40                       # globe center
    neck_top, neck_bot = gy + 78, gy + 168
    p = [f'<g filter="url(#lift)">',
         f'<path d="M{cx - 92:.0f} {neck_top:.0f} A {r} {r} 0 1 1 {cx + 92:.0f} {neck_top:.0f} '
         f'C {cx + 70:.0f} {neck_top + 40:.0f} {cx + 52:.0f} {neck_bot - 30:.0f} {cx + 52:.0f} {neck_bot:.0f} '
         f'H {cx - 52:.0f} C {cx - 52:.0f} {neck_bot - 30:.0f} {cx - 70:.0f} {neck_top + 40:.0f} {cx - 92:.0f} {neck_top:.0f} Z" '
         f'fill="{NAVY}" stroke="{EDGE}" stroke-width="1.5"/>',
         f'<rect x="{cx - 56}" y="{neck_bot - 2}" width="112" height="64" rx="10" fill="{NAVY2}" stroke="{EDGE}" stroke-width="1.5"/>',
         f'<path d="M{cx - 40} {neck_bot + 92} L{cx + 40} {neck_bot + 92} L{cx + 22} {neck_bot + 108} H{cx - 22} Z" fill="{NAVY2}"/>',
         '</g>']
    for i in range(3):                 # screw threads
        y = neck_bot + 14 + i * 16
        p.append(f'<path d="M{cx - 50} {y} L{cx + 50} {y + 7}" stroke="{BAR}" stroke-opacity=".55" stroke-width="3"/>')
    p.append(f'<rect x="{cx - 46}" y="{neck_bot + 62}" width="92" height="30" rx="8" fill="{NAVY2}" stroke="{EDGE}" stroke-width="1.5"/>')
    # warm glow and filament inside the globe
    p.append(f'<circle cx="{cx}" cy="{gy + 6}" r="150" fill="url(#glowO)"/>')
    p.append(f'<path d="M{cx - 26} {neck_top + 36} V{gy + 22} M{cx + 26} {neck_top + 36} V{gy + 22}" stroke="{BAR}" stroke-opacity=".7" stroke-width="3"/>')
    p.append(f'<path d="M{cx - 26} {gy + 22} c 6 -26 12 -26 17 0 s 11 26 17 0 s 12 -26 17 0 s 11 26 18 0" '
             f'stroke="{ORANGE}" stroke-width="5" filter="url(#soft)"/>')
    p.append(f'<path d="M{cx - 64} {gy - 52} a 76 76 0 0 1 40 -40" stroke="#fff" stroke-opacity=".35" stroke-width="6"/>')
    return "".join(p)

def kelvin_strip(cx, y, w=640, h=22):
    x0 = cx - w / 2
    out = ['<defs><linearGradient id="kelvin" x1="0" x2="1" y1="0" y2="0">'
           '<stop offset="0%" stop-color="#F2A65A"/><stop offset="35%" stop-color="#FBD9A6"/>'
           '<stop offset="62%" stop-color="#FFF4E2"/><stop offset="100%" stop-color="#BFD9F2"/></linearGradient></defs>',
           f'<rect x="{x0}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" fill="url(#kelvin)" stroke="{EDGE}" stroke-opacity=".45" stroke-width="1.5"/>']
    for frac, fill in ((0.18, ORANGE), (0.40, BLUE), (0.86, NAVY)):   # 2700K, 3000K, 5000K
        x = x0 + w * frac
        out.append(f'<circle cx="{x:.0f}" cy="{y + h / 2}" r="15" fill="{fill}" stroke="#fff" stroke-width="4"/>')
    return "".join(out)

def cover():
    cx, cy = 600, 300
    b = ['<circle cx="600" cy="300" r="360" fill="url(#glowB)" opacity=".5"/>']
    ring = [("bulb", 196, 150), ("motion", 1004, 150), ("wire", 196, 410), ("clock", 1004, 410)]
    for name, x, y in ring:
        b.append(f'<path d="M{cx} {cy - 40} L{x} {y}" stroke="{LINE}" stroke-width="2.5" stroke-dasharray="3 9"/>')
    b.append(big_bulb(cx, cy))
    b.append(kelvin_strip(cx, 560))
    for name, x, y in ring:
        b.append(f'<circle cx="{x}" cy="{y}" r="58" stroke="{BLUE}" stroke-opacity=".25" stroke-width="2"/>')
        b.append(disc(x, y, 46, NAVY2 if name in ("wire", "motion") else BLUE, name, isize=44))
    return page(LIGHT, "\n".join(b))

if __name__ == "__main__":
    with open(os.path.join(OUT, f"{SLUG}.html"), "w", encoding="utf-8") as f:
        f.write(cover())
    print("wrote", SLUG)
