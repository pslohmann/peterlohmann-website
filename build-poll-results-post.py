#!/usr/bin/env python3
"""
Builds the "21 Polls Later" blog post (Nov 2026) from two files:

    data/poll-results-2026.json     the 21 polls: question, month, issue, answers and vote counts
    data/poll-results-2026-copy.md  Peter's post copy (Markdown), used word for word. Two markers in it:
                                      [POLL CHART: key]  -> the results chart for that poll
                                      [HIGHLIGHTS]       -> "The year in four numbers" strip + topic jump links

Output: blog/property-management-poll-results-2026.html

Every percentage, bar length and vote line is calculated here, so nobody types a number by hand:
  - percent  = votes / that poll's total votes, rounded to a whole number (halves round up)
  - bar      = votes / the poll's top answer (the top answer fills the track and is orange)
  - "sorted" polls list answers by votes, with Other / None / N/A / Not sure / email-feedback answers last;
    "natural" polls keep the given order (scales such as agree to disagree)
  - a bar shorter than 22% of the top bar shows its percent outside the bar

First run: creates the page from the payroll post's shell (menu, footer, analytics) with a noindex line,
ready for publish-scheduled.py. Later runs: only the article body between the POLL-BODY markers is
rebuilt, so the header, publish date and anything the publish scripts changed are left alone.

    python3 build-poll-results-post.py
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = "property-management-poll-results-2026"
POST = os.path.join(HERE, "blog", f"{SLUG}.html")
DATA = os.path.join(HERE, "data", "poll-results-2026.json")
COPY = os.path.join(HERE, "data", "poll-results-2026-copy.md")
SHELL = os.path.join(HERE, "blog", "payroll-tips-property-management-business-owners.html")
CSS_V = 3   # bump after editing blog/poll-results.css

TITLE = "21 Polls Later: What Property Managers Told Me in 2026"
DESC = ("21 polls from my Tuesday newsletter: PM software, AI, trust accounting, org structure, churn, "
        "NARPM, and more, with real comments from operators.")
DATE_ISO, DATE_LABEL = "2026-11-18", "Nov 18, 2026"
SITE = "https://www.peterlohmann.com"

# answers that always sit at the bottom of a "sorted" poll
BOTTOM = ("other", "none", "n/a for me", "not sure yet", "i'll email you my feedback")
SMALL = 22.0   # % of the top bar below which the percent label moves outside the bar

START, END = "<!-- POLL-BODY:START (built by build-poll-results-post.py; edit the data/copy files, not this) -->", "<!-- POLL-BODY:END -->"


# ---------- text helpers ----------
def smart(s):
    """Escape for HTML and curl straight quotes, matching the rest of the blog (&rsquo; etc.)."""
    s = html.escape(s, quote=False)
    s = re.sub(r'(^|[\s(\[])"', r'\1&ldquo;', s)
    s = s.replace('"', '&rdquo;')
    s = re.sub(r"(^|[\s(\[])'", r"\1&lsquo;", s)
    s = s.replace("'", "&rsquo;")
    return s

def inline(s):
    """Markdown inline -> HTML: links, **bold**, *italic*, curly quotes."""
    links = []
    def keep(m):
        links.append((m.group(1), m.group(2)))
        return f"\x00{len(links) - 1}\x00"
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", keep, s)
    s = smart(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)\*", r"<em>\1</em>", s)
    def put(m):
        text, url = links[int(m.group(1))]
        ext = ' target="_blank" rel="noopener"' if url.startswith("http") else ""
        return f'<a href="{html.escape(url)}"{ext}>{smart(text)}</a>'
    return re.sub(r"\x00(\d+)\x00", put, s)

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("'", "")).strip("-")

def pct(v, total):
    return int(v * 100 / total + 0.5)


# ---------- the chart ----------
def is_bottom(label):
    l = label.lower()
    return l in BOTTOM or l.startswith("none")

def ordered(p):
    ch = list(p["choices"])
    if p["order"] == "sorted":
        main = sorted([c for c in ch if not is_bottom(c[0])], key=lambda c: -c[1])
        tail = sorted([c for c in ch if is_bottom(c[0])], key=lambda c: -c[1])
        ch = main + tail
    return ch

def grouped(p):
    """Small answers listed in a poll's "group_other" are folded into one "Other" row (Andrew, 2026-11-18).
    Returns the chart's choices plus the folded answers, biggest first, with the poll's own "Other" last."""
    members = p.get("group_other")
    if not members:
        return list(p["choices"]), []
    keep = [c for c in p["choices"] if c[0] not in members]
    folded = [c for c in p["choices"] if c[0] in members]
    if len(folded) != len(members):
        sys.exit(f"{p['key']}: group_other names an answer that isn't in the poll")
    folded.sort(key=lambda c: (c[0] == "Other", -c[1]))
    return keep + [["Other", sum(v for _, v in folded)]], folded

def chart(p):
    total = sum(v for _, v in p["choices"])
    choices, folded = grouped(p)
    top = max(v for _, v in choices)
    rows = []
    top_done = False
    for label, v in ordered({**p, "choices": choices}):
        w = v * 100 / top
        cls = ["poll-row"]
        if v == top and not top_done:
            cls.append("is-top"); top_done = True
        if w < SMALL:
            cls.append("is-small")
        votes = f'<span class="poll-votes">{v} of {total} votes</span>'
        if folded and label == "Other":
            # "Breakdown" button next to Other: a native <details> dropdown, so it works with or without JavaScript
            cls.append("has-more")
            items = "".join(f'<li><span>{smart("Other answers" if n == "Other" else n)}</span><span>{c} vote{"s" if c != 1 else ""}</span></li>' for n, c in folded)
            label_html = (f'<details class="poll-more"><summary><span class="poll-choice">Other '
                          f'<span class="pm-btn">Breakdown<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3"/></svg></span></span>'
                          f'{votes}</summary><ul class="pm-list">{items}</ul></details>')
        else:
            label_html = f'<span class="poll-choice">{smart(label)}</span>{votes}'
        rows.append(
            f'<li class="{" ".join(cls)}"><div class="poll-label">{label_html}</div>'
            f'<div class="poll-track" aria-hidden="true"><div class="poll-fill" style="--w:{w:.1f}%">'
            f'<span class="poll-pct">{pct(v, total) or "&lt;1"}%</span></div></div></li>')   # 1 vote of 212 reads "<1%", not "0%"
    q = smart(p["question"])
    return (f'<figure class="poll-card" id="poll-{p["key"]}" aria-label="Poll results: {q}">'
            f'<span class="poll-kicker">Poll results &middot; {p["date"]}</span>'
            f'<p class="poll-q">{q}</p><ol class="poll-bars">{"".join(rows)}</ol>'
            f'<figcaption class="poll-foot"><span><b>{total} votes</b> &middot; {smart(p["edition"])}</span>'
            f'<span>Peter Lohmann&rsquo;s Newsletter</span></figcaption></figure>')


# ---------- highlights strip + jump links ----------
def share(polls, key, labels):
    p = polls[key]
    total = sum(v for _, v in p["choices"])
    return pct(sum(v for l, v in p["choices"] if l in labels), total)

def highlights(polls, topics):
    tiles = [
        (share(polls, "switching-software", {"Switched at least once and glad I did"}), "switched PM software and are glad they did"),
        (share(polls, "open-api", {"Required / deal-breaker", "Very important"}), "call an Open API a deal-breaker or very important"),
        (share(polls, "trust-accounting", {"In-house"}), "handle trust accounting in-house"),
        (share(polls, "narpm-favorability", {"Very favorable", "Somewhat favorable"}), "view NARPM favorably"),
    ]
    expected = [60, 79, 57, 67]   # the numbers in Peter's brief; stop if the data ever disagrees
    got = [n for n, _ in tiles]
    if got != expected:
        sys.exit(f"Highlights changed: expected {expected}, data gives {got}")
    cells = "".join(f'<div class="hl"><span class="hl-num">{n}%</span><span class="hl-txt">{t}</span></div>' for n, t in tiles)
    jump = "".join(f'<a href="#{slugify(t)}">{smart(t)}</a>' for t in topics)
    return (f'<div class="hl-wrap"><p class="hl-title">The year in four numbers</p><div class="hl-grid">{cells}</div></div>\n'
            f'<nav class="jump" aria-label="Jump to a topic"><span class="jump-label">Jump to:</span>{jump}</nav>')


# ---------- Markdown copy -> article body ----------
def body(polls):
    text = open(COPY, encoding="utf-8").read().strip()
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    topics = [b[3:].strip() for b in blocks if b.startswith("## ") and b[3:].strip() != "What's next"]
    out, quotes, used = [], [], []
    def flush():
        if quotes:
            out.append('<blockquote class="reader">' + "".join(f"<p>{q}</p>" for q in quotes) + "</blockquote>")
            quotes.clear()
    for b in blocks:
        if b.startswith(">"):
            quotes.append(inline(re.sub(r"^>\s?", "", b, flags=re.M).replace("\n", " ")))
            continue
        flush()
        m = re.fullmatch(r"\[POLL CHART:\s*([a-z0-9-]+)\]", b)
        if m:
            key = m.group(1)
            if key not in polls:
                sys.exit(f"No poll data for chart key: {key}")
            used.append(key); c = chart(polls[key])
            # Jump links (Andrew, 2026-11-23): #poll-<key> lands on the poll's own heading when it
            # has one, so the reader sees the question and month; otherwise on the chart card.
            if out and out[-1].startswith("<h3>"):
                out[-1] = out[-1].replace("<h3>", f'<h3 id="poll-{key}">', 1)
                c = c.replace(f' id="poll-{key}"', "", 1)
            out.append(c)
        elif b == "[HIGHLIGHTS]":
            out.append(highlights(polls, topics))
        elif b.startswith("## "):
            t = b[3:].strip(); out.append(f'<h2 id="{slugify(t)}">{smart(t)}</h2>')
        elif b.startswith("### "):
            out.append(f"<h3>{inline(b[4:].strip())}</h3>")
        else:
            out.append(f"<p>{inline(b.replace(chr(10), ' '))}</p>")
    flush()
    missing = [k for k in polls if k not in used]
    if missing or len(used) != len(set(used)):
        sys.exit(f"Chart problem. Unused polls: {missing}; used: {used}")
    return "\n".join(out)


# ---------- page shell (first run only) ----------
def new_page(shell):
    url = f"{SITE}/blog/{SLUG}"
    t_html = smart(TITLE)
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": TITLE, "description": DESC,
          "image": f"{SITE}/images/blog/{SLUG}--cover.webp", "url": url,
          "author": {"@type": "Person", "name": "Peter Lohmann", "url": f"{SITE}/"},
          "publisher": {"@type": "Person", "name": "Peter Lohmann"}, "mainEntityOfPage": url, "datePublished": DATE_ISO}
    head_end = shell.index('<link rel="icon"')
    head = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8" />\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
        '<link rel="preconnect" href="https://use.typekit.net" crossorigin />\n'
        f'<title>{t_html} &middot; Peter Lohmann</title>\n'
        f'<meta name="description" content="{html.escape(DESC)}" />\n'
        '<meta name="robots" content="noindex" data-scheduled="1" />\n'
        f'<link rel="canonical" href="{url}" />\n'
        '<meta property="og:type" content="article" />\n'
        f'<meta property="og:title" content="{html.escape(TITLE)}" />\n'
        f'<meta property="og:description" content="{html.escape(DESC)}" />\n'
        f'<meta property="og:url" content="{url}" />\n'
        f'<meta property="og:image" content="{SITE}/images/blog/{SLUG}--cover.webp" />\n'
        '<meta property="og:image:width" content="1200" />\n<meta property="og:image:height" content="630" />\n'
        '<meta property="og:site_name" content="Peter Lohmann" />\n<meta name="twitter:card" content="summary_large_image" />\n'
        f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(",", ":"))}</script>\n')
    rest = shell[head_end:]
    # the post's own stylesheet, plus a tiny script that turns on the bar animation before the first paint
    css = rest.index("\n", rest.index("styles.css?v=")) + 1
    rest = (rest[:css] + f'<link rel="stylesheet" href="poll-results.css?v={CSS_V}" />\n'
            "<script>(function(){try{if('IntersectionObserver' in window&&!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches))document.documentElement.classList.add('js-anim');}catch(e){}})();</script>\n"
            + rest[css:])
    # header: date, title, CSS-drawn cover
    rest = re.sub(r'<div class="article-meta">.*?</div>', f'<div class="article-meta">{DATE_LABEL} &middot; by Peter Lohmann</div>', rest, count=1)
    rest = re.sub(r"<h1>.*?</h1>", f"<h1>{t_html}</h1>", rest, count=1)
    cover = ('<figure class="article-cover"><div class="cover-card" role="img" aria-label="Poll results 2026: 21 polls. '
             'What property managers told me this year."><span class="cover-kicker">Poll results &middot; 2026</span>'
             '<div class="cover-bars" aria-hidden="true"><i style="width:92%"></i><i style="width:64%"></i><i style="width:41%"></i><i style="width:22%"></i></div>'
             '<div class="cover-text"><div class="cover-big">21 polls.</div><div class="cover-sub">What property managers told me this year</div></div></div></figure>')
    rest = re.sub(r'<figure class="article-cover">.*?</figure>', cover, rest, count=1, flags=re.S)
    # body placeholder, between the body opening and the follow-links row
    a = rest.index('<div class="article-body">')
    b = rest.index('        <div class="post-follow">')
    rest = rest[:a] + f'<div class="article-body polls">\n{START}\n{END}\n' + rest[b:]
    # bar animation: watch each chart and grow its bars when it scrolls into view
    anim = ("<script>(function(){try{if(!document.documentElement.classList.contains('js-anim'))return;"
            "var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in-view');io.unobserve(e.target);}})},{threshold:.25});"
            "document.querySelectorAll('.poll-card').forEach(function(c){io.observe(c)});}catch(e){document.documentElement.classList.remove('js-anim');}})();</script>\n")
    rest = rest.replace('<script src="../site.js', anim + '<script src="../site.js', 1)
    return head + rest


def main():
    polls = {p["key"]: p for p in json.load(open(DATA, encoding="utf-8"))}
    if not os.path.exists(POST):
        page = new_page(open(SHELL, encoding="utf-8").read())
        print(f"created blog/{SLUG}.html (noindex until publish-scheduled.py runs)")
    else:
        page = open(POST, encoding="utf-8").read()
    i, j = page.index(START), page.index(END)
    page = page[:i + len(START)] + "\n" + body(polls) + "\n" + page[j:]
    if re.search("[–—]|&mdash;|&ndash;", page):
        sys.exit("Stopped: an em or en dash slipped into the page.")
    open(POST, "w", encoding="utf-8").write(page)
    print(f"built {len(polls)} charts into blog/{SLUG}.html")

if __name__ == "__main__":
    main()
