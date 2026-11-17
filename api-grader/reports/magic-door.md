# API Report Card: MagicDoor company-portal API

**Published score: 87 / 100 — B+**
(B / 85 from the gates and placement, then one step up for MagicDoor's official MCP server)

## Run metadata
- Methodology version: 1.2
- Grading model (fixed for this version): Claude Opus 5.5 (`claude-opus-5-5`), high effort. All three runs were launched with effort set to high. Run 3 reported that it was running below high effort; the launch request asked for high, and this is recorded here as a possible deviation.
- Date run: 2026-11-17
- Provisional evidence-packet version or ID: MD-EVP-2026-11-17-v0.1
- Final evidence-packet version or ID: MD-EVP-2026-11-17-v1.0 (frozen 2026-11-17 18:45:57 UTC)
- Evidence-discovery mode: supplied final packet. The evidence session itself used tool-enabled discovery. The grading runs made no web or API calls and added no sources.
- Evidence tier: baseline verified
- Credential: a staging (vendor test-environment) API key supplied by the operator, used for read calls only. Its token carries `permissions: "*"` and `property_access: "*"`, so it is unscoped (packet §0, T01).
- Minimum live-test battery: complete, steps 1–5 (packet §8 "Battery completion"). Step 3 was completed with documented filters that worked: `ended=true/false` on leases (T05–T07) and `status` on work orders (T13). The documented work-order `closedAfter` filter was **not** honored (T12). No updated-since filter exists to test.
- Process notes from the packet: the live battery ran before the controlled verification pass (disclosed in packet §0), and it ran against MagicDoor's staging environment.
- Live tests performed: T01 token exchange; T02–T04 paging through properties; T05–T07 lease `ended` filter; T08 work orders; T09 chart of accounts; T10 rental applications; T11–T13 work-order `closedAfter` and `status` filters; T14–T15 lease and ledger typing; T16 permission catalog; E01–E10 deliberate errors; R01–R05 API-host root and `/.well-known/api-catalog` checks.
- Documentation-graded checks: the write-path checks C1.2, C1.3, C2.4 and C2.9. Also C1.1 operations, C1.4, C2.1, C2.2 (with live corroboration), C2.7, C2.10, C2.12, C3.1–C3.6, C4.1–C4.4, C5.1 and C5.2. C2.8 is N-A.
- Checks applicable: 27 of 28. N-A: C2.8 (no webhooks or events). Unverified: none.

## Final evidence packet manifest
All sources were accessed 2026-11-17.
- S00 MagicDoor homepage, https://magicdoor.com/ [Documented]
- S01 API docs, Introduction [Documented]
- S02 Quickstart [Documented]
- S03 Authentication [Documented]
- S04 API reference overview [Documented]
- S05 Errors [Documented]
- S06 Pagination [Documented]
- S07 API stability [Documented]
- S08 Walkthrough, "Finding a lease" [Documented]
- S09 `llms.txt` [Documented]
- S10 `llms-full.txt`: the full reference, 975 pages and 967 endpoints [Documented]
- S11 Docs `sitemap.xml` and `robots.txt` [Documented]
- S12 Site `sitemap.xml` [Documented]
- S13 Pricing [Documented]
- S14 Security [Documented]
- S15 Terms of Service [Documented]
- S16 Trust accounting feature page [Documented]
- S17 MCP Server feature page [Documented]
- S18 MCP launch blog and September 2026 updates [Documented]
- S19 August and October 2026 update posts [Documented]
- S20 MCP server README (github.com/MagicDoorInc/magicdoor-mcp) [Documented]
- S21 `@magicdoor/mcp` npm listing and `package.json` [Documented]
- S22 MCP server `src/config.ts` [Documented]
- S23 MagicDoorInc GitHub organisation [Documented]
- S24 Official MCP Registry search for "magicdoor": 0 results [Documented (registry)]
- S25 Open Source page [Documented]
- S26 Help center [Documented]
- L Live tests T01–T16, E01–E10 and R01–R05 on `*.magicdoor-test.com` (staging) [Live-tested]

Documentation home: found at step 1 of the discovery sequence. The footer link "API Docs" leads to `https://api-docs.magicdoor.com/`. The `docs.`, `developer.`, `developers.`, `api.` and `dev.` subdomains were also checked for the record and all returned 404.

Standard locations checked (packet §6):

| Location | magicdoor.com | api-docs.magicdoor.com |
|---|---|---|
| `/llms.txt` | 404 | 200 |
| `/llms-full.txt` | 404 | 200 (7.2 MB) |
| Per-page `.md` | — | 200 |
| `/sitemap.xml` | 200 | 200 |
| `/openapi.json`, `/openapi.yaml`, `/swagger.json` | 404 | 404 |
| `/changelog`, `/release-notes` | 404 | 404 |
| `/.well-known/api-catalog` | 404 | 404 |
| Status page | `status.magicdoor.com` 404; `/status` 404 | `/status` 404 |
| MCP | `/features/ai/mcp-server` 200 | `/mcp` 404 |

On the API hosts, `/.well-known/api-catalog` also returned 404 (R02, R05).

## Evidence-amendment log
As recorded in the packet (§7, A-01 to A-12, 2026-11-17 18:38–18:41 UTC). No grading run added anything.
- A-01 Inventory (C1.1)
- A-02 Lifecycle endpoint semantics (C1.3)
- A-03 Webhooks, updated-since filters and history endpoints (C1.4, C2.7)
- A-04 Typing (C2.2)
- A-05 Ordering (C2.6)
- A-06 Concurrency (C2.9)
- A-07 Status page and SLA (C2.12)
- A-08 Test environment (C3.5)
- A-09 OAuth, OpenAPI and SDK (C3.6, C4.2)
- A-10 Changelog and deprecation (C2.10, C4.4)
- A-11 `errorCode` (C2.3)
- A-12 `idempotencyKey` (C2.4)

## Grading runs
- Evidence session (tester: discovery, verification, live battery, packet frozen): 2026-11-17
- Runs 1–3: 2026-11-17. PLM ran all three at the same time, as three separate agents. Each was given only the methodology and the frozen packet, was told only its run number, and received no vendor-specific guidance.
- Result of each run:

| Run | Letter from gates | Placement share | Score before MCP step | Published |
|---|---|---|---|---|
| Run 1 | B (gate 2) | 12.0 / 21 | 85 | 87 B+ |
| Run 2 | B (gate 2) | 11.5 / 21 | 85 | 87 B+ |
| Run 3 | B (gate 2) | 12.0 / 21 | 85 | 87 B+ |

- Check-level agreement: **26 of 27 applicable checks were unanimous.** All 32 checklist rows were also unanimous: Inventory 0.0 and every other row 1.0.

| Check | Run 1 | Run 2 | Run 3 | Resolved | Basis |
|---|---|---|---|---|---|
| C2.11 Request traceability | yes | partial | yes | **partial** | See below. |

Basis for C2.11: under "yes", every response must carry a unique, *documented* identifier. The docs describe the body `traceId` only on error responses (S05). Live, the `x-trace-id` header appeared on every success and error response (T01–T16, E01–E10), but the packet records that "the header itself is not documented" (packet §4). On successful responses, then, the only identifier is undocumented. That matches the "partial" definition: "an identifier is present but undocumented." Runs 1 and 3 gave yes because the documented `traceId` mechanism is usable with support. The resolution follows the literal wording of the check, not the majority of runs.

Score effect: none. With C2.11 at yes, the share is 12.0 / 21, which gives 80 + round(5.14) = 85. With C2.11 at partial, the share is 11.5 / 21, which gives 80 + round(4.93) = 85. Both lead to 87 B+ after the MCP step.

- Unresolved disagreements: none.
- Sensitivity, noted by all three runs: C1.4 is the only mark whose plausible alternative would change the published grade. All three runs independently marked it **no**. If it were partial, gate 2 would allow an A: 90 + round(6 × 0.548) = 93, then 97 (A+) after the MCP step. The evidence does not support partial. The methodology requires efficient incremental polling (updated-since plus filtering). No list endpoint has an updated-since filter (A-03), and the one documented date filter that was tested, `closedAfter`, was not honored live (T12).

## API eligibility
- Qualifying API: yes
- Interface label: none. A public REST API exists alongside the MCP server.
- API operator: MagicDoor. The REST API is the interface MagicDoor's own apps use. [S01 Introduction; S04] [Documented]
- Access or credential issuer: MagicDoor. A signed-in property manager creates keys in the portal (Profile → Developer), and they are exchanged for 15-minute tokens at `auth.magicdoor.com/api-keys/token`. [S02, S03] [Documented] The live token was issued by `auth.magicdoor-test.com`. [T01] [Live-tested]
- Eligibility basis: first-party docs describe a REST API of 967 endpoints in 121 groups that exposes MagicDoor's company-portal functions (S01, S10, packet §9). Key issuance is documented as self-serve (S02, S03). Authenticated live reads confirmed it (T01–T16).

## Context
- Product type: Accounting/PMS
- What the API is for and its core objects and workflows: the API is the programmatic side of MagicDoor's company portal, the property manager's view of the platform. It covers portfolios, properties, units, leases, tenants, owners, vendors, maintenance and work orders, and rental applications. It also covers built-in trust accounting: lease ledgers, chart of accounts, journal entries, bank accounts, reconciliation and owner distributions. The core workflows are reading the property → unit → lease tree, posting lease charges and payments, and creating and changing leases through move-out.

## Provider and property-management fit
- What this product is: AI-enabled property management software for companies with a few to thousands of doors, covering leasing, maintenance, accounting and tenant communication. [S00] [Documented]
- Bank status: not a bank. MagicDoor's terms state it is not a payment processor or money transmitter, and that payments are processed by third-party processors. [S15] [Documented]
- Who provides any bank account or regulated banking service:
  - Payments are handled by third-party processors. The security page calls them PCI-compliant partners whose names are available only under NDA [S14].
  - The help center mentions Plaid and Stripe integrations [S26], and the bank-feed endpoints name the provider `plaid` [S10].
  - The trust and operating accounts are held at the operator's own bank.
  - [Documented]
- What the customer actually receives: property management software with trust and operating ledgers that track the operator's own bank accounts. MagicDoor does not provide the bank accounts. [S16; S10 bank-accounts and bank-feeds] [Documented]
- Property-management fit: PM-specialized [S00, S01, S08, S16] [Documented]
- Documented PM-specific workflows, all [Documented]:
  - Lease lifecycle through move-out and lease end (`portal/leases/{id}/move-outs`, `/end`) [S08, S10]
  - Lease charge and deposit ledgers [S10]
  - Security deposits: hold, allocate and release (`.../deposits/allocate`, `.../deposits/release`) [S10]
  - Owner distributions and owner statements [S10]
  - Rental applications with screening [S10]
  - Work orders and vendors [S10]
  - HOA associations [S10]
- Trust or fiduciary workflow support: **documented**.
  - The trust-accounting page describes separate trust and operating accounts and ledgers, per-property and per-owner balances, tenant deposits held separately, three-way reconciliation, and period locks [S16].
  - The API exposes a separate deposit ledger, deposit allocate and release, owner distributions, owner contributions and transfers, company payouts, and reconciliation periods with lock and reopen [S10; packet §3 rows 13, 16, 17].
- Operational role and dependencies: MagicDoor is the system of record for properties, leases and trust accounting. The operator still needs its own bank accounts, linked through Plaid bank feeds, and MagicDoor's third-party payment processors to move money.

## Coverage classification (fixed before inspection)
- Checklist: the published Accounting/PMS list, with no deviation. Frozen 2026-11-17T18:30:47Z (packet §2), and used unchanged by all three runs.
- Size, re-added in code from the item rows (matches the packet's stated totals):
  - 32 items, total weight 69
  - Objects: 22 items, weight 46
  - Workflows: 3 items, weight 9
  - Lifecycle actions: 7 items, weight 14
- One missing critical item = 3 ÷ 69 = 4.35% of capability coverage

| # | Item | Kind | Class | Weight | State | Score |
|---|---|---|---|---|---|---|
| 1 | Properties | object | critical | 3 | present (list, get, batch, create, `PUT`, deactivate, delete; T02–T04) | 1.0 |
| 2 | Units | object | critical | 3 | present (CRUD, move, deactivate) | 1.0 |
| 3 | Leases | object | critical | 3 | present (CRUD, activate draft, end, reactivate; T05–T07, T14) | 1.0 |
| 4 | Tenants | object | critical | 3 | present (CRUD, deactivate and reactivate, move in and out of a lease) | 1.0 |
| 5 | Lease ledgers/transactions | object | critical | 3 | present (ledger read; charges, payments and credits can be added, adjusted and deleted; T15) | 1.0 |
| 6 | General ledger | object | critical | 3 | present (chart of accounts CRUD, manual journal entries with post, GL report; T09) | 1.0 |
| 7 | Bank accounts | object | critical | 3 | present (CRUD, activate and deactivate, Plaid bank feeds) | 1.0 |
| 8 | Owners | object | important | 2 | present (CRUD, deactivate and reactivate) | 1.0 |
| 9 | Bills | object | important | 2 | present (vendor bills CRUD, pay, settle) | 1.0 |
| 10 | Payments | object | important | 2 | present (record, adjust, delete, return, refund) | 1.0 |
| 11 | Applicants | object | important | 2 | present (rental applications, decision, convert to tenant; T10) | 1.0 |
| 12 | Work orders/tasks | object | important | 2 | present (CRUD, status, vendor, visits; T08, T11–T13) | 1.0 |
| 13 | Reconciliation | object | important | 2 | present (manual reconciliations, periods, items) | 1.0 |
| 14 | Vendors | object | important | 2 | present (CRUD, deactivate and reactivate) | 1.0 |
| 15 | Recurring charges | object | important | 2 | present (GET, POST, PUT, DELETE) | 1.0 |
| 16 | Security deposits (hold, apply, refund) | object | important | 2 | present (add, allocate, release) | 1.0 |
| 17 | Owner distributions or statements | object | important | 2 | present (calculate, disburse, post; owner statement reports) | 1.0 |
| 18 | Files | object | optional | 1 | present | 1.0 |
| 19 | Communications | object | optional | 1 | present (chats, emails, announcements) | 1.0 |
| 20 | Custom fields | object | optional | 1 | present | 1.0 |
| 21 | Associations | object | optional | 1 | present (HOA architectural requests, board members, surveys, violations) | 1.0 |
| 22 | Inventory | object | optional | 1 | absent (only a portfolio/property/unit "inventory report"; no inventory-item object; A-01) | 0.0 |
| 23 | Read core records | workflow | critical | 3 | present (T02–T15) | 1.0 |
| 24 | Post ledger charges and payments | workflow | critical | 3 | present | 1.0 |
| 25 | Create and update leases | workflow | critical | 3 | present | 1.0 |
| 26 | Change lease status through move-out | lifecycle | critical | 3 | present | 1.0 |
| 27 | Void or reverse a posted lease-ledger transaction | lifecycle | important | 2 | present (deleting a charge, payment or credit unwinds it; adjust) | 1.0 |
| 28 | Record a returned or refunded payment | lifecycle | important | 2 | present (payment return; credit release; deposit release; application-fee refund) | 1.0 |
| 29 | Void a bill | lifecycle | important | 2 | present (vendor-bill soft delete; void a check) | 1.0 |
| 30 | Finalize or undo a bank reconciliation | lifecycle | important | 2 | present (complete, cancel, delete; lock and reopen a period) | 1.0 |
| 31 | Deactivate or archive a property, unit, tenant, or owner | lifecycle | important | 2 | present (all four) | 1.0 |
| 32 | Delete or archive optional records | lifecycle | optional | 1 | present (delete notes, remove files, clear custom fields, archive chats) | 1.0 |

## Functional coverage map
- Core objects: 21 of 22 are present with read and write operations (packet §3 rows 1–21) [Documented S10]. Reads were confirmed live for properties, leases, work orders, chart of accounts, rental applications, a lease, and a lease ledger (T02–T15) [Live-tested]. Inventory (optional, weight 1) is absent (A-01).
- Primary operational workflows, all documented [Documented S10]:
  - Read core records (live, T02–T15)
  - Post charges, payments, deposit payments and credits: `POST portal/leases/{id}/charges`, `.../charges/payments`, `.../deposits/payments`, `.../charges/credits`
  - Create, update and activate leases: `POST portal/leases`, `PUT portal/leases/{id}`, `.../activate-draft`
- Lifecycle actions: all 7 present.
  - Row 27 (void or reverse a ledger transaction) is delivered by delete and adjust endpoints that unwind the entry, not by an endpoint titled "void". The methodology accepts DELETE as a way to void a financial record (C2.1), and S14 says deleted records keep their history.
  - Row 29 (void a bill) is delivered by a vendor-bill soft delete plus check void.
  - [Documented S10, the pages listed in A-02]

## Category 1: Functional Coverage and Usefulness (gate 2)
- C1.1 Object coverage: **97.83%** (45 of 46 weight) [Documented S10; packet §3 rows 1–22; A-01]
- C1.2 Write coverage: **100%** (rows 24 and 25; row 23 is read-only and left out) [Documented S10: `POST portal/leases/{id}/charges`, `POST .../charges/payments`, `POST portal/leases`, `PUT portal/leases/{id}`]
- C1.3 Lifecycle coverage: **100%** (14 of 14 weight) [Documented S10, the pages listed in A-02; packet §3 rows 26–32]
- C1.4 Change notification: **no**.
  - The docs state there are no webhooks and say to poll instead (S01, "What this API does not have") [Documented].
  - No list endpoint has an updated-since or modified-since filter (A-03) [Documented].
  - Change history exists only for work orders and maintenance requests (`.../history`).
  - The documented work-order `closedAfter` filter was not honored live: an open, pending work order came back for a 2030 cutoff (T12) [Live-tested].
  - Status filters do work (lease `ended`, T05–T07; work-order `status`, T13). But detecting changes to lease status or ledger postings would mean re-reading and comparing whole collections. That is not the efficient incremental polling that "partial" requires.

Gate 2 math (computed in code):
- Capability coverage = 68 ÷ 69 = 98.55%, over 69 weight
- Write coverage: 100%
- C1.4: no
- Critical item scored 0: none
- Unverified weight: 0%
- Gate 2 allows **B**. Coverage is at least 85%, but an A also requires C1.4 to be yes or partial.
- Verification coverage = 4 ÷ 4 = 100%

What this means for you: on paper, almost everything you run the business on can be read and changed through the API. That includes properties, units, leases, tenants, rent and deposit ledgers, bills, bank reconciliations, owner distributions, work orders and applications. The gap is change alerts. The published documentation shows no webhooks and no "changed since" filter. Your automations won't be told when something changes, so they have to re-check the data on a schedule.

## Category 2: API Design, Reliability, and Operability (placement)
- **C2.1 Modern API conventions: yes.** Resource-oriented REST with GET, POST, PUT, PATCH and DELETE over JSON (S01, S04; packet §9 method counts). Deactivating through `DELETE .../deactivate` and using POST for action endpoints are acceptable conventions. [Documented; Live-tested T02–T15]
- **C2.2 Consistent typing: no.**
  - S01 says ids are always strings, but 15 reference pages document ids as JSON numbers, including on core financial endpoints (A-04). S07 also says some endpoints return ids as JSON numbers. Examples:
    - `coaId` on `accounting-reports/get-general-ledger`
    - `transactionId` on `accounting-dashboard/get-returns-and-disputes`
    - `propertyId` and `ownerId` in the `owner-transfers/request-owner-contribution` request
  - So identifier types vary across endpoints on core fields. That fails the "partial" bar, which allows only a few inconsistencies confined to non-core fields.
  - Money is a plain JSON number, not integer minor units or a decimal string with a documented scale (S01). That alone caps this check at partial.
  - The docs also note PascalCase enum values on 24 pages and UTC-offset timestamps on 79 pages, contrary to the stated conventions (A-04).
  - Live ids and booleans were consistently typed on the endpoints tested (T09, T14, T15).
  - [Documented S01, S07, S10 pages in A-04; Live-tested]
- **C2.3 Structured errors: partial.**
  - RFC 7807 problem+json is documented, with `status`, `title`, `detail` and `traceId`, and status codes are correct (S05).
  - A stable machine-readable `errorCode` exists only for rental applications, listing syndication and some payment-account endpoints (S05). None was observed on any tested endpoint, including the rental-application 404 (E09).
  - Error shapes vary:
    - 404s match the documented shape (E01, E07–E09).
    - 400s drop `detail` and `instance` and use arrays under capitalised field names (E02, E03, E10).
    - A 401 from a bad or missing token has an empty body (E04, E05).
  - [Documented S05; Live-tested E01–E10]
- **C2.4 Duplicate prevention: no.**
  - There is no `Idempotency-Key`, and the docs say a retried POST creates a second record (S01, S05).
  - The only mechanism is `idempotencyKey` on paying a MagicDoor invoice, which is the operator paying MagicDoor itself (A-12). That does not cover the operator's consequential writes: ledger charges and payments, leases, distributions or bill pay.
  - [Documented]
- **C2.5 Graceful handling under load: yes.**
  - Documented: a 429 with a `Retry-After` header and a `retry_after` body field (S01, S06).
  - Observed: `x-rate-limit-limit`, `x-rate-limit-remaining` and `x-rate-limit-reset` on every live response, counting down per endpoint (T01–T16, E01–E10).
  - No 429 was provoked.
  - [Documented; Live-tested]
- **C2.6 Pagination for large collections: partial.**
  - Page and pageSize paging (1–100) with `totalCount` and `totalPages` is documented (S06). Live paging went page 1 → page 2 → an empty page 3 (T02–T04), and `pageSize=500` was rejected (E02).
  - Limitation: there is no stable-ordering guarantee. Core lists for properties, leases, units and work orders state no order (A-05, S07), and S06 warns that pages shift mid-walk.
  - [Documented; Live-tested]
- **C2.7 Bulk or incremental export: partial.**
  - There are no bulk or async export endpoints and no updated-since filter (A-03).
  - Full datasets can be read through paged lists and batch-by-id reads (up to 100 ids).
  - A dedicated unpaged "list all" path exists only for work orders (described as "for exports and pickers") and for active vendors, so export covers only some resources.
  - [Documented]
- **C2.8 Webhook security and delivery: N-A.** There are no webhooks or events (S01). Their absence is already counted under C1.4.
- **C2.9 Concurrency and conflict control: no.**
  - No ETag, If-Match, version field or stale-write error is documented (A-06).
  - A property `PUT` is a full rewrite, and a posted manual journal entry can be re-edited with no state guard (S10 `manual-journal-entries/update-manual-journal-entry`).
  - [Documented]
- **C2.10 Versioning and backward compatibility: no.** There is no version identifier anywhere. The docs say the API "can change at any time without notice", with no compatibility guarantee and no deprecation window (S01, S07). The site terms allow changes without notice (S15). [Documented]
- **C2.11 Request traceability: partial** (resolved; see "Grading runs").
  - The docs say the body `traceId` on error responses identifies the request and should be quoted to support (S05).
  - Live, an `x-trace-id` header appeared on every success and error response and matched `traceId` on errors (T01–T16, E01–E10). That header is undocumented, so on successful responses the identifier is present but undocumented.
  - [Documented S05; Live-tested]
- **C2.12 Service availability and status transparency: no.** There is no public status page (`status.magicdoor.com` 404; `/status` 404), no incident history and no SLA (packet §6, A-07). The marketing claim "99.9%+ uptime" (S14) is not a status signal. [Documented]

Checks earned: 4.0 of 11 applicable; verification coverage = 11 ÷ 11 = 100%.

What this means for you: the basics are solid. It's ordinary REST, it warns you when you're near the rate limit, and every response carries a trace ID that support can use. Running it in production is riskier:
- MagicDoor says the API can change at any time without notice, and there is no version number.
- The published documentation shows nothing that stops a retried payment post from being recorded twice.
- Nothing stops two people from overwriting each other's edits.
- There is no status page to check when something breaks.

## Category 3: Access Control and Safe Automation (placement)
- **C3.1 Read-only credentials: yes.** A key's `permissions` list takes `resource:action` codes (for example `properties:read`), so a read-only key is possible (S03). The MCP README suggests read-only permissions (S20). The live permission catalog lists 55 `read` permissions (T16). [Documented; Live-tested]
- **C3.2 Scoped credentials: yes.** Scoping is fine-grained, using any subset of 149 permissions across 57 categories (S03; T16). Leaving the list out gives an unscoped key, as with this run's `"*"` key (T01). [Documented; Live-tested]
- **C3.3 Multiple keys: yes.** Named keys are created on the Developer page or through `POST /company-portal/api-keys`, and the company-wide listing shows every key (S02, S03). [Documented]
- **C3.4 Rotation and revocation: yes.** Revocation is self-serve, immediate and permanent. Rotation means issuing a new key and revoking the old one, and keys can carry an expiry date (S03). [Documented]
- **C3.5 Test environment and isolation: partial.**
  - The docs state there is no sandbox and no test environment, and that calls hit production (S04, S07).
  - However, the vendor's own MCP configuration lists separate staging, demo and development hosts (S22). The staging key used in this run works on `*.magicdoor-test.com` and is not valid on the production auth host (packet §0, T01–T16).
  - So an isolated test environment with its own credentials exists, but no first-party page offers it to operators. That is the "exists but available only on request" case. Under Core rule 8, the observed environment outweighs the docs' denial.
  - [Documented S04, S07, S22; Live-tested]
- **C3.6 Delegated access: no.** No OAuth or other delegated-authorization flow is documented; S03 says explicitly "this is not OAuth" (A-09). The official MCP server runs locally and takes a pasted key through `MAGICDOOR_API_KEY` (S20), which earns no C3.6 credit. [Documented]

Checks earned: 4.5 of 6 applicable; verification coverage = 6 ÷ 6 = 100%.

What this means for you: you can give each tool or AI agent its own key, limit it to exactly what it needs (read-only, accounting-only, and so on), and revoke it instantly. That is a strong setup for safe automation. Two weak spots remain. There is no published way to test without touching your real data. And there is no "sign in with MagicDoor" approval flow, so any third-party app needs one of your keys.

## Category 4: Documentation and AI-Agent Readiness (placement)
- **C4.1 Complete self-serve reference: yes.**
  - The public reference covers all 967 endpoints, with method, URL, authentication, and parameters with types and enum values.
  - Every endpoint page has a cURL example, and 863 of them include a JSON response example.
  - The quickstart and walkthrough include worked TypeScript and Python code.
  - [Documented S02, S04, S08, S10]
- **C4.2 Reliable machine-consumable integration path: partial.**
  - There is no OpenAPI or Swagger file at any standard location (packet §6), and no supported client library (S07; A-09).
  - The only mechanism is the official MCP server `@magicdoor/mcp`. It lives in the vendor's GitHub organisation, is published under the vendor's npm scope, and is linked from the vendor's site, but it is read-only by design. A read-only MCP server counts as partial.
  - [Documented S17, S20–S23]
- **C4.3 AI-readable documentation: yes.**
  - `llms.txt` indexes all 975 pages.
  - `llms-full.txt` (7.2 MB) holds every reference page in full, with parameters, authentication and examples.
  - Every page has a `.md` version, advertised with `rel="alternate" type="text/markdown"`.
  - [Documented S09, S10]
- **C4.4 Kept current: partial.**
  - There is no API changelog or release notes: `/changelog` and `/release-notes` return 404, and S07 says no changelog is offered.
  - Currency signals that do exist:
    - The reference is generated from the source, and moved endpoints name their replacements (S07).
    - 16 endpoints carry undated deprecation notices (A-10).
    - API items appear only occasionally in the monthly product-update posts (S19).
  - The sitemap has no `lastmod` dates.
  - [Documented]
- AI agent path: official MCP server (read-only).
  - Package `@magicdoor/mcp` v0.1.0, running locally over stdio.
  - MCP standard version checked: built on `@modelcontextprotocol/sdk` 1.30.0, whose latest protocol is `2025-11-25` (S21; packet §5 note).
  - Not listed in the official MCP Registry (S24).
  - No OpenAPI specification and no SDKs.

Checks earned: 3.0 of 4 applicable; verification coverage = 4 ÷ 4 = 100%.

What this means for you: the documentation is unusually complete and ready for AI coding tools. Claude, Cursor and similar tools can load the whole reference at once. What's missing:
- A machine-readable spec or official code library for generating code.
- An MCP connector that can act, not just read.
- A changelog to warn you when things change.

## Category 5: Accessibility and Cost (gate 1)
- **C5.1 Self-serve API key: yes.** Any signed-in property manager can create a key under Profile → Developer → Create API key, with no sales or support step (S02, S03). [Documented]
- **C5.2 Not commercially gated: yes.**
  - Pricing says "No tiers, no gated features" and lists "API/MCP Access: Included" on the Advanced, Professional and Enterprise plans (S13).
  - The MCP server costs nothing extra (S17, S18).
  - [Documented]

Gate 1 allows: **A** (both yes); verification coverage = 2 ÷ 2 = 100%.

What this means for you: if you're a MagicDoor customer on any plan, you can create a key yourself today at no extra cost.

## Grade
- Gate 1, open access: allows A (C5.1 yes, C5.2 yes)
- Gate 2, documented capability: allows B. Capability coverage is 98.55% and write coverage is 100%, but C1.4 is no. No critical item scored 0.
- Letter from the gates: B. Binding gate: gate 2, because of C1.4 (change notification).
- Placement share: 11.5 of 21 Category 2–4 checks = 0.547619
  - Category 2: 4.0 of 11
  - Category 3: 4.5 of 6
  - Category 4: 3.0 of 4
- Score math: 80 + round(9 × 0.547619) = 80 + round(4.93) = **85 (B)**
- Official MCP server (one-step bump): **yes**. `@magicdoor/mcp` is maintained by MagicDoor: it sits in the MagicDoorInc GitHub organisation, is published under the `@magicdoor` npm scope, and has a vendor feature page and launch post. It reads MagicDoor data, read-only. [S17, S18, S20, S21, S23] After the step: **87 (B+)**.
- Published numeric score: **87 / 100**
- Letter grade: **B+**
- Evidence tier: baseline verified
- Overall verification coverage: 27 ÷ 27 = 100%. No group is Unable to verify, unverified checklist weight is 0% (the limit is 30%), and overall coverage is at least 80%.
- Partial-result flag: no
- Unresolved evaluator disagreements: none. The one disagreement, C2.11, was resolved to partial with no effect on the score.

Calculation (computed in Python):
```
items 32, weight 69 (objects 46, workflows 9, lifecycle 14)
one critical item = 3/69 = 4.3478%
capability 68/69 = 98.5507%   C1.1 45/46 = 97.8261%   C1.2 6/6 = 100%   C1.3 14/14 = 100%
share = (4.0 + 4.5 + 3.0) / (11 + 6 + 4) = 11.5/21 = 0.547619
B score = 80 + round(9 × 0.547619 = 4.928571) = 85  ->  MCP step B -> B+ = 87
Alternate C2.11 = yes: share 12/21 = 0.571429 -> 80 + round(5.142857) = 85 -> 87 (no change)
Alternate C1.4 = partial: A = 90 + round(6 × 0.547619 = 3.285714) = 93 -> MCP step A+ = 97
```

## Good for / Not built for
- **Good for:**
  - Reading and writing nearly every core property-management record: leases, rent and deposit ledgers, bills, reconciliations, owner distributions, work orders and applications.
  - Doing it with tightly scoped, revocable keys.
  - Asking AI assistants about your portfolio through the read-only MCP server.
- **Not built for:**
  - Real-time, event-driven automations. The published documentation shows no webhooks and no changed-since filter.
  - Long-lived production integrations that need a version contract, retry-safe payment posting, a published test environment, or third-party sign-in.

## Bottom line for a property manager
MagicDoor's API reaches almost everything in the product. The published documentation shows how to read and change leases, tenants, rent and deposit ledgers, bills, bank reconciliations, owner distributions and work orders. Any customer can create tightly limited keys at no extra cost. The biggest strengths are that breadth, the fine-grained revocable keys, and AI-ready documentation.

The biggest limitation is that MagicDoor publishes this as the interface its own apps use, not as a supported product. Its docs say the API can change at any time without notice. The published documentation also shows no way to be alerted when data changes and no protection against a retried payment post being recorded twice.

MagicDoor is not a bank. Payments run through third-party processors, and the bank accounts are your own, linked through Plaid. Its trust-accounting features (separate trust ledgers, deposit ledgers, three-way reconciliation, period locks) are documented and reachable through the API.

Build on it for scheduled syncs, reporting, AI assistants and carefully supervised write automations. Plan for scheduled re-checks and monitoring rather than real-time alerts, and test write automations carefully, because the docs offer no published sandbox.
