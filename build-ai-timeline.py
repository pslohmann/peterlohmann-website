#!/usr/bin/env python3
"""
Build step for the AI timeline (/blog/ai-property-management-timeline/). Run after editing blog/ai-property-management-timeline/data/*.json:

    python3 build-ai-timeline.py

What it does (plain English):
  1. Checks every event in data/events.json (required fields, allowed values, unique ids,
     known company slugs, no em/en dashes). Problems are printed and the build stops.
  2. Points each company in data/companies.json at the logo file that actually exists in
     assets/logos/ (.svg preferred, else .png). No file = "" (the page shows a letter tile).
  3. Writes one small share page per event at blog/ai-property-management-timeline/e/<id>/index.html, a copy of the
     main page with that event's title and summary in the link-preview tags. Renamed events
     listed in data/redirects.json get a page too, so old links keep working.
  4. Draws the 1200x630 link-preview image blog/ai-property-management-timeline/og-image.png from the same data.

It never deletes anything. If an old e/<id>/ folder no longer matches an event or redirect,
it prints a warning (ids are permanent: retire one with a redirect instead of deleting it).
"""
import json, os, re, sys, html, datetime
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
TL = os.path.join(HERE, "blog", "ai-property-management-timeline")
DATA = os.path.join(TL, "data")
SITE = "https://www.peterlohmann.com"
PAGE_URL = SITE + "/blog/ai-property-management-timeline/"
# PREVIEW MODE. True = every page carries <meta name="robots" content="noindex"> so Google and AI
# crawlers stay out while Peter reviews it (the page is also left out of the sitemap, llms.txt and the
# blog list). To go public: set False, rerun this script, then see "TO LAUNCH" in CLAUDE.md.
HIDDEN = False
PUBLISHED = "2026-10-27"
TITLE = "AI & Property Management: A Comprehensive Timeline"
DESCRIPTION = ("A running timeline of AI in residential property management since ChatGPT: the big AI model "
               "releases, the AI launches, APIs and MCP connectors from property management software, and "
               "what Peter Lohmann published along the way.")
OG_DESCRIPTION = "In the age of AI, things move so fast it's hard to keep up."

LANES = ["frontier", "pm_software", "leasing", "maintenance", "risk", "data_pricing", "plm"]
TYPES = {"frontier_model": "star", "api_access": "diamond", "mcp_connector": "diamond", "platform_launch": "dot",
         "product_release": "dot", "ai_agent": "dot", "acquisition": "dot", "funding": "dot",
         "access_cutoff": "dot", "report": "dot"}
# same lane colors as timeline.css (--lane-*)
LANE_RGB = {"frontier": (31, 58, 77), "pm_software": (44, 124, 176), "leasing": (36, 138, 92),
            "maintenance": (176, 125, 20), "risk": (192, 73, 47), "data_pricing": (127, 180, 221),
            "plm": (224, 112, 60)}
REQUIRED = ["id", "date", "display_date", "date_precision", "status", "company", "companies", "lane", "type",
            "title", "summary", "source_url", "source_label", "confidence", "notable"]


def load(name, default=None):
    p = os.path.join(DATA, name)
    if not os.path.exists(p) and default is not None:
        return default
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def sort_key(d):
    d = str(d)
    if re.fullmatch(r"\d{4}", d): return d + "-12-31"
    if re.fullmatch(r"\d{4}-\d{2}", d): return d + "-15"
    return d


# ---------- 1. check the data ----------
def validate(events, companies):
    slugs = {c["slug"] for c in companies}
    errors, seen = [], set()
    for n, e in enumerate(events, 1):
        where = f"event #{n} ({e.get('id', 'no id')})"
        for k in REQUIRED:
            if k not in e or e[k] in (None, "") and k not in ("notable",):
                errors.append(f"{where}: missing '{k}'")
        eid = e.get("id", "")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", eid):
            errors.append(f"{where}: id must be lowercase-with-hyphens")
        if eid in seen: errors.append(f"{where}: duplicate id")
        seen.add(eid)
        if not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(e.get("date", ""))):
            errors.append(f"{where}: date must be YYYY, YYYY-MM or YYYY-MM-DD")
        if e.get("lane") not in LANES: errors.append(f"{where}: unknown lane '{e.get('lane')}'")
        if e.get("type") not in TYPES: errors.append(f"{where}: unknown type '{e.get('type')}'")
        if e.get("status") not in ("released", "announced"): errors.append(f"{where}: status must be released or announced")
        if e.get("confidence") not in ("high", "med", "low"): errors.append(f"{where}: confidence must be high, med or low")
        if e.get("date_precision") not in ("day", "month", "approx"): errors.append(f"{where}: bad date_precision")
        cos = e.get("companies") or []
        if not 1 <= len(cos) <= 2: errors.append(f"{where}: companies needs 1 or 2 slugs")
        for s in cos:
            if s not in slugs: errors.append(f"{where}: company slug '{s}' is not in companies.json")
        for k, v in e.items():
            if isinstance(v, str) and ("—" in v or "–" in v):
                errors.append(f"{where}: '{k}' has an em or en dash (use a comma, parentheses or a hyphen)")
            if k in ("title", "summary") and isinstance(v, str) and re.search(r"(^|\s)#\w", v):
                errors.append(f"{where}: '{k}' looks like it has a hashtag")
    return errors


# ---------- 2. logo paths ----------
def sync_logos(companies):
    changed = False
    for c in companies:
        found = ""
        for ext in ("svg", "png"):
            rel = f"assets/logos/{c['slug']}.{ext}"
            if os.path.exists(os.path.join(TL, rel)):
                found = rel
                break
        if c.get("logo", "") != found:
            c["logo"] = found
            changed = True
    if changed:
        body = "[\n" + ",\n".join("  " + json.dumps(c, ensure_ascii=False) for c in companies) + "\n]\n"
        with open(os.path.join(DATA, "companies.json"), "w", encoding="utf-8") as f:
            f.write(body)
    missing = [c["slug"] for c in companies if not c["logo"]]
    return changed, missing


# ---------- 3. share pages ----------
META_RE = re.compile(r"<!-- SHARE-META START.*?<!-- SHARE-META END -->", re.S)


def seo_block(events, ev=None, url=None):
    """The <head> SEO tags. ev=None means the main page; otherwise one event's share page."""
    a = lambda x: html.escape(x, quote=True)
    # Event share pages point their canonical at the main post: they exist so a shared link shows the
    # right preview, and search engines fold them into (and credit links to) the one post. They are kept
    # out of the sitemap and nothing on the site links to them. noindex only while the whole thing is hidden.
    robots = '<meta name="robots" content="noindex, follow" />\n' if HIDDEN else ""
    modified = datetime.date.today().isoformat()
    if ev is None:
        url = PAGE_URL
        title, og_title, desc, og_desc = TITLE + " · Peter Lohmann", TITLE, DESCRIPTION, OG_DESCRIPTION
        ld = [{
            "@context": "https://schema.org", "@type": "BlogPosting",
            "headline": TITLE, "description": DESCRIPTION, "url": url, "mainEntityOfPage": url,
            "image": PAGE_URL + "og-image.png", "datePublished": PUBLISHED, "dateModified": modified,
            "author": {"@type": "Person", "name": "Peter Lohmann", "url": SITE + "/"},
            "publisher": {"@type": "Person", "name": "Peter Lohmann"},
            "about": ["Artificial intelligence", "Property management", "Property management software"],
            "keywords": "AI, property management, property management software, AI agents, MCP, API, ChatGPT, Claude, AppFolio, Rentvine, Buildium",
        }, {
            "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog"},
                {"@type": "ListItem", "position": 3, "name": TITLE, "item": url}]
        }]
        kind = "article"
    else:
        t = f"{ev['title']}, {ev['display_date']}"
        title, og_title, desc, og_desc = t + " · AI & Property Management Timeline", t, ev["summary"], ev["summary"]
        ld = []
        kind = "article"
    out = ("<!-- SHARE-META START (generated by build-ai-timeline.py; edit the constants there, not this block) -->\n"
           f"<title>{a(title)}</title>\n"
           f'<meta name="description" content="{a(desc)}" />\n' + robots +
           f'<link rel="canonical" href="{PAGE_URL}" />\n'
           f'<meta property="og:type" content="{kind}" />\n'
           f'<meta property="og:title" content="{a(og_title)}" />\n'
           f'<meta property="og:description" content="{a(og_desc)}" />\n'
           f'<meta property="og:url" content="{url}" />\n'
           f'<meta property="og:image" content="{PAGE_URL}og-image.png" />\n'
           '<meta property="og:image:width" content="1200" />\n'
           '<meta property="og:image:height" content="630" />\n'
           '<meta property="og:site_name" content="Peter Lohmann" />\n'
           '<meta name="twitter:card" content="summary_large_image" />\n'
           f'<meta property="article:published_time" content="{PUBLISHED}" />\n'
           f'<meta property="article:modified_time" content="{modified}" />\n'
           '<meta name="author" content="Peter Lohmann" />\n')
    for block in ld:
        out += '<script type="application/ld+json">' + json.dumps(block, ensure_ascii=False).replace("</", "<\\/") + "</script>\n"
    return out + "<!-- SHARE-META END -->"


# Plain-HTML version of every event, inside the page for search engines, AI crawlers and anyone
# without JavaScript. The interactive timeline replaces it as soon as it loads.
STATIC_RE = re.compile(r"<!-- STATIC-LIST START.*?<!-- STATIC-LIST END -->", re.S)
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def static_list(events):
    a = lambda x: html.escape(x, quote=True)
    evs = sorted(events, key=lambda e: sort_key(e["date"]))
    released = [e for e in evs if e["status"] != "announced"]
    soon = [e for e in evs if e["status"] == "announced"]
    out = ["<!-- STATIC-LIST START (generated by build-ai-timeline.py) -->", '<div class="tl-static">']
    def item(e):
        extra = f' (expected: {a(e["expected"])})' if e.get("expected") else ""
        src = f' <a href="{a(e["source_url"])}" rel="noopener">Source: {a(e["source_label"])}</a>' if e.get("source_url") else ""
        return (f'<li id="s-{a(e["id"])}"><strong>{a(e["display_date"])}</strong>, {a(e["company"])}: '
                f'<a href="{PAGE_URL}#e/{a(e["id"])}">{a(e["title"])}</a>{extra}. {a(e["summary"])}{src}</li>')
    for y in sorted({sort_key(e["date"])[:4] for e in released}):
        rows = [e for e in released if sort_key(e["date"])[:4] == y]
        out.append(f"<h2>{y}</h2><ul>" + "".join(item(e) for e in rows) + "</ul>")
    if soon:
        out.append("<h2>Announced, not shipped yet</h2><ul>" + "".join(item(e) for e in soon) + "</ul>")
    out.append("</div>")
    out.append("<!-- STATIC-LIST END -->")
    return "\n".join(out)


def build_main_page(events):
    p = os.path.join(TL, "index.html")
    with open(p, encoding="utf-8") as f:
        page = f.read()
    if not STATIC_RE.search(page):
        sys.exit("blog/ai-property-management-timeline/index.html is missing its STATIC-LIST START/END markers")
    page = META_RE.sub(lambda m: seo_block(events), page)
    page = STATIC_RE.sub(lambda m: static_list(events), page)
    with open(p, "w", encoding="utf-8") as f:
        f.write(page)


def build_share_pages(events, redirects):
    build_main_page(events)
    with open(os.path.join(TL, "index.html"), encoding="utf-8") as f:
        template = f.read()
    if not META_RE.search(template):
        sys.exit("blog/ai-property-management-timeline/index.html is missing its SHARE-META START/END markers")
    by_id = {e["id"]: e for e in events}
    pages = {e["id"]: e for e in events}
    for old, new in redirects.items():
        target, hops = new, 0
        while target not in by_id and target in redirects and hops < 5:
            target, hops = redirects[target], hops + 1
        if target in by_id and old not in by_id:
            pages[old] = by_id[target]
        else:
            print(f"  ! redirect '{old}' -> '{new}' does not lead to an event; skipped")
    for pid, ev in pages.items():
        url = f"{PAGE_URL}e/{pid}/"
        out = META_RE.sub(lambda m: seo_block(events, ev, url), template)
        # the plain-text list lives on the main post only (share pages point search engines there)
        out = STATIC_RE.sub("<!-- STATIC-LIST START -->\n<!-- STATIC-LIST END -->", out)
        d = os.path.join(TL, "e", pid)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(out)
    existing = set(os.listdir(os.path.join(TL, "e"))) if os.path.isdir(os.path.join(TL, "e")) else set()
    orphans = sorted(x for x in existing if os.path.isdir(os.path.join(TL, "e", x)) and x not in pages)
    return len(pages), orphans


# ---------- 4. link-preview image ----------
def font(paths, size):
    for p in paths:
        try: return ImageFont.truetype(p, size)
        except Exception: continue
    return ImageFont.load_default()


SERIF = ["/System/Library/Fonts/Supplemental/Georgia Bold.ttf", "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"]
BLACK = ["/System/Library/Fonts/Supplemental/Arial Black.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"]
SANS_B = ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/System/Library/Fonts/Helvetica.ttc"]
SANS = ["/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Helvetica.ttc"]
NAVY, BLUE, ORANGE, MUTED = (31, 58, 77), (44, 124, 176), (224, 112, 60), (95, 114, 128)
LINE, WASH = (220, 228, 236), (247, 250, 252)


def draw_marker(d, cx, cy, r, shape, color, announced=False):
    import math
    if shape == "star":
        pts = []
        for i in range(10):
            rr = r * 1.25 if i % 2 == 0 else r * 0.56
            a = math.radians(-90 + i * 36)
            pts.append((cx + rr * math.cos(a), cy + r * 0.1 + rr * math.sin(a)))
    elif shape == "diamond":
        rr = r * 1.12
        pts = [(cx, cy - rr), (cx + rr, cy), (cx, cy + rr), (cx - rr, cy)]
    else:
        pts = None
    if announced:
        if pts: d.polygon(pts, outline=color, width=3)
        else: d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=3)
    else:
        if pts: d.polygon(pts, fill=color)
        else: d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)


def build_og(events):
    S = 2  # draw at 2x, then shrink, for smooth edges
    W, H = 1200 * S, 630 * S
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 10 * S], fill=BLUE)
    # tricolor ticks
    for i, c in enumerate((BLUE, ORANGE, NAVY)):
        x = 64 * S + i * 36 * S
        d.rounded_rectangle([x, 58 * S, x + 28 * S, 64 * S], radius=3 * S, fill=c)
    f_h1 = font(SERIF, 60 * S)
    d.text((64 * S, 82 * S), "AI & Property Management:", font=f_h1, fill=NAVY)
    d.text((64 * S, 150 * S), "A Comprehensive Timeline", font=f_h1, fill=NAVY)
    d.text((64 * S, 232 * S), "From ChatGPT to now", font=font(SANS_B, 32 * S), fill=BLUE)
    # wordmark, top right corner
    f_wm = font(SERIF, 30 * S)
    wa, wb = d.textlength("Peter ", font=f_wm), d.textlength("Lohmann", font=f_wm)
    x0 = W - 64 * S - wa - wb
    d.text((x0, 52 * S), "Peter ", font=f_wm, fill=NAVY)
    d.text((x0 + wa, 52 * S), "Lohmann", font=f_wm, fill=BLUE)

    # one continuous line across the years: AI models above, property management below
    released = [e for e in events if e["status"] != "announced"]
    soon = [e for e in events if e["status"] == "announced"]
    years = sorted({int(sort_key(e["date"])[:4]) for e in released})
    first_m = int(sort_key(min(released, key=lambda e: sort_key(e["date"]))["date"])[5:7])
    left, right = 64 * S, W - 64 * S
    tail = 150 * S
    time_w = right - left - tail
    n_full, frac = len(years) - 1, (13 - first_m) / 12
    unit = time_w / (n_full + frac)
    first_w = max(frac * unit, 90 * S)
    unit = (time_w - first_w) / n_full
    zones = {}
    for i, y in enumerate(years):
        a_ = left if i == 0 else left + first_w + (i - 1) * unit
        zones[y] = (a_, a_ + (first_w if i == 0 else unit))
    line_y = 410 * S

    def xpos(e):
        k = sort_key(e["date"]); y, m, dd = int(k[:4]), int(k[5:7]), int(k[8:10])
        sm = first_m if y == years[0] else 1
        za, zb = zones[y]
        return za + ((m - sm) + (dd - 0.5) / 31) / (13 - sm) * (zb - za)

    d.line([left, line_y, left + time_w, line_y], fill=(159, 178, 193), width=3 * S)
    xx = left + time_w
    while xx < right:
        d.line([xx, line_y, min(xx + 9 * S, right), line_y], fill=(159, 178, 193), width=3 * S)
        xx += 16 * S
    f_year, f_soon = font(BLACK, 30 * S), font(SERIF, 24 * S)
    for i, y in enumerate(years):
        za, zb = zones[y]
        if i:
            d.line([za, line_y - 8 * S, za, line_y + 8 * S], fill=(159, 178, 193), width=3 * S)
        fy = f_year if zb - za > 110 * S else font(BLACK, 21 * S)
        d.text((za + 10 * S, line_y + 84 * S), str(y), font=fy, fill=NAVY)
    d.text((left + time_w + 12 * S, line_y + 86 * S), "Coming soon", font=f_soon, fill=NAVY)

    marks = [(xpos(e), e, False) for e in released]
    marks += [(left + time_w + 26 * S + i * 24 * S, e, True) for i, e in enumerate(soon)]
    r, step, base = 7 * S, 13 * S, 18 * S
    placed = {True: [], False: []}
    for x, e, is_soon in sorted(marks, key=lambda m: m[0]):
        col = LANE_RGB[e["lane"]]
        if not e.get("notable") or is_soon:   # faint dot on the line, like the page
            faint = tuple(int(c + (255 - c) * 0.5) for c in col)
            draw_marker(d, x, line_y, 4.5 * S, TYPES[e["type"]], faint, is_soon)
            continue
        up = e["lane"] == "frontier"
        lv = 0
        while any(abs(px - x) < 2 * r + 2 * S and pl == lv for px, pl in placed[up]):
            lv += 1
        placed[up].append((x, lv))
        ln = base + lv * step
        y = line_y - ln if up else line_y + ln
        col = LANE_RGB[e["lane"]]
        d.line([x, line_y, x, y], fill=tuple(int(c + (255 - c) * 0.5) for c in col), width=2 * S)
        draw_marker(d, x, y, r, TYPES[e["type"]], col, is_soon)
    d.text((64 * S, H - 42 * S), "peterlohmann.com/blog", font=font(SANS, 20 * S), fill=MUTED)
    img = img.resize((1200, 630), Image.LANCZOS)
    img.save(os.path.join(TL, "og-image.png"), "PNG", optimize=True)


def main():
    events = load("events.json")
    companies = load("companies.json")
    redirects = load("redirects.json", {})
    errors = validate(events, companies)
    if errors:
        print("Found problems in blog/ai-property-management-timeline/data/events.json:")
        for e in errors: print("  - " + e)
        sys.exit(1)
    changed, missing = sync_logos(companies)
    n, orphans = build_share_pages(events, redirects)
    build_og(events)
    print(f"Checked {len(events)} events and {len(companies)} companies: OK")
    print(f"Logos: {'updated companies.json paths' if changed else 'paths already current'}"
          + (f"; letter tile for {', '.join(missing)}" if missing else ""))
    print(f"Share pages: wrote {n} pages in blog/ai-property-management-timeline/e/")
    if orphans:
        print("  ! these share pages no longer match an event or redirect (left in place): " + ", ".join(orphans))
    print("Preview image: blog/ai-property-management-timeline/og-image.png")


if __name__ == "__main__":
    main()
