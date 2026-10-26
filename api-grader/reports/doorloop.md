# API Report Card: DoorLoop Property Management API (v1, with v2 OAuth)

## Run metadata
- Methodology version: 1.1
- Evaluating model: Claude Opus 5.5 (claude-opus-5-5)
- Date run: 2026-10-16 (operator local); live tests 2026-10-17 02:47–02:48 UTC
- Provisional evidence-packet version or ID: DL-2026-10-16-P1
- Final evidence-packet version or ID: DL-2026-10-16-F2 (frozen; F1 plus the operator-access attempt on the gated MCP endpoint, recorded in the amendment log; no mark changed). Merged v1 OpenAPI, rebuilt from the definitions embedded in each reference page: sha256 `f91910413a2372ef3937cb0a0f44e3f2db508cea56885aed474c76663ac0f28f`. Merged v2 OpenAPI: sha256 `2d205e0d3e7f6c494f3092d4d4ac5de6812cbf4fffe0c7f6a2317eaef3710af4`
- Evidence-discovery mode: tool-enabled discovery (clean run, with no prior runs or cached data used)
- Evidence tier: **baseline verified**
- Live-write method and safety: none. All writes were graded from documentation. No write, delete, payment, or notification was sent. Every live call was a GET.
- Minimum live-test battery: complete for steps 1–5. Step 6 was not run (no sandbox and no write authorization). Step 7 is N-A because the API documents no idempotency mechanism. Step 8 is N-A because the API offers no webhooks.
- Live tests performed: (1) authentication via `GET /users/me`; (2) paginated reads of `/properties`, pages 1 and 2, plus `/leases`; (3) filtered and incremental queries on `/tasks` (createdAt range), `/leases` (`filter_status`, `sort_by=updatedAt&sort_descending=true`) and `/lease-charges` (date range); (4) deliberate errors: no auth, bad token, unknown ID, malformed ID, `page_size` over the limit, bad enum value, unknown path; (5) inspection of rate-limit and trace headers on every response
- Live tests not possible: step 6, create or update a core resource (no sandbox exists and no live-data write authorization was given)
- Documentation-graded checks (baseline verified): C1.2, C1.3, C2.4. C2.9 was also graded from documentation, because conditional writes cannot be observed without a write.
- Host note: the operator asked for testing "against api.doorloop.com". That host serves the ReadMe documentation. The published OpenAPI `servers` entry, and every doc example, name `https://app.doorloop.com/api` as the production API (v2: `https://app.doorloop.com/api/v2`). All live calls therefore went to `app.doorloop.com/api`. The API key was never sent to the documentation host. The key was referenced only as `$DOORLOOP_API_KEY` and was confirmed absent from every saved artifact.

## Final evidence packet manifest
API reference (ReadMe, v1.0 default version), each page also fetched as Markdown with embedded OpenAPI 3.1 (`<url>.md`):
- https://api.doorloop.com/reference/introduction
- https://api.doorloop.com/reference/authentication
- https://api.doorloop.com/reference/pagination
- https://api.doorloop.com/reference/sorting
- https://api.doorloop.com/reference/rate-limiting
- https://api.doorloop.com/reference/open-api-31
- https://api.doorloop.com/reference/my-requests (placeholder page)
- 96 endpoint pages under https://api.doorloop.com/reference/… (accounts, communications, expenses, files, lease-charges, lease-credits, lease-payments, lease-reversed-payments, leases, leases/full, leases/move-in, leases/move-out, leases/tenants, notes, owners, properties, property-groups, reports ×4, tasks, tasks/update, tenants, units, users, vendor-bills, vendor-credits, vendors). The full list is in links.txt.
- https://api.doorloop.com/llms.txt
- https://api.doorloop.com/llms-full.txt (HTTP 404)
- https://api.doorloop.com/openapi/62bf5e83c9f2a70074e93684. This is the OpenAPI URL published on the open-api-31 page, and it returns HTTP 404.
- https://api.doorloop.com/mcp (ReadMe-hosted docs MCP endpoint; returns HTTP 401 `www-authenticate: Bearer realm="mcp"` / "Authorization required", with `x-readme-*` CORS allow-headers) — **unverified: gated by vendor-issued ReadMe key; operator attempted access**
- https://docs.readme.com/main/docs/mcp (ReadMe platform documentation, a non-DoorLoop source, used only to explain the access mechanism and the platform's standard toolset; it credits no DoorLoop capability)

API reference, v2.0:
- https://api.doorloop.com/v2.0/reference/introduction
- https://api.doorloop.com/v2.0/reference/authentication
- https://api.doorloop.com/v2.0/reference/rate-limiting
- https://api.doorloop.com/v2.0/reference/open-api-31
- https://api.doorloop.com/v2.0/llms.txt
- 32 v2 endpoint pages (leases, lease-payments, lease-charges, lease-credits, portfolios, owners, properties, tasks, tenants, units, vendors)

Vendor site, support, and status:
- https://www.doorloop.com/llms.txt
- https://www.doorloop.com/robots.txt
- https://www.doorloop.com/sitemap.xml
- https://www.doorloop.com/pricing
- https://www.doorloop.com/partner (redirect target of /api)
- https://www.doorloop.com/integrations
- https://www.doorloop.com/features/accounting
- https://www.doorloop.com/features/workflows
- https://www.doorloop.com/legal/terms (client-rendered; little text retrievable)
- https://status.doorloop.com
- https://status.doorloop.com/api/v2/summary.json
- https://status.doorloop.com/api/v2/incidents.json
- Live-test observations against https://app.doorloop.com/api, 2026-10-17 UTC (request IDs recorded in the checks below)

## Evidence-amendment log
Sources added during the single controlled verification pass:
- C3.3, C3.4, C5.1: https://support.doorloop.com/en/articles/6457764-using-zapier-with-doorloop. Added to confirm how keys are created: Settings → Company → "Zapier & API Keys", an SMS identity check, acceptance of the API ToS, then a named key created with "Add Line Item".
- C5.1: https://support.doorloop.com/en/articles/7902913-api-documentation-and-where-to-find-help. Added to check whether key access requires approval. It does not describe any approval step.
- C2.12: https://status.doorloop.com/uptime/9m0pkby0z852.json. Added to confirm that uptime percentages are published for the "DoorLoop API" component.
- C4.4, C2.10: https://support.doorloop.com/en/collections/3851236-doorloop-updates. Added to look for an API changelog. It holds product release notes only and has no API-specific entries.
- Provider fit only (unscored): https://support.doorloop.com/en/articles/6088168-set-up-property-bank-accounts. Covers Stripe payouts and escrow handling.
- C4.2 (operator-supplied gated-documentation attempt, 2026-10-17 ~03:10 UTC; methodology core rule 4 and step 9): the operator tried to grant access to https://api.doorloop.com/mcp.
  - The DoorLoop API key sent as `Authorization: Bearer` was rejected with HTTP 401, `www-authenticate: Bearer realm="mcp"`, and the response advertised `x-readme-conversation-id`, `x-readme-user-id`, `x-readme-project-id` and other `x-readme-*` allow-headers.
  - No OAuth discovery metadata is published: `/.well-known/oauth-protected-resource`, `/.well-known/oauth-protected-resource/mcp` and `/.well-known/oauth-authorization-server` all return 404.
  - The browser sign-in redirects to DoorLoop's login at `app.doorloop.com/auth/select-account`.
  - Per https://docs.readme.com/main/docs/mcp ("Private projects… Custom login (JWT/SSO) — `x-readme-auth: Bearer rdme_xxx` (ReadMe API key)"), access requires a ReadMe project key that only DoorLoop can issue.
  - ReadMe's documentation describes the platform's standard tools as `list-endpoints`, `get-endpoint`, `search-specs`, `list-specs`, `get-server-variables`, and `execute-request` ("Makes a live API call"), plus optional doc `search`/`fetch`. Which of these DoorLoop has enabled could not be observed.
  - Result: **unverified: gated by vendor-issued ReadMe key; operator attempted access.** No credit is given. C4.2 stays partial on its OpenAPI, SDK, and spec-accuracy grounds, and the score is unchanged.
  - The temporary `doorloop` entry was removed from the project `.mcp.json`.
- Targeted first-party searches for webhooks, idempotency, sandbox, read-only keys, changelog, and versioning found no further API sources. C1.4, C2.4, C2.8, C2.9, C3.5, and C4.4 are unchanged.

## API eligibility
- Qualifying API: **yes**
- API operator: DoorLoop Inc. The OpenAPI `info.contact` is "DoorLoop Inc.", the license is DoorLoop Terms, and the production server is `https://app.doorloop.com/api` (get-leases.md, embedded OpenAPI `info` and `servers`).
- Access or credential issuer: DoorLoop. For v1, a company admin creates API keys in DoorLoop under Settings → "Zapier & API Keys" (reference/authentication; support article 6457764). For v2, DoorLoop's OAuth server at `https://app.doorloop.com/oauth` issues tokens after a DoorLoop owner or full-access user approves an app that DoorLoop has registered (v2.0/reference/authentication §1–3).
- Eligibility basis: a documented first-party REST API exposes DoorLoop's own records (leases, tenants, ledgers, tasks, and more). Live `GET /users/me` returned 200 with a valid key (request ID `daebf246-2ff8-4e23-b741-ccbc3c7ae755`).

## Context
- Software category: Accounting/PMS platform
- What the API is for and its core objects and workflows: the API gives programmatic read/write access to a DoorLoop company's property-management records. Core objects are properties, units, leases, tenants, lease ledger transactions (charges, credits, payments, returned payments), the chart of accounts and financial reports, owners, vendors and bills, and tasks or work orders. Core workflows are reading the portfolio, posting lease charges and payments, and creating leases and moving tenants in and out.

## Provider and property-management fit
- What this product is: all-in-one residential property-management software covering accounting, leasing, rent collection, maintenance, and owner and tenant portals [www.doorloop.com/llms.txt, header paragraph]
- Bank status: **not a bank**. First-party materials present DoorLoop as software. Online payments are processed through Stripe, and bank sync runs through Plaid [support article 6088168 "Business Verification – Powered by Stripe"; www.doorloop.com/features/accounting "Bank sync & reconciliation"]
- Who provides any bank account or regulated banking service: the operator's own banks. Stripe handles payment processing and payouts. The accounting page mentions "Open a dedicated bank account and credit card," but the reviewed pages do not name a banking partner, so this point is unclear [features/accounting]
- What the customer actually receives: a PMS ledger and accounting system that tracks the operator's own bank accounts as chart-of-accounts entries, plus rent collection through Stripe [support 6088168; reference/get-accounts `filter_type=ASSET_BANK`]
- Property-management fit: **PM-specialized** [www.doorloop.com/llms.txt; www.doorloop.com/pricing]
- Documented PM-specific workflows: full lease creation with deposits, recurring rent, and tenant move-in (reference/post-leases-full); move-in and move-out (post-leases-move-in, post-leases-move-out); returned tenant payments (post-lease-reversed-payments); rent roll (get-reports-rent-roll); owner records and owner-filtered P&L, balance sheet, and cash-flow reports (get-reports-*); work orders and tenant or owner requests (get-tasks `filter_type`)
- Trust or fiduciary workflow support: **limited**. Leases expose `totalDepositsHeld`, and lease charges classify deposits (reference/get-lease-charges description in v2 llms.txt). In the product, escrow accounts exist, but online security-deposit payments land in the operating account and need a manual transfer (support 6088168). The API documents no trust-account reconciliation and no deposit-transfer workflow.
- Operational role and dependencies: DoorLoop is the system of record for leases and the ledger. Payment processing depends on Stripe and bank feeds depend on Plaid. A custom build needs no other PMS, but any event-driven design needs its own polling scheduler.

## Coverage classification (fixed before inspection)
This uses the methodology's default Accounting/PMS classification without deviation. The "State" column was filled in after inspection.

| Object or workflow | Class | Weight | Present / read-only / absent |
|---|---|---|---|
| Properties | critical | 3 | read-only (GET list/get only) |
| Units | critical | 3 | present, partial ops (GET + PUT; no create) |
| Leases | critical | 3 | present, partial ops (GET, create via /leases/full, move-in/out; no update) |
| Tenants | critical | 3 | present (full CRUD) |
| Lease ledgers/transactions | critical | 3 | present (charges, credits, payments CRUD; returned payments) |
| General ledger | critical | 3 | partial (chart of accounts CRUD + GL reports; no journal-entry read/write) |
| Bank accounts | critical | 3 | present as `ASSET_BANK` accounts (CRUD via /accounts) |
| Owners | important | 2 | present (CRUD) |
| Bills | important | 2 | present (vendor-bills, vendor-credits CRUD) |
| Payments | important | 2 | present (lease payments CRUD; expenses CRUD) |
| Applicants | important | 2 | partial (prospects via tenants `PROSPECT_TENANT`; no applications/screening) |
| Work orders/tasks | important | 2 | present (tasks CRUD + task updates; `WORK_ORDER` type) |
| Reconciliation | important | 2 | absent |
| Files | optional | 1 | present (CRUD + download) |
| Communications | optional | 1 | present (communication-log CRUD) |
| Custom fields | optional | 1 | absent |
| Associations (HOA) | optional | 1 | absent (property class only RESIDENTIAL/COMMERCIAL) |
| Inventory | optional | 1 | absent |
| Workflow: read core records | critical | 3 | present (live-verified) |
| Workflow: post ledger charges and payments | critical | 3 | present (POST /lease-charges, /lease-payments) — documentation-graded |
| Workflow: create and update leases | critical | 3 | partial (create yes; no lease update endpoint) — documentation-graded |

## Functional coverage map
- Core objects:
  - Properties (C3): read-only
  - Units (C3): read + update
  - Leases (C3): read + create + move-in/out
  - Tenants (C3): full
  - Lease transactions (C3): full
  - General ledger (C3): chart of accounts plus reports, with no journal entries
  - Bank accounts (C3): full, as GL accounts
  - Owners (I2): full
  - Bills (I2): full
  - Payments (I2): full for lease payments; no vendor-bill payment endpoint
  - Applicants (I2): prospects only
  - Tasks/work orders (I2): full
  - Reconciliation (I2): absent
  - Files (O1): full
  - Communications (O1): full
  - Custom fields (O1): absent
  - Associations (O1): absent
  - Inventory (O1): absent
- Primary operational workflows: read the portfolio and ledgers; create a complete lease in one transaction (`POST /leases/full`); post charges, credits, and payments; record returned payments; create and update tenants, owners, and vendors; create and update tasks and work orders and post task updates; manage bills, expenses, files, notes, and communication logs; pull rent roll, P&L, balance sheet, and cash flow
- Principal lifecycle changes:
  - Tenant move-in (C3): present
  - Tenant move-out (C3): present
  - Lease renewal or term change (C3): absent, since no lease update endpoint exists
  - Return or reverse a payment (C3): present
  - Void or delete a charge, credit, or payment (C3): present (DELETE)
  - Task or work-order status to completion (I2): present (PUT task `status`)
  - Void or delete a bill (I2): present
  - Deactivate or archive owners, vendors, units, and tenants (I2): present (`active` flag, DELETE)
  - Reconcile or close a period (I2): absent
  - Approve or reject an application (I2): absent

## Category 1: Functional Coverage and Usefulness: 7.5/15
- **C1.1 Object coverage: partial. Weighted coverage = 26/38 = 68%.**
  - Critical objects: properties 0.5, units 0.5, leases 0.5, tenants 1, lease transactions 1, GL 0.5, bank accounts 1, which gives 15/21.
  - Important objects: owners 1, bills 1, payments 1, applicants 0.5, tasks 1, reconciliation 0, which gives 9/12.
  - Optional objects: files 1, communications 1, custom fields 0, associations 0, inventory 0, which gives 2/5.
  - No critical object is absent.
  - Citations: reference/get-properties and get-property (no POST/PUT exists in the spec); reference/put-unit; post-leases-full, post-leases-move-in, post-leases-move-out; get/post/put/delete-tenant; lease-charge, lease-credit, and lease-payment CRUD pages; get-accounts `filter_type` enum including `ASSET_BANK`; get-tenants `filter_type` enum `PROSPECT_TENANT`; get-tasks `filter_type` `WORK_ORDER`.
  - Live reads of `/properties` (total 76) and `/leases` (total 213) succeeded.
- **C1.2 Core operational actions: partial. Weighted coverage = 24.5/38 = 64%.**
  - Critical (13.5/21): properties 0, units 0.5, leases 0.5, tenants 1, lease transactions 1, GL 0.5, bank accounts 1.
  - Important (9/12): owners 1, bills 1, payments 1, applicants 0.5, tasks 1, reconciliation 0.
  - Optional (2/5): files 1, communications 1, others 0.
  - Charges and payments can be posted, and leases can be created, so no critical write workflow is absent.
  - Citations: post-lease-charge, post-lease-payment, post-leases-full, post-tenant, put-tenant, post-owner, put-owner, post-task, put-task, post-vendor-bill, post-account.
  - Documentation-graded. No write was observed.
- **C1.3 Delete or lifecycle actions: partial. Weighted coverage = 18/25 = 72%.**
  - Critical (12/15): move-in 1, move-out 1, lease renewal or term change 0, return payment 1, void/delete charge, credit, or payment 1.
  - Important (6/10): task completion 1, delete bill 1, deactivate or delete records 1, reconcile 0, application decision 0.
  - Lease renewal is a critical lifecycle action and it is absent, because no `PUT /leases/{id}` exists.
  - Citations: post-leases-move-in, post-leases-move-out, post-lease-reversed-payments ("marks an existing Lease Payment as returned"), delete-lease-charge, delete-lease-credits-leasecreditid, delete-lease-payment, put-task (`status` enum incl. `COMPLETED`), delete-vendor-bill, delete-tenant.
  - Documentation-graded.
- **C1.4 Change notification: partial.**
  - No webhooks or events are documented. ReadMe project config shows `"webhooks":[]`, and no webhook page exists in v1 or v2.
  - Change detection is possible by polling. Every list endpoint accepts `sort_by` on any field plus `sort_descending` (reference/sorting), and many lists have date or createdAt filters (get-tasks, get-owners, get-vendors, get-files, get-notes, lease-transaction `filter_date_*`).
  - Live test: `GET /leases?sort_by=updatedAt&sort_descending=true` returned the newest-modified leases first (all `updatedAt` 2026-10-16T22:14:56Z; request ID `8ee1540a-5276-4066-a9ab-e7f74399131c`). `filter_createdAt_from/to` on `/tasks` was honored (total 1314 → 201, all createdAt ≥ 2026-09-01; request ID `29156237-c408-4198-a5db-f95c1579e3cf`).
  - Limitation: there is no updated-since filter, and deletions cannot be detected by polling.
  - DoorLoop's Zapier triggers belong to Zapier's interface and are not credited.
- Score math: earned 2.0 of 4 applicable checks; unrounded fraction = 0.5000; category points = 7.500/15 (displayed 7.5); verification coverage = 4/4 = 100%
- What this means for you: you can read nearly everything and do the day-to-day ledger work: create leases, move tenants in and out, post charges and payments, record bounced payments, and manage tasks, owners, vendors, and bills. You cannot create properties or units, edit or renew an existing lease, read journal entries, reconcile, or handle rental applications through the API. Nothing pushes changes to you, so your tools must poll on a schedule.

## Category 2: API Design, Reliability, and Operability: 5.5/10
- **C2.1 Modern API conventions: yes.** Resource-oriented REST with GET/POST/PUT/DELETE, JSON in and JSON out (reference/introduction: "organized around REST… predictable resource-oriented URLs… standard HTTP response codes, authentication, and verbs"). Confirmed live with JSON responses on `/users/me`, `/properties`, and `/leases`. One limitation: v1 `PUT` replaces the whole record and does not patch it (reference/put-unit).
- **C2.2 Consistent typing: partial.**
  - Live values were consistently typed in every response sampled: booleans were booleans, money fields were numbers, and timestamps were ISO strings.
  - The published schemas disagree with live payloads in several places:
    - Lease `rolloverToAtWill` is `type: string` in the spec but a boolean live.
    - The spec has `totalBalancedue`, `TotalRecurringCharges`, and `evictonPending`, while live responses return `totalBalanceDue` and `totalRecurringCharges`, and the filter is spelled `filter_evictionPending`.
    - Task and note `createdAt`/`updatedAt` are `type: number` in the spec but ISO strings live.
  - Citations: OpenAPI `components.schemas.Lease`, `task`, and `note` in the merged packet spec; live `/leases` and `/tasks` responses on 2026-10-17.
  - This is limited to a few fields, but it touches core objects.
- **C2.3 Structured errors: partial.**
  - HTTP status codes were correct (401, 404, 400) and messages were usable, but the error shapes vary and there is no stable machine-readable code field.
  - Observed shapes:
    - 401: `{"name":"401 Unauthorized","message":"Your session has expired. Please log in again. (E250)","statusCode":401,"httpErrorCode":401}`. The code E250 appears only inside the message text, and an API-key caller is told their "session has expired" (request ID `70aa337c-21d4-4989-9543-8f276c829bce`).
    - 404 on a resource: `{"name":"GET /api/leases/:id","message":"Not found",…}` (request ID `7a9d7c45-60a7-412c-9aee-05d9a77ad284`).
    - 400 validation: `{"errors":{"page_size":"page_size must not be greater than 1000"},"message":"Validation Failed"}` (request ID `4d26b74a-3213-4628-9486-146251838a62`).
    - 400 on an invalid enum value returned a misleading `"filter_status":"This field is required"` (request ID `d3ef9434-d30c-420c-9ffa-e231eaf66be9`).
    - 404 on an unknown path returned `{"error":"Not found"}` (request ID `2782bb96-d0ca-4ac5-81b0-de1c2b9c2c3f`).
  - The spec defines no error schema: error responses are bare descriptions such as `"400": {"description": "Bad Request"}`.
  - v2 documents OAuth error codes (`invalid_token`, `insufficient_scope`), but only for authentication (v2.0/reference/authentication §Errors).
- **C2.4 Duplicate prevention: no (documentation-graded).**
  - The packet contains no idempotency key, request de-duplication, or natural-key protection for consequential writes such as `POST /lease-payments`, `POST /lease-charges`, `POST /vendor-bills`, or `POST /expenses`. The merged spec has zero occurrences of "idempot".
  - `POST /leases/full` is transactional and de-duplicates *inline new tenants* by email (post-leases-full description), but a retried lease creation is not protected.
  - Live step 7 is N-A because no idempotency is claimed.
- **C2.5 Graceful handling under load: yes.**
  - reference/rate-limiting documents 429 with "Wait the number of seconds in the `Retry-After` response header", gives an explicit edge backoff rule ("exponentially with jitter, starting at no less than 30 seconds"), and states limits of 50/min and 500/hour per credential and 10 rps per IP.
  - Live: every authenticated response carried `ratelimit-limit: 500`, `ratelimit-remaining`, and `ratelimit-reset`.
  - Observed oddity: `ratelimit-remaining` stayed at 499 across about 20 calls, and `ratelimit-reset` varied between 611 and 1635 seconds. Treat the remaining-count header as approximate. A 429 was not deliberately triggered, to avoid loading production.
- **C2.6 Pagination for large collections: partial.**
  - Documented offset pagination (`page_number`, `page_size` default 50, max 1000) with a `total` count (reference/pagination), plus a user-selectable `sort_by` (reference/sorting).
  - Live: `/properties` page 1 and page 2 with `sort_by=createdAt` returned distinct records with `total: 76` on both (request IDs `bc550e10-…`, `c0c697c4-…`). `page_size=5000` was rejected with a clear 400.
  - Limitation: no stable-ordering guarantee is documented ("default varies by resource"), and offset paging over changing data can skip or repeat rows.
- **C2.7 Bulk or incremental export: partial.** Full datasets can be pulled at up to 1000 rows per page, with filters and `sort_by=updatedAt` (live-verified above). There is no async export job, bulk endpoint, or documented updated-since sync. The report endpoints (rent roll, P&L, balance sheet, cash flow) are summaries, not data exports.
- **C2.8 Webhook security and delivery reliability: N-A.** No webhooks are offered. Their absence is already penalized in C1.4.
- **C2.9 Concurrency and conflict control: no (documentation-graded).**
  - No ETag/If-Match, version field, or 409 semantics are documented. The spec has zero occurrences of "ETag", "If-Match", or "409".
  - `PUT` is full replacement, and put-unit warns that omitted properties are cleared, so lost updates are a real risk.
  - Live GETs return a weak `etag` header, but no documentation says it is honored on writes.
- **C2.10 Versioning and backward compatibility: partial.**
  - The docs have v1.0 and v2.0 versions, and v2 has an explicit path version, `https://app.doorloop.com/api/v2` (v2.0/reference/authentication table).
  - v1 has no version identifier in its path (`/api`).
  - The v2 guide states "Paths and payloads stay the same" as v1.
  - No backward-compatibility policy (breaking vs. non-breaking) and no deprecation windows were found in the docs or support center.
- **C2.11 Request traceability: partial.**
  - Every live response, including 401s, carried a unique `x-global-id` UUID, and authenticated responses also carried `x-documentation-url: https://api.doorloop.com/logs/<uuid>` (for example, `daebf246-2ff8-4e23-b741-ccbc3c7ae755`).
  - Neither header is documented. The rate-limiting support guidance asks for IPs and a UTC time range, not a request ID. The "My Requests" page is an unfilled placeholder (reference/my-requests).
- **C2.12 Service availability and status transparency: yes.**
  - status.doorloop.com is a public status page with a dedicated "DoorLoop API" component, subscribable incident updates, and incident history (incidents.json, which includes "Service Disruption" on 2026-07-24).
  - Monthly uptime percentages are published for the API component (status.doorloop.com/uptime/9m0pkby0z852.json, `months[].uptime_percentage`).
  - No public SLA was found, but uptime data satisfies the check.
- Score math: earned 6.0 of 11 applicable checks (C2.8 N-A); unrounded fraction = 0.54545; category points = 5.4545/10 (displayed 5.5); verification coverage = 11/11 = 100%
- What this means for you: the API is plain REST and easy to call. Rate limits are documented, and a status page shows API uptime. Production automations still need defensive code:
  - Error formats vary.
  - Retries can create duplicate payments or charges.
  - Updates overwrite whole records with no conflict protection.
  - There's no bulk export.
  - The spec's field names and types are not fully trustworthy.

## Category 3: Access Control and Safe Automation: 5.0/5
- **C3.1 Read-only credentials: yes.** v2 OAuth tokens carry only the approved `<resource>:<action>` scopes, and `read` means "List and get" (v2.0/reference/authentication §Scopes). Each endpoint declares its scope (for example, `GET /leases` requires `leases:read` in the v2 OpenAPI `security`). A `*:read`-only token is therefore read-only. Limitation: v2 apps must be registered by contacting DoorLoop (§1). v1 keys inherit the creating user's role, and no read-only v1 role is documented.
- **C3.2 Scoped credentials: yes.** v2 offers fine-grained resource and action scopes (`owners:read`, `tasks:create`, `tenants:update`, …; v2 OpenAPI `components.securitySchemes.OAuth2.flows.authorizationCode.scopes`). v1 has role-based restriction only ("Each API token is assigned an access role…", reference/authentication, 405 callout).
- **C3.3 Multiple keys: yes.** Keys are named and created per line item ("enter a name for this key in the Key Name field… click Add Line Item… This will create and save a new api key", support article 6457764). The docs also say "view and manage your API keys" (reference/authentication). Live responses carry an `x-api-key-id` header that identifies the individual key.
- **C3.4 Rotation and revocation: yes.**
  - v2 revocation is self-serve: the user can disconnect the app in DoorLoop and "All of its tokens stop working right away", and apps can revoke a token at `/oauth/token/revocation`. Refresh tokens rotate on every use (v2.0/reference/authentication §5, §Disconnecting).
  - For v1, keys are managed self-serve in settings (reference/authentication). An explicit v1 delete or rotate step is not spelled out.
- **C3.5 Test and production isolation: N-A.** No sandbox or test environment is documented in v1, v2, or the support center, and the spec lists only the "Production" server.
- Score math: earned 4.0 of 4 applicable checks (C3.5 N-A); unrounded fraction = 1.0; category points = 5.000/5 (displayed 5.0); verification coverage = 4/4 = 100%
- What this means for you: with the newer OAuth (v2) path you can give an app or AI agent narrow, read-only, or per-resource access and cut it off instantly. The catch is practical:
  - v2 apps must be registered with DoorLoop and currently cover fewer endpoints.
  - The everyday v1 key you create yourself can do whatever its user can do.
  - There is no sandbox, so every test touches live data.

## Category 4: Documentation and AI-Agent Readiness: 3.1/5
- **C4.1 Complete self-serve reference: partial.** The reference is public, with an auth guide, pagination, sorting, rate limits, and per-endpoint parameters and schemas (api.doorloop.com/reference/*). Only 20 of 96 v1 operations include a worked response example (merged OpenAPI, `responses.200.content.*.example(s)`), and error bodies are undocumented. Field names and types also disagree with live data (see C2.2), so some flows still need trial and error.
- **C4.2 Reliable machine-consumable integration path: partial.**
  - OpenAPI 3.1 definitions are embedded in every reference page's Markdown (96 operations, 43 schemas once merged).
  - The single spec URL the docs publish, https://api.doorloop.com/openapi/62bf5e83c9f2a70074e93684, returned HTTP 404, so the spec must be assembled from individual pages.
  - The schemas need manual correction (C2.2).
  - No official SDK exists. The open-api-31 page suggests generating your own.
  - MCP: https://api.doorloop.com/mcp is a ReadMe-hosted docs MCP server. Its tools are **unverified: gated by vendor-issued ReadMe key; operator attempted access** (amendment log). ReadMe's platform toolset is centered on endpoint and spec lookup, with an `execute-request` passthrough. The tools DoorLoop has enabled could not be observed, so the server earns no credit.
- **C4.3 AI-readable documentation: yes.** Every reference page is available as clean per-endpoint Markdown with the full OpenAPI fragment (`<page>.md`; all 103 v1 and 39 v2 pages retrieved), and each page's front matter declares `agentTools.projectIndex`. Limitation: the v1 `llms.txt` indexes only 2 pages, and `llms-full.txt` returns 404.
- **C4.4 Kept current: partial.**
  - Reference pages carry recent `updatedAt` stamps (for example, authentication 2026-09-24 and v2 authentication 2026-10-01), and v2 rolled out with a migration note.
  - The ReadMe changelog module is disabled ("No Changelogs" / `changelog visibility: disabled`).
  - The support "DoorLoop Updates" collection covers product releases, not API changes.
  - Docs-vs-live drift (C2.2) shows the reference is not reliably updated when the API changes.
- Score math: earned 2.5 of 4 applicable checks; unrounded fraction = 0.625; category points = 3.125/5 (displayed 3.1); verification coverage = 4/4 = 100%
- What this means for you: AI coding tools can read DoorLoop's docs page by page in Markdown, which helps. But the downloadable spec link is broken, there are no SDKs, examples are sparse, and there is no API changelog. Expect to correct some field names and types by hand, and to find changes by testing rather than reading release notes.

## Category 5: Accessibility and Cost: 15.0/15
- **C5.1 Self-serve API key: yes.** A company user creates keys in Settings → Company → "Zapier & API Keys" after an SMS identity code and acceptance of the API Terms. There is no sales call or approval step (support article 6457764; reference/authentication). The operator for this run provisioned their own key, and it worked live. Note: the www.doorloop.com/partner page says DoorLoop is "selective about who gets access", and v2 OAuth apps must be registered by contacting DoorLoop. These describe partner and third-party app access, not an operator's own key (see disagreements).
- **C5.3 Not commercially gated: yes.** The base plan, "DoorLoop One", lists "Unlimited users, unlimited document storage and full API access", and the pricing FAQ states that "Everything that used to sit behind Premium, including… the API… is in DoorLoop One" (www.doorloop.com/pricing). The FAQ also says "Existing plans and prices stay as they are", so legacy Starter or Pro customers may still lack access, as the support article 6457764 Zapier note indicates.
- Score math: earned 2.0 of 2 applicable checks; unrounded fraction = 1.0; category points = 15.000/15 (displayed 15.0); verification coverage = 2/2 = 100%
- What this means for you: on any current plan, you can generate your own API key in settings today, with no sales call or upgrade. If you are on a legacy Starter or Pro plan, confirm that your plan includes the API.

## Total
- Raw: 36.08 / 50 (7.5000 + 5.4545 + 5.0000 + 3.1250 + 15.0000 = 36.0795)
- Normalized before rounding: 72.16 / 100
- Published numeric score: **72 / 100**
- Letter grade: **C-**
- Evidence tier: baseline verified. Write checks C1.2, C1.3, and C2.4 were documentation-graded, plus C2.9.
- Overall verification coverage: 25/25 applicable checks = 100%. Gate passed: no category is Unable to verify, coverage is at least 80%, and steps 1–5 are complete.
- Partial-result flag: **yes**.
  - The DoorLoop MCP server (https://api.doorloop.com/mcp) is unverified: gated by vendor-issued ReadMe key; operator attempted access. Only DoorLoop can issue the needed `x-readme-auth` ReadMe key. If DoorLoop supplies one and the enabled tools prove to cover core operations, C4.2 could move from partial to yes: +0.625 raw, +1.25 normalized, 73/C.
  - Write-path checks would move to observed evidence with a sandbox or operator-authorized controlled-live fixtures.
- Unresolved evaluator disagreements:
  - C5.1 (yes vs. partial). The partner page's "selective" language could be read as approval sometimes being required. Effect: −3.75 raw, −7.5 normalized, giving 65/D.
  - C2.2 (partial vs. no). The spec-vs-live type mismatches touch core lease and task fields. Effect: −0.45 raw, −0.9 normalized, giving 71/C-.
  - C4.3 (yes vs. partial). The llms.txt index lists only 2 pages. Effect: −0.625 raw, −1.25 normalized, giving 71/C-.
  - C3.1/C3.2 (yes vs. partial). Scoped and read-only credentials require DoorLoop-registered v2 apps. Effect: −1.25 raw each, −2.5 normalized each.

## Bottom line for a property manager
You can generate a DoorLoop API key yourself on any current plan and build working tools today: rent-roll and delinquency dashboards, lease and tenant syncs, posting charges and payments, recording returned payments, and creating or updating work orders. All of it runs on plain, documented REST with published rate limits and a status page. The biggest strength is easy, ungated access plus scoped OAuth (v2) for safely connecting apps or AI agents. The biggest limitations are that DoorLoop never pushes changes to you, and that the API has gaps an operator will notice:
- No webhooks.
- No property or unit creation.
- No lease edits or renewals.
- No reconciliation or journal entries.
- No protection against duplicate payments when a request is retried.

DoorLoop is property-management software, not a bank. Payments run through Stripe and bank feeds through Plaid. The API does not document trust or escrow reconciliation workflows, so trust-accounting compliance still rests on your own bank accounts and processes.
