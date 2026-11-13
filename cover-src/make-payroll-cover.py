"""Nov 13, 2026 cover: payroll tips for property management business owners (LIGHT).
A navy paycheck in the middle with a glowing orange dollar, ringed by the topics the post
covers: pay schedule, payroll taxes, mileage, bonuses, PTO, and maintenance techs.
Writes cover-src/<slug>.html."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cover_kit import *

SLUG = "payroll-tips-property-management-business-owners"
LINE = "#7d97ab"   # connector lines on a light ground (see CLAUDE.md)

ICON.update({
    "calendar": '<rect x="3" y="4.5" width="18" height="17" rx="2"/><path d="M16 2.5v4M8 2.5v4M3 10h18"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "car": '<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>',
    "gift": '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5C10 3 12 8 12 8s2-5 4.5-5a2.5 2.5 0 0 1 0 5"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
})

def paycheck(cx, cy, w=500, h=240):
    x0, y0 = cx - w / 2, cy - h / 2
    p = [f'<g filter="url(#lift)"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="20" fill="{NAVY}" stroke="{EDGE}" stroke-width="1.5"/></g>',
         # payer block, top left
         f'<rect x="{x0 + 32}" y="{y0 + 34}" width="120" height="11" rx="5.5" fill="{BAR}" fill-opacity=".8"/>',
         f'<rect x="{x0 + 32}" y="{y0 + 56}" width="84" height="8" rx="4" fill="{BAR}" fill-opacity=".4"/>',
         # pay-to line
         f'<rect x="{x0 + 32}" y="{y0 + 112}" width="250" height="10" rx="5" fill="{BAR}" fill-opacity=".55"/>',
         f'<path d="M{x0 + 32} {y0 + 140} H{x0 + 300}" stroke="{BAR}" stroke-opacity=".35" stroke-width="2"/>',
         # signature, bottom right
         f'<path d="M{x0 + w - 200} {y0 + h - 52} c 14 -26 22 -26 26 -6 s 10 18 22 -4 s 14 -18 20 2 s 14 10 30 -8 s 18 -6 26 4" stroke="#fff" stroke-opacity=".85" stroke-width="3"/>',
         f'<path d="M{x0 + w - 214} {y0 + h - 36} H{x0 + w - 32}" stroke="{BAR}" stroke-opacity=".5" stroke-width="2"/>',
         ]
    # account-number dots, bottom left
    for i in range(9):
        p.append(f'<circle cx="{x0 + 38 + i * 15}" cy="{y0 + h - 40}" r="3.6" fill="{BAR}" fill-opacity=".45"/>')
    return "".join(p)

def cover():
    b = ['<circle cx="600" cy="338" r="360" fill="url(#glowB)" opacity=".55"/>']
    cx, cy = 600, 338
    ring = [("calendar", -150), ("shield", -90), ("car", -30), ("gift", 30), ("clock", 90), ("wrench", 150)]
    rx, ry = 420, 250
    pts = []
    for name, deg in ring:
        a = math.radians(deg)
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        pts.append((name, x, y))
        b.append(f'<path d="M{cx} {cy} L{x:.1f} {y:.1f}" stroke="{LINE}" stroke-width="2.5" stroke-dasharray="3 9"/>')
    b.append(f'<g transform="rotate(-4 {cx} {cy})">{paycheck(cx, cy)}</g>')
    # glowing orange dollar on the check
    dx, dy = 748, 282
    b.append(f'<circle cx="{dx}" cy="{dy}" r="130" fill="url(#glowO)"/>')
    b.append(disc(dx, dy, 48, ORANGE, "dollar", glow="soft", isize=46))
    for name, x, y in pts:
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="54" stroke="{BLUE}" stroke-opacity=".25" stroke-width="2"/>')
        b.append(disc(round(x, 1), round(y, 1), 42, NAVY2 if name in ("shield", "clock") else BLUE, name, isize=40))
    return page(LIGHT, "\n".join(b))

if __name__ == "__main__":
    with open(os.path.join(OUT, f"{SLUG}.html"), "w", encoding="utf-8") as f:
        f.write(cover())
    print("wrote", SLUG)
