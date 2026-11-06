"""Shared pieces for drawn blog covers: light/dark backgrounds, glow filters, brand colors, icons."""
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

