# API Report Card: Column N.A. Column API

**Score: 95 / 100 · Grade: A** · baseline verified · all three grading runs scored 95 (A)

## Run metadata
- Methodology version: 1.2
- Grading model (fixed for this version): Claude Opus 5.5 (`claude-opus-5-5`) at high effort
- Date run: 2026-11-17
- Provisional evidence-packet version or ID: COLUMN-EP-2026-11-17-P1
- Final evidence-packet version or ID: COLUMN-EP-2026-11-17-F1 (frozen 2026-11-17)
- Evidence-discovery mode: supplied final packet. The grading runs did no discovery, opened no links and made no API calls.
- Evidence tier: baseline verified
- Credential: a Column sandbox key (`test_` prefix), used by the tester for read (GET) calls only. The key does not appear in the packet or in this report.
- Minimum live-test battery: complete (steps 1–5; packet §8)
- Live tests performed: T01–T30 (32 GET requests, 2026-11-17 17:40:04Z–17:40:59Z UTC)
  - Authentication: T03 returned 200; T22 (wrong key) returned 401
  - Core reads with a full cursor traversal: 13 transfers across 3 pages (T03–T05, T11, T12, T24, T25, T27–T29)
  - Filtered and incremental queries: T06–T10, T13, T14, T30
  - Deliberate errors: T15–T23
  - Header tally on all 32 responses
- Documentation-graded checks: C1.2, C1.3, C2.4, C2.8, C2.9 (write path), plus C1.4, C2.7, C2.10, C2.12, C3.1–C3.6, C4.1–C4.4, C5.1 and C5.2
- Checks applicable: 28 of 28 (none N-A, none unverified)

## Final evidence packet manifest
All sources are first-party, were read 2026-11-17 and are labeled [Documented] unless marked otherwise. Nothing is labeled Discovered (supplied).

| ID | Source |
|---|---|
| S01 | column.com homepage |
| S02 | column.com/llms.txt and /llms-full.txt (product overview) |
| S03 | docs.column.com/llms.txt (API index) |
| S04 | docs.column.com/llms-full.txt (2.18 MB full API corpus) |
| S05 | docs.column.com/openapi.json and /openapi.yaml (OpenAPI 3.0.3, info.version 1.4, 202 paths, 254 operations) |
| S06 | Authentication |
| S07 | Sandbox and Testing |
| S08 | Getting Started |
| S09 | API Key Security |
| S10 | Roles & Permissions |
| S11 | Pagination |
| S12 | Idempotency |
| S13 | Errors |
| S14 | Events and Webhooks |
| S15 | Reporting guide |
| S16 | Bank Statements |
| S17 | Bank account API reference |
| S18 | Account Number data model |
| S19 | Transfer lifecycle endpoints |
| S20 | Transfer objects (remittance and settlement fields) |
| S21 | Counterparty |
| S22 | Reporting API reference |
| S23 | Going live |
| S24 | Bank Accounts use-case guide |
| S25 | column.com/changelog |
| S26 | status.column.com, plus /history, RSS and 90-day uptime |
| S27 | column.com/property-management |
| S28 | column.com/appfolio |
| S29 | API Terms of Service |
| S30 | github.com/column and npm @column-na/card-reveal |
| S31 | Card Reveal SDK version policy |
| S32 | International wire transfer fees |
| S33 | Pricing: record of absence after search |
| T01–T30 | Live sandbox reads [Live-tested] |

**Standard locations checked** (packet §4, 2026-11-17):

| Location | docs.column.com | column.com |
|---|---|---|
| llms.txt | 200 (API index) | 200 (product index) |
| llms-full.txt | 200 (full API corpus) | 200 (product overview) |
| openapi.json / openapi.yaml | 200 | 404 |
| swagger.json | 404 | 404 |
| sitemap | sitemap.xml 200 | sitemap-index.xml 200 |
| Changelog | 404 | /changelog 200 |
| release-notes | 404 | 404 |
| MCP page and /.well-known/mcp.json | 404 | 404 |

- Status page: status.column.com 200.
- The official MCP Registry has no Column listing.
- The developer., developers., api-docs. and dev. subdomains did not respond.
- The documentation-home sequence was completed in full with dates (packet §3).

## Evidence-amendment log
Amendments A1–A12, from the tester's single controlled verification pass (packet §7):

| # | Check(s) | Result |
|---|---|---|
| A1 | C5.2 | S32 and S33 added |
| A2 | C2.5 | Nothing new |
| A3 | C2.10, C4.4 | S25 deprecation entries and S31 added |
| A4 | C3.6 | No OAuth found |
| A5 | C2.11 | `request-id` header seen live but documented nowhere |
| A6 | C2.9 | No concurrency control found |
| A7 | C2.7 | S25 batch-upload entries added |
| A8 | Checklist item 16 | S25 note added: Column's team, not the customer, sets the frozen status |
| A9 | Checklist item 17 | S21 annotated: no update operation |
| A10 | C2.3 | A missing record returns 400; a wrong key returns 401 with an empty body |
| A11 | C2.2 | Type inconsistencies recorded |
| A12 | C1.4, C2.12 | Full event list and uptime data added |

No sources were removed. The grading runs added nothing.

## Grading runs
- Evidence session (tester: discovery, verification, live battery, packet frozen): 2026-11-17
- Runs 1–3 (PLM; methodology and frozen packet only; no vendor-specific guidance): 2026-11-17. The three runs ran at the same time as separate, isolated subagents on Claude Opus 5.5 at high effort.
- Check-level agreement: **28 of 28 checks unanimous.**
- Coverage-checklist agreement: 16 of 17 items unanimous.
- C1.3 and capability coverage differ only because of that one checklist item (item 16).
- Score agreement: all three runs scored 95 (A).

| Check / item | Run 1 | Run 2 | Run 3 | Resolved | Basis |
|---|---|---|---|---|---|
| Checklist item 16: Freeze or close an account (important, weight 2) | 1.0 | 0.5 | 0.5 | **0.5** | See below |
| → C1.3 Lifecycle coverage | 87.5% | 75.0% | 75.0% | **75.0%** | Follows item 16 |
| → Capability coverage | 97.5% | 95.0% | 95.0% | **95.0%** | Follows item 16 |

**Basis for item 16.** The only documented operator action is `DELETE /bank-accounts/{id}`, which works only at a $0 balance (S17). Run 1 counted that delete as "close" and gave full credit. The evidence supports only partial credit, for three reasons:
- It is a hard delete, not a close. Afterward the account reads back as "not found" (T15), not as `closed`.
- No documented operation lets the operator set the `closed` or `frozen` status. The PATCH body has no status field (S05).
- Only Column's team can freeze an account (S25, Sep 30 2025).

The item's operations are therefore present but limited, so it scores 0.5.

- Unresolved disagreements: none.
- If run 1's reading were used, capability coverage would be 97.5% and C1.3 87.5%. The gates, placement and score would not change: still **95 (A)**.

Other differences between runs did not change any mark:
- **C1.4 push-coverage estimates:** 88.2%, 87.1% and 90.8%. Each is at least 85%, so all three runs marked C1.4 yes.
- **Rounding edge (noted by every run):** placement is exactly 6 × 0.75 = 4.5, which rounds up. Losing half a point anywhere in Categories 2–4 (for example C2.6 or C2.7 dropping to partial) would give 94, still an A.
- **C5.2 (run 2's note):** reading the absence of any published pricing as "partial" would cap gate 1 at B (87, B+). No run made that call. The packet shows no plan tiers, API fee or paid add-on after a targeted search (S33, A1), and the API terms list no fees (S29).

## API eligibility
- Qualifying API: yes
- Interface label: none
- API operator: Column, N.A. ("Bank") [S29 API Terms, parties clause; S05 `servers: https://api.column.com/`]
- Access or credential issuer: Column N.A., through its self-serve developer dashboard [S06; S09]
- Eligibility basis: Column has a public REST API at api.column.com, defined by a public OpenAPI spec of 254 operations. The API covers Column's own accounts and payment rails [S05]. A sandbox key authenticated and returned data live [T03].

## Context
- Product type: Banking/payments
- What the API is for: Column is a bank. Its API opens and manages deposit accounts and account numbers, and sends or receives money over ACH, wire, realtime (instant), book transfer, check and international wire. It also exposes balances, transaction activity, statements, settlement reports and signed webhooks. The core objects are accounts, balances, transactions, payments, statements and reconciliation data.

## Provider and property-management fit
- What this product is: a nationally chartered bank that gives developers API access to bank accounts and payment rails [S01; S02].
- Bank status: **bank**. Column N.A. is nationally chartered and Member FDIC [S01 hero "Column NA Member FDIC"; S29].
- Who provides any bank account or regulated banking service: Column N.A. itself [S24; S27; S28].
- What the customer actually receives: FDIC-insured deposit accounts held at Column, with any number of account numbers per account, money movement, statements and reports, run through the API or the dashboard [S16; S18; S24].
- Property-management fit: **dedicated PM offering**. Column serves a broad developer and fintech market, but it has a dedicated "Property Management & HOAs" page [S27], an AppFolio partnership page [S28] and a Real Estate industry tab [S01].
- Documented PM-specific workflows:
  - client and broker trust accounts (FBO owner), operating accounts and per-property balances [S27]
  - owner disbursements, vendor payments and security-deposit refunds [S27]
  - trust-account check deposits and Positive Pay [S27]
  - reconciliation sync into PM accounting software [S27]
  - next-business-day owner distributions inside AppFolio [S28]

  All of these are described as banking, dashboard or AppFolio-integration features. None names an API endpoint [packet §6].
- Trust or fiduciary workflow support: **limited**.
  - PM trust-account workflows are documented at the product level [S27; S28].
  - The API reference is general-purpose banking. It offers FBO/sub-ledger account types and multiple account numbers per account [S16; S18; S24], but no endpoints specific to PM trust accounting, security deposits or owner ledgers [S04; S05].
  - The "Trust accounts" in the Jul 30 2026 changelog are revocable and irrevocable personal trusts, not PM client-trust accounting [S25].
- Operational role and dependencies: Column supplies the bank accounts and payment rails. An operator still needs a PMS or trust-accounting system (for example AppFolio, which has a direct Column integration) to keep tenant and owner ledgers. Going live requires KYC/KYB [S23], and opening accounts for end customers requires a Program Management Agreement [S24].

## Coverage classification (fixed before inspection)
- Checklist: Banking/payments published v1.2 list, no deviation. It was frozen 2026-11-17T17:36:04Z, before any API reference was read or any call was made [packet §1–2].
- Size, re-added in code from the item rows: 17 items, total weight 40. This matches the stated totals.
  - Objects: 10 items, weight 23
  - Workflows: 3 items, weight 9
  - Lifecycle actions: 4 items, weight 8
- One missing critical item = 3 ÷ 40 = **7.5%** of capability coverage

| Item | Kind | Class | Weight | State | Score |
|---|---|---|---|---|---|
| Accounts | object | critical | 3 | present: GET/POST `/bank-accounts`, GET/PATCH/DELETE `/bank-accounts/{id}` [S05; S17; T03] | 1.0 |
| Balances | object | critical | 3 | present (computed, read-only by nature): `balances` {available, pending, locked, holding} in integer cents; `/history` [S17; T03] | 1.0 |
| Transactions | object | critical | 3 | present: `/transfers`, per-rail lists, `/activities` with running balance [S05; S17; T04–T06, T25] | 1.0 |
| Payment initiation | object | critical | 3 | present: POST `/transfers/ach`, `/wire`, `/realtime`, `/book`, `/checks/issue`, `/international-wire` [S05; S12] | 1.0 |
| Statements | object | important | 2 | present: monthly statements via the reporting API; `GET /reporting/customized-bank-account-statement` [S16; S22] | 1.0 |
| Reconciliation data | object | important | 2 | present: settlement reports by transaction and by account summary (CSV, JSON, Parquet); activities with running balance [S15; S17; S22] | 1.0 |
| Settlement webhooks | object | important | 2 | present: `ach.*.settled`, wire and realtime `.completed`, check settled, `reporting.*.completed`, all HMAC-signed [S14] | 1.0 |
| Sub-accounts or virtual account numbers per property or owner | object | important | 2 | present: `POST /bank-accounts/{id}/account-numbers` (many per account); FBO and custom account types [S05; S18; S24] | 1.0 |
| Incoming payment remittance detail | object | important | 2 | present: ACH `payment_related_info` (CTX up to 9,999 × 80 characters); wire `originator_to_beneficiary_information_line_1–4`; international wire `remittance_info` [S20] | 1.0 |
| Counterparty metadata | object | optional | 1 | present: create, list, get, delete [S05; S21; T28] (the missing update is scored in item 17) | 1.0 |
| Read balances and transactions | workflow | critical | 3 | present, live-tested [T03–T06, T25] | 1.0 |
| Initiate a payment | workflow | critical | 3 | present on all rails, with Idempotency-Key [S05; S12] | 1.0 |
| Reconcile settlement | workflow | critical | 3 | present: `POST /reporting` settlement reports, `settled_at` fields, settled events, activity running balances [S15; S17; S20; S22]. Needs a one-time dashboard time-zone setting [S15; T26]. | 1.0 |
| Cancel a pending payment | lifecycle | critical | 3 | present: ACH cancel (INITIATED or HOLD), held wire, realtime, book and international wire cancel, check stop-payment [S19; S05] | 1.0 |
| Initiate a return or reversal | lifecycle | important | 2 | present: ACH reverse and return; wire return-request and incoming reverse; realtime return and return-request; check and international wire returns [S19; S05] | 1.0 |
| Freeze or close an account | lifecycle | important | 2 | partial: close only by hard `DELETE` at a $0 balance, after which the account reads as not found [S17; T15]. No operator freeze: the frozen status is set only by Column's team [S25 Sep 30 2025; S05 PATCH has no status field]. | 0.5 |
| Update counterparty details | lifecycle | optional | 1 | absent: no PATCH or PUT [S05; S21; A9] | 0.0 |

## Functional coverage map
- Core objects: all 10 present (23 of 23 weight):
  - accounts (critical, 3)
  - balances (critical, 3)
  - transactions (critical, 3)
  - payment initiation (critical, 3)
  - statements (important, 2)
  - reconciliation data (important, 2)
  - settlement webhooks (important, 2)
  - sub-accounts and account numbers (important, 2)
  - remittance detail (important, 2)
  - counterparty metadata (optional, 1)
- Primary operational workflows:
  - read balances and transactions (live-confirmed)
  - initiate payments on six rails
  - schedule settlement reports and pull activity lines to reconcile
- Lifecycle actions:
  - cancel a pending payment: present (critical, 3)
  - return or reversal: present (important, 2)
  - freeze or close: partial (important, 2)
  - update counterparty: absent (optional, 1)

## Category 1: Functional Coverage and Usefulness (gate 2)
- **C1.1 Object coverage: 100%** (23/23) [Documented S05, S14–S22; Live-tested T03–T05, T25, T28]
- **C1.2 Write coverage: 100%** (6/6: initiate a payment, reconcile settlement; the read-only workflow is excluded) [Documented S05 POST /transfers/*, S12, S15, S22]
- **C1.3 Lifecycle coverage: 75.0%** (6/8) [Documented S17, S19, S21, S25]
- **C1.4 Change notification: yes** [Documented S14; Live-tested T08, T09]
  - Signed webhooks cover transfer states on every rail: initiated, submitted, settled, completed, returned, canceled, hold and manual review.
  - They also cover statement and report completion, `account.frozen` and `account.overdrafted`.
  - Gaps: no account opened or closed event, and no account-number event.
  - Weighted push coverage of critical-plus-important state changes was estimated at 87–91% across runs, above the 85% threshold.
  - Missed events can be caught up through `GET /events?created.gte=` (live-confirmed, T09).

Gate 2 math: capability coverage = **95.0%** (38/40) over 40 weight; write coverage 100%; C1.4 yes; critical item scored 0: none; unverified weight: 0%; **gate 2 allows: A**; verification coverage = 100% (4/4).

What this means for you: through the API you can open accounts, give each property or owner its own account number, and see balances and every transaction. You can also send, cancel, return or reverse payments on every major rail, pull statements and settlement reports, and get signed alerts when payments settle or fail. Two small gaps:
- The published documentation shows no way to freeze an account yourself, or to close one except by deleting it once it holds $0.
- The published documentation shows no way to edit a saved payee. You delete it and create it again.

## Category 2: API Design, Reliability, and Operability (placement)
- **C2.1 Modern conventions: yes.** Resource-oriented REST using GET, POST, PATCH and DELETE with JSON, defined in OpenAPI. Actions such as cancel use POST, which is an accepted convention. [Documented S05; Live-tested T03–T30]
- **C2.2 Consistent typing: partial.** Money is integer minor units in 49 of 50 `amount` schemas and on every live response. IDs and booleans keep one type. Limitations [Documented S05, S17; Live-tested T04, T11, T24; A11]:
  - `CustomerFacingAdminTransfer.amount` is typed as a string.
  - The spec types the error `code` as an integer, but it is a string live.
  - The docs show balances as `number`; the spec says integer.
  - Status casing differs by endpoint for the same value: `completed` vs `COMPLETED`.
- **C2.3 Structured errors: partial.** The documented body (`type`, a stable string `code`, `message`, `documentation_url`, `details`) appeared on every non-401 error [Documented S13; Live-tested T01, T15–T21, T23]. Scored on observed behavior, which falls short in two ways:
  - A missing record returns HTTP 400 instead of the documented 404 [T15, T23].
  - A wrong key returns 401 with an empty body and no code [T22].
- **C2.4 Duplicate prevention: yes.** An `Idempotency-Key` header works on every money-moving create: ACH, book, wire, realtime, check issue and deposit, international wire, and ACH and wire reverse. Account creation is covered too. A worked example shows a repeated request returning the same ID. [Documented S12]
- **C2.5 Load handling: partial.** The docs give 429 retry guidance with numbers: start at 1 s, double each time, wait at most 30 s, stop after 5 retries [S13]. But no rate-limit or `Retry-After` header appeared on any of 32 responses, and no 429 was met. The evidence-parity rule therefore caps this at partial. [Documented S13; Live-tested §8 header tally]
- **C2.6 Pagination: yes.** Cursor pagination with `starting_after`/`ending_before`, a `has_more` flag, newest-first order and a 100-record limit [Documented S11]. Live, 13 of 13 transfers were read in 3 pages with no duplicates or gaps, and `total_results_count` matched [Live-tested T05]. Minor caveat: no tie-break order is documented for identical timestamps (§8 note 6).
- **C2.7 Bulk or incremental export: yes.** Background settlement-report jobs export every balance-affecting transaction and per-account summary as CSV, JSON or Parquet (up to 93 days per job), alongside automatic daily reports. Created-since filters and the `/events` feed support incremental sync. Limitation: there is no updated-since filter. [Documented S15, S22, S05; Live-tested T06, T09, T27]
- **C2.8 Webhook security and delivery: yes.** HMAC-SHA256 `Column-Signature` header with a per-endpoint secret. Failed deliveries are retried up to 25 times over 3 days with exponential backoff. Event IDs stay the same on redelivery, the docs say to process idempotently, and an events API recovers missed events. [Documented S14]
- **C2.9 Concurrency control: no.** PATCH exists on bank accounts, account numbers, book transfers and webhook endpoints, but there is no ETag, If-Match, version field or stale-write rejection. The corpus has 0 matches for "ETag", "If-Match" or "optimistic", and the only 409 is a card-fee configuration conflict. [Documented S04, S05; A6]
- **C2.10 Versioning: no.**
  - There is no version identifier in the path (`https://api.column.com/`) or in any header. The spec's `info.version` "1.4" labels the document but gives integrations nothing to pin.
  - No breaking-change definition or deprecation policy is published ("deprecat" 0, "sunset" 0).
  - The API terms allow changes with notice "by any reasonable means" and no minimum period.
  - [Documented S05, S04, S29 §5; A3]
- **C2.11 Request traceability: partial.** A unique `request-id` header (`apir_…`) appeared on 32 of 32 responses, including errors and the 401. It is documented nowhere: the spec declares no response headers and the corpus has 0 matches. [Live-tested §8; Documented S05; A5]
- **C2.12 Status transparency: yes.** status.column.com shows each component (Sandbox, Production, FedWire, FedACH), 90-day uptime (100%), a historical uptime page, and incident history with RSS/Atom feeds listing incidents from 2025 and 2026. [Documented S26]

Checks earned: **8.0 of 12** applicable; verification coverage = 100%.

What this means for you: the API is modern and predictable. Payments can be retried without sending money twice, webhooks are signed and retried, and paging and exports work as documented. The status page is public. Things to watch:
- The published documentation shows no protection against two tools overwriting each other's edits.
- There is no version pinning or promised notice before API changes.
- Rate-limit headers are not exposed.
- A "not found" comes back as a 400 instead of the documented 404.

## Category 3: Access Control and Safe Automation (placement)
- **C3.1 Read-only credentials: yes.** "View Only" key permission. [Documented S09]
- **C3.2 Scoped credentials: yes.** "Custom" keys can be limited:
  - per transfer type (ACH credits and debits, returns, wires, checks, book, realtime, stop payments)
  - per resource (entities, bank accounts, counterparties, loans, reports)
  - with overrides per entity or account, and per-key approval rules

  [Documented S09]
- **C3.3 Multiple keys: yes.** The docs say "One key per workload", one key per application. [Documented S09; S06]
- **C3.4 Rotation and revocation: yes.** Self-serve in the dashboard: issue a replacement, cut over, then delete the old key. Compromised keys can be revoked immediately. [Documented S09; S10]
- **C3.5 Test environment: yes.** A self-serve sandbox mirrors production, with separate `test_` keys, isolated data and simulation routes. [Documented S07, S01; Live-tested on the sandbox key, T03]
- **C3.6 Delegated access: no.** Only static API keys (HTTP Basic). No OAuth or other delegated-authorization flow is documented ("OAuth" 0 matches), and there is no MCP server. [Documented S04, S06; A4; §3]

Checks earned: **5 of 6** applicable; verification coverage = 100%.

What this means for you: you can give each tool or AI agent its own narrowly limited key, for example read-only, or "ACH credits from the trust account only". You can require approvals, build in a free sandbox, and kill a key yourself. The published documentation shows no sign-in-and-approve (OAuth) option, so connecting an outside app means giving it a key.

## Category 4: Documentation and AI-Agent Readiness (placement)
- **C4.1 Complete self-serve reference: yes.** A public per-endpoint reference with method, path, parameters, a curl request and a JSON response for each endpoint, plus guides on authentication, errors, pagination, idempotency and webhooks. Minor gaps: the response headers and the batch and NACHA upload endpoints are undocumented. [Documented S04, S06, S11–S14]
- **C4.2 Machine-consumable path: yes.** A public OpenAPI spec (JSON and YAML, 254 operations) that the docs recommend for generating SDKs and importing into Postman. Minor defects: it claims version 3.1 but is 3.0.3, and the error `code` type is wrong. There is no official general SDK (the npm packages are card-reveal UI only), and no MCP server. [Documented S05, S04, S30]
- **C4.3 AI-readable docs: yes.** docs.column.com/llms.txt is an API index, llms-full.txt is a 2.18 MB corpus covering every endpoint, and every page is available as Markdown. The OpenAPI spec is credited under C4.2, not here. [Documented S03, S04]
- **C4.4 Kept current: partial.** There is a dated changelog through Sep 16 2026, with deprecation notices from 2021–2022 [Documented S25]. Limitations [S25, S03, S05; A7; §4]:
  - It is a product changelog; there are no API-specific release notes.
  - API features announced on Jul 30 2026 (batch-file and NACHA uploads) are still missing from the public spec and reference.
  - llms.txt says "OpenAPI 3.1" while the spec served is 3.0.3.
- AI agent path: none found. There is no official MCP server: no Registry listing, no MCP page, and 0 mentions in the docs corpus. Machine-readable resources are a public OpenAPI 3.0.3 spec, llms.txt and llms-full.txt. There is no general SDK. MCP standard version checked: N-A [§3; S05; S03; S04; S30].

Checks earned: **3.5 of 4** applicable; verification coverage = 100%.

What this means for you: a developer or an AI coding tool (Claude, ChatGPT and the like) can learn this whole API from public files without logging in. The weak spot is change tracking. The changelog is product-level and lags the reference.

## Category 5: Accessibility and Cost (gate 1)
- **C5.1 Self-serve API key: yes.** Self-serve signup ("Create an account — Start building in sandbox"), with keys created in the dashboard and no sales call or ticket. Going live requires KYC/KYB, a legally required step that does not count against this check. [Documented S01, S06, S08, S09, S23]
- **C5.2 Not commercially gated: yes.**
  - First-party materials show no plan tiers, API fees or paid add-ons after a targeted search, and the API terms list no fees.
  - The sandbox is free and self-serve.
  - KYC/KYB and the Program Management Agreement are compliance requirements, not commercial gating.
  - Caveat: Column publishes no pricing at all; commercial terms go through "Contact sales".
  - [Documented S01, S07, S23, S24, S29, S33; A1]

Gate 1 allows: **A** (both yes); verification coverage = 100%.

What this means for you: you can sign up, get sandbox keys and start building today without talking to sales. Going live requires the bank's normal identity and business checks. Column publishes no price list, so ask about account and payment fees.

## Grade
- Gate 1, open access: allows **A** (C5.1 yes, C5.2 yes)
- Gate 2, documented capability: allows **A** (capability coverage 95.0%; write coverage 100%; C1.4 yes; no critical item at 0; unverified weight 0%)
- Letter from the gates: **A**; binding gate: **none**
- Placement share: 16.5 of 22 Category 2–4 checks = **75.0%** (Category 2: 8.0/12; Category 3: 5/6; Category 4: 3.5/4)
- Score math (computed in code): 90 + round(6 × 0.75) = 90 + round(4.5) = 90 + 5 = **95 (A)**. The exact half rounds up.
- Official MCP server (one-step bump): no. None was found in the MCP Registry, on either domain, on GitHub or npm, or in the docs corpus [§3]. Not applied.
- **Published numeric score: 95 / 100**
- **Letter grade: A**
- Evidence tier: baseline verified
- Overall verification coverage: 100% (28/28). Every group is at 100%, unverified checklist weight is 0%, gate 1 is verified, and overall coverage is at least 80%.
- Partial-result flag: no
- Unresolved evaluator disagreements: none. One checklist-item disagreement (item 16) was resolved against the evidence with no score effect; see "Grading runs".

## Good for / Not built for
- Good for: holding operating and trust-style funds at an FDIC bank and giving each property or owner its own account number. Also sending and receiving ACH, wire, instant and check payments with duplicate protection, cancelling or returning payments, and pulling transactions, statements and settlement reports into your own reconciliation tools or AI agents.
- Not built for: tenant, owner or lease ledgers and trust-accounting rules (that stays in your PMS). The published documentation also shows no OAuth app connections, no official MCP server, no self-serve account freeze, no way to edit saved payees and no overwrite protection on edits.

## Bottom line for a property manager
Column is an actual bank (Column N.A., Member FDIC), so your money sits at Column itself, not at a software company layered on someone else's bank. Its API is one of the most complete banking APIs an operator can build on. You can open accounts and per-property or per-owner account numbers, move money on every major U.S. payment rail, cancel or reverse payments, and pull statement and settlement data. You can do all of that with tightly limited, self-serve keys and a free sandbox. Its biggest strengths are payments that can be retried without double-sending, signed and retried webhooks, and documentation an AI tool can read in one file.

Its main limits come from the published documentation, not from observed failures:
- The documentation shows no version or deprecation contract.
- It shows no protection against two tools overwriting each other's edits.
- It shows no OAuth sign-in for outside apps and no official MCP server.

Column markets property-management trust accounts, owner distributions and an AppFolio integration. The API itself is general-purpose banking, with no property-management trust-accounting endpoints, so you still need a PMS or trust-accounting system for tenant and owner ledgers alongside it.
