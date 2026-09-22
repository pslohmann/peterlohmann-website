# API Report Card: Mason (Enduring Labs, Inc.) — External API v2

## Run metadata
- Methodology version: 1.1
- Evaluating model: Claude Fable 5.1 (claude-fable-5-1)
- Date run: Monday 2026-09-21 (live battery executed 2026-09-22 01:49 UTC = 2026-09-21 19:49 MDT)
- Provisional evidence-packet version or ID: MASON-EP-2026-09-21-p1
- Final evidence-packet version or ID: **MASON-EP-2026-09-21-f1** (frozen; supersedes the withheld 2026-09-04 packets v1/v2)
- Evidence-discovery mode: tool-enabled discovery
- Evidence tier: **Fully verified — controlled live (read path).** Write-path steps 6–8 are **not applicable**: the published contract contains only `GET` endpoints, documents no idempotency mechanism, and offers no webhooks. See the labeling note under "Unresolved evaluator disagreements."
- Live-write method and safety: **none — no writes performed.** Operator instruction for this run: no live writes; grade write checks from documentation. The API publishes no write endpoints, so no write was possible in any case. C1.2 and C1.3 are documentation-graded.
- Minimum live-test battery: **steps 1–5 complete.** Step 6 N-A (no write endpoints in the contract; operator prohibited live writes). Step 7 N-A (no idempotency documented). Step 8 N-A (no webhooks documented).
- Live tests performed: authenticate (valid / invalid / missing token); read `/work-orders` and page three cursor pages; last-page behaviour on a narrow filter; `updatedAfter`, `status`, invalid-date and unknown-parameter filters; `/work-order-activity-logs` read; deliberate errors (random UUID, malformed ID, unknown resource, `limit=abc`, `limit=1000`, `limit=0`, missing required params on `/on-call-coverage`); response-header capture; 40-request sequential burst; live-vs-schema typing check on 5 core resources (126 fields, 250 records).
- Live tests not possible: none on the read path.
- Documentation-graded checks: C1.2, C1.3 (no write surface exists to observe).
- Credential and authorization: production bearer token issued by the vendor to the operator's account on 2026-09-21 (Gmail thread `[mail thread id withheld]`, message `[id withheld]`); stored in the operator's 1Password (Agents vault, item `[id withheld]`); loaded at call time from the secret store, never printed. Operator authorized read-only live testing in this session.
- Redaction: all captured evidence cites record IDs only. No tenant names, addresses, phones, emails, account numbers, or dollar amounts were captured or printed. See `evidence/live-battery.txt`.

## Final evidence packet manifest
All files under `evidence/` with SHA-256 in `evidence/SHA256SUMS.txt` and inline below.
1. https://www.thisismason.com/docs/api-reference — public developer page ("Mason developer API"), accessed 2026-09-21. Saved: `evidence/docs-api-reference.html` (sha256 7a2f5bd4…511fe7).
2. https://www.thisismason.com/docs/api-reference/api.md — full Markdown API guide, 74,087 bytes. Saved: `evidence/api.md` (sha256 b9b8fbf2…0a02e6).
3. https://www.thisismason.com/openapi.json — OpenAPI **3.1.0**, title "Mason External API", `info.version` `2-b0dfb930aad19685`, 242,773 bytes; also served at `https://mason.enduring-labs.com/api/external/v2/openapi.json` (HTTP 200, no token). Saved: `evidence/openapi.json` (sha256 decdc3bf…d1f9fb).
4. https://www.thisismason.com/legal/terms — Terms of Service (operator identity, §3 credentials, §5 availability). Saved: `evidence/terms.txt`.
5. https://www.thisismason.com/ and https://www.thisismason.com/llms.txt — product pages, "Plans" section, PM workflows (accessed 2026-09-04 and re-checked 2026-09-21).
6. Live-test observations against `https://mason.enduring-labs.com/api/external/v2`, 2026-09-22 01:49 UTC. Saved: `evidence/live-battery.txt` (sha256 44bee98d…8372b).
7. Product-interface observation, operator's logged-in Mason account, Settings page, 2026-09-04 (carried forward from the earlier packet): no API-key, developer, webhook, or integrations section; "Switch to Test / Toggle Test/Live PM" workspace toggle present.
8. Negative probes, 2026-09-21: `status.thisismason.com` and `status.enduring-labs.com` do not resolve; `/docs`, `/docs/changelog`, `/docs/api-reference/changelog` return 404.
9. Credential-issuance observation: vendor e-mail of 2026-09-22 00:01 UTC delivering the token by 1Password share link and the docs URL (message ID only; contents not reproduced).

## Evidence-amendment log
Provisional marks were assigned from items 1–3 and 6. The controlled verification pass added:
- **C2.2:** OpenAPI `Invoice.selectedMarkupPercentage` / `selectedDiscountPercentage` declared as `string` ("decimal string; 10 means ten percent") while all money fields are `integer` cents — found by a targeted scan of numeric-looking fields. Moved C2.2 from provisional `yes` to `partial`.
- **C2.3:** `/on-call-coverage` without required `start`/`end` returned HTTP 400 with the documented `{error}` envelope — adds a 400 observation to the 401/404 set. No change to mark.
- **C2.12:** Terms of Service §5 ("We strive to maintain 99.9% uptime… Scheduled maintenance windows will be communicated in advance") added; status-page subdomains re-probed (do not resolve). Moved C2.12 from provisional `no` to `partial`.
- **C3.4:** OpenAPI 401 response description ("Missing, malformed, invalid, **inactive, or expired** bearer token") added as evidence that server-side token deactivation exists. Moved C3.4 from provisional `no` to `partial`.
- **C3.5, C5.1:** 2026-09-04 authenticated Settings observation (item 7) carried into this packet.
- **C4.4:** `/openapi.json` response headers checked for `ETag`/`Last-Modified` (only `cache-control: no-store` returned; the spec's own text says "ETag supports identifying the published document"). Contract-revision identifier retained as the only currency signal. No change to mark.
- **C1.1:** targeted search for a tags object in all 15 component schemas — none (the only "tag" hits are OpenAPI operation tags). Tags scored absent.
No sources were removed.

## API eligibility
- Qualifying API: **yes**
- API operator: Enduring Labs, Inc. — Terms §1 "operated by Enduring Labs, Inc."; OpenAPI `servers[0].url` = `https://mason.enduring-labs.com/api/external/v2`; docs page footer "© Enduring Labs, Inc."
- Access or credential issuer: Enduring Labs, Inc. — docs page: "Mason provides a bearer token scoped to your property management account"; token delivered by the vendor to the operator on 2026-09-21 (item 9).
- Eligibility basis: a public, first-party OpenAPI 3.1 contract and Markdown guide identify the interface, its 25 endpoints expose Mason's own objects (work orders, calls, texts, emails, invoices, estimates, contacts, properties, units, scheduling blocks, on-call coverage, activity and control logs), and the docs state how access is authorized (vendor-issued account-scoped bearer token). Live authentication succeeded (HTTP 200) on 2026-09-22 01:49 UTC.

## Context
- Software category: **maintenance / operations tool**
- What the API is for and its core objects and workflows: Mason is an AI maintenance coordinator that sits on top of a PMS. The External API v2 is a **read-only** window into everything Mason records — work orders and their activity logs, the calls, texts and emails behind them, vendor estimates and invoices, contacts, properties, units, technician scheduling blocks, and on-call coverage — so an operator can pull that data into their own reporting, sync, or agent tooling. It exposes no way to create, assign, dispatch, approve, or close anything.

## Provider and property-management fit
- What this product is: an AI assistant that answers resident maintenance calls, texts and emails, creates work orders, dispatches vendors or in-house techs, collects estimates and chases invoices for residential property managers (thisismason.com/llms.txt; product pages /intake, /vendor-dispatch, /in-house-maintenance, /invoicing).
- Bank status, when relevant: **N-A** — not represented as a bank anywhere in the reviewed materials.
- Who provides any bank account or regulated banking service: **none** — no evidence Mason holds or moves funds; its billing role is coding and routing vendor bills to the PMS ledger (thisismason.com/invoicing).
- What the customer actually receives: a subscription AI service priced by door count and plan tier (After-Hours / Intake / Full Suite / In-House) that works the maintenance queue and writes back into the customer's PMS (thisismason.com "Plans").
- Property-management fit: **PM-specialized** — property management is the product's entire purpose; five core PM workflows documented.
- Documented PM-specific workflows: after-hours emergency triage and dispatch; resident maintenance intake → work order; third-party vendor dispatch, estimates, follow-up; in-house technician routing, scheduling, billing; vendor-invoice chasing, coding, and ledger routing (llms.txt + the five product pages).
- Trust or fiduciary workflow support, when relevant: **not documented** — no trust, client-fund, security-deposit, or escrow workflow appears in any reviewed material.
- Operational role and dependencies: Mason is a maintenance-operations layer that requires AppFolio, Rentvine, Buildium, or Propertyware underneath it as the system of record for properties, units, leases, residents, and the ledger.

## Coverage classification (fixed before inspection)
Category: maintenance/operations. Default classification applied unchanged (identical to the 2026-09-04 withheld run).

| Object or workflow | Class | Weight | Present / read-only / absent |
|---|---|---|---|
| Work orders | critical | 3 | present, **read-only** — `GET /work-orders`, `/work-orders/{id}` |
| Status transitions | critical | 3 | present, **read-only** — `status` field; `GET /work-order-activity-logs` (`eventType`) |
| Vendor / technician assignment | critical | 3 | present, **read-only** — `vendorContactId`, `assignedUsers`; `SchedulingBlock.contactId` |
| Vendors | important | 2 | present, **read-only** — `GET /contacts` (`contactType` = vendor) |
| Scheduling / appointments | important | 2 | present, **read-only** — `GET /scheduling-blocks` |
| Residents | important | 2 | present, **read-only** — `GET /contacts` (`contactType` = tenant) |
| Units / properties | important | 2 | present, **read-only** — `GET /units`, `GET /properties` |
| Estimates | optional | 1 | present, **read-only** — `GET /estimates` |
| Invoices | optional | 1 | present, **read-only** — `GET /invoices` |
| Owner approval | optional | 1 | present, **read-only** — `Estimate.approvedByRole/pmApprovedAt`, `Invoice.pmApproved/pmRejected` |
| Tags | optional | 1 | **absent** — no tag object or field in any of the 15 component schemas |
| **Workflow:** create a work order | critical | 3 | **absent** — no `POST` in the contract |
| **Workflow:** assign it | critical | 3 | **absent** |
| **Workflow:** transition status to completion | critical | 3 | **absent** |

## Functional coverage map
- Core objects: as tabled — 10 of 11 present, all read-only; tags absent.
- Primary operational workflows: none writable. The Markdown guide is explicit: "Use only the documented read-only GET endpoints… Do not infer write capabilities from response fields" (api.md, Agent guidance). The spec: "This specification describes implemented endpoints only" — every operation is `GET`.
- Principal lifecycle changes (readable, not actionable): status change (created → reviewed → dispatched → work_in_progress → work_done → closed / cancelled / duplicate, api.md `status` parameter), estimate approve/reject, invoice approve/reject, scheduling-block supersession (`supersedesBlockId`), token inactive/expired.

## Category 1: Functional Coverage and Usefulness: 1.9/15
- **C1.1 Object coverage: no** — weighted coverage = **47.6%** (10 present-read-only × 0.5 = 10.0 ÷ Σweight 21). Every critical and important object is present but read-only where writes are operationally expected; tags absent. Citations in the table above (OpenAPI paths). Falls just under the 0.50 `partial` floor.
- **C1.2 Core operational actions: no** — weighted coverage = **0%**. No create/update operation exists for any object or workflow; all 25 operations are `GET` (openapi.json `paths`; api.md "read-only GET endpoints"). Documentation-graded: nothing to observe.
- **C1.3 Delete or lifecycle actions: no** — weighted coverage = **0%**. Status change, cancel, close, approve, reject are all visible as fields but none is invocable (no `PATCH`/`POST`/`DELETE` in the contract). Documentation-graded.
- **C1.4 Change notification: partial** — no webhooks or events are offered; the only mechanism is incremental polling, which is efficient and was live-verified: `updatedAfter` on `/work-orders` (api.md line 38; live: `updatedAfter=<3 days ago>` honoured, 0 records, all `lastUpdated ≥ bound`), plus `GET /work-order-activity-logs` with `createdAfter` as an event stream (live: 5 records, fields `eventType`, `internalWorkOrderId`, `timestamp`). Documented limitation: "Related-record changes do not necessarily advance this timestamp" and "Incremental date bounds… do not provide complete historical changes" (api.md lines 27, 38).
Score math: earned 0.5 of 4 applicable checks; unrounded fraction = 0.125; category points = **1.875 → 1.9/15**; verification coverage = 4/4 = 100%.
What this means for you: you can *see* everything Mason knows about a work order, but you cannot *do* anything to it through the API — no creating, assigning, approving, or closing. To catch changes you poll `updatedAfter` (or read the activity log); there is no push.

## Category 2: API Design, Reliability, and Operability: 5.6/10
- **C2.1 Modern API conventions: yes** — resource-oriented REST over HTTPS, JSON envelopes `{data, pagination}`, standard `GET` on collections and `/{id}`, query-string filters (openapi.json; live 2026-09-22: `/work-orders?limit=5` → 200).
- **C2.2 Consistent typing: partial** — live-vs-schema check across work-orders, invoices, contacts, properties, units (250 records, 126 fields): **0 mismatches, 0 undeclared fields**; nulls declared explicitly via `anyOf [type, null]`; money is `integer` cents (`Invoice.totalAmount/subtotal/tax`, `Estimate.estimateAmount/approvedAmount`). Limitation: two documented numeric-as-string fields — `Invoice.selectedMarkupPercentage` and `Invoice.selectedDiscountPercentage`, "decimal string; 10 means ten percent" — a number that does not stay a number, confined to non-core fields.
- **C2.3 Structured errors: partial** — correct status semantics and a consistent JSON envelope, but **no machine-readable error code**. Schema `Error` = `{error: string}` only ("Human-readable error message"). Observed: 401 `{"error":"Invalid API token"}`, 401 `{"error":"Missing or invalid Authorization header"}`, 404 `{"error":"Not found"}` (random UUID and malformed ID alike), 404 `{"error":"Unknown resource \"…\""}`, 400 on `/on-call-coverage` without `start`/`end`.
- **C2.4 Duplicate prevention: N-A** — purely read-only API.
- **C2.5 Graceful handling under load: no** — no 429, `Retry-After`, or backoff guidance anywhere in openapi.json or api.md (keyword scan: 0 hits). Live: 40 sequential requests → 40 × 200, no rate-limit headers of any kind. Throttling behaviour is undocumented and unobservable.
- **C2.6 Pagination for large collections: yes** — documented opaque-cursor pagination with `hasMore`/`nextCursor`, a stated ordering guarantee ("ordered by createdAt descending, then by ID descending"), and a documented cap (`limit` clamped 1–100, default 50) (api.md lines 17, 27, 31–32; `Pagination` schema). Live: 3 pages, `createdAt` non-increasing, 0 duplicate IDs; narrow filter → `hasMore=false` and `nextCursor` omitted exactly as documented; `limit=abc`→50, `limit=1000`→100, `limit=0`→50 all as documented.
- **C2.7 Bulk or incremental export: partial** — incremental sync is possible on standard list endpoints (`updatedAfter`+`updatedBefore` on 7 of 12 list endpoints; `createdAfter` on 11) with cursor pagination, but there is no dedicated bulk/export path, and the docs state the incremental bounds "do not provide complete historical changes or a snapshot across pages" and that related-record changes may not advance the timestamp (api.md line 27, 38).
- **C2.8 Webhook security and delivery: N-A** — no webhooks or events offered (already penalised in C1.4).
- **C2.9 Concurrency and conflict control: N-A** — purely read-only API.
- **C2.10 Versioning and backward compatibility: partial** — explicit path version `/api/external/v2`, a v1 contract referenced ("v1 retains its legacy numeric-or-null priority contract"), and a contract-revision identifier `2-b0dfb930aad19685` (api.md line 5; openapi `info.version`). No compatibility policy, no definition of breaking vs non-breaking, no deprecation window.
- **C2.11 Request traceability: partial** — every response carries `X-Vercel-Id` (e.g. `sfo1::pdx1::s7x5x-1790041782825-8ae9427d5609`, live headers 2026-09-22) but it is undocumented and is the hosting platform's identifier; whether Mason support can use it is unverified.
- **C2.12 Service availability and status transparency: partial** — no public status page (`status.thisismason.com` / `status.enduring-labs.com` do not resolve; no link on the docs page). Terms §5: "We strive to maintain 99.9% uptime for the Service. Scheduled maintenance windows will be communicated in advance." Scored as an availability commitment that exists only inside the contract; it is a target, not a remedy-backed SLA.
Score math: earned 5.0 of 9 applicable checks (C2.4, C2.8, C2.9 N-A); unrounded fraction = 0.5556; category points = **5.556 → 5.6/10**; verification coverage = 9/9 = 100%.
What this means for you: the API is clean, well-typed, and pages reliably — a script or an agent will not get surprised by the data shape. But it tells you nothing about rate limits, gives you no error codes to branch on, and there is no status page to check when it is down.

## Category 3: Access Control and Safe Automation: 1.3/5
- **C3.1 Read-only credentials: N-A** — the whole API is read-only.
- **C3.2 Scoped credentials: no** — one token "scoped to your property management account" (openapi `securitySchemes.bearerAuth`; api.md line 7). No resource, action, or role scoping exists; the vendor's own issuance note warns the token "can access a lot of data."
- **C3.3 Multiple keys: no** — no documented way to obtain more than one token; the docs describe a single vendor-provided token and the product has no key-management surface (item 7).
- **C3.4 Rotation and revocation: partial** — no self-serve mechanism; tokens are issued by the vendor by e-mail (item 9). Server-side deactivation demonstrably exists — the 401 response is documented for an "inactive, or expired bearer token" (openapi `/work-orders` 401 description) — so revocation is a support-mediated process, not an absent one.
- **C3.5 Test and production isolation: partial** — a separate Test workspace exists in the product ("Switch to Test / Toggle Test/Live PM", item 7), but no test credential is documented, the docs never mention a sandbox, and whether the production token can reach the test workspace is undocumented. Mason itself warns "Mailboxes are shared with your test workspace."
Score math: earned 1.0 of 4 applicable checks (C3.1 N-A); unrounded fraction = 0.25; category points = **1.25 → 1.3/5**; verification coverage = 4/4 = 100%.
What this means for you: one all-or-nothing key for your whole account, handed to you by e-mail. If you give it to an agent or a contractor, it sees every call, text, email, invoice, and contact. To shut it off you e-mail Mason.

## Category 4: Documentation and AI-Agent Readiness: 3.8/5
- **C4.1 Complete self-serve reference: partial** — the public reference is complete on authentication, every endpoint, every parameter (with semantics such as clamping and invalid-date behaviour), and response *schemas*, plus one worked `curl` request (docs page; api.md). Limitation: **zero worked response examples** — openapi.json contains no `example`/`examples` keys and api.md gives response shapes only as `{ data: WorkOrder[], pagination: Pagination }`.
- **C4.2 Reliable machine-consumable integration path: yes** — public OpenAPI 3.1 specification, complete for all 25 operations, served without a token, and verified against live responses with zero type or field drift (typing check above). No SDK or MCP server found (not required for yes).
- **C4.3 AI-readable documentation: yes** — `api.md` is a single Markdown corpus of the entire API, published with explicit "give the docs to your agent… Copy docs as Markdown" affordances and an "Agent guidance" section (docs page; api.md line 10).
- **C4.4 Kept current: partial** — the contract carries a revision identifier (`2-b0dfb930aad19685`) so change is *detectable*, but there is no changelog, release notes, or deprecation notice (probes for `/docs/changelog` → 404; `/openapi.json` served `cache-control: no-store` with no `ETag`/`Last-Modified` despite the spec's own note that "ETag supports identifying the published document").
Score math: earned 3.0 of 4 applicable checks; unrounded fraction = 0.75; category points = **3.75 → 3.8/5**; verification coverage = 4/4 = 100%.
What this means for you: this is the API's strongest area. An AI coding tool can be pointed at `api.md` or `openapi.json` and build correctly on the first try. What is missing is sample responses and any way to learn what changed between revisions.

## Category 5: Accessibility and Cost: 7.5/15
- **C5.1 Self-serve API key: no** — credentials are manually provisioned by the vendor. Docs: "Mason provides a bearer token" (passive, vendor-issued); the product's Settings page has no API or developer section (item 7); the operator's token arrived by e-mail from the vendor's founder a week after asking (items 9; thread `[mail thread id withheld]`, asked 2026-09-04, promised 2026-09-15, delivered 2026-09-22 UTC).
- **C5.3 Not commercially gated: yes** — the token was issued on the operator's existing subscription with no tier change and no charge mentioned; neither the docs nor the "Plans" section (After-Hours / Intake / Full Suite / In-House) ties API access to a tier; the specification is public ("Public documentation requires no token").
Score math: earned 1.0 of 2 applicable checks; unrounded fraction = 0.5; category points = **7.5/15**; verification coverage = 2/2 = 100%.
What this means for you: the API is free with your subscription, but you cannot get a key yourself — you ask a person and wait.

## Total
- Raw: **19.93 / 50** (1.875 + 5.556 + 1.25 + 3.75 + 7.5)
- Normalized before rounding: **39.86 / 100**
- Published numeric score: **40 / 100**
- Letter grade: **F**
- Evidence tier: fully verified — controlled live (read path; write-path steps N-A)
- Overall verification coverage: **100%** (23 of 23 applicable checks verified; gate: no category Unable to verify; overall ≥ 80% — passed)
- Partial-result flag: **no.** Nothing is unverified. The score is low because the API is read-only and the credential model is single-key/vendor-issued, not because evidence was missing.
- Unresolved evaluator disagreements:
  1. **C1.1 (±1.9 pts).** Tags scored *absent* (0). If a second grader treats tags as having no legitimate use for Mason and marks the item N-A, coverage becomes 10.5/20 = 52.5% → `partial` → C1 = 3.75 and the total rises to 44 (still F).
  2. **C2.2 (±0.6 pts).** Two percentage fields typed as decimal strings were scored as a documented non-core inconsistency (`partial`). A grader who reads "type-consistent" strictly as schema-vs-live agreement would score `yes` → total 41.
  3. **C2.12 (±0.6 pts).** A "strive to maintain 99.9% uptime" clause in the Terms was scored as an in-contract availability commitment (`partial`). A grader may hold that a target without remedies is not an SLA → `no` → total 39.
  4. **Tier label (0 pts).** Labelled Fully verified with steps 6–8 N-A because the contract has no write surface. A grader may prefer Baseline verified with C1.2/C1.3 disclosed as documentation-graded. The score is identical either way; both disclosures are made above.
  Full range across all four: **38–45**, grade F in every case.

## Bottom line for a property manager
You can build read-only tools on Mason today — dashboards, KPI pulls, a nightly sync into your own database, an agent that answers "what happened on this work order" — and the documentation is good enough that an AI coding tool will get it right the first time. You cannot build anything that acts: no creating, assigning, approving, or closing work orders through the API, and no webhook to tell you when something changed, so everything is polling. The biggest strength is a clean, fully typed, well-paginated contract with a public OpenAPI spec and a Markdown guide written for agents; the biggest limitations are the read-only surface (which alone costs most of Category 1), a single vendor-issued all-access token you cannot scope, rotate, or duplicate yourself, and no rate-limit, error-code, changelog, or status-page signals. Mason is not a bank, holds no client funds, and documents no trust or deposit workflows; it is a maintenance layer that still needs your PMS as the system of record for properties, leases, residents, and money. The F is a grade for buildability, not for the product: as a maintenance coordinator Mason is PM-specialized and well-documented; as a platform to automate *on*, it is a one-way mirror.
