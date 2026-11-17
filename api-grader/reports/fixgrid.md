# API Report Card: FixGrid FixGrid API v1

## Run metadata
- Methodology version: 1.2
- Grading model (fixed for this version): Claude Opus 5.5 (`claude-opus-5-5`), high effort
- Date run: 2026-11-17 (three grading runs, reconciled; this card carries the resolved marks)
- Provisional evidence-packet version or ID: FG-EVP-2026-11-17-P1
- Final evidence-packet version or ID: FG-EVP-2026-11-17-F1 (frozen 2026-11-17 17:53:57 UTC)
- Evidence-discovery mode: supplied final packet (no grading run did discovery, browsing or API calls)
- Evidence tier: baseline verified
- Credential: account API key, scope `read` (LT-01), used for read calls only
- Minimum live-test battery: complete (steps 1–5; packet §11 table)
- Live tests performed: LT-01 authenticate; LT-02–LT-07, LT-12, LT-23–LT-31 read and page; LT-08–LT-11, LT-13 incremental and filtered queries; LT-14–LT-21 deliberate errors; LT-22 and the header inventory (§11.3) for rate-limit and traceability signals; LT-32–LT-35 discovery checks
- Documentation-graded checks: C1.2, C1.3, C1.4, C2.2 (money representation), C2.4, C2.7 (partly), C2.8, C2.9, C2.10, C2.12, C3.1–C3.6, C4.1–C4.4, C5.1, C5.2
- Checks applicable: 28 of 28 (no N-A, no unverified)

## Final evidence packet manifest
- S-01 https://www.fixgrid.app/ [Documented]
- S-02 https://www.fixgrid.app/llms.txt [Documented]
- S-03 https://www.fixgrid.app/llms-full.txt [Documented]
- S-04 https://www.fixgrid.app/sitemap.xml and robots.txt [Documented]
- S-05 https://www.fixgrid.app/pricing.html [Documented]
- S-06 https://www.fixgrid.app/integrations.html [Documented]
- S-07 https://www.fixgrid.app/modules.html [Documented]
- S-08 https://developers.fixgrid.app/openapi.json (OpenAPI 3.1.0, 30 operations) [Documented]
- S-09 https://developers.fixgrid.app/ (Start here) [Documented]
- S-10 https://developers.fixgrid.app/authentication.html [Documented]
- S-11 https://developers.fixgrid.app/objects.html [Documented]
- S-12 https://developers.fixgrid.app/errors.html [Documented]
- S-13 https://developers.fixgrid.app/webhooks.html [Documented]
- S-14 https://developers.fixgrid.app/limits.html [Documented]
- S-15 https://developers.fixgrid.app/changelog.html [Documented]
- S-16 https://developers.fixgrid.app/reference.html [Documented]
- S-17 https://developers.fixgrid.app/llms.txt [Documented]
- S-18 https://developers.fixgrid.app/llms-full.txt [Documented]
- S-19 https://developers.fixgrid.app/sitemap.xml and robots.txt [Documented]
- S-20 https://status.fixgrid.app/ and /history (browser-rendered) [Documented]
- S-21 https://www.fixgrid.app/security.html [Documented]
- S-22 https://www.fixgrid.app/terms.html [Documented]
- S-23 https://www.fixgrid.app/features.html [Documented]
- S-24 https://www.fixgrid.app/grid-auriga.html [Documented]
- S-25 https://www.fixgrid.app/owner-portal.html [Documented]
- S-26 about, compare, resident-portal, report-a-problem, privacy, subprocessors, responsible-disclosure pages [Documented]
- S-A1 https://www.fixgrid.app/demo.html (amendment) [Documented]
- S-A2 https://www.fixgrid.app/founding.html (amendment) [Documented]
- S-A3 https://www.fixgrid.app/ai.html (amendment) [Documented]
- S-A4 https://www.fixgrid.app/procore.html (amendment) [Documented]
- LT-01 – LT-35 https://app.fixgrid.app/api/v1/… (38 GET requests, 2026-11-17 17:41–17:43 UTC) [Live-tested]
- Standard locations checked (packet §5, 2026-11-17): `/llms.txt` 200 on both domains; `/llms-full.txt` 200 on both; `/openapi.json` 404 on www, 200 on developers (identical to the API-host copy, LT-32); `/openapi.yaml` and `/swagger.json` 404 on both; `/sitemap.xml` 200 on both; `/changelog` 404 on www, 200 on developers; `/release-notes` 404 on both; `/.well-known/api-catalog` 404 on both and on the API host; `/mcp` 404 on both; status page `status.fixgrid.app` found (UptimeRobot, client-rendered, read in a browser); no MCP server page, so no MCP standard version to record.
- Documentation-home sequence (packet §4, 2026-11-17): step 1 vendor pointers found the home (`developers.fixgrid.app`, linked from the header, footer and homepage); API root and error bodies carry no docs link (LT-33, LT-34); api-catalog 404 (LT-35); MCP Registry 0 results; step 2 stopped once the home was found; step 3 searches, GitHub org (404) and npm/PyPI found nothing first-party.

## Evidence-amendment log
- C3.5 and C5.2: S-A1 demo.html added (search for a sandbox or test account). Shows a 7-day seeded demo company with app login credentials; no API sandbox, test mode or test key.
- C1.4, C2.8 and C5.2: S-A2 founding.html added (meaning of "paid plan" in webhook timing). Shows a no-charge founding period; "paid plan" is not defined.
- C3.6, C4.2, C4.3 and the MCP step: S-A3 ai.html added (check for an MCP server or AI connector). None found.
- C3.6: S-A4 procore.html added (check for an OAuth or app-authorization flow into FixGrid). The flow runs outward into Procore.
- Searches inside captured sources that added no source are listed in packet §10 (items 4, 5, 6, 8, 10, 12–14, 20; C2.5, C2.7, C2.10, C3.5, C3.6, C4.1, C5.2).

## Grading runs
- Evidence session (tester: discovery, verification, live battery, packet frozen): 2026-11-17
- Runs 1–3 (PLM; this prompt and the frozen packet only; no vendor-specific guidance): all three on 2026-11-17, run at the same time as three separate agents on Claude Opus 5.5 (`claude-opus-5-5`) at high effort. Each received only `methodology-v1.2.md` and `FixGrid-evidence-packet-2026-11-17.md`, was told its run number, and was told to grade once without starting other runs.
- Run results: Run 1 = 87 (B+), Run 2 = 87 (B+), Run 3 = 87 (B+). All three: baseline verified, gate 1 = A, gate 2 = B (binding), no MCP step, 28 of 28 checks applicable, verification coverage 100%.
- Check-level agreement: 26 of 28 checks unanimous (C1.1 differs only as a consequence of checklist item 7; every other check, including C1.4's mark, matched). 19 of 20 checklist items unanimous.

| Check | Run 1 | Run 2 | Run 3 | Resolved | Basis |
|---|---|---|---|---|---|
| Checklist item 7, Units/properties (important, 2) | 1.0 | 1.0 | 0.5 | 1.0 | The 0.5 rule applies when an item is "materially read-only where writes are operationally expected." FixGrid documents that it is "maintenance-first, not a full PMS" and that units and properties come from the PMS by rent-roll file (S-23; S-06 "Rent roll & CSV"), so creating or editing the property roster is not this item's operational need. Units and properties are readable with filters and `updated_since` (S-08, S-11; LT-07, LT-11, LT-12), and occupancy writes (notice, move-in) are present (S-11). Run 3's 0.5 rested on the missing roster create/update, which the role does not require. |
| C1.1 Object coverage | 60.71% | 60.71% | 57.14% | 60.71% | Follows from item 7. |
| C4.2 Machine-consumable path | yes | partial | yes | yes | The check's partial bar is a mechanism that is "incomplete, covers a limited subset, or requires substantial manual correction." The public OpenAPI 3.1 document covers all 30 operations with operationIds, schemas for all 17 objects and request examples on every write, and the API serves the identical file (S-08; LT-32). The defect is three undeclared path parameters (`ticket_id` on `PATCH /tickets/{ticket_id}`, `unit_id` on notice and move-in; packet §9 tester observations), which is a small fix, not a substantial correction. Run 2's concern is real and is recorded here, but it does not meet "substantial." |

- Same mark, different working: C1.4 was `partial` in all three runs. Runs 1 and 3 put webhook coverage of the critical-plus-important rows at 26 of 41 (63.4%); Run 2 put it at 28 of 41 (68.3%). Both figures fall in the 0.50–0.84 partial band, so the mark and the gates are unaffected. This card uses 63.4%.
- Unresolved disagreements: none. Both disputes were resolved against the frozen packet as shown, and neither changes the published result. Alternate scores (computed with code):
  - Item 7 at 0.5 (Run 3): capability coverage 68.18%, gate 2 still B, score 87 (B+).
  - C4.2 at partial (Run 2): placement share 17.5/22 = 79.55%, 80 + round(7.16) = 87 (B+).
  - Both alternates together: 87 (B+).

## API eligibility
- Qualifying API: yes
- Interface label: none
- API operator: FixGrid ("the application located at app.fixgrid.app operated by FixGrid", S-22 preamble). No legal-entity suffix appears in the captured pages.
- Access or credential issuer: the customer's Company Admin mints keys inside FixGrid on Integrations → Developers (S-09 "What the key is" and "How you get one"; S-05 plan table).
- Eligibility basis: a documented REST API at `https://app.fixgrid.app/api/v1` with bearer-key authentication over the customer's own FixGrid maintenance records (S-09, S-10, S-08 `servers`), confirmed by live reads of the account's tickets, units, vendors and other records (LT-01 to LT-31).

## Context
- Product type: Maintenance/operations
- What the API is for and its core objects and workflows: FixGrid is a maintenance-management system (CMMS) for multifamily operators. The API exposes the maintenance record (work-order tickets, properties, units, assets, vendors, inspections, turns, meters and staff) for reading, lets an integration file, update, assign, complete, cancel, reopen and annotate tickets, records occupancy notices and move-ins, and pushes 19 signed webhook events.

## Provider and property-management fit
- What this product is: residential-native maintenance-management software (CMMS) for multifamily property operators [S-01 "What is FixGrid?"; S-02].
- Bank status, when relevant: N-A (not a funds-handling product) [S-01, S-22 §2].
- Who provides any bank account or regulated banking service: N-A.
- What the customer actually receives: a hosted maintenance system of record (tickets, make-ready turns, inspections, preventive maintenance, assets, compliance) plus a resident portal and technician portal, with a public API and signed webhooks on every plan [S-01; S-05 "On every plan"].
- Property-management fit: PM-specialized [S-01 "purpose-built for multifamily property operators"; S-23 "maintenance-first, not a full PMS. It runs alongside the system you use for leasing and accounting"].
- Documented PM-specific workflows: resident maintenance requests and ticketing [S-07 "Work orders & residents"]; make-ready and unit-turn tracking with move-out/move-in [S-03; S-11 turn and occupancy]; inspections including NSPIRE readiness [S-02]; vendor COI compliance and dispatch holds [S-24; S-11 vendor_blocked]; rent-roll import from the PMS [S-06].
- Trust or fiduciary workflow support, when relevant: N-A (the product does not hold or move funds).
- Operational role and dependencies: FixGrid is the maintenance record that runs beside a PMS; leasing, accounting and resident master data stay in the operator's PMS, and today data crosses between them by rent-roll file and CSV, not live sync [S-06 "Rent roll & CSV", "Honesty"].

## Coverage classification (fixed before inspection)
- Checklist: Maintenance/operations published list; no deviation recorded (packet §3, frozen 2026-11-17 17:38:13 UTC).
- Size: 20 items, 44 total weight (objects 14, 28 · workflows 3, 9 · lifecycle actions 3, 7). Re-added by code from the item rows; matches the packet's stated totals.
- One missing critical item = 6.82% of capability coverage (3 ÷ 44).

| Item | Kind (object / workflow / lifecycle) | Class | Weight | Present / partial / alert-only / absent | Score |
|---|---|---|---|---|---|
| 1 Work orders | object | critical | 3 | present (list, fetch, create, update, reopen, note) | 1.0 |
| 2 Status transitions | object | critical | 3 | present (PATCH status, reopen, status filter, events) | 1.0 |
| 3 Vendor/technician assignment | object | critical | 3 | present (PATCH assignee_id / assigned_vendor_id, staff lookup, event) | 1.0 |
| 4 Vendors | object | important | 2 | partial (read-only; no create, update or deactivate) | 0.5 |
| 5 Scheduling/appointments | object | important | 2 | absent (no appointment or schedule on work orders) | 0.0 |
| 6 Residents | object | important | 2 | partial (move-in writes parties; no resident read) | 0.5 |
| 7 Units/properties | object | important | 2 | present (read with filters and updated_since; occupancy writes) | 1.0 |
| 8 Photos or attachments on a work order | object | important | 2 | partial (single photo_url read; no upload) | 0.5 |
| 9 Messages or comments on a work order | object | important | 2 | partial (add a note; notes cannot be read back) | 0.5 |
| 10 Links to PMS records | object | important | 2 | partial (external_id readable; cannot set it when creating a ticket) | 0.5 |
| 11 Entry permission and access instructions | object | important | 2 | partial (readable; cannot be set through the API) | 0.5 |
| 12 Estimates | object | optional | 1 | absent | 0.0 |
| 13 Invoices | object | optional | 1 | absent | 0.0 |
| 14 Owner approval | object | optional | 1 | absent | 0.0 |
| 15 Create a work order | workflow | critical | 3 | present (POST /tickets) | 1.0 |
| 16 Assign it | workflow | critical | 3 | present (PATCH /tickets/{id}) | 1.0 |
| 17 Transition its status to completion | workflow | critical | 3 | present (PATCH status Completed with note) | 1.0 |
| 18 Cancel a work order | lifecycle | critical | 3 | present (PATCH status Cancelled with reason code) | 1.0 |
| 19 Reassign the vendor or technician | lifecycle | important | 2 | present (PATCH assignee / vendor) | 1.0 |
| 20 Approve or reject an estimate or invoice | lifecycle | important | 2 | absent | 0.0 |

## Functional coverage map
- Core objects:
  - Work orders (critical, 3): present. `GET /tickets` with filters, `GET /tickets/{ticket_id}`, `POST /tickets`, `PATCH /tickets/{ticket_id}`, reopen and notes routes [S-08 operations table; S-11 "Writing a ticket"]; read live LT-02 to LT-06, LT-23.
  - Status transitions (critical, 3): present. Five-value status enum, PATCH status rules (hold note, closing note, cancellation code), 422 `ticket_closed` then `POST /tickets/{id}/reopen`, `ticket.status_changed` with from/to [S-11; S-12; S-13]; status filter honored live LT-09, LT-10.
  - Vendor/technician assignment (critical, 3): present. `assignee_id` from `GET /staff?property_id=`, `assigned_vendor_id` from `GET /vendors`, null unassigns; live insurance check (`vendor_blocked`) that only a person can override in the app [S-11 "Assignment"; S-12]; `ticket.assigned` event [S-13]. The override limit is a deliberate business rule, not a missing operation.
  - Vendors (important, 2): partial (0.5). List and fetch with compliance state; no vendor create, update or deactivate route among the 30 operations [S-08; packet §10 "Vendor write routes"]. Adding or editing a vendor is an ordinary operator task, so the item is materially read-only.
  - Scheduling/appointments (important, 2): absent (0.0). The Ticket schema has no scheduled date, appointment or time window; `preferred_access_time` is a free-text resident preference; no route sets a schedule [S-08 Ticket schema; packet §9.1 row 5]. Inspection `scheduled_date` and turn dates are attributes of other records, not work-order scheduling.
  - Residents (important, 2): partial (0.5). No resident object or read route; residents are "not on this object" (unit) [S-11 unit `updated_at`]; `POST /units/{unit_id}/move-in` writes parties and `/notice` records a notice [S-11 occupancy; S-08].
  - Units/properties (important, 2): present (1.0). List and fetch with `property_id` and `updated_since` filters, occupancy state fields, and occupancy writes (notice, move-in) that change unit status [S-08; S-11]; live LT-07, LT-11, LT-12. FixGrid is not the system of record for the property roster (S-23), so create/update of the roster is not this item's operational need.
  - Photos or attachments (important, 2): partial (0.5). One `photo_url` readable; no upload, list or delete route [S-08; packet §9.1 row 8], although the app supports several captioned photos (S-07).
  - Messages or comments (important, 2): partial (0.5). `POST /tickets/{ticket_id}/notes` adds a note, but "Notes cannot be read back through the API yet" [S-11]; only `closing_note` is readable.
  - Links to PMS records (important, 2): partial (0.5). `external_id` and `source` readable on every object and nested reference; occupancy writes accept `external_id` [S-08; S-11]; the `POST /tickets` body has no `external_id` field [S-08 request bodies], and properties/units cannot be tagged through the API.
  - Entry permission and access instructions (important, 2): partial (0.5). `permission_to_enter` and `preferred_access_time` readable; neither is in the `POST /tickets` or PATCH body [S-08].
  - Estimates, Invoices, Owner approval (optional, 1 each): absent. No object, field or route [S-08, S-16, S-18; packet §10]. `parts_cost` is a parts total, not an invoice.
- Primary operational workflows: create a work order (`POST /tickets`); assign it (`PATCH` `assignee_id` / `assigned_vendor_id`); complete it (`PATCH` `status: Completed` with a 5+ word note). Caveat: a company that requires a close-out photo cannot complete through the API, because the API has no photo upload [S-11 "Status"].
- Lifecycle actions: cancel a work order (critical, 3) present via `PATCH status: Cancelled` + `cancellation_reason_code` [S-11; S-08]; reassign vendor or technician (important, 2) present via PATCH, with 409 `ticket_held` while a technician holds it offline [S-11; S-12]; approve or reject an estimate or invoice (important, 2) absent.

## Category 1: Functional Coverage and Usefulness (gate 2)
- C1.1 Object coverage: 60.71% (17.0 of 28) [Documented + Live-tested] [S-08 operations and schemas; S-11; LT-02–LT-31]
- C1.2 Write coverage: 100.00% (9 of 9) [Documented] [S-08 `POST /tickets`, `PATCH /tickets/{ticket_id}`; S-11 "Writing a ticket"]
- C1.3 Lifecycle coverage: 71.43% (5 of 7) [Documented] [S-11 PATCH status Cancelled and assignment; S-08 PATCH body enum]
- C1.4 Change notification: partial [Documented + Live-tested] [S-13 "The events" (19 keys: `ticket.created`, `ticket.status_changed`, `ticket.assigned`, `vendor.hold`, `vendor.compliance_changed`, `unit.status_changed`, `unit.notice.changed`, `turn.*`, …); S-11 note "A note sends no webhook"; S-11 `updated_since` on every list except staff, honored live LT-08, LT-10, LT-11, LT-13]. Push covers all critical state changes (create, status, assignment, cancel, reassign) but none for scheduling, photos, notes, PMS links or entry permission, and only part of vendors, residents and units/properties: 63.4% weighted of the critical-plus-important rows (26 of 41), inside the 0.50–0.84 partial band.

Gate 2 math: capability coverage = 70.45% over 44 weight; write coverage 100.00%; C1.4 partial; critical item scored 0: none; unverified weight: 0%; gate 2 allows: B; verification coverage = 100% (4 of 4)

What this means for you: you can open, assign, complete, cancel and reopen work orders from your own tools, and you hear about new tickets, status changes and assignments by webhook. The published documentation shows no way to schedule appointments, upload photos, read back notes, add or edit vendors, or handle estimates, invoices or owner approvals through the API.

## Category 2: API Design, Reliability, and Operability (placement)
- C2.1 Modern API conventions: yes [Documented + Live-tested] Resource-oriented REST with GET/POST/PATCH/DELETE and JSON bodies [S-08 operations table; S-12 `method_not_allowed` row lists verbs per path]; observed LT-01–LT-31.
- C2.2 Consistent typing: partial [Documented + Live-tested] Identifiers, booleans, enums and timestamps are consistently typed, and live reads match every declared type with no undeclared fields (§11.4, all objects). Limitation: money is carried as binary floating-point JSON numbers with no precise representation — `Ticket.parts_cost` (number, "two decimals") and `UtilityReading.cost` (number, no scale documented; observed fractional values such as 701.4, LT-29) [S-08 "Declared descriptions of numeric money-like fields"]. Both are non-core fields for a maintenance API, so this is partial rather than no. (Separately noted, not a type defect: OccupancyRecord status is lower-case while Turn status is Title-Case for the same fact, S-11 occupancy.)
- C2.3 Structured errors: yes [Documented + Live-tested] One shape `{error:{code,message}}` with 28 stable, documented codes and correct statuses [S-12 "The contract", "The twenty-eight codes"]; observed 404 `not_found` (LT-14), 422 `invalid_request` (LT-15), 400 `invalid_request` (LT-16, LT-19, LT-20), 400 `invalid_cursor` (LT-17), 400 `invalid_limit` (LT-18), 401 `unauthorized` with `WWW-Authenticate` (LT-21).
- C2.4 Duplicate prevention: yes [Documented] `Idempotency-Key` required on every write (ticket create, PATCH, reopen, notes, notice, move-in, webhook create); replay returns the stored response with `X-Idempotent-Replay: 1`; 409 `idempotency_mismatch` / `idempotency_in_progress` [S-11 "Writing a ticket"; S-12 codes; S-16 `POST /tickets` Idempotency-Key parameter; S-08 required header on all 7 writes].
- C2.5 Graceful handling under load: partial [Documented + Live-tested] Documented 429 `rate_limited` with an integer `Retry-After` and 120/min per key [S-14 "On 429"; S-12]. Evidence parity: no rate-limit header appeared on any of 38 live responses and no 429 was met (§11.3), so the documented behavior is not confirmed by an observed signal.
- C2.6 Pagination for large collections: yes [Documented + Live-tested] Keyset cursor, ascending id order, `next_cursor` null at the end, limit up to 200 with documented clamp [S-11 "Paging", "The list envelope"]; observed full traversal 10+10+4 = 24 unique ascending ids ending in null (LT-04a–c) matching LT-05, non-overlapping pages (LT-02/LT-03), clamp to 200 (LT-06).
- C2.7 Bulk or incremental export: yes [Documented + Live-tested] Documented incremental sync: `updated_since` on every object list except staff, with sync instructions ("Re-send updated_since with each cursor, and start your next sync from the time you started this one") and 200-row pages [S-11 "Filters"; S-15 2026-10-30 "Every object list except staff now syncs incrementally"]; honored live (LT-08 returned exactly the 17 of 24 matching tickets; LT-11, LT-13). No dedicated bulk/export job exists [packet §10], but the check's yes definition expressly includes documented updated-since plus pagination.
- C2.8 Webhook security and delivery reliability: yes [Documented] HMAC-SHA256 over `<timestamp>.<body>` in `FixGrid-Signature` with verification code and a 5-minute replay window; retries at 1·2·4·8·24 h after timeout/5xx/408/429 then parked; `event_id` dedupe and at-least-once guidance [S-13 "Verifying the signature", "Delivery, retries, and giving up", "Your endpoint"].
- C2.9 Concurrency and conflict control: yes [Documented] `ETag` on ticket fetch and every ticket-write 200; `If-Match` on PATCH and reopen returns 412 `precondition_failed` with nothing written, checked under a lock [S-11 "Overwrite protection"; S-12 `precondition_failed`; S-08 If-Match on PATCH/reopen]. Tickets are the only records the API updates in place (occupancy and notes are appends). `ETag` observed on LT-23; enforcement not exercised (read-only testing).
- C2.10 Versioning and backward compatibility: partial [Documented] Path version `/api/v1`, written breaking vs non-breaking list, dated deprecation notices [S-14 "Versioning"; S-15 "Deprecation"]. Missing elements: the notice period is 90 days, below the required 6 months [S-14, S-15]; one behavior change shipped without the promised notice [S-15 2026-10-30 "This change did not get the 90-day notice"]; Terms §4 "Features may change, be added, or be removed" during an as-is period [S-22].
- C2.11 Request traceability: yes [Documented + Live-tested] `X-Request-Id` on every response, client value echoed, quote to support [S-12 "Every response carries a request id"]; present on all 38 responses and echoed in LT-22 (§11.3).
- C2.12 Service availability and status transparency: yes [Documented] Public status page with 90-day uptime per monitor (App, Developer Docs, Website, all 100.000%) and a status-update history page (exists; no entries in Nov 2026) [S-20]. A written SLA exists only in Enterprise agreements [S-05], which the check does not require for yes.

Checks earned: 10.5 of 12 applicable; verification coverage = 100% (12 of 12)

What this means for you: the API behaves predictably — clear error codes, safe retries, reliable paging, change syncing, signed webhooks and protection against two people overwriting the same ticket. The weak spots are a short 90-day notice for breaking changes (one change already skipped it), no live rate-limit signal before you hit the limit, and cost figures sent as plain decimal numbers.

## Category 3: Access Control and Safe Automation (placement)
- C3.1 Read-only credentials: yes [Documented + Live-tested] `read` scope opens every list and fetch only [S-10 "Scopes"]; supplied key showed `scope: read`, `actions: []` (LT-01).
- C3.2 Scoped credentials: yes [Documented] Three scopes (read, write, webhook_only) plus per-action limits on write keys (`tickets.create`, `tickets.update`, `tickets.reopen`, `tickets.notes`, `occupancy.record`, `webhooks.manage`) [S-10 "Write actions"; S-08 `x-scope` / `x-action`].
- C3.3 Multiple keys: yes [Documented] Admins create and label a key per integration; limits are counted "per key … so two integrations at the same customer never spend each other's budget" [S-09 "How you get one"; S-14 "The limit"; S-07 "API keys"].
- C3.4 Rotation and revocation: yes [Documented] Self-serve revoke on Integrations → Developers at any time; lost keys are replaced by minting a new one and revoking the old [S-09 "How you get one", "If you have lost a value"; S-12 `key_revoked`].
- C3.5 Test environment and isolation: no [Documented] No API sandbox, test mode or test key is documented; the only test offering is a 7-day seeded demo company with app login credentials that does not mention API access [S-A1; packet §10 search of S-03, S-18, S-A1]. The live account held seeded data (LT-05), but the packet does not establish how it was provisioned, so it cannot establish a test environment.
- C3.6 Delegated access: no [Documented] No OAuth or other delegated flow: "User-level OAuth ('connect as yourself') is a later, separate door" [S-09; S-08 `info.description`]; "no user OAuth" [S-21]; the Procore app delegates outward, not into FixGrid [S-A4]; no official MCP server [packet §2, §4].

Checks earned: 4 of 6 applicable; verification coverage = 100% (6 of 6)

What this means for you: you can give each tool or AI agent its own key, limited to reading or to just the actions it needs, and revoke it yourself. The published documentation shows no API sandbox, so testing happens against a real account, and there is no "sign in with FixGrid" option, so connecting a third-party tool means handing it a key.

## Category 4: Documentation and AI-Agent Readiness (placement)
- C4.1 Complete self-serve reference: partial [Documented] Public reference generated from the OpenAPI document covers all 30 operations with auth, parameters, request bodies, response-code tables, field tables and a curl request example on every operation [S-16; packet §8.15 notes]. Limitation: no operation shows a worked example response body; only `/whoami` (S-09) and `POST /webhooks` (S-13) show response bodies, and the OpenAPI document declares no response examples [S-08; packet §8.15].
- C4.2 Reliable machine-consumable integration path: yes [Documented] Public OpenAPI 3.1 document, no key needed, 30 operations with operationIds, schemas for all 17 objects and a request example on every write; the API serves the identical file [S-08; S-16 header; LT-32]. Defect noted: three path parameters are not declared (`ticket_id` on `PATCH /tickets/{ticket_id}`, `unit_id` on notice and move-in) [packet §9 tester observations]; a small correction, not a substantial one. No SDK; no MCP server.
- C4.3 AI-readable documentation: yes [Documented] Developer `llms.txt` index plus `llms-full.txt` (183,956 bytes) holding every guide and the full per-operation reference as one plain-text file [S-17; S-18]; robots.txt allows AI crawlers [S-19].
- C4.4 Kept current: yes [Documented] Dated changelog with frequent entries from 2026-09-08 to 2026-11-09, each naming what changed and whether it is additive, plus a stated deprecation process [S-15]; reference regenerated from the served document [S-16]; sitemap lastmod dates [S-19]. Minor irregularities noted: two changes documented about 12 days after they shipped (S-15 2026-10-13, 2026-10-14 entries, both disclosed), the 2026-10-26 entry's "26 operations" is now 30, and the changelog lastmod (2026-11-03) trails its newest entry (2026-11-09) [S-19 tester note].
- AI agent path: none found (no official MCP server: MCP Registry 0 results, `/mcp` 404 on both domains, and the vendor tells developers not to put a key in a Claude/MCP connector); public OpenAPI 3.1 specification; no SDKs; `llms.txt` / `llms-full.txt`. MCP standard version checked: N-A [packet §2, §4, §5; S-09; S-08 `info.description`]

Checks earned: 3.5 of 4 applicable; verification coverage = 100% (4 of 4)

What this means for you: a developer or an AI coding tool can build from the public spec and the single-file text docs without logging in. The reference shows requests but not sample responses, so a builder relies on field tables for what comes back.

## Category 5: Accessibility and Cost (gate 1)
- C5.1 Self-serve API key: yes [Documented] A Company Admin mints keys on Integrations → Developers; "You do not apply to FixGrid for a key"; no ticket or approval [S-09 "How you get one", "Talk to us (optional)"; S-05 plan table].
- C5.2 Not commercially gated: yes [Documented] "Public API + signed webhooks included on every plan … No partner fee, no API add-on", Starter through Enterprise [S-05 plan table and FAQ; S-06; S-07 "API keys … Starter"]; rate limit is one figure for all keys [S-14]. No test environment, delegated access or MCP server exists to be gated. Noted, not gating: five-minute delivery of ticket events applies to "a paid plan" (every published plan is paid; the free founding period is undefined) [S-13; S-A2]; vendor management (Grid Auriga) and uptime terms are product/contract features on higher tiers, not API capabilities [S-05].

Gate 1 allows: A (both yes); verification coverage = 100% (2 of 2)

What this means for you: any FixGrid customer on any plan can turn on the API themselves, today, with no extra fee and no sales call.

## Grade
- Gate 1, open access: allows A (C5.1 yes, C5.2 yes)
- Gate 2, documented capability: allows B (capability coverage 70.45%; below 85% so A is not available; no critical item at 0)
- Letter from the gates: B; binding gate: gate 2
- Placement share: 18.0 of 22 Category 2–4 checks = 81.82%
- Score math: 80 + round(9 × 0.818182) = 80 + round(7.3636) = 80 + 7 = 87 (B+)
- Official MCP server (one-step bump): no (MCP Registry 0 results; no `/mcp` page; packet §2, §4); not applied
- Published numeric score: 87 / 100
- Letter grade: B+
- Evidence tier: baseline verified
- Overall verification coverage: 100% (28 of 28; gate: no group Unable to verify; unverified checklist weight 0% ≤ 30%; overall ≥ 80%)
- Partial-result flag: no
- Unresolved evaluator disagreements: none. Two check-level disagreements (item 7, C4.2) were resolved against the frozen packet; every alternate still gives 87 (B+) (see "Grading runs")

Arithmetic (computed with code; weights re-added from the 20 item rows = 44, matching the packet's stated total):
```
objects   14 items  earned 17.0 / 28  = 0.607143
workflows  3 items  earned  9.0 /  9  = 1.000000
lifecycle  3 items  earned  5.0 /  7  = 0.714286
capability          earned 31.0 / 44  = 0.704545
one critical item = 3/44 = 0.068182
C1.4 push coverage, critical+important rows = 26.0 / 41 = 0.634146
Category 2 = 10.5/12 · Category 3 = 4/6 · Category 4 = 3.5/4
placement share = 18.0 / 22 = 0.818182
9 × share = 7.363636 → 7 (half-up) → 80 + 7 = 87
```

## Good for / Not built for
- Good for: syncing work orders, units, turns, vendors and inspections into your own dashboards, and letting an automation or AI agent file, assign, complete, cancel and reopen tickets with a tightly limited key and signed webhooks.
- Not built for: scheduling vendor or technician appointments, uploading photos, reading ticket notes, managing vendors or resident records, or handling estimates, invoices and owner approvals — the published documentation shows no way to do these through the API.

## Bottom line for a property manager
FixGrid is a maintenance system that runs beside your PMS, not a PMS or a bank, and its API is a well-built, free-on-every-plan way to get maintenance data out and push the core work-order actions in: create, assign, complete, cancel and reopen tickets, plus record notices and move-ins. Its biggest strength is engineering discipline — read-only and per-action keys, safe retries, overwrite protection, documented change syncing, signed webhooks and AI-friendly docs. Its biggest limitation is reach: the published documentation shows no way to schedule appointments, add photos, read notes, add or edit vendors, read residents, or handle estimates, invoices or owner approvals, and there is no API sandbox or "sign in with FixGrid" connection. You would still need your PMS for leasing, residents and accounting, and today data moves between the two by file, not live sync.
