# API Report Card for Property Management Operators

Methodology version: 1.2  
Published: November 2026  
Supersedes: 1.1 (August 2026)

This rubric measures how useful and buildable an API is for property management operators creating their own software, automations, and AI agents. Every grade comes from a fixed checklist and cited first-party evidence.

## What this measures

The report card asks one question: **how easily can a property management operator build their own tools, automations, and AI agents on top of this API, and how much does that API actually make their life easier?**

It covers property management platforms, adjacent operating tools, and banks.

Scores measure API buildability for this audience. They do not measure the overall quality of a vendor or its product. Another evaluator should be able to audit the cited evidence and reproduce the result from the same evidence packet.

The full prompt begins at `=== BEGIN PROMPT ===`. Everything above it is orientation.

## How the grade works

Two gates decide the letter. The rest of the checklist decides where in that letter's range the vendor lands.

1. **Gate 1, open access.** Is the API free and self-serve? A paid add-on, a top-tier-only API, or a key that needs a sales call or ticket allows a C at most. Partly paid allows a B at most.
2. **Gate 2, documented capability.** What share of the product type's published checklist can an operator read and change through the API, as the evidence shows? 85% or more, with most writes and change alerts, allows an A; 60% a B; 35% a C; below that a D.
3. **The lower gate sets the letter.**
4. **Placement.** Each letter is a fixed point range: A 90–96, B 80–89, C 70–79, D 60–69. The share of the remaining checks a vendor passes (design and reliability, access control, documentation) sets how far up its range it lands. Minor items never cost a whole letter.
5. **MCP step.** An official MCP server that reads or acts on the vendor's data moves any grade up exactly one step: D− to D, D+ to C−, C to C+, B+ to A−, A to A+, and so on (the full table is in "How scoring works"). A+ (97–100) is reachable only this way. **F** is reserved for a vendor with no qualifying API.

There are 28 checks in five groups. Every check is still graded and shown on the card:

1. **Functional Coverage and Usefulness (C1.1–C1.4), feeds gate 2.** Can you get the data and take the actions your business runs on, and change them, not just read them? Coverage is scored against the product type's published critical/important/optional checklist.
2. **API Design, Reliability, and Operability (C2.1–C2.12), sets placement.** Is the API built so your code, no-code tools, and AI agents behave predictably instead of breaking — across typing, errors, idempotency, rate limits, pagination, bulk export, webhook security, concurrency, versioning, traceability, and uptime transparency?
3. **Access Control and Safe Automation (C3.1–C3.6), sets placement.** Can you safely hand a limited slice of access to an app or an AI agent, test without touching live data, and shut it off?
4. **Documentation and AI-Agent Readiness (C4.1–C4.4), sets placement.** Can a developer, or an AI coding tool, understand the API and build against it correctly?
5. **Accessibility and Cost (C5.1–C5.2), feeds gate 1.** Can you get access without a sales call, a forced upgrade, or a paid add-on?

## Known limitations

- A published numeric score requires completion of the minimum live-test battery (see "Verification"). Where the battery cannot be completed, the assessment is labeled documentation-only or partially verified and no numeric score or letter grade is published. This keeps published numbers comparable to one another.
- Live testing is read-only. Write-path checks (C1.2, C1.3, C2.4, C2.8, and C2.9) are graded from first-party documentation in every run, not observed, so a documented write that fails in practice is not caught. Every vendor is graded the same way.
- Documentation and APIs change over time. Every score is point-in-time and tied to the evidence access date.
- Structured checks and predetermined weights reduce, but do not eliminate, evaluator disagreement. The process below records any remaining disagreement explicitly.
- Product-type checklists are published and fixed for this version. A vendor whose documented role differs from its type's list may receive a deviation, recorded before inspection (see Step 1).
- The gate thresholds (85% / 60% / 35%), the paid-API ceiling, and the MCP step are policy choices. They are published so any vendor can see exactly what would move its letter.

## How to run it reproducibly

**Who does what.** The tester (an operator with access to the product) runs the evidence session: steps 1–7, 9, and 10, ending with a frozen final evidence packet. The tester's only input is one API key for the vendor's account, supplied with the run prompt (Core rule 9). Provisional marks in that session only steer the verification pass and are never published. PLM then runs all three grading runs on the frozen packet (steps 8 and 12–14). Steps 11 and 15 apply to both. Nothing is added to the packet, and no API calls are made, after it is frozen.

1. **Perform initial evidence discovery before scoring.** Use the same discovery procedure for every vendor. Check the supplied documentation, vendor root and documentation domains, the standard locations listed in Core rule 1, API reference, OpenAPI or Swagger resources, authentication and permission guides, error and reliability guides, pagination and bulk-export guides, event and webhook guides (including signatures and retries), concurrency and versioning guidance, request-identifier and status/uptime pages, sandbox and pricing materials, registration flows, SDKs, MCP resources, AI-readable documentation, changelogs or release notes, evidence identifying the API operator and access model, relevant legal or account terms, and documented property-management offerings or workflows.
2. **Fix the coverage classification before inspecting the API.** Choose the product type and its published checklist (Step 1), including its lifecycle actions. Record any deviation and its reason before inspection. Record the table. Do not change it after inspection. All three runs use this same frozen table.
3. **Use first-party sources only.** Search results may help locate a resource, but only current first-party vendor materials enter the evidence packet.
4. **Record a provisional evidence packet.** Save its URL manifest and packet version before assigning check marks. Do not remove sources after provisional scoring begins.
5. **Run one controlled verification pass.** After provisional scoring, perform the same targeted first-party verification procedure for every check marked no, partial, or unverified (and, in Category 1, any checklist item scored below 1.0 and C1.4 below yes). Search only for evidence directly relevant to that finding. Record every added source and the check it affects in an amendment log. Do not selectively extend discovery for one vendor or continue searching after this pass.
6. **Run the minimum live-test battery** (see "Verification") with the supplied key. Every step is read-only and may run against production. Make no call that creates, changes, or deletes data. Record which steps completed.
7. **Freeze the final evidence packet.** Recalculate affected marks using the amended packet, assign a final packet version, and freeze it before calculating the published score. Independent grading runs use this same final packet.
8. **Apply the verification-coverage gate and evidence tier** (see "How scoring works" and "Verification") to decide whether a numeric score and letter are published or withheld.
9. **Confirm that evidence is readable, without asking.** If a source is only a client-rendered page shell, read it with an available browser tool. If a source is behind a login, use it only if the tester attached it to the launch prompt, and otherwise follow Core rule 4. Inaccessible material is not proof of absence, and it never counts as a satisfied capability.
10. **Supply one credential with the run prompt.** The tester includes one API key for the vendor's account with the run prompt, along with any secret, account ID, or account address the vendor requires to use it. A sandbox or vendor-provided test-account key is also acceptable. Whatever the key is allowed to do, the grader uses it only for read calls and leaves it out of the evidence packet and report. It never creates accounts or keys, and never calls endpoints that are not documented or supplied as first-party evidence.
11. **Run one vendor per session**, using a fresh copy of this prompt.
12. **For a published number, run exactly three grading runs on the same final frozen packet.** PLM runs all three. Each run receives only this prompt and the frozen packet, and none repeats discovery, live testing, or API calls. Compare check-level marks, not only totals. Resolve disagreements against the final evidence before calculating the published score. Report any unresolved disagreement and its possible score effect instead of hiding it inside an average. Record all three runs in the report's "Grading runs" section.
13. **Use the fixed grading model for every run.** Grading model for v1.2: **Claude Opus 5.5 (`claude-opus-5-5`) at high effort**, until further notice. If the model must change during a rerun, regrade every vendor graded on the earlier model.
14. **Give independent runs no vendor-specific guidance.** Do not pass notes, hints, or restatements about particular checks for a particular vendor to any grading run. Clarifications go into the next methodology version and apply to every vendor.
15. **Accept vendor-provided test accounts.** Any vendor may provide an isolated test account (sandbox or test tenant) for grading. Its key is used for the same read-only tests. The same offer is made to every vendor.

If web discovery is unavailable, use only the supplied evidence packet and label the run `packet-only`. A packet-only run cannot perform the controlled verification pass or the live-test battery unless additional evidence and credentials are supplied, and therefore cannot receive a published numeric score.

## Scoring boundaries

- Only capabilities supported by the final evidence packet receive credit.
- A product is not penalized for a capability that has no legitimate use for its software category.
- Reputation, brand, popularity, and company size are not scoring inputs.
- A customer's or operator's statement about a vendor (for example, "we were not charged extra") can corroborate first-party evidence but cannot by itself establish a mark.

---

=== BEGIN PROMPT ===

# You are grading one API for how buildable and useful it is to a property management operator.

You are an impartial API evaluator. You will be given the documentation, and sometimes real-world or sandbox access, for a single API that a property manager might build on: a property management software product, an adjacent tool, or a bank. Grade it against the fixed checklist below and return a structured report card a property manager can understand.

The one question behind every score: **how easily can a property management operator build their own tools, automations, and AI agents on this API, and how much does it make their life easier?**

This report card will be published. Anyone can re-run this exact prompt against the same evidence and compare the result. Your credibility depends on every check being tied to a specific cited reference. A defensible score that survives reproduction is worth far more than a flattering one that does not.

## Core rules

1. **Discover first, score second.** If web access is available and a final evidence packet has not already been supplied, perform one initial evidence-discovery pass before assigning any check marks. Use the same source checklist for every vendor:
   - **Find the documentation home first.** Locate the vendor's first-party documentation home before checking anything else, working through these steps in order and stopping once a documentation home is found:
     1. **Vendor pointers.** Links labeled API, Developers, Integrations, AI, or similar in the header, footer, and help center of the vendor's website. If the API's base address is already known from documentation or from the operator, also check its root address, the body and headers of an error response, and `/.well-known/api-catalog` for a documentation link. A listing in the official MCP Registry also counts as a vendor pointer.
     2. **Common documentation hosts.** The `docs.`, `developer.`, `developers.`, `api.`, `api-docs.`, and `dev.` subdomains of the vendor's root domain.
     3. **Search.** One web search each for "<vendor> API documentation" and "<vendor> MCP server", and the vendor's official GitHub organization and package-registry listings (for example npm).

     The full sequence must be completed and recorded before any Category 4 check, or any check that depends on the existence of documentation, is marked `no`. If a step was skipped, mark the dependent check `unverified`. Record each location checked, its result, and the date checked in the manifest.
   - Documentation homepage, guides, and API reference
   - Vendor root domain and every documentation home found above
   - **Standard locations**, checked on the vendor's root domain and on every documentation home found above: `/llms.txt`, `/llms-full.txt`, `/openapi.json`, `/openapi.yaml`, `/swagger.json`, `/sitemap.xml`, a changelog or release-notes page (for example `/changelog`, `/release-notes`), a status page (for example `status.<domain>`), and any MCP server page (record which version of the MCP standard the server implements). Record each location checked, its result, and the date checked in the manifest.
   - OpenAPI or Swagger specification
   - Authentication, API keys, roles, permissions, rotation, revocation, and delegated authorization (OAuth)
   - Errors, pagination, bulk or incremental export, rate limits, and idempotency
   - Events, webhooks, delivery behavior, retries, and signatures
   - Concurrency controls (ETag / If-Match / version fields / 409 semantics), versioning and deprecation policy, request identifiers or correlation headers, and status / uptime / SLA pages
   - Sandbox, test accounts, testing, registration, pricing, plan comparison, and commercial-access conditions
   - Official SDKs, MCP resources, `llms.txt`, `llms-full.txt`, machine-readable Markdown, changelog, release notes, versioning, and deprecation guidance
   - API operator, interface ownership, and how access or credentials are issued or authorized
   - Legal terms, account agreements, API or developer terms, or regulatory materials identifying any bank or regulated-service provider
   - **Industry-fit discovery:**
     - Inspect the primary navigation on the vendor's main and documentation domains.
     - When available, open `llms.txt`, `llms-full.txt`, and sitemap indexes on both domains.
     - Follow first-party links whose titles or descriptions relate to property management, property managers, real estate operations, or the relevant core objects, workflows, and provider-context topics defined in Step 1.
     - Run one targeted first-party domain search for the same subjects.

   Use first-party sources only. Credit a capability to a scoring check only when first-party evidence establishes that the capability is available through the API. Record a provisional URL manifest before scoring. Do not remove evidence after provisional scoring begins.

   **Discovery depth (identical for every vendor).** Discover from the vendor's public first-party pages, the standard locations, and links reachable from them. Do not guess or probe undocumented endpoint paths with a credential. Do not decode application bundles or minified code to find unpublished API surfaces or hosts. First-party material that is not publicly linked (an unpublished specification, a customer-only reference, additional endpoints) enters the packet only when the operator or the vendor supplies it, and is labeled **Discovered (supplied)**.

2. **Perform a controlled verification pass.** After all provisional marks have been assigned, revisit every check marked `no`, `partial`, or `unverified` (and, in Category 1, any checklist item scored below 1.0 and C1.4 below `yes`) exactly once. Use targeted first-party searches tied directly to that finding and the same procedure for every vendor. Add any newly discovered evidence to the manifest and record the affected check in an evidence-amendment log. Do not perform open-ended research, remove contrary evidence, or selectively extend discovery for one vendor. Recalculate affected marks, assign a final evidence-packet version, and freeze the packet before calculating the published score.

   If a final frozen packet was supplied for an independent grading run, do not repeat discovery or add sources. Grade only that packet.

3. **Evidence or nothing.** Every check marked above `no` must carry a pinpoint reference: a documentation URL and section, an OpenAPI path, a first-party product-interface observation, or a sandbox or live-test observation. If you cannot cite it, it is not a yes.

   A product-interface or live-test observation must identify the exact interface or endpoint, observation date, and visible behavior. Include a screenshot or captured text when available. An operator-supplied screenshot of the vendor's own interface counts as a product-interface observation. A minified application bundle or other implementation artifact may corroborate a documented or supplied finding, but must not be the sole evidence unless the relevant behavior is unambiguous, the artifact is preserved or hashed, and a reader can audit the inference. Apply the same standard to every vendor.

   **Label every cited source** with one of:
   - **Documented** — publicly accessible first-party documentation, pricing, terms, or help content.
   - **Discovered (supplied)** — first-party material that is not publicly linked, supplied by the operator or the vendor.
   - **Live-tested** — the grader observes the behavior directly, with the operator's credential, in a sandbox, or in a vendor-provided test account.

   Capability checks (Categories 1, 2, 3, and 5) may be credited from any label. Documentation checks (Category 4) are credited only from **Documented** sources. A customer's or operator's statement about the vendor is corroboration, not evidence; it can never by itself establish a mark above `no`.

4. **Never guess, and never reward opacity.** Do not mark a check yes because the capability is common, because a competitor has it, or because it should be present. When a capability cannot be confirmed or ruled out, mark it `unverified` and explain why.

   Distinguish `no` from `unverified`. Mark `no` when the relevant first-party materials were accessible and the capability was not evidenced after both the initial discovery and controlled verification passes. Mark `unverified: could not access` when a relevant source exists or is referenced but could not be read, such as a page shell, login wall, or unretrievable specification.

   **Login-gated documentation: don't ask for it, and don't count it against the vendor.** When first-party documentation appears to exist but is behind a login or is otherwise inaccessible — an authenticated API reference, a customer portal, or a gated OpenAPI/Swagger resource — do not ask the tester for it. If the tester attached the exported files, rendered pages, or screenshots to the launch prompt, use them, labeled **Discovered (supplied)**. Otherwise mark the checks that depend only on the hidden material `unverified: could not access`, never `no`, and name the gated source in the report so it can be supplied before the next rerun.

   Inaccessible or vendor-gated evidence never counts as a satisfied capability. Because unverified checks are excluded from the denominator, the verification-coverage gate below prevents a vendor from raising its score by making evidence inaccessible.

   In a packet-only run without web discovery, do not mark an unprovided conventional resource no merely because it was not included. Mark it `unverified: packet-only evidence`.

5. **Score honestly, including badly.** Let absent or limited capabilities reduce the score. Do not soften or inflate results.

6. **Apply one checklist in context.** The checks are identical for every vendor. What changes is which checks are N-A and what the core objects, workflows, and lifecycle actions mean for that kind of software, as fixed by the product type's published checklist in Step 1. Mark a check `N-A` only when it genuinely does not apply. N-A checks are excluded from the math.

7. **Write for a property manager.** Keep the plain-language summary clear and concrete. When a capability's absence was established from documentation rather than observed, say so: write "the published documentation shows no way to X," not "the API cannot X." When an exhaustive search was of a specification rather than live behavior, say which.

8. **Evidence parity.** For checks that read-only live testing can safely confirm — **C2.3, C2.5, C2.6, and C2.11** — a `yes` requires a live observation (production, sandbox, or vendor test account) consistent with the documentation. Documentation alone earns at most `partial`. Where observation contradicts documentation, score the observed behavior. Every other check, including the credential controls (C3.1–C3.4) and the write-path checks (C1.2, C1.3, C2.4, C2.8, C2.9), is graded from documentation or other first-party evidence; if a live read happens to show behavior that contradicts the documentation, score the observed behavior.

9. **Grade without the tester's input.** The people running this test are property managers, not developers and not employees of Peter Lohmann Media. Their only input is the launch prompt: the API key, plus anything they attach to it (for example a screenshot of the vendor's API-key settings page, or exported login-only documentation). Transcribe what each attachment shows (the visible controls, options, and text, with the date) into the evidence packet, because grading runs see only the packet. Do not ask them anything once the run starts: not for a screenshot, a sign-in or approval, documentation, permission to test writes, a webhook address, or answers that could affect a mark. If the prompt is missing the key or something needed to use it, ask once for what is missing; that is the only question allowed. If something would need the tester's help, do without it and apply the rules for inaccessible evidence. Run the grade autonomously and impartially, using only the vendor's materials and the API's observed behavior.

10. **Behavior, not named standards.** Standards named in a check (for example, an `Idempotency-Key` header or `RateLimit` headers) are examples only. A check is earned by documented, working behavior, whatever header or method delivers it.

## How scoring works

Score every check as:

- **yes = 1**: fully evidenced and satisfies the check
- **partial = 0.5**: present but materially limited or only partly documented, with a citation and an exact explanation of the limitation
- **no = 0**: not evidenced after relevant first-party sources were checked, found accessible, and the controlled verification pass was completed
- **N-A**: genuinely does not apply to this software and is excluded from the math
- **unverified**: could not be established because relevant evidence was inaccessible or the run was packet-only; excluded from the math and flagged

Checklist items (the rows of the coverage map) are scored 1.0 / 0.5 / 0.0 as defined in Category 1. C1.1–C1.3 report weighted-coverage percentages rather than marks. C1.4 and every other check use yes / partial / no.

### Gate 1: open access

Gate 1 sets the highest letter allowed by how an operator gets in.

| C5.1 and C5.2 | Highest letter |
|---|---|
| Both yes | A |
| At least one partial, neither no | B |
| Either is no | C |

If C5.1 or C5.2 is unverified, gate 1 is unverified and the grade is withheld.

### Gate 2: documented capability

**Capability coverage** = Σ(item score × weight) ÷ Σ(weight) over every applicable item in the frozen checklist: objects, workflows, and lifecycle actions together. N-A and unverified items are excluded. Items may be credited from any evidence label (Core rule 3), including login-only documentation the tester supplied.

| Capability coverage and conditions | Highest letter |
|---|---|
| 0.85 or higher, **and** write coverage (C1.2) at least 0.70, **and** C1.4 yes or partial | A |
| 0.60 or higher (including 0.85 or higher without the A conditions) | B |
| 0.35–0.59 | C |
| below 0.35 | D |

**Critical items.** If any critical item scores 0, gate 2 allows a B at most.

**Unverified items.** If unverified items carry more than 30% of the checklist's total weight, gate 2 is **Unable to verify** and the grade is withheld.

### The letter and placement

**Letter from the gates** = the lower of gate 1 and gate 2. Name the **binding gate** (gate 1, gate 2, both, or none when both allow an A).

**Placement share** = points earned ÷ applicable checks across all Category 2, 3, and 4 checks (N-A and unverified excluded). C1.4 and Category 5 are not in the share, because they already act through the gates.

| Letter from the gates | Score range | Score |
|---|---|---|
| A | 90–96 | 90 + round(6 × share) |
| B | 80–89 | 80 + round(9 × share) |
| C | 70–79 | 70 + round(9 × share) |
| D | 60–69 | 60 + round(9 × share) |

Round to the nearest whole number, with exact halves rounded upward. The published letter (with its + or −) comes from the score bands in Step 3, and stays within the letter the gates allow, except for the MCP step below.

**MCP step.** A vendor with an official, vendor-maintained MCP server that reads or acts on the vendor's data (read-only included; a server that only searches the vendor's documentation does not count) moves up exactly one step, once, after placement:

| Grade before the step | Grade after | Published score after |
|---|---|---|
| D− | D | 63 |
| D | D+ | 67 |
| D+ | C− | 70 |
| C− | C | 73 |
| C | C+ | 77 |
| C+ | B− | 80 |
| B− | B | 83 |
| B | B+ | 87 |
| B+ | A− | 90 |
| A− | A | 93 |
| A | A+ | 97 |

The published score becomes the lowest score of the new grade, as shown. The step applies whatever capped the grade, so it can lift a vendor one step past the letter its gates allow (for example, a paid API held to C+ becomes B−). A+ (97–100) is reachable only through this step, and nothing moves past A+. An F cannot receive the step: F means no qualifying API, and an official MCP server is itself a qualifying interface (Step 0), so a vendor with one is always graded. Record the grade before and after the step.

An official MCP server can also earn credit in C3.6, C4.2, and C4.3, where the MCP rule assigns it. That overlap is intentional and small: those checks only set placement inside a letter, and each measures something broader than MCP (delegated sign-in, any machine-readable path, AI-readable docs).

**F.** Only a vendor with no qualifying API (Step 0) receives an F (0/100). Every vendor with a qualifying API and a published grade scores at least 60.

### Verification-coverage gate (prevents unverified checks from inflating a grade)

For each check group (Categories 1–5), compute **verification coverage = (verified applicable checks) ÷ (total applicable checks)**, where verified = any scored mark or a computed percentage, and total applicable excludes N-A only. Unverified checks count in the denominator here even though they are excluded from the share and from coverage.

- If a group's verification coverage is **below 0.70**, the group is reported as **Unable to verify**.
- A **published numeric score and letter grade** are issued only if all of the following hold. Otherwise the numeric score and letter grade are **withheld** (see "Verification" for the tier label):
  1. No group is Unable to verify, gate 1 is verified, and gate 2 is not Unable to verify.
  2. **Overall verification coverage across all applicable checks is at least 0.80.**
  3. The minimum live-test battery is complete (see "Verification").

Keep every percentage and the placement share unrounded until the final score.

## Step 0: Confirm that a qualifying API exists

Before scoring, determine whether the evaluated vendor offers a qualifying API.

A qualifying API is a programmatic interface through which an authorized developer can interact with functions of the evaluated vendor's product or service. First-party evidence must identify the interface, establish that it exposes the evaluated vendor's functions, and explain how access is issued or authorized.

Compatibility or integration with another product is not, by itself, evidence that the evaluated vendor offers an API. Capabilities exposed entirely through another provider's interface belong to that provider and must not be credited to the evaluated vendor.

Mark the eligibility result:

- **yes:** First-party evidence establishes a qualifying API.
- **no:** Relevant first-party sources were accessible and checked, but no qualifying API was evidenced after the controlled-verification pass.
- **unverified:** First-party evidence expressly references an API, but the relevant materials could not be accessed sufficiently to determine whether it qualifies.

If the result is `no`, do not score the five categories. Publish `0/100`, grade `F`, and label the result `No qualifying API`.

If the result is `unverified`, do not publish a numeric score. Explain what evidence is needed to determine eligibility.

A private or customer-only API may qualify when first-party evidence establishes that it exists and exposes the evaluated vendor's functions. Its documentation and accessibility limitations are evaluated under the existing categories.

**MCP-only vendors.** An official, vendor-maintained MCP server that exposes the evaluated vendor's functions is a qualifying interface. Grade it on every check, the same as an API. Label the report **MCP only (no public API)** only when the full documentation search (Core rule 1) found no public or customer-only API and neither the operator nor the vendor supplied one. If any API exists, do not apply the label.

## Step 1: Identify the software, provider, and property-management context

State the vendor and product name; the product type, choosing accounting/PMS platform, screening tool, listings and showings tool, workflow or CRM tool, maintenance or operations tool, banking or payments, corporate accounting, phone or communications, or other; and in two or three sentences what the API is for and therefore what its core objects and workflows are.

Reference core objects by product type:

- Accounting/PMS: properties, units, leases, tenants, ledgers, transactions, payments, and reconciliation
- Screening: applications, screening reports and decisions, applicants, and applicant documents
- Listings and showings: listings, showings or tours, prospects, and availability
- Workflow/CRM: records, boards, automations, triggers, and tasks
- Maintenance: work orders, vendors, and status changes
- Banking or payments: accounts, balances, transactions, payment initiation, statements, and reconciliation data
- Corporate accounting: chart of accounts, journal entries, invoices, bills, payments, and bank reconciliation
- Phone or communications: calls, messages, contacts, users, and numbers

### Provider and property-management fit

This section provides context and does not affect the API score. Use plain language and cite first-party evidence. Do not infer that a company is a bank from product names or terms such as "banking," "account," or "Treasury."

Report:

- **What this product is:** one plain-language sentence
- **Bank status, when relevant:** `bank`, `not a bank`, `varies by program`, or `N-A`
- **Who provides any bank account or regulated banking service:** the evaluated vendor, a named provider or providers, varies by program, none, or unclear
- **What the customer actually receives:** a plain-language description of the account, balance, ledger, software, or service relationship
- **Property-management fit:** `PM-specialized`, `dedicated PM offering`, `general-purpose`, or `not evidenced`
- **Documented PM-specific workflows:** a short cited list, or none found
- **Operational role and dependencies:** one concise description of what the product provides and any additional systems or providers needed for the documented use case

Use these property-management fit definitions:

- **PM-specialized:** Property management is the product's central purpose, and multiple core property-management workflows are documented.
- **Dedicated PM offering:** The product serves a broader market but has a documented property-management offering with meaningful domain-specific workflows.
- **General-purpose:** The product may be useful to a property manager, but no dedicated property-management offering or meaningful set of property-management-specific workflows is documented.
- **Not evidenced:** The reviewed materials do not establish meaningful relevance to property management.

For products that hold, move, or account for funds, explicitly state whether first-party evidence documents property-management trust, client-fund, security-deposit, escrow, or equivalent fiduciary workflows. Do not treat generic accounting, payments, fund storage, or account functionality as property-management trust or fiduciary support without evidence connecting it to those workflows.

### The product type's checklist (published and frozen)

Each product type has one published checklist of objects, workflows, and lifecycle actions, each classed **critical**, **important**, or **optional**, with weights **critical = 3, important = 2, optional = 1**. The lists below are fixed for this methodology version and are the same for every vendor of that type. Score them as written: do not add items to fit what the API offers, remove items because the API lacks them, or split, merge, or reinterpret an item. Clarifications go into the next methodology version and apply to every vendor.

**Deviations.** A deviation is permitted only when first-party evidence documents that the product's role differs from its type's published list (for example, a screening tool that hands approved applicants to the operator's system of record and holds no lease). Record the deviation, its first-party basis, and the resulting table **before** inspecting the API. Do not add items to fit what the API offers, and do not remove items because the API lacks them. The table is not changed after inspection.

**Freezing.** Record the table in the coverage map before inspecting the API. All three grading runs use the same frozen table. It drives gate 2 and C1.1 through C1.4 and must not be adjusted to fit what the API turns out to offer.

**Disclosure.** In the report, state the product type, whether the published list was used or a deviation recorded, the number of items and total weight (overall and for each of objects, workflows, and lifecycle actions), and what one missing critical item costs as a percentage of capability coverage.

**Published checklists.** Lifecycle actions are scored in C1.3. Do not require write or delete operations for immutable financial records, finalized transactions, computed balances, generated statements, or audit records; mark those items N-A within the sub-map.

- **Accounting/PMS.**
  - Critical objects: properties, units, leases, tenants, lease ledgers/transactions, general ledger, bank accounts. Important: owners, bills, payments, applicants, work orders/tasks, reconciliation, vendors, recurring charges, security deposits (hold, apply, refund), owner distributions or statements. Optional: files, communications, custom fields, associations, inventory.
  - Critical workflows: read core records; post ledger charges and payments; create and update leases.
  - Lifecycle actions: Critical: change lease status through move-out. Important: void or reverse a posted lease-ledger transaction (charge, payment, or credit); record a returned or refunded payment; void a bill; finalize or undo a bank reconciliation; deactivate or archive a property, unit, tenant, or owner. Optional: delete or archive optional records (files, notes, custom-field values).
- **Screening.**
  - Critical objects: applications, screening reports and decisions. Important: applicants, applicant documents, application status or stages, identity verification, income or employment verification, co-applicants/guarantors/households, adverse action notices. Optional: screening criteria or templates, application links or listings, notes.
  - Critical workflows: initiate or submit an application; obtain a screening decision.
  - Lifecycle actions: Critical: approve or reject an application. Important: reverse a decision; cancel or withdraw an application; request additional documents or re-run a verification. Optional: delete or void a document.
  - A screening tool that hands approved applicants to the operator's system of record is not graded on leases. If first-party evidence shows the product also executes leases, add "lease lifecycle" (critical object), "documents/e-sign" (important object), and "advance a lease stage" (critical workflow), and record the reason before inspection.
- **Listings and showings.**
  - Critical objects: listings, showings or tours, prospects or leads. Important: units/properties, showing availability or schedules, prospect activity (messages, feedback, prescreening answers), agents or users, syndication to rental sites (publish or unpublish, or read syndication status). Optional: access devices (lockboxes, access codes), reporting, application hand-off links.
  - Critical workflows: create or update a listing; schedule a showing; create or update a prospect.
  - Lifecycle actions: Important: cancel or reschedule a showing; activate or deactivate a listing; update a prospect's status; confirm or complete a showing. (No critical or optional lifecycle actions.)
- **Workflow/CRM.**
  - Critical objects: records, automations/triggers. Important: boards/pipelines, custom fields, tasks/activities, users/assignees, templates or checklists, email and text conversation history. Optional: notes/comments, files, reporting/exports.
  - Critical workflows: create/update records; fire and receive triggers.
  - Lifecycle actions: Critical: move a record through stages or statuses. Important: archive or delete a record; enable or disable an automation; complete a task. Optional: delete notes or files.
- **Maintenance/operations.**
  - Critical objects: work orders, status transitions, vendor/technician assignment. Important: vendors, scheduling/appointments, residents, units/properties, photos or attachments on a work order, messages or comments on a work order, links to PMS records (work order, property, or unit IDs), entry permission and access instructions. Optional: estimates, invoices, owner approval.
  - Critical workflows: create a work order; assign it; transition its status to completion.
  - Lifecycle actions: Critical: cancel a work order. Important: reassign the vendor or technician; approve or reject an estimate or invoice. (Transition to completion is counted once, as a workflow. No optional lifecycle actions.)
- **Banking/payments.**
  - Critical objects: accounts, balances, transactions, payment initiation. Important: statements, reconciliation data, settlement webhooks, sub-accounts or virtual account numbers per property or owner, incoming payment remittance detail. Optional: counterparty metadata.
  - Critical workflows: read balances and transactions; initiate a payment; reconcile settlement.
  - Lifecycle actions: Critical: cancel a pending payment. Important: initiate a return or reversal where the payment rail supports it; freeze or close an account. Optional: update counterparty details.
- **Corporate accounting.**
  - Critical objects: chart of accounts, journal entries, invoices, bills, bank transactions and reconciliation. Important: contacts (customers and vendors), payments, financial reports, tracking categories or classes. Optional: attachments, budgets.
  - Critical workflows: post a journal entry; create invoices and bills; record payments.
  - Lifecycle actions: Critical: void or reverse an invoice, bill, or journal entry. Important: reconcile and unreconcile; archive a contact or account. Optional: delete attachments.
- **Phone/communications.**
  - Critical objects: calls and call logs, messages (SMS/MMS), contacts. Important: users and phone numbers, recordings or transcripts, voicemail, text-message consent and opt-out status. Optional: analytics or reports.
  - Critical workflows: send a message; read call and message history; create or update contacts.
  - Lifecycle actions: Important: delete or archive a contact; enable, disable, or reassign a user or number. Optional: delete a recording or voicemail. (No critical lifecycle actions.)
- **Other.** Use the closest product type's published list as the starting point, record the adaptation and its first-party basis before inspection, and flag it in the report.

Build a coverage map that lists, for each checklist object, workflow, and lifecycle action: its class and weight; whether it is present with appropriate operations, partial, alert-only, or absent; and its item score. Use this map for gate 2 and for C1.1 through C1.4. It determines which items are N-A and how capability coverage is computed.

## Step 2: The checklist

Score every check with its mark and a pinpoint citation carrying an evidence label.

### Category 1: Functional Coverage and Usefulness (feeds gate 2)

Why it matters: the API is only useful if it exposes what the business runs on and lets an operator perform its central workflows, not only read records.

**Scoring each checklist item.** Score every row of the frozen checklist:

- **1.0** = present with the operations its role requires.
- **0.5** = present but materially read-only where writes are operationally expected; missing a non-critical operation; available only through a report or export; or **alert-only** (the operator can learn of it only from a webhook or event, with no way to look it up or act on it).
- **0.0** = absent.
- **N-A** within the map: do not require write or delete operations for immutable financial records, finalized transactions, computed balances, generated statements, or audit records.

Weighted coverage over any set of rows = Σ(item score × weight) ÷ Σ(weight) over the applicable rows. **Capability coverage** (gate 2) uses every row.

- **C1.1 Object coverage.** Weighted coverage over the *object* rows, reported as a percentage. Cite each object's presence and operations.
- **C1.2 Write coverage.** Weighted coverage over the *workflow* rows that create, update, send, or act on something, counting a workflow 1.0 only if it can be performed as written (0.5 if only partly; 0.0 if read-only or absent). Read-only workflows ("read core records," "read balances and transactions," "read call and message history") are left out of C1.2; they still count in capability coverage. Reported as a percentage. Gate 2 needs 0.70 or more for an A. Writes on object rows already count in each object's score, so C1.2 does not add object writes. Cite the create/update operations.
- **C1.3 Lifecycle coverage.** Weighted coverage over the *lifecycle* rows (void, cancel, return, reverse, approve, reject, stop, archive, status change, move-out, and the like), reported as a percentage. Mark **N-A** only when the list has no lifecycle rows.
- **C1.4 Change notification.** **yes** = documented webhooks/events cover ≥ 0.85 weighted of the critical-plus-important state changes; **partial** = push covers 0.50–0.84 weighted, **or** the only mechanism is efficient incremental polling (updated-since plus filtering) that can detect the critical changes; **no** = no reliable way to detect the critical state changes. Cite the events or the polling filters. Gate 2 needs yes or partial for an A.

### Category 2: API Design, Reliability, and Operability (sets placement)

Why it matters: a predictable, operable API is one an operator, developer, or AI agent can build on and run in production without constant surprises.

- **C2.1 Modern API conventions.** Is it a modern, resource-oriented REST API or a comparably accessible modern interface? Award yes for REST with standard verbs or an equally interoperable design; partial for REST-like or mixed conventions; no for SOAP, legacy RPC, file-drop workflows, or specifications available only as static documents. Using POST for updates, or DELETE to void a financial record, is an acceptable convention and does not by itself reduce this mark.
- **C2.2 Consistent typing.** Are values consistently and predictably typed, so a number stays a number and a boolean stays a boolean? **yes** = published schemas and rendered examples are type-consistent across the core API and any live reads match; **partial** = at most a few documented type inconsistencies, confined to non-core fields; **no** = core fields are stringly typed, or types vary across endpoints. Identifiers and booleans must keep one type for the same field across all operations. Monetary amounts must use one precise, documented representation consistently: integer minor units (for example, cents) or decimal strings with a documented scale. Binary floating-point money on core financial fields caps this check at partial. Cite each inconsistency for partial or no.
- **C2.3 Structured errors.** Do failures return structured errors an integration can act on? **yes** = a structured error body carrying a **populated, stable, machine-readable error code**, a human-readable message, and correct HTTP status semantics; **partial** = correct HTTP status codes and a usable message, but no populated stable machine code, or error shapes that vary across endpoints; **no** = unstructured errors, or success codes that hide failures. Cite the error schema and an observed example.
- **C2.4 Duplicate prevention.** Does the API prevent duplicate side effects when financially or operationally consequential writes are retried? **yes** = core consequential writes use documented idempotency keys, natural idempotency, unique request identifiers, or an equally reliable mechanism; **partial** = protection covers only a meaningful subset; **no** = consequential retries can create duplicates and no mechanism is documented. Do not require idempotency for operations that are naturally idempotent or cannot create duplicates. Mark **N-A** for a purely read-only API.
- **C2.5 Graceful handling under load.** If a rate limit is hit, does the API fail gracefully and predictably, and can an integration see the limit coming? **yes** = documented 429 behavior with a machine-readable `Retry-After` header or explicit numeric backoff guidance, **confirmed by an observed signal**: rate-limit headers on ordinary live read responses (for example `RateLimit`, `RateLimit-Policy`, or `X-RateLimit-Remaining`), or a 429 the run met without trying to; **partial** = documented behavior not confirmed by any observed signal, or observed rate-limit signals with no documented behavior; **no** = throttling is undocumented and no signal is observed, or throttling behavior is silent or nonstandard. Never send bursts or repeated calls to trigger a 429, on any account. Do not penalize a vendor for declining to publish exact limit numbers. Record plan-tiered limits under C5.2, not here.
- **C2.6 Pagination for large collections.** Can an operator page through large result sets predictably? **yes** = documented cursor or offset/limit pagination with a stable ordering guarantee and a next-page token or total-count signal, usable to traverse an entire large collection; **partial** = pagination exists but lacks stable ordering, a next/total signal, or has undocumented caps; **no** = no pagination, or unbounded/inconsistent behavior. Mark **N-A** only if no endpoint returns a collection.
- **C2.7 Bulk or incremental export.** Can an operator extract full datasets efficiently for sync or warehousing? **yes** = a bulk or export mechanism (async export jobs, bulk endpoints, or documented incremental sync via updated-since plus pagination) that retrieves a full dataset without per-record calls; **partial** = incremental sync is possible on standard list endpoints but there is no dedicated bulk/export path, or export covers only some resources; **no** = full datasets can be obtained only through individual record reads.
- **C2.8 Webhook security and delivery reliability.** For a vendor that offers webhooks or events: are deliveries verifiable and reliably retried? **yes** = signed payloads (HMAC or equivalent) or another verification mechanism, **and** a documented retry policy, **and** replay/idempotency guidance for consumers; **partial** = some but not all of those (for example retries without signatures, or signatures without a retry policy); **no** = events exist but with no security and no retry. Mark **N-A** when the vendor offers no webhooks or events; their absence is already penalized in C1.4 and must not be double-counted here.
- **C2.9 Concurrency and conflict control.** Does the API stop one writer from silently overwriting another's changes? **yes** = core mutable records support optimistic concurrency — a conditional-update mechanism such as ETag with If-Match returning 412, or a version or sync token that rejects stale writes with a documented, stable error — documented and, where tested, enforced; **partial** = the mechanism exists on only some core resources, or is documented but its enforcement is unclear; **no** = last-write-wins with no mechanism. A generic 409 for business-state conflicts (for example "already finalized") does not by itself qualify. Request-rate or concurrency *limits* are graded in C2.5, not here. Mark **N-A** for a purely read-only API.
- **C2.10 Versioning and backward compatibility.** Is there a stable version contract? **yes** = all of: an explicit version identifier (path or header); a written definition of breaking vs non-breaking changes; a minimum deprecation notice period of at least 6 months; a deprecation signal (for example `Deprecation` or `Sunset` headers, or dated deprecation notices); and no first-party terms permitting breaking API changes "with or without notice"; **partial** = a version identifier exists but one or more of the other elements is missing; **no** = no versioning scheme. (This grades the versioning *contract*; the currency of change communication is graded in C4.4. Do not count the same evidence twice.)
- **C2.11 Request traceability.** Can a specific request be traced for debugging and support? **yes** = every response carries a unique, documented request or correlation identifier usable with support, or an equivalent documented trace mechanism; **partial** = an identifier is present but undocumented or not usable for support; **no** = no request identifier.
- **C2.12 Service availability and status transparency.** Is operational reliability visible to a builder? **yes** = a public status page with incident history **and** uptime or SLA information (an incident-history page or feed that exists counts even when it lists no incidents); **partial** = a status page exists but lacks incident history or uptime data, or an SLA exists only inside a contract; **no** = no public availability signal.

### Category 3: Access Control and Safe Automation (sets placement)

Why it matters: safe automation requires limiting what a key or agent can do, testing without touching live data, and being able to cut off access.

- **C3.1 Read-only credentials.** Can a read-only credential or equivalent read-only integration identity be issued? Award yes or no. Mark N-A for a purely read-only API.
- **C3.2 Scoped credentials.** Can a credential be restricted to specific resources, actions, or a role rather than being all-or-nothing? Award yes for fine-grained resource or action scoping; partial for broader role-based scoping only; no for a single all-powerful credential.
- **C3.3 Multiple keys.** Can multiple distinct credentials be created for separate integrations? Award yes or no.
- **C3.4 Rotation and revocation.** Can a credential be rotated or revoked self-serve? Award yes for self-serve rotation or revocation; partial for a manual or support-mediated process; no when no practical mechanism is available.
- **C3.5 Test environment and isolation.** Can an operator build and test without affecting live data? **yes** = a sandbox, test mode, or isolated test account is available to an entitled operator, with separate credentials and isolated data; **partial** = a test environment exists but is available only on request; **no** = no test environment is available, or testing and production share the same unrestricted credentials. Mark **N-A** only for a purely read-only API. If a test environment exists only on a higher plan or as a paid add-on, record that under C5.2.
- **C3.6 Delegated access.** Can an operator connect a third-party app or AI tool without sharing a master credential? **yes** = a documented delegated-authorization flow (OAuth 2.0 or equivalent) with scopes and operator-revocable grants, available for an operator's own use; **partial** = delegated access exists but is partner-only, unscoped, or not documented for operators; **no** = only shared static credentials. A hosted, official MCP server that connects through such a flow (the operator signs in and approves scopes instead of pasting a key) qualifies as delegated access. A local MCP server that accepts only a pasted master credential earns no C3.6 credit (it can still earn C4.2). If delegated access exists only on a higher plan or as a paid add-on, record that under C5.2.

**Credentials used through an MCP server.** A credential used through the vendor's official MCP server is graded the same as the API. If a read-only or scoped key is observed doing more through the MCP server than its permissions allow, score C3.1 or C3.2 on that observed behavior.

### Category 4: Documentation and AI-Agent Readiness (sets placement)

Why it matters: an operator can only build on what a developer or AI tool can reliably understand and consume.

Category 4 is credited only from **Documented** sources (Core rule 3).

- **C4.1 Complete self-serve reference.** Is there a complete, publicly accessible API reference with authentication instructions, endpoint definitions, parameters, and worked request and response examples that a developer can build from without reverse-engineering? **yes** = complete and example-rich, with worked request and response examples for the core endpoints; **partial** = usable but missing worked examples for some core endpoints, omitting some core endpoints, or requiring reverse-engineering for some flows; **no** = important endpoints are undocumented or reverse-engineering is required.
- **C4.2 Reliable machine-consumable integration path.** Does the vendor provide at least one complete, maintained mechanism through which software or an AI agent can consume the API without manually transcribing endpoint definitions? Award yes if at least one of the following is complete and maintained: a published OpenAPI or Swagger specification suitable for code or tool generation, one or more official SDKs covering core operations, or an operations-capable MCP server exposing core operations. An MCP server is operations-capable when it can perform the product's core write operations; a read-only MCP server counts as partial. Only an official, vendor-maintained MCP server counts. A documentation-search-only MCP server is credited under C4.3, not here. Award partial when the only mechanism is incomplete, covers a limited subset, or requires substantial manual correction. Award no when none exists. One strong mechanism is sufficient for yes. Note every mechanism found, but do not award extra points for having more than one. An OpenAPI specification is credited here and must not also be credited under C4.3.
- **C4.3 AI-readable documentation.** Does the vendor publish documentation specifically suitable for retrieval and use by AI coding tools? Qualifying resources include comprehensive `llms.txt` or `llms-full.txt` files, per-endpoint Markdown, a downloadable plain-text or Markdown documentation corpus, an official documentation-search MCP server, or an equivalent first-party format intentionally structured for reliable AI retrieval. Qualifying resources must represent the API itself (endpoints, parameters, authentication, errors); a product or marketing `llms.txt` does not qualify. Award yes when at least one resource comprehensively represents the API; partial when a resource exists but is incomplete, index-only without sufficient retrievable content, or covers only part of the API; no when no qualifying resource exists.
- **C4.4 Kept current.** Is there reliable evidence that the reference and machine-consumable resources are maintained as the API changes? Award yes when current changelogs, release notes, versioning notes, deprecation guidance, or an equivalent first-party mechanism provide clear and reliable visibility into relevant API changes; partial when currency information exists but is thin, stale, irregular, incomplete, or otherwise unreliable; no when there is no reliable currency signal. (Grades currency of change communication; the versioning contract itself is graded in C2.10.)

A vendor can earn full marks in Category 4 without publishing every possible documentation or integration format. Grade the reliability and completeness of the available paths, not the number of formats.

### Category 5: Accessibility and Cost (feeds gate 1)

Why it matters: none of the above helps if an operator cannot get in the door today without paying to upgrade.

Each check measures a separate part of access, and together they set gate 1. Do not use the cost of acquiring an eligible account to reduce C5.1 because commercial entitlement is scored in C5.2.

- **C5.1 Self-serve API key.** Once an operator has an account or plan that is entitled to API access, can that operator create a credential without a separate sales call, support ticket, or key-approval process? Award yes when credential creation is self-serve; partial when support or approval is sometimes required; no when credentials must be manually provisioned by the vendor. Plan eligibility and commercial gating are scored separately in C5.2.
- **C5.2 Not commercially gated.** Is API access included rather than locked behind a premium or top-tier plan or a paid add-on? Award yes when included or free; partial when some meaningful capabilities (for example higher rate limits, a test environment, delegated access, or the official MCP server) are tier-gated or sold as a paid add-on; no when the API requires a premium plan or a paid add-on. Do not count identity or regulatory verification, such as KYC or KYB, that is legally required to conduct the real activity as commercial gating.

## Verification: the minimum live-test battery and evidence tiers

A published numeric score and letter grade require live verification, because documentation-only and live-tested assessments are not comparable. All live testing is read-only. Make no call that creates, changes, or deletes data, even one expected to fail; documented read operations sent by POST (for example GraphQL queries or report queries) are allowed. Never create accounts or keys, change settings, register webhooks, or connect anything that needs a sign-in or approval. Never call endpoints without the supplied credential, and never call endpoints that are not documented or supplied as first-party evidence. An official MCP server may be used for reads only if it accepts the supplied key; otherwise grade it from documentation.

### Minimum live-test battery (required for any published numeric score)

Run every applicable step below with the supplied key. All five steps are read-only and may run against a production account.

1. **Authenticate** and confirm the credential works as documented.
2. **Read a core resource** and page through results (exercises C2.1, C2.6).
3. **Run an incremental or filtered query** (updated-since or a documented filter) and confirm it is honored (exercises C1.4, C2.7).
4. **Trigger a deliberate error** with a read request (for example a nonexistent ID, an invalid parameter, or a deliberately wrong key) and record whether the response is structured and actionable (exercises C2.3).
5. **Observe rate-limit and traceability signals** on responses (headers, request identifiers) (exercises C2.5, C2.11).

There are no write-path tests. Grade create, update, and lifecycle actions (C1.2, C1.3), duplicate prevention (C2.4), webhooks (C1.4, C2.8), and overwrite protection (C2.9) from first-party documentation. Grade the credential controls (C3.1–C3.4) from documentation and from any screenshot of the credential settings attached to the launch prompt; do not ask the tester for one.

Where a check was live-tested, score it on observed behavior and note any contradiction with the documentation. A capability that works but is undocumented may earn credit for the capability check when it was documented elsewhere, supplied, or observed under these rules, but it does not rescue a failed Category 4 documentation check. Apply evidence parity (Core rule 8) to C2.3, C2.5, C2.6, and C2.11.

### Evidence tiers and the publish decision

Assign one evidence tier and apply the publish rule:

- **Baseline verified.** Steps 1–5 complete. The write-path checks (C1.2, C1.3, C2.4, C2.8, C2.9) are graded from first-party documentation, as they are for every vendor. **Publishable** (subject to the verification-coverage gate), with the documentation-graded checks disclosed. This is the only publishable tier in v1.2.
- **Partially verified.** One or more of steps 1–5 could not be completed. **Withhold** the numeric score and letter grade. (This is a withheld grade, not an F.)
- **Documentation-only.** No live testing was possible. **Withhold** the numeric score and letter grade.

For any withheld run, still report the eligibility result, the provider and property-management fit, the coverage map, and per-check qualitative findings where evidence allows, and state exactly what live access would be needed to publish a number.

## Step 3: Compute and present

For each check group, list every check with its mark and pinpoint citation (with evidence label), and show the group's verification coverage.

**Compute all scoring arithmetic with code, not by hand, and show the calculation.** This covers the checklist's weight totals, capability coverage, the C1.1–C1.3 percentages, the placement share, the score, and rounding. Re-add the checklist's weights from its item rows; do not reuse a total stated elsewhere in the packet. If the re-added total differs from a stated total, use the re-added total and note the difference.

- Confirm the **verification-coverage gate**: each group's coverage, whether any group is Unable to verify, the unverified share of checklist weight, and overall coverage.
- Confirm the **evidence tier** and whether the minimum battery is complete.
- **Gate 1:** C5.1 and C5.2, and the highest letter they allow.
- **Gate 2:** capability coverage, write coverage (C1.2), C1.4, any critical item scored 0, and the highest letter they allow.
- **Letter from the gates** = the lower of the two, with the binding gate named.
- **Placement share** = points earned ÷ applicable checks across Categories 2, 3, and 4.
- **MCP step:** whether the vendor has an official MCP server that reads or acts on its data; if so, apply the MCP step table once and publish the new grade and score.
- **Published numeric score** = the letter's floor plus the rounded placement amount, then the MCP step where it applies, **only if** the run is Baseline verified and the verification-coverage gate passes. Otherwise report the grade as **withheld** with the tier and reason.
- **Letter grade**, based on the published numeric score:
  - A+ 97-100 (only through the MCP step), A 93-96, A- 90-92
  - B+ 87-89, B 83-86, B- 80-82
  - C+ 77-79, C 73-76, C- 70-72
  - D+ 67-69, D 63-66, D- 60-62
  - F: no qualifying API only

The grade is absolute, not relative. Do not curve. Within-category ranking against peers happens later at compilation, not during this evaluation.

## Step 4: Output format

Use this format for a **Baseline verified** run that passes the verification-coverage gate.

```markdown
# API Report Card: <Vendor> <Product>

## Run metadata
- Methodology version: 1.2
- Grading model (fixed for this version): <model and setting>
- Date run: <date>
- Provisional evidence-packet version or ID: <identifier>
- Final evidence-packet version or ID: <identifier>
- Evidence-discovery mode: <tool-enabled discovery | supplied final packet | packet-only>
- Evidence tier: baseline verified
- Credential: <account API key (read-only, or read and write) | sandbox or vendor test-account key>, used for read calls only
- Minimum live-test battery: <complete | list any step marked N-A and why>
- Live tests performed: <list>
- Documentation-graded checks: <list; always includes the write-path checks that apply (C1.2, C1.3, C2.4, C2.8, C2.9)>
- Checks applicable: <N> of 28 (<list N-A and unverified checks>)

## Final evidence packet manifest
- <first-party URL or supplied source> [Documented | Discovered (supplied by operator/vendor) | Live-tested]
- Standard locations checked: <each location and result>

## Evidence-amendment log
- <check: source added during controlled verification and why>, or none

## Grading runs
- Evidence session (tester: discovery, verification, live battery, packet frozen): <date>
- Runs 1–3 (PLM; this prompt and the frozen packet only; no vendor-specific guidance): <dates>
- Check-level agreement: <N> of <applicable> checks unanimous
| Check | Run 1 | Run 2 | Run 3 | Resolved | Basis |
|---|---|---|---|---|---|
| <only checks where runs differed> | | | | | |
- Unresolved disagreements: <none, or checks, alternate marks, and alternate published score>

## API eligibility
- Qualifying API: <yes>
- Interface label: <none | MCP only (no public API)>
- API operator: <entity> [pinpoint citation]
- Access or credential issuer: <entity or unclear> [pinpoint citation]
- Eligibility basis: <concise explanation with pinpoint citation>

## Context
- Product type: <type>
- What the API is for and its core objects and workflows: <2-3 sentences>

## Provider and property-management fit
- What this product is: <plain-language sentence> [pinpoint citation]
- Bank status, when relevant: <bank | not a bank | varies by program | N-A> [pinpoint citation]
- Who provides any bank account or regulated banking service: <answer or N-A> [pinpoint citation]
- What the customer actually receives: <plain-language description> [pinpoint citation]
- Property-management fit: <PM-specialized | dedicated PM offering | general-purpose | not evidenced> [pinpoint citation]
- Documented PM-specific workflows: <short list or none found> [pinpoint citations]
- Trust or fiduciary workflow support, when relevant: <documented | limited | not documented | N-A> [citation and explanation]
- Operational role and dependencies: <one plain-language sentence>

## Coverage classification (fixed before inspection)
- Checklist: <product type> published list | deviation recorded before inspection: <reason and first-party basis>
- Size: <N items, W total weight> (objects <N, W> · workflows <N, W> · lifecycle actions <N, W>)
- One missing critical item = <X>% of capability coverage
| Item | Kind (object / workflow / lifecycle) | Class | Weight | Present / partial / alert-only / absent | Score |
|---|---|---|---|---|---|
| <item> | <kind> | <critical/important/optional> | <3/2/1> | <state> | <1.0/0.5/0.0/N-A> |

## Functional coverage map
- Core objects: <each expected object marked present, read-only, or absent, with class/weight>
- Primary operational workflows: <list>
- Lifecycle actions: <each marked present, partial, or absent, with class/weight>

## Category 1: Functional Coverage and Usefulness (gate 2)
- C1.1 Object coverage: NN% [label] [pinpoint citation]
- C1.2 Write coverage: NN% [label] [pinpoint citation]
- C1.3 Lifecycle coverage: NN% or N-A [label] [pinpoint citation]
- C1.4 Change notification: yes/partial/no/N-A/unverified [label] [pinpoint citation]
Gate 2 math: capability coverage = NN% over <W> weight; write coverage NN%; C1.4 <mark>; critical item scored 0: <none | item>; unverified weight: NN%; gate 2 allows: <A/B/C/D>; verification coverage = NN%
What this means for you: <plain language>

## Category 2: API Design, Reliability, and Operability (placement)
- C2.1 through C2.12: <each mark with evidence label and pinpoint citation; note N-A checks; note where evidence parity capped a mark>
Checks earned: Y of Z applicable; verification coverage = NN%
What this means for you: ...

## Category 3: Access Control and Safe Automation (placement)
- C3.1 through C3.6: <each mark with evidence label and pinpoint citation>
Checks earned: Y of Z applicable; verification coverage = NN%
What this means for you: ...

## Category 4: Documentation and AI-Agent Readiness (placement)
- C4.1 through C4.4: <each mark with pinpoint citation to Documented sources>
- AI agent path: <official MCP (read-write) | official MCP (read-only) | official MCP (docs-only) | none found>, plus any OpenAPI specification or SDKs; MCP standard version checked: <version or N-A> [pinpoint citation]
Checks earned: Y of Z applicable; verification coverage = NN%
What this means for you: ...

## Category 5: Accessibility and Cost (gate 1)
- C5.1 and C5.2: <each mark with evidence label and pinpoint citation>
Gate 1 allows: <A/B/C> (<reason>); verification coverage = NN%
What this means for you: ...

## Grade
- Gate 1, open access: allows <A/B/C> (<reason>)
- Gate 2, documented capability: allows <A/B/C/D> (capability coverage NN%)
- Letter from the gates: <letter>; binding gate: <gate 1 | gate 2 | both | none>
- Placement share: Y of Z Category 2–4 checks = NN%
- Score math: <floor> + round(<span> × share) = <score> (<letter>)
- Official MCP server (one-step bump): <yes, with citation | no>; after the step: <score> (<letter>) | not applied
- Published numeric score: XX / 100
- Letter grade: <grade>
- Evidence tier: baseline verified
- Overall verification coverage: NN% (gate: no group Unable to verify; unverified checklist weight ≤ 30%; overall ≥ 80%)
- Partial-result flag: <yes/no; what would resolve it>
- Unresolved evaluator disagreements: <none, or see "Grading runs">

## Good for / Not built for
- Good for: <the jobs a property manager can run through this API today, in one line>
- Not built for: <the jobs it can't do through the API, in one line>

## Bottom line for a property manager
<3-5 plain sentences stating what can and cannot be built today, the biggest API strength and limitation, and the product's practical role for a property manager. Distinguish API quality from product fit. Where a limitation was established from documentation rather than observed, say "the published documentation shows no way to..." rather than "the API cannot...". When relevant, state whether the product is a bank, whether another institution provides the banking service, whether property-management trust or fiduciary workflows are documented, and what additional system or provider the operator would still need. Do not imply that a high API score makes the product a substitute for a bank, PMS, or trust-accounting system unless the evidence establishes that role.>
```

If the qualifying API result is `no`, use this shorter output instead of scoring the five categories:

```markdown
# API Report Card: <Vendor> <Product>

## Run metadata
- Methodology version: 1.2
- Evaluating model: <model>
- Date run: <date>
- Final evidence-packet version or ID: <identifier>
- Evidence-discovery mode: <tool-enabled discovery | supplied final packet | packet-only>

## Final evidence packet manifest
- <first-party URL or supplied source>

## API eligibility
- Qualifying API: no
- API operator: none evidenced
- Eligibility basis: <concise explanation with pinpoint citations>

## Provider and property-management fit
- <as above>

## Total
- Published numeric score: 0 / 100
- Letter grade: F
- Result: No qualifying API

## Bottom line for a property manager
<State what the vendor offers, explain that no qualifying API was evidenced, and distinguish compatibility with other products from a vendor-provided API.>
```

If the run is **Partially verified**, **Documentation-only**, the run is `unverified` on eligibility, or the **verification-coverage gate fails**, use this withheld-score output:

```markdown
# API Report Card: <Vendor> <Product> — Grade withheld

## Run metadata
- Methodology version: 1.2
- Evaluating model: <model>
- Date run: <date>
- Final evidence-packet version or ID: <identifier>
- Evidence-discovery mode: <tool-enabled discovery | supplied final packet | packet-only>
- Assessment tier: <documentation-only | partially verified>
- Reason grade withheld: <no live battery | battery incomplete: list missing steps | verification coverage below 0.80 | group(s) Unable to verify | gate 1 unverified | gate 2 Unable to verify | eligibility unverified>

## Final evidence packet manifest
- <first-party URL or supplied source>

## API eligibility
- Qualifying API: <yes | unverified> [pinpoint citation]
- Interface label: <none | MCP only (no public API)>

## Provider and property-management fit
- <as above>

## Coverage classification and map
- <as above, where evidence allows>

## Provisional per-category findings (not a published score)
- For each check group, list the check marks and citations, the verification coverage, and note "Unable to verify" where coverage < 0.70. Give provisional gate results where evidence allows. Do not present a numeric score or letter.

## What would resolve it
- <the specific read-only access or evidence needed to reach Baseline verified and publish a number>

## Bottom line for a property manager
<Explain what could and could not be established, and that a comparable grade is withheld pending live verification. Do not imply the vendor lacks an API when eligibility is yes.>
```

## Final integrity check before answering

Recheck the completed report and correct it if any statement below is false:

- The standardized discovery and controlled verification procedures were completed, the standard locations were checked and recorded, and all evidence added after provisional scoring appears in the amendment log.
- The "find the documentation home first" sequence was recorded with dates, and it was completed in full before any documentation-dependent check was marked `no`. MCP servers were credited only if official, under the checks the MCP rule assigns, and the "AI agent path" line is filled in. The "MCP only" label was applied only if no API was found or supplied.
- Discovery depth was the same as for every vendor: no undocumented endpoint paths were probed, no application bundles were decoded to find new API surface, and any unpublished first-party material was supplied by the operator or vendor and labeled Discovered (supplied).
- The coverage classification used the product type's published list (or a deviation recorded before inspection with its first-party basis), was frozen before inspection, was used unchanged by all three runs, and was scored as written, with no items added, removed, split, or merged. Capability coverage and C1.1–C1.3 use its weights; alert-only items scored 0.5; C1.2 counts the workflow rows that write or act, not read-only workflows; C1.4 uses its stated thresholds.
- The report discloses the checklist size and the cost of one missing critical item as a share of capability coverage.
- Every mark above `no` has an auditable pinpoint citation with an evidence label, and every partial identifies the exact limitation. No mark rests solely on a customer's or operator's statement. Category 4 marks rest only on Documented sources.
- Evidence parity was applied: C2.3, C2.5, C2.6, and C2.11 are `yes` only where observed, and documentation contradicted by observation was scored on the observed behavior. No call was made to trigger a 429.
- Every no was assigned only after relevant first-party evidence was accessible and checked; inaccessible or inconclusive evidence was marked unverified, and no inaccessible evidence was counted as a satisfied capability.
- The tester was asked nothing after the run started, apart from any part of the credential the prompt omitted (Core rule 9).
- The verification-coverage gate was applied: no check group is below 0.70 coverage, unverified items carry no more than 30% of checklist weight, gate 1 is verified, overall coverage is reported, and a grade is published only when the gate and the minimum battery are satisfied.
- The evidence tier is stated, and the documentation-graded checks are disclosed. A withheld run does not present a numeric score or letter.
- Every live call was read-only: nothing was created, changed, or deleted; no webhook, key, account, or setting was created or changed; and no sign-in or approval was requested. The key does not appear in the evidence packet or report.
- Every N-A and unverified mark was excluded from capability coverage and the placement share, and both gates, the share, the score, and rounding were independently recalculated under the v1.2 rules. The published letter stays within the letter the gates allow, apart from the MCP step, which was applied once and only for a qualifying official MCP server; the binding gate is named.
- All scoring arithmetic was computed with code, and the checklist's weights were re-added from its item rows and match the totals used for capability coverage and C1.1–C1.4.
- Three grading runs were performed on the fixed grading model; all three runs received only this prompt and the frozen packet, with no vendor-specific guidance; the "Grading runs" section records agreement, resolutions, and any alternate score.
- Each capability or barrier was scored only under the checks that measure it, without unintended double-counting (notably: webhook absence in C1.4 vs C2.8; versioning contract in C2.10 vs currency in C4.4; rate-limit behavior in C2.5 vs plan-tiered limits in C5.2; test-environment existence in C3.5 vs its plan availability in C5.2; an OpenAPI specification in C4.2, not C4.3). C1.4 and Category 5 act only through the gates and are not in the placement share. An official MCP server is credited where the MCP rule assigns it (C3.6, C4.2, C4.3) and, by design, also through the MCP step.
- No check imposed requirements beyond its written definition, and no capability was credited from reputation, competitors, or unstated background knowledge.
- Plain-language sections describe documented absences as documentation findings ("the published documentation shows no..."), not as observed facts about the API.
- API eligibility, provider status, and property-management fit were based on cited first-party evidence and were not inferred from product names or compatibility claims.

=== END PROMPT ===
