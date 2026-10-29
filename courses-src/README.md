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
tags: ["Operations", "Pricing"]    # optional; shown on the hub cards
---
```

## Body rules

- `## Heading {t=12:34}` (or `{t=1:02:03}`) marks a module: it gets a "Watch this part" button and a
  chapter in Google's video results. Timestamps must go up and stay inside the video.
- `## Heading` with no timestamp is a normal section ("What you'll learn", "Resources mentioned").
- The video is placed just before the first timed module.
- Images: `![alt text](/courses/assets/<slug>/file.jpg)`, with the file saved in `courses/assets/<slug>/`.
- No placeholders left (`[IMAGE:`, `[ALT:`, `[LINK]`, `[TODO:`) and no em or en dashes.

`_built.json` is written by the builder (what's live on the hub). Don't edit it.
This folder is kept out of search engines by robots.txt.
