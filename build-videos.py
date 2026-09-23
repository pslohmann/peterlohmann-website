#!/usr/bin/env python3
"""
Builds videos.html: the long-form videos from Peter's main YouTube channel (@peterlohmann).

WHY THIS EXISTS
    From Sep 2026 full podcast episodes publish on their own channel (@PeterLohmannsPodcast,
    see build-podcast.py). Peter's main channel is now where the agency-produced videos go.
    This page gives those videos a home on the site.

WHERE THE LIST COMES FROM
    YouTube's long-form-only uploads feed for the main channel (playlist "UULF" + the channel
    id), so Shorts never appear. From that feed it keeps only:
      - videos published on or after START_DATE (the agency era), and
      - videos that are not podcast episodes (the old back catalog is also on this channel).
    Move START_DATE earlier to also show older non-podcast videos (PM News, webinar replays).
    The feed returns the latest 15 long-form uploads, which is plenty for a "latest" page.

STATUS
    PREVIEW ONLY (Sep 23, 2026). Lives on the videos-preview branch, carries noindex, and is not
    in the menu or the sitemap. At launch: drop the ROBOTS line below, add videos.html to the
    sitemap, and link it from the footer and the podcast page.

RUN
    python3 build-videos.py
"""
import html as htmlmod
import re
import urllib.request
from datetime import datetime

from site_common import finalize

CHANNEL_ID = "UCGrk6yRgb0NAOBt10z2VZoA"             # @peterlohmann, Peter's main channel
LONGFORM_FEED = f"https://www.youtube.com/feeds/videos.xml?playlist_id=UULF{CHANNEL_ID[2:]}"
START_DATE = "2026-09-21"                              # first agency video landed Sep 23, 2026
EPISODE_MARK = "Peter Lohmann's Podcast"              # podcast episodes carry this in the title
CHANNEL_URL = "https://www.youtube.com/@peterlohmann"
SUBSCRIBE_URL = CHANNEL_URL + "?sub_confirmation=1"
ROBOTS = '<meta name="robots" content="noindex" />\n'  # PREVIEW: remove at launch
SITE = "https://www.peterlohmann.com"
OUT = "videos.html"
CHROME = "podcast.html"   # the header and footer are borrowed from the built podcast page


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "replace")


def esc(s):
    return htmlmod.escape(s or "", quote=True)


def fmt_date(d):
    dt = datetime.strptime(d, "%Y-%m-%d")
    return dt.strftime("%b ") + str(dt.day) + ", " + str(dt.year)


def first_lines(desc, limit=260):
    """The first paragraph of the YouTube description, trimmed at a sentence where possible."""
    paras = [re.sub(r"https?://\S+", "", p).replace("\n", " ").strip()
             for p in htmlmod.unescape(desc or "").split("\n\n")]
    text = next((p for p in paras if len(p) > 40), "")    # skip link-only lines at the top
    if len(text) <= limit:
        return text
    cut = text[:limit]
    end = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
    return (cut[:end + 1] if end > 80 else cut.rsplit(" ", 1)[0] + "...").strip()


def fetch_videos():
    xml = get(LONGFORM_FEED)
    out = []
    for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        vid = re.search(r"<yt:videoId>([^<]+)</yt:videoId>", e)
        title = re.search(r"<media:title>([^<]+)</media:title>", e) or re.search(r"<title>([^<]+)</title>", e)
        pub = re.search(r"<published>([^<]+)</published>", e)
        desc = re.search(r"<media:description>(.*?)</media:description>", e, re.S)
        if not (vid and title and pub):
            continue
        t = htmlmod.unescape(title.group(1)).strip()
        d = pub.group(1)[:10]
        if d < START_DATE or EPISODE_MARK in t:
            continue
        out.append({"id": vid.group(1), "title": t, "date": d,
                    "blurb": first_lines(desc.group(1) if desc else "")})
    out.sort(key=lambda v: v["date"], reverse=True)
    return out


def card(v):
    return f"""        <div class="ep-card">
          <div class="ep-player" data-id="{v['id']}" role="button" tabindex="0" aria-label="Play: {esc(v['title'])}">
            <img src="https://i.ytimg.com/vi/{v['id']}/hqdefault.jpg" alt="" loading="lazy" />
            <span class="ep-play" aria-hidden="true"></span>
          </div>
          <div class="ep-body">
            <div class="ep-date">{esc(fmt_date(v['date']))}</div>
            <h3>{esc(v['title'])}</h3>
          </div>
        </div>"""


def build():
    vids = fetch_videos()
    if not vids:
        raise SystemExit("No videos after the start date; aborting (leaving videos.html unchanged).")
    hero, rest = vids[0], vids[1:13]
    print(f"Featured: {hero['title']} ({hero['id']}) | more: {len(rest)}")

    chrome = open(CHROME, encoding="utf-8").read()
    head = chrome[:chrome.index('<main id="main">')]
    foot = chrome[chrome.index("</main>"):]

    # head: this page's own title, description, canonical and share tags
    desc = "The latest videos from Peter Lohmann's YouTube channel: process builds, software walkthroughs and lessons from running a property management company."
    swaps = [
        (r"<title>.*?</title>", "<title>Videos &middot; Peter Lohmann</title>"),
        (r'<meta name="description" content="[^"]*" />', f'<meta name="description" content="{esc(desc)}" />\n{ROBOTS.strip()}'),
        (r'<link rel="canonical" href="[^"]*" />', f'<link rel="canonical" href="{SITE}/videos" />'),
        (r'<meta property="og:title" content="[^"]*" />', '<meta property="og:title" content="Videos &middot; Peter Lohmann" />'),
        (r'<meta property="og:description" content="[^"]*" />', f'<meta property="og:description" content="{esc(desc)}" />'),
        (r'<meta property="og:url" content="[^"]*" />', f'<meta property="og:url" content="{SITE}/videos" />'),
    ]
    for pat, rep in swaps:
        head, n = re.subn(pat, lambda m: rep, head, count=1, flags=re.S)
        if n != 1:
            raise SystemExit(f"head swap failed: {pat}")
    head = head.replace(' class="active">Podcast<', '>Podcast<')   # Videos is not in the menu

    grid = ""
    if rest:
        grid = f"""
  <!-- MORE VIDEOS -->
  <section class="band tight">
    <div class="wrap">
      <span class="kicker">More Videos</span>
      <h2 class="h-lead">Keep watching.</h2>
      <p class="sub" style="margin-bottom:22px;">Tap any video to play it right here.</p>
      <div class="ep-grid">
{chr(10).join(card(v) for v in rest)}
      </div>
    </div>
  </section>
"""

    main = f"""<main id="main">

  <header class="page-hero">
    <div class="wrap">
      <div class="ticks" aria-hidden="true"><i></i><i></i><i></i></div>
      <span class="kicker">Videos</span>
      <h1>Watch Peter on YouTube.</h1>
      <p class="lead">Process builds, software walkthroughs and lessons from running a property management company, straight from Peter&#x27;s YouTube channel.</p>
      <div class="listen-row mt-md">
        <a class="btn btn-yt" href="{SUBSCRIBE_URL}" target="_blank" rel="noopener">Subscribe on YouTube</a>
        <a class="btn btn-ghost" href="/podcast">Looking for the podcast? &rarr;</a>
      </div>
    </div>
  </header>

  <!-- LATEST VIDEO -->
  <section class="band">
    <div class="wrap">
      <div class="split" style="align-items:center;">
        <div>
          <span class="tag tag-warn">Latest video</span>
          <h2 class="h-lead" style="margin:14px 0 10px;">{esc(hero['title'])}</h2>
          <p class="ep-date" style="margin:0 0 10px;">{esc(fmt_date(hero['date']))}</p>
          {'<p class="sub">'+esc(hero['blurb'])+'</p>' if hero['blurb'] else ''}
          <div class="listen-row mt-sm">
            <a class="btn btn-ghost" href="{CHANNEL_URL}/videos" target="_blank" rel="noopener">See all videos on YouTube</a>
          </div>
        </div>
        <div>
          <div class="embed-frame video">
            <iframe src="https://www.youtube.com/embed/{hero['id']}?rel=0" title="{esc(hero['title'])}"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
          </div>
        </div>
      </div>
    </div>
  </section>
{grid}
</main>"""

    page = head + main + foot[len("</main>"):]
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(finalize(page, "/videos.html"))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
