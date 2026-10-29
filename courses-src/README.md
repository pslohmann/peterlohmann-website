# Free Courses: source files

Each course is two files in this folder, written by the content project:

- `<slug>.md`: frontmatter + the course body (becomes https://www.peterlohmann.com/courses/<slug>/)
- `<slug>.llm.md`: the plain-text companion for AI tools (copied unchanged to /courses/<slug>.llm.md)

Then, from the repo folder:

```
python3 build-courses.py
```

It checks every course, builds the pages and the /courses/ hub, updates llms.txt and the sitemap,
and stops with the exact file and line if anything is wrong. A course that fails is not published.
Commit and push everything it changed.

## Frontmatter

```yaml
---
title: "Course title"              # required; page H1 and <title>
slug: "course-slug"                # required; must match the filename
date: 2026-11-04                   # required; page publish date
updated: 2026-11-20                # optional; set when you revise a course (sitemap + schema use it)
description: "..."                 # required; 150-160 characters
youtube_id: "dQw4w9WgXcQ"          # required; the 11-character video ID
upload_date: 2026-11-03            # required; YouTube publish date
duration: "PT42M15S"               # required; ISO 8601 video length
thumbnail: ""                      # optional; blank = the video's YouTube thumbnail
tags: ["Operations", "Pricing"]    # optional; shown on the hub cards and used for the topic filter pills
                                   # (current topics: Operations, Leadership, Technology, AI)
sponsor_domains: ["leadsimple.com"]  # optional; when a video is sponsored, links to these sites get rel="sponsored"
---
```

## Body rules

- `## Heading {t=12:34}` (or `{t=1:02:03}`) marks a module: it gets a "Watch this part" button and a
  chapter in Google's video results. Timestamps must go up and stay inside the video.
- `## Heading` with no timestamp is a normal section ("What you'll learn", "Resources mentioned").
- The video is placed just before the first timed module.
- Images: `![alt text](/courses/assets/<slug>/file.webp)`, with the file saved in `courses/assets/<slug>/`.
  Screenshots: WebP, about 1460px wide max. Portrait shots are shown at a readable 420px.
- Downloads (a PDF checklist, etc.): save the file in `courses/assets/<slug>/` and link it like any link,
  `[download it here](/courses/assets/<slug>/file.pdf)`. The page link downloads the file and is counted in GA4
  as `course_download_click`. The file's public address is https://www.peterlohmann.com/courses/assets/<slug>/file.pdf
- Diagrams: `![alt text](/courses/assets/<slug>/diagram.svg)` with an optional `*caption*` on the next line.
  SVGs are pasted into the page (site font, readable by search engines) after scripts/outside links are stripped.
- Components (blockquotes that start with a tag):
  `> [!TAKEAWAY]` (blue "Key takeaway" box), `> [!WARNING]` ("Where this goes wrong"), `> [!NOTE]`,
  `> [!STAT] 8-12 | Label` (big number; STATs in a row sit side by side),
  `> [!VIDEO] youtubeID | Caption` (a second, click-to-play YouTube video), and
  `<details><summary>Question</summary> ...markdown... </details>` (closed by default).
- Numbered lists inside a timed module become step cards.
- No placeholders left (`[IMAGE:`, `[ALT:`, `[LINK]`, `[TODO:`) and no em or en dashes.

`_built.json` is written by the builder (what's live on the hub). Don't edit it.
This folder is kept out of search engines by robots.txt.
