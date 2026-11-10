"""Nov 10, 2026 cover: 2026 property management industry reports (DARK).
A fan of eight report cards, each with its topic icon, and a glowing orange magnifier
with a check mark: the eight worth reading. Writes cover-src/<slug>.html."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cover_kit import *

SLUG = "2026-property-management-industry-reports"

def report_card(icon_name, w=172, h=228):
    """One report, drawn centered on (0,0): folded corner, topic icon, text lines, small bar chart."""
    x0, y0 = -w / 2, -h / 2
    fold = 26
    shape = (f"M{x0 + 14} {y0} H{x0 + w - fold} L{x0 + w} {y0 + fold} V{y0 + h - 14} "
             f"Q{x0 + w} {y0 + h} {x0 + w - 14} {y0 + h} H{x0 + 14} Q{x0} {y0 + h} {x0} {y0 + h - 14} "
             f"V{y0 + 14} Q{x0} {y0} {x0 + 14} {y0} Z")
    p = [f'<g filter="url(#rim)"><path d="{shape}" fill="{NAVY}" stroke="{EDGE}" stroke-width="1.5"/></g>',
         f'<path d="M{x0 + w - fold} {y0} V{y0 + fold} H{x0 + w}" fill="{NAVY2}" stroke="{EDGE}" stroke-width="1.5"/>',
         disc(x0 + 42, y0 + 44, 26, BLUE, icon_name, isize=28)]
    for i, lw in enumerate((110, 82, 98)):
        p.append(f'<rect x="{x0 + 18}" y="{y0 + 92 + i * 20}" width="{lw}" height="7" rx="3.5" fill="{BAR}" fill-opacity="{.7 if i == 0 else .4}"/>')
    for i, bh in enumerate((26, 40, 32, 52)):
        p.append(f'<rect x="{x0 + 22 + i * 28}" y="{y0 + h - 18 - bh}" width="16" height="{bh}" rx="3" fill="{BAR}" fill-opacity=".55"/>')
    return "".join(p)

def cover():
    b = ['<circle cx="600" cy="330" r="360" fill="url(#glowB)" opacity=".5"/>']
    icons = ["chart", "sparkle", "users", "house", "key", "dollar", "clock", "alert"]
    pivot_x, pivot_y, radius = 600, 930, 630
    angles = [-35 + i * 10 for i in range(8)]
    cards = []
    for name, a in zip(icons, angles):
        r = math.radians(a)
        cx = pivot_x + radius * math.sin(r)
        cy = pivot_y - radius * math.cos(r)
        cards.append((a, f'<g transform="translate({cx:.1f} {cy:.1f}) rotate({a})">{report_card(name)}</g>'))
    # left to right, like a hand of cards, so every topic icon (top left) stays visible
    for _, svg in cards:
        b.append(svg)
    # magnifier: the eight worth reading
    lx, ly, lr = 690, 478, 78
    b.append(f'<circle cx="{lx}" cy="{ly}" r="190" fill="url(#glowO)"/>')
    b.append(f'<path d="M{lx + 54} {ly + 54} L{lx + 132} {ly + 132}" stroke="#fff" stroke-width="22" filter="url(#soft)"/>')
    b.append(f'<circle cx="{lx}" cy="{ly}" r="{lr}" fill="{ORANGE}" fill-opacity=".92" stroke="#fff" stroke-width="12" filter="url(#soft)"/>')
    b.append(icon("check", lx, ly, 78, "#fff", 3))
    return page(DARK, "\n".join(b))

if __name__ == "__main__":
    with open(os.path.join(OUT, f"{SLUG}.html"), "w", encoding="utf-8") as f:
        f.write(cover())
    print("wrote", SLUG)
