#!/usr/bin/env python3
"""One-time swap of the orange "NEW" announcement bar on the homepage, from the
Top 40 list to the PM API Report Card. Approved by Andrew on 2026-09-18 to go live
at 4:00am Eastern on Tuesday 2026-09-22. Run by
.github/workflows/announce-api-grader.yml; safe to run again (it does nothing once
swapped). Delete this file and that workflow after the bar has changed."""
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

GO_LIVE = datetime(2026, 9, 22, 4, 0, tzinfo=ZoneInfo("America/New_York"))

OLD = '''  <a class="announce" href="/largest-pm-companies"
     aria-label="New: Top 40 Largest PM Companies in the U.S. plus Top 10 by State, updated for 2026. Click to view the list.">
    <span class="announce-msg"><b>NEW</b> Top 40 Largest PM Companies in the U.S. + Top 10 by State &nbsp;&middot;&nbsp; Updated for 2026<span class="announce-cta"> &nbsp;&middot;&nbsp; Click to view <span class="announce-arrow">&rarr;</span></span></span>
  </a>'''

NEW = '''  <a class="announce" href="/api-grader/"
     aria-label="New: The PM API Report Card. PM software, graded on whether it lets you access your own data. Click to view.">
    <span class="announce-msg"><b>NEW</b> The PM API Report Card: PM software, graded on whether it lets you access your own data<span class="announce-cta"> &nbsp;&middot;&nbsp; Click to view <span class="announce-arrow">&rarr;</span></span></span>
  </a>'''

force = "--now" in sys.argv
now = datetime.now(ZoneInfo("America/New_York"))
if now < GO_LIVE and not force:
    print(f"{now:%Y-%m-%d %H:%M %Z}: before {GO_LIVE:%Y-%m-%d %H:%M %Z}, nothing to do yet.")
    sys.exit(0)

s = open("index.html", encoding="utf-8").read()
if NEW in s:
    print("Announcement bar already points at the API Report Card. Nothing to do.")
elif s.count(OLD) == 1:
    open("index.html", "w", encoding="utf-8").write(s.replace(OLD, NEW))
    print("Swapped the homepage announcement bar to the PM API Report Card.")
else:
    sys.exit("The announcement bar in index.html has changed since this was set up; not touching it.")
