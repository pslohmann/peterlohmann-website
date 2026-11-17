# v1.2 platform data files (data/api-grader-v12/<slug>.json)

One JSON file per platform regraded under methodology v1.2. build-api-grader.py reads
these and builds (1) that platform's row on /api-grader/ and (2) its page at
/api-grader/<slug>.html. A platform with a file here is a v1.2 platform; its old v1.1
entry in RESULTS stays in the script only as history and is no longer shown.

Source of truth: the final report card, `<Platform>-API-Report-Card-<date>.md`, in
`~/Documents/Claude/Projects/API Grader Runs/<Platform>-<date>/2-grading/`.
Every number and mark must come from that report. Never invent a fact.

## House rules for every string
- No em dashes or en dashes anywhere. Use commas, parentheses, colons, or two sentences.
  Ranges use a hyphen: "90-96". Arrows are fine as "&rarr;" in HTML or "->" avoided; prefer words.
- Oxford comma in lists.
- Plain English for a property manager. Short sentences. No jargon without a gloss.
- When something is missing, say "The published documentation shows no ..." (never
  "the API cannot"). It was graded from documentation, not proven impossible.
- Strings are HTML-safe text: escape & as &amp;, use &rsquo; or a plain apostrophe. Inline
  <code>...</code> and <strong>...</strong> are allowed; nothing else.

## Fields

```json
{
  "name": "Column",                         // must match CATEGORIES in build-api-grader.py exactly
  "slug": "column",                         // matches the existing page file name
  "report_file": "/abs/path/to/the/final/report.md",
  "score": 95,                              // published score (after any MCP step)
  "grade": "A",
  "pre_mcp": {"score": 95, "grade": "A"},   // same as published when no MCP step
  "meta": {
    "run": "Nov 17, 2026",
    "method": "1.2",
    "model": "Claude Opus 5.5 (high effort)",
    "tier": "Baseline verified",
    "packet": "COLUMN-EP-2026-11-17-F1",
    "product_type": "Banking/payments"      // the methodology product type the report used
  },
  "gate1": {
    "allows": "A",                          // A | B | C
    "c5_1": "yes", "c5_2": "yes",           // marks
    "read": "2-3 plain-English sentences: what access and cost mean for a PM."
  },
  "gate2": {
    "allows": "A",                          // A | B | C | D
    "coverage_pct": 95.0,                   // capability coverage, one decimal
    "earned": 38.0, "weight": 40,           // checklist weight earned / total
    "write_pct": 100.0,
    "c1_4": "yes",                          // yes | partial | no
    "critical_zero": false,                 // true if any critical item scored 0
    "read": "2-4 plain-English sentences on what the API lets you do and the main gaps."
  },
  "letter": "A",                            // letter from the gates (lower of the two)
  "binding_gate": "none",                   // "none" | "gate1" | "gate2" | "both"
  "placement": {
    "c2": [8.0, 12], "c3": [5.0, 6], "c4": [3.5, 4],   // checks earned, checks applicable
    "share_pct": 75.0,                                   // earned / applicable, one decimal
    "math": "90 + round(6 x 0.75) = 95"                  // as the report states it, "x" not a times sign is fine
  },
  "mcp": {
    "has": false,
    "note": "One plain sentence: what was found (or not) and whether the step applied."
  },
  "reads": {                                // plain-English "what this means for you", per group
    "c2": "2-4 sentences.",
    "c3": "2-4 sentences.",
    "c4": "2-4 sentences."
  },
  "checklist": [                            // every checklist row from the report, in report order
    {"item": "Accounts", "kind": "object", "class": "critical", "weight": 3,
     "state": "present", "score": 1.0,
     "note": "Short plain-English note, 25 words max."}
    // kind: object | workflow | lifecycle ; class: critical | important | optional
    // state: present | partial | absent | alert-only
  ],
  "checks": [                               // all 28 checks, C1.1 ... C5.2, in order
    {"id": "C1.1", "group": 1, "title": "Object coverage", "mark": "100%",
     "why": "1-2 plain-English sentences with the key evidence."},
    {"id": "C2.1", "group": 2, "title": "Modern API conventions", "mark": "yes",
     "why": "..."}
    // group: 1..5 matching the methodology categories.
    // mark: for C1.1-C1.3 a percentage string like "75.0%"; for every other check
    //       one of yes | partial | no | na | unverified.
    // titles: use the methodology's check names (methodology-v1.2.md, Step 2).
  ],
  "runs": {
    "scores": [95, 95, 95],                 // run 1, 2, 3 published scores
    "agreement": "28 of 28 checks unanimous",
    "disagreements": [                      // every disputed check or checklist item, may be []
      {"what": "Checklist item 16, freeze or close an account",
       "runs": "1.0 / 0.5 / 0.5", "resolved": "0.5",
       "why": "One or two plain sentences on the basis.", "score_effect": "none"}
    ],
    "summary": "One or two sentences: how the three runs compared and whether any reading would change the score."
  },
  "sensitivity": "Optional. One sentence if the report flags a near-miss that would change the letter, else \"\".",
  "strengths": ["8-10 short bullets, under 15 words each"],
  "watch": ["8-10 short bullets, under 15 words each, the things that cost a PM work"],
  "bottom": "One paragraph (4-6 sentences), the verdict a property manager should read. Drawn from the report's Bottom line.",
  "provider_fit": "One or two sentences: what the product is and what you still need alongside it."
}
```

Score math (methodology v1.2, used by check_math): letter from the gates (lower wins), then
placement inside the letter's range from share = (c2+c3+c4 earned)/(applicable):
A = 90 + round(6 x share), B = 80 + round(9 x share), C = 70 + round(9 x share),
D = 60 + round(9 x share), rounding half up. An official MCP server then moves the grade
up one step to the bottom of the next step's range (D- 60-62, D 63-66, D+ 67-69, C- 70-72,
C 73-76, C+ 77-79, B- 80-82, B 83-86, B+ 87-89, A- 90-92, A 93-96, A+ 97-100).
Confirm these formulas against methodology-v1.2.md "How scoring works" before relying on them.
