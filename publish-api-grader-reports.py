#!/usr/bin/env python3
"""
Copy the vendor grader reports into api-grader/reports/ so each vendor page can offer
its own markdown for download.

Redaction: the reports were written against LIVE accounts and a few name them.
Both repos are public, so a small list of account identifiers is replaced on the
way out. This touches identifiers only. No mark, score, category, finding or
sentence of reasoning is altered, and every substitution made is printed so it
can be checked against the source.

Run after a new report lands:

    python3 publish-api-grader-reports.py
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "grader-reports" / "reports"     # local archive, gitignored
DST = HERE / "api-grader" / "reports"         # published, served at /api-grader/reports/

# vendor slug -> the report file behind the PUBLISHED score. Kept in step with
# SOURCES in extract-api-grader-checks.py; a superseded run must never be offered here.
SOURCES = {
    "appfolio":          "appfolio-2026-09-01.md",
    "aptly":             "aptly-2026-09-03.md",
    "boom":              "boom-2026-09-25.md",   # corrected report: carries both the 2026-09-09 and 2026-09-25 corrections
    "buildium":          "buildium-2026-08-27.md",
    "column":            "column-2026-09-09.md",
    "latchel":           "latchel-2026-09-10.md",
    "leadsimple":        "leadsimple-2026-08-28.md",
    "magic-door":        "magic-door-2026-09-10.md",
    "mason":             "mason-2026-09-21.md",
    "process-street":    "process-street-2026-08-31.md",
    "property-meld":     "property-meld-2026-09-01.md",
    "propertyware":      "propertyware-2026-09-14.md",
    "quickbooks-online": "quickbooks-online-2026-09-02.md",
    "quo":               "quo-2026-09-08.md",
    "rentengine":        "rentengine-2026-09-03.md",
    "rent-manager":      "rent-manager-2026-09-07.md",
    "rentvine":          "rentvine-2026-09-02.md",
    "ringcentral":       "ringcentral-2026-09-01.md",
    "showdigs":          "showdigs-2026-09-10.md",
    "showmojo":          "showmojo-2026-09-02.md",
    "simplevoip":        "simplevoip-2026-09-10.md",
    "tenant-turner":     "tenant-turner-2026-09-01.md",
    "xero":              "xero-2026-08-27.md",
    "zoom":              "zoom-2026-09-08.md",
}

REDACT = [
    (r"cucPATSDM9kbS3xKg",                 "[account id withheld]"),
    (r"Dream Big Property Management",     "[operator account]"),
    (r"dreambig\.rentvine\.com",           "[account].rentvine.com"),
    (r"`dreambig`",                        "`[account]`"),
    (r"BANK-ENTERPRISE CLIENT TRUST MAIN", "[trust account name withheld]"),
    # Propertyware: the operator's live org number and the IDs of its test-fixture contacts
    (r"\b610009088\b",                    "[org id withheld]"),
    (r"\b(8483110918|8483569669|8477179913)\b", "[test contact id withheld]"),
    # Mason: the operator's credential-delivery mail ids and password-manager item id
    (r"`1a06c6986575955a`", "`[mail thread id withheld]`"),
    (r"thread `1a06c6986575955a`", "thread `[id withheld]`"),
    (r"message `1a0c66b6a11cd434`", "message `[id withheld]`"),
    (r"item `vobntdzmapgyvdqpbt5jd7qbba`", "item `[id withheld]`"),
]


# ---------------------------------------------------------------------------
# LAUNCH-SCOPE SUPPRESSION
#
# For the preview launch, published reports must not indicate that any vendor
# made changes or upgrades, or that any vendor saw an earlier grade. Two reports
# carried that framing. Removing it changes NO mark, score, category total or
# finding: only the before-and-after narration around them, and one manifest
# entry recording vendor correspondence.
#
# The archived reports under grader-reports/ are untouched and remain the record
# of what was submitted. This suppression is applied on the way out, here, so a
# rebuild cannot quietly reintroduce it.
#
# When re-scores resume and updates become publishable, delete this block.
# ---------------------------------------------------------------------------
SUPPRESS = {
    "leadsimple": [
        ("- Date run: 2026-08-28 (re-run after LeadSimple shipped access-control "
         "and documentation improvements)",
         "- Date run: 2026-08-28"),
        # the whole "what changed" section, opening line through its closing paragraph
        (r"- \*\*What changed since the 2026-08-27 run.*?This run supersedes the "
         r"2026-08-27 re-score\.\n", "", "regex"),
        (' Previously the single key was full read/write (the existing default key '
         'is tagged "Read and write").', ""),
        (" Previously one key per account.", ""),
        (" Previously rotate-only.", ""),
        ("This used to be the weakest area and is now much stronger. ", ""),
        ("LeadSimple's REST API has improved markedly. Under clean methodology v1.1 "
         "it now scores 87/100 (B+), up from 78 (C+), because LeadSimple fixed its "
         "two weakest areas: access control and documentation. You can now create",
         "Under clean methodology v1.1, LeadSimple's REST API scores 87/100 (B+). "
         "You can create"),
    ],
    "rentengine": [
        ('- Operator-supplied vendor communication: "Response to API Report Card '
         'v1.1" (PDF, 4 pages, received 2026-09-03)\n', ""),
        (r"\n\*\*Use of the vendor communication:\*\*.*?live observation\.\n", "", "regex"),
        (" The vendor states these are built and due to ship by 2 pm on 2026-09-03; "
         "they were not in production when this packet was frozen and are therefore "
         "not credited.", ""),
    ],
}


# ---------------------------------------------------------------------------
# PUBLISHED CORRECTIONS
#
# Applied on the way out, like SUPPRESS, so a rebuild cannot revert them. Each
# rule must match or the build aborts.
#
# Boom C5.3, corrected 2026-09-09. The run marked "not commercially gated" as
# partial while its own text established that no gate exists, withholding a pass
# because Boom publishes no pricing. The methodology does not ask for published
# pricing: C5.3 awards yes "when included or free", partial "when some meaningful
# capabilities are tier-gated", no "when the API requires a premium plan". No
# tier-gating was found. The one genuine gap, that the account owner could not
# confirm whether their access carried a fee, has since been answered by the
# operator: they were not charged extra, so access was included. Run 1 originally
# marked this yes; the correction restores that mark.
#
# Nothing else in the run changes. All other marks, the evidence and the findings
# stand; only the figures derived from C5.3 move.
# ---------------------------------------------------------------------------
CORRECTIONS = {
    "propertyware": [
        # Propertyware coverage-map figure, corrected 2026-09-15. The functional coverage map
        # still carried run 1's pre-reconciliation C1.2 figure (81.4%, objects-only sub-map).
        # The C1.2 check itself, and the published score, use the reconciled 85.2%. No mark,
        # category value or score changes; only the stale summary line is brought into line.
        ("# API Report Card: Propertyware Open API",
         "> **Correction, 2026-09-15.** The functional coverage map below originally repeated\n"
         "> run 1's pre-reconciliation figure for core write coverage (81.4%). The reconciled\n"
         "> figure used by check C1.2 and by the published score is 85.2%, and the map now\n"
         "> says so. **No mark or score changes: Propertyware remains 71 (C-).**\n\n"
         "# API Report Card: Propertyware Open API"),
        ('Weighted mutable coverage **28.5 / 35 = 81.4%** (general-ledger transactions marked N-A within the sub-map as computed records, per the C1 method).',
         "Weighted mutable coverage **85.2%** after reconciliation, as scored in C1.2 below "
         "(run 1's original objects-only construction gave 28.5 / 35 = 81.4%; see the "
         "reconciliation note under C1.2)."),
    ],
    "aptly": [
        # Aptly C5.3 language, corrected 2026-09-09. The run reported that Aptly
        # publishes no plan tiers or prices. It does: getaptly.com/pricing shows
        # Essential, Premium and Enterprise with prices, and lists "Access to
        # Aptly API" as a Premium feature. That does not change the mark, which
        # rests on the Help Center's Premium requirement; the pricing page
        # independently confirms it. Verified against the live page 2026-09-09.
        ("# API Report Card: Aptly",
         "> **Correction, 2026-09-09.** This report stated that Aptly publishes no\n"
         "> plan tiers or prices. That was wrong. getaptly.com/pricing publishes three\n"
         "> tiers, Essential, Premium and Enterprise, with prices, and lists \"Access to\n"
         "> Aptly API\" as a Premium plan feature. The language below is corrected.\n"
         "> **The score is unchanged at 58 (F).** C5.3 was never scored on the pricing\n"
         "> page: it rests on Aptly's Help Center stating the API requires a Premium\n"
         "> Subscription, which the pricing page now independently corroborates.\n\n"
         "# API Report Card: Aptly"),
        ("- https://www.getaptly.com/pricing \u2014 no published plan tiers; demo-gated pricing",
         "- https://www.getaptly.com/pricing \u2014 three published tiers (Essential, "
         "Premium, Enterprise) with prices; \"Access to Aptly API\" listed as a Premium "
         "plan feature [rechecked live 2026-09-09]"),
        ('Aggravating rather than mitigating: Aptly publishes no plan tiers or prices at all \u2014 https://www.getaptly.com/pricing carries only "Book a demo to get custom pricing for your portfolio" \u2014 so an operator cannot determine the cost of API entitlement without a sales conversation.',
         'Corroborated by the pricing page: https://www.getaptly.com/pricing publishes '
         'three named tiers \u2014 Essential, Premium and Enterprise \u2014 with prices, and '
         'lists "Access to Aptly API" as a Premium plan feature and "Enterprise API" '
         'under Enterprise. That independently confirms the Help Center\'s Premium '
         'requirement, so an operator can both see the gate and price it '
         '[rechecked live 2026-09-09].'),
    ],
    # Boom: both corrections (C5.3 on 2026-09-09, the leasing/screening classification ruling
    # on 2026-09-25) are written into the source file itself, boom-2026-09-25.md, so no
    # on-the-way-out rules are needed. The original run stays archived as boom-2026-09-03.md.
}


def main():
    if not SRC.is_dir():
        raise SystemExit(f"source reports not found: {SRC.resolve()}")
    DST.mkdir(parents=True, exist_ok=True)
    n = 0
    for slug, fname in sorted(SOURCES.items()):
        src = SRC / fname
        if not src.exists():
            print(f"  ! {slug}: missing {fname}")
            continue
        text = src.read_text(encoding="utf-8", errors="replace")
        hits = []
        suppressed = 0
        corrected = 0
        for pat, repl in REDACT:
            text, count = re.subn(pat, repl, text)
            if count:
                hits.append(f"{pat} x{count}")
        for rule in SUPPRESS.get(slug, []):
            find, repl = rule[0], rule[1]
            if len(rule) > 2 and rule[2] == "regex":
                text, count = re.subn(find, repl, text, flags=re.S)
            else:
                count = text.count(find)
                text = text.replace(find, repl)
            if not count:
                raise SystemExit(
                    f"{slug}: suppression rule matched nothing, so the report may "
                    f"have changed underneath it:\n  {find[:90]}")
            suppressed += count
        for find, repl in CORRECTIONS.get(slug, []):
            count = text.count(find)
            if not count:
                raise SystemExit(
                    f"{slug}: correction rule matched nothing, so the report may "
                    f"have changed underneath it:\n  {find[:90]}")
            text = text.replace(find, repl)
            corrected += count
        (DST / f"{slug}.md").write_text(text, encoding="utf-8")
        n += 1
        note = ("  redacted: " + ", ".join(hits)) if hits else ""
        if suppressed:
            note += f"  |  {suppressed} launch-scope passage(s) suppressed"
        if corrected:
            note += f"  |  {corrected} correction(s) applied"
        print(f"  {slug:20} {len(text):>7,} bytes{note}")
    print(f"\nPublished {n} reports to {DST}/")


if __name__ == "__main__":
    main()
