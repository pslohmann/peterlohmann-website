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
  4. Cuts the 1200x630 share image images/blog/ai-property-management-timeline--og.jpg from the blog
     card cover, so Slack, LinkedIn and X show the same graphic as the blog list.
  5. Writes blog/ai-property-management-timeline/timeline.md, a plain-text (Markdown) copy of the whole
     timeline plus an FAQ, for AI tools and crawlers. People browsing the site never land on it: the
     page only points to it with a small footer link, a <link rel="alternate"> tag and llms.txt.
     Hand-written FAQ answers live in data/faq.json; the rest of the FAQ is worked out from the events.

It never deletes anything. If an old e/<id>/ folder no longer matches an event or redirect,
it prints a warning (ids are permanent: retire one with a redirect instead of deleting it).
"""
import json, os, re, sys, html, datetime
from PIL import Image

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
COVER = "images/blog/ai-property-management-timeline--cover.webp"   # blog card + share image source
OG_IMAGE = "images/blog/ai-property-management-timeline--og.jpg"
OG_DESCRIPTION = "In the age of AI, things move so fast it's hard to keep up."
MD_URL = PAGE_URL + "timeline.md"   # step 5

LANES = ["frontier", "pm_software", "leasing", "maintenance", "risk", "data_pricing", "plm"]
TYPES = {"frontier_model": "star", "api_access": "diamond", "mcp_connector": "diamond", "platform_launch": "dot",
         "product_release": "dot", "ai_agent": "dot", "computer_use": "dot", "acquisition": "dot", "funding": "dot",
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
    # "Coming soon" items with no date at all (expected starts "No date") sort after the dated ones
    if isinstance(d, dict):
        if d.get("status") == "announced" and str(d.get("expected", "")).lower().startswith("no date"):
            return "9999-12-31"
        d = d["date"]
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
            "image": SITE + "/" + OG_IMAGE, "datePublished": PUBLISHED, "dateModified": modified,
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
           f'<link rel="alternate" type="text/markdown" href="{MD_URL}" title="Plain-text version for AI tools" />\n'
           f'<meta property="og:type" content="{kind}" />\n'
           f'<meta property="og:title" content="{a(og_title)}" />\n'
           f'<meta property="og:description" content="{a(og_desc)}" />\n'
           f'<meta property="og:url" content="{url}" />\n'
           f'<meta property="og:image" content="{SITE}/{OG_IMAGE}" />\n'
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
    evs = sorted(events, key=sort_key)
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
    page = re.sub(r"<p>Last updated [A-Z][a-z]+ \d{1,2}, \d{4}\.", "<p>Last updated " + nice_date() + ".", page)
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
# Social shares (Slack, LinkedIn, X...) use the same wordless graphic as the blog card, cut to
# 1200x630 JPG like every other post's images/blog/<slug>--og.jpg. Replace the cover file to change it.
def build_og():
    im = Image.open(os.path.join(HERE, COVER)).convert("RGB")
    w, h = im.size
    nh = round(w * 630 / 1200)
    y = (h - nh) // 2
    im = im.crop((0, y, w, y + nh)).resize((1200, 630), Image.LANCZOS)
    im.save(os.path.join(HERE, OG_IMAGE), "JPEG", quality=88, optimize=True, progressive=True)


# ---------- 5. Markdown copy for AI tools ----------
# Labels match LANES and TYPES at the top of timeline.js.
LANE_LABEL = {"frontier": "Frontier AI models", "pm_software": "Property management software",
              "leasing": "Leasing, showings and CRM", "maintenance": "Maintenance and inspections",
              "risk": "Screening, fraud and insurance", "data_pricing": "Data and pricing", "plm": "Peter Lohmann Media"}
TYPE_LABEL = {"frontier_model": "Frontier model", "api_access": "API", "mcp_connector": "MCP or connector",
              "platform_launch": "AI platform", "product_release": "AI feature", "ai_agent": "AI agent", "computer_use": "Computer-use agent",
              "acquisition": "Acquisition", "funding": "Funding", "access_cutoff": "Access cut-off", "report": "Report"}
CONF_LABEL = {"high": "", "med": "medium confidence", "low": "low confidence"}


def nice_date(d=None):
    d = d or datetime.date.today()
    return f"{MONTHS[d.month - 1]} {d.day}, {d.year}"


def build_markdown(events):
    evs = sorted(events, key=sort_key)
    released = [e for e in evs if e["status"] != "announced"]
    soon = [e for e in evs if e["status"] == "announced"]
    pub = datetime.date.fromisoformat(PUBLISHED)
    link = lambda e: f"{PAGE_URL}e/{e['id']}/"

    def line(e):
        tags = [e["company"], TYPE_LABEL[e["type"]]]
        if CONF_LABEL[e["confidence"]]: tags.append(CONF_LABEL[e["confidence"]])
        out = f"- **{e['display_date']}** ({'; '.join(tags)}): [{e['title']}]({link(e)}). {e['summary']}"
        if e.get("expected"): out += f" Expected: {e['expected']}."
        return out + f" Source: [{e['source_label']}]({e['source_url']})"

    def short(e):
        return f"- {e['display_date']}: {e['company']}, [{e['title']}]({link(e)})"

    L = [f"# {TITLE}", "",
         "> A dated, sourced timeline of AI in residential property management since ChatGPT (November 2022): "
         "frontier AI model, personal AI agent and computer-use agent launches, AI features, APIs and MCP connectors from property "
         "management software and vendors, access fights, and Peter Lohmann's own reports.", "",
         "- Author: [Peter Lohmann](https://www.peterlohmann.com/)",
         f"- Interactive version (the original): {PAGE_URL}",
         f"- Published {nice_date(pub)}. Last updated {nice_date()}.",
         f"- {len(released)} events that have shipped, plus {len(soon)} announced but not shipped yet.",
         f"- Cite as: Peter Lohmann, \"{TITLE}\", {PAGE_URL}",
         "",
         "## How to read this", "",
         "- Each event lists its date, the company, the type of event, what happened, a permanent link to that event, and the original source.",
         "- A date like \"By Sep 2026\" means the exact date isn't public; the event had happened by then.",
         "- Events marked medium or low confidence rest on secondary sources or an unconfirmed date. Unmarked events come from first-party sources.",
         "- Events are listed as shipped only when customers can actually use them. Announcements without real availability are in the last section.",
         "- Columns on the interactive version: " + ", ".join(LANE_LABEL.values()) + ".",
         "",
         "## FAQ", ""]
    for item in load("faq.json", []):
        L += [f"### {item['q']}", "", item["a"], ""]

    def pm(e): return e["lane"] != "frontier" and e["lane"] != "plm"
    groups = [
        ("Which property management software, and other tools property managers use, have an MCP server or AI connector?",
         [e for e in released if pm(e) and e["type"] == "mcp_connector"],
         [e for e in soon if pm(e) and e["type"] == "mcp_connector"]),
        ("Which property management software, and other tools property managers use, have launched or opened an API?",
         [e for e in released if pm(e) and e["type"] == "api_access"], []),
        ("Which vendors have cut off or restricted third-party access?",
         [e for e in released if e["type"] == "access_cutoff"], []),
        ("Which personal AI agents have launched?",
         [e for e in released if e["lane"] == "frontier" and e["type"] == "ai_agent"], []),
        ("Which AI agents can use websites and software through the screen, without an API?",
         [e for e in released if e["type"] == "computer_use" or e["id"] == "amazon-blocks-comet"], []),
        ("When were the major frontier AI models released?",
         [e for e in released if e["type"] == "frontier_model"], []),
    ]
    for q, rows, later in groups:
        if not rows: continue
        L += [f"### {q}", "", f"As of {nice_date()}, in date order:", ""] + [short(e) for e in rows]
        if later:
            L += ["", "Announced but not shipped yet:", ""] + [short(e) for e in later]
        L.append("")

    L += ["## Timeline", ""]
    for y in sorted({sort_key(e["date"])[:4] for e in released}):
        L += [f"### {y}", ""] + [line(e) for e in released if sort_key(e["date"])[:4] == y] + [""]
    if soon:
        L += ["## Announced, not shipped yet", "",
              "These have been announced but aren't generally available yet. They move onto the timeline when they ship.", ""]
        L += [line(e) for e in soon] + [""]
    L += ["## Disclosure", "",
          "Some companies shown have advertised with Peter Lohmann Media. "
          "Financial interest disclosure: https://www.peterlohmann.com/financial-interest-disclosure", "",
          "Something missing or wrong? https://www.peterlohmann.com/contact", ""]
    text = "\n".join(L)
    if "—" in text or "–" in text:
        sys.exit("timeline.md would contain an em or en dash; fix data/faq.json")
    with open(os.path.join(TL, "timeline.md"), "w", encoding="utf-8") as f:
        f.write(text)


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
    build_og()
    build_markdown(events)
    print(f"Checked {len(events)} events and {len(companies)} companies: OK")
    print(f"Logos: {'updated companies.json paths' if changed else 'paths already current'}"
          + (f"; letter tile for {', '.join(missing)}" if missing else ""))
    print(f"Share pages: wrote {n} pages in blog/ai-property-management-timeline/e/")
    if orphans:
        print("  ! these share pages no longer match an event or redirect (left in place): " + ", ".join(orphans))
    print("Share image: " + OG_IMAGE)
    print("Markdown for AI tools: blog/ai-property-management-timeline/timeline.md")


if __name__ == "__main__":
    main()
