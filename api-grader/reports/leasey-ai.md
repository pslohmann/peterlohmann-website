# API Report Card: Leasey.AI Leasey API (v1, docs release 3.19)

*Final report card (methodology step 12): three independent grading runs on the same frozen packet, compared check by check and reconciled against the packet's evidence.*

## Run metadata
- Methodology version: 1.2
- Grading model (fixed for this version): Claude Opus 5.5 (`claude-opus-5-5`) at high effort. All three runs and the reconciliation used it.
- Date run: 2026-11-17
- Provisional evidence-packet version or ID: LEASEY-EP-2026-11-17-P1
- Final evidence-packet version or ID: LEASEY-EP-2026-11-17-F1 (frozen 2026-11-17)
- Evidence-discovery mode: supplied final packet. No grading run did discovery, opened links, made API calls or added sources.
- Evidence tier: baseline verified
- Credential: sandbox key (`lsy_test_…`, full scope per L02), used for read (GET) calls only. The key does not appear in the packet or in this report.
- Minimum live-test battery: complete (steps 1–5; packet §8.1)
- Live tests performed: step 1 authenticate (L01, L02, L16, L34); step 2 read and page (L03→L04, L19, L05–L08, L20–L29); step 3 incremental or filtered query (L09, L10, L17, L18 `updated_since`; L11 `stage`); step 4 deliberate errors (L12–L16, L30–L34); step 5 header observation on every response (§8.2)
- Documentation-graded checks: C1.2, C1.3, C2.4, C2.8, C2.9 (write path), plus C1.1, C1.4, C2.1, C2.2, C2.10, C2.12, C3.1–C3.6, C4.1–C4.4, C5.1, C5.2. Live observations corroborate several of these (C2.2, C3.1, C3.3, C3.5).
- Checks applicable: 28 of 28 (no N-A, no unverified)
- Procedural note: in the evidence session the live battery ran before the controlled verification pass, which reverses methodology steps 5 and 6. The packet discloses this, and no source was removed. All three runs found that the order breaks no rule and changes no mark.

## Final evidence packet manifest
- S01 Homepage https://www.leasey.ai/ [Documented]
- S02 Pricing https://www.leasey.ai/a-price/ [Documented]
- S03 Integrations https://www.leasey.ai/a-integrations/ [Documented]
- S04 llms.txt https://www.leasey.ai/llms.txt [Documented]
- S05 API guide (Markdown) https://www.leasey.ai/api/leasey-api.md, v3.19 [Documented]
- S06 llms-full.txt https://www.leasey.ai/llms-full.txt, byte-identical to S05 [Documented]
- S07 OpenAPI 3.0.3 https://www.leasey.ai/api/openapi.yaml, 68 operations [Documented]
- S08 API documentation page https://www.leasey.ai/leasey-api-documentation/ [Documented]
- S09 Syndication API docs page https://www.leasey.ai/syndication-api/ [Documented]
- S10 Rental syndication API marketing page https://www.leasey.ai/rental-syndication-api/ [Documented]
- S11 Status page https://status.leasey.ai/ [Documented]
- S12 Status repository https://github.com/silverhomes/status: README, issues, history, uptime JSON [Documented]
- S13 GitHub org https://github.com/silverhomes [Documented]
- S14 Terms of Service https://www.leasey.ai/terms/ [Documented]
- S15 Showing Scheduler page https://www.leasey.ai/showing-scheduler/ [Documented]
- S16 Press & product updates https://www.leasey.ai/press-product-updates/ [Documented]
- S17 docs.leasey.ai, a Documenso sign-in page and not API docs [Documented, location check]
- S18 Sitemaps [Documented]; S19 robots.txt [Documented]
- S20, S21 blog articles; S22 Rent Manager page [Documented, added in verification]
- L01–L34, D01–D03 live calls [Live-tested]
- Standard locations checked (packet §5.2): `/llms.txt` 200 (API-specific); `/llms-full.txt` 200; `/openapi.json`, `/openapi.yaml`, `/swagger.json` at the root were 404; `/api/openapi.yaml` 200; `/sitemap.xml` 200; `/changelog` and `/release-notes` 404, with the changelog inside the guide at S05 §8.6; `status.leasey.ai` 200; MCP paths 404; `mcp.leasey.ai` bare 404, with nothing pointing to an MCP server; `/.well-known/api-catalog` 404 or 403 on all hosts. The documentation-home sequence (vendor pointers, common hosts, search) was completed and recorded with dates (packet §5.1).

## Evidence-amendment log
- As recorded in the packet (A-01 to A-15). It affects checklist rows 5, 6, 7, 9, 16 and 18, plus C1.4, C2.2, C2.5, C2.9, C2.10, C2.12, C3.5, C3.6, C4.2, C4.3, C5.1 and the documentation-home step. S20–S22 and D01–D03 were added. No grading run added anything.

## Grading runs
- Evidence session (tester: discovery, verification, live battery, packet frozen): 2026-11-17
- Runs 1–3 (PLM; this prompt and the frozen packet only; no vendor-specific guidance): all three on 2026-11-17, run at the same time as separate, independent agents. Each received only the methodology file and the frozen packet, was told its run number, and was told to grade once without starting other runs. No run saw another's work.
- Results by run:

| Run | Capability coverage | Gate 1 / Gate 2 | Placement share | Score | Grade |
|---|---|---|---|---|---|
| Run 1 | 89.74% (35.0 / 39) | A / A | 18.0 / 22 = 81.82% | 95 | A |
| Run 2 | 89.74% (35.0 / 39) | A / A | 17.5 / 22 = 79.55% | 95 | A |
| Run 3 | 89.74% (35.0 / 39) | A / A | 18.5 / 22 = 84.09% | 95 | A |
| **Resolved** | **89.74% (35.0 / 39)** | **A / A** | **17.5 / 22 = 79.55%** | **95** | **A** |

- Check-level agreement: **26 of 28** applicable checks unanimous. All 18 checklist-row scores were also unanimous (same item scores in every run), so C1.1–C1.3 percentages and gate 2 match exactly. C1.4 was unanimous at partial. The runs' rough estimates of how much of the state-change weight webhooks cover differed (33%, 44% and 42%), but all fell below the 0.50 push threshold, so the mark did not change.

| Check | Run 1 | Run 2 | Run 3 | Resolved | Basis |
|---|---|---|---|---|---|
| C2.2 Consistent typing | partial | no | partial | **no** | The check's text says identifiers "must keep one type for the same field across all operations", and `partial` is limited to inconsistencies "confined to non-core fields". The packet records that `application_id` is text in `/properties/leads` and `lead.received` but an integer in `/applications`. It also records `rent_amount`, `price`, `bedrooms` and `bathrooms` as text on some endpoints (S05 §1.4; S07, 9 `deprecated: true` properties). Those are core lead and listing fields, and the text versions are still returned in `v1`. The deprecated numeric `_number` twins are a mitigation, but the check grades the types actually returned, so the `partial` condition is not met. |
| C3.5 Test environment and isolation | partial | partial | yes | **partial** | A fully isolated sandbox exists, with separate credentials and Stripe test mode (S05 §1.3, L34), and it is included on every plan (S02). But the packet documents no self-serve way to get it. "Sandbox credentials … go through the same channel", meaning the Leasey technical contact (S05 §8.5), and the sandbox dashboard user is the one "Leasey gives you at onboarding" (S05 §1.3). Access is issued by the vendor on contact, which matches `partial` ("available only on request"), not `yes`. |

- Unresolved disagreements: none. Both differences were resolved against the packet as shown above.
- Possible score effect of the alternate marks (computed by code): C2.2 at partial → share 81.82% → 95. C3.5 at yes → 81.82% → 95. Both → 84.09% → 95. **Neither difference changes the published score or grade.**
- Gate-2 sensitivity (not a disagreement; every run flagged it): the A gate needs at least 85% capability coverage, and Leasey is at 89.74%. All three runs scored checklist rows 16 (activate or deactivate a listing) and 18 (confirm or complete a showing) at 1.0. Row 16 is credited through per-marketplace publish/unpublish (S05 §3.6). Row 18 reads "confirm *or* complete", and `POST /showings/{slot_id}/confirm` exists (S05 §4.11). If both rows were scored 0.5, coverage would be 33/39 = 84.62%, gate 2 would allow only B, and the score would be 80 + round(9 × 0.795455) = **87 (B+)**. One of the two at 0.5 still leaves an A (87.18%). Run 2 noted one more alternate reading: rows 1 and 4 (listings and units) at 0.5, treated as "available only through a report". That gives 83.33% and also 87 (B+). No run adopted it, because listings and units have direct create and update endpoints (S05 §3.3–3.4).

## API eligibility
- Qualifying API: yes
- Interface label: none
- API operator: Silver Homes Technology Inc. (operating as Leasey.AI) [S14, opening paragraph, which defines the Services to include "any Application Programming Interface ("API")"; S13 GitHub org "Leasey.AI"] (Documented)
- Access or credential issuer: Leasey.AI. Company administrators create per-company keys in the dashboard (Profile → Developers) or with `POST /api-keys`. Leasey issues legacy tokens and organization keys. [S05 §1.1–1.2, §9.2] (Documented)
- Eligibility basis: a documented REST/JSON API at `https://api.leasey.ai/v1` (sandbox at `https://sandbox.api.leasey.ai/v1`) exposing Leasey's own units, syndication, leads, showings, reports, webhooks and leasing functions [S04; S05 §0.1, §1.3; S07 `servers` and paths]. Authenticated sandbox calls returned the expected data [L01–L33] (Live-tested).

## Context
- Product type: Listings and showings
- What the API is for: it lets a property manager push units to rental marketplaces, pull back the leads they generate, and book, reschedule, confirm or cancel showings, including from voice or chat agents. Its core objects are listings/units, marketplace syndication, prospects/leads and showings. It also exposes a leasing pipeline (applications, screening, leases, e-signature), which falls outside this product type's checklist and is noted for context only.

## Provider and property-management fit
- What this product is: an AI leasing platform for property managers that lists units, answers leads, schedules showings, screens applicants and signs leases. [S01 hero text] (Documented)
- Bank status: N-A. No banking role is documented. [S05 §3.2, §10.8: the account's card is charged through Stripe]
- Who provides any bank account or regulated banking service: N-A (none documented). Stripe processes Leasey's own fees. [S05 §3.2]
- What the customer actually receives: leasing software (syndication, lead response, showing scheduling, and optional screening and e-sign modules) plus API access to it. [S01, S02]
- Property-management fit: PM-specialized. [S01 "PMs with 100+ doors"; Built For list; S04 "the leasing platform for property managers"]
- Documented PM-specific workflows: listing syndication with prices before publish [S05 §2.1, §3.5–3.6]; showing booking for voice/chat agents [S05 §2.3, Part 4]; lead pull and push [S05 §3.7, §6]; pre-qualification questions [S05 §4.3]; applications, households, stage and decision changes [S05 §10.2, §10.7]; screening orders [S05 §10.8]; lease creation, e-signature and signed PDF [S05 §10.4, §10.5, §10.9]; multi-company organizations [S05 Part 9].
- Trust or fiduciary workflow support: not documented. Lease records carry `security_deposit` and `pet_deposit` amounts as lease terms only [S05 §10.4]. No rent collection, trust, escrow or deposit holding is documented.
- Operational role and dependencies: Leasey is the leasing front end (marketing, leads, showings, and optionally applications, screening and leases). The operator still needs a PMS or accounting system of record (it integrates with Rent Manager, Buildium, DoorLoop, AppFolio and Property Vista per S03). Screening goes through providers such as Certn (S05 §10.8), and listings go to third-party marketplaces.

## Coverage classification (fixed before inspection)
- Checklist: Listings and showings published list. No deviation recorded [packet §3].
- Size: 18 items, total weight 39 (re-added by code: objects 11 items / 22 weight, workflows 3 / 9, lifecycle actions 4 / 8). This matches the packet's stated totals.
- One missing critical item = 3 ÷ 39 = 7.69% of capability coverage.

| # | Item | Kind | Class | Weight | State | Score |
|---|---|---|---|---|---|---|
| 1 | Listings | object | critical | 3 | Present: create `POST /properties`, partial update `PUT /properties/{id}`, list and read via `GET /reports/properties` (paginated, `updated_since`), per-unit marketplace state [S05 §3.3–3.5, §5.3; S07; L03, L04, L19, L21] | 1.0 |
| 2 | Showings or tours | object | critical | 3 | Present: book, read by id, list by person, reschedule, cancel, confirm, report [S05 Part 4, §5.3; S07; L06, L29] | 1.0 |
| 3 | Prospects or leads | object | critical | 3 | Present: `GET /properties/leads`, `/reports/leads`, `GET/POST /applications`, `PATCH /applications/{id}`, `lead.received` [S05 §3.7, §5.3, §10.2, §10.7, §6.1; L07, L08, L10–L13, L20] | 1.0 |
| 4 | Units/properties | object | important | 2 | Present: the same unit endpoints as row 1, with building and floorplan fields [S05 §7; L05] | 1.0 |
| 5 | Showing availability or schedules | object | important | 2 | Partial: read-only (`GET /showings/availability`, `/lookup`, `/questions`). Availability windows are configured only in the Leasey app, and no write endpoint was found [S05 §4.1, §4.4; A-01] | 0.5 |
| 6 | Prospect activity | object | important | 2 | Partial: prescreening answers (`include_answers=true`) and `Showing_Feedback` are readable only through report columns. No message/conversation endpoint and no feedback write [S05 §5.3, §5.5; A-02] | 0.5 |
| 7 | Agents or users | object | important | 2 | Partial: team members can be assigned or created only inside unit create/update and are readable only as report columns. No user list, read or update endpoint; role edits and removals happen in the dashboard [S05 §7, §8.4, §5.5; A-03] | 0.5 |
| 8 | Syndication to rental sites | object | important | 2 | Present: publish/unpublish per marketplace, read status, syndication report, `unit.published` and `unit.unpublished` events [S05 §3.5–3.6, §5.1, §6.1; L21, L22] | 1.0 |
| 9 | Access devices | object | optional | 1 | Absent [A-04] | 0.0 |
| 10 | Reporting | object | optional | 1 | Present: five report endpoints [S05 Part 5; L03–L07, L22, L23] | 1.0 |
| 11 | Application hand-off links | object | optional | 1 | Present: `rental_application_url` + `use_custom_application_link` on the unit; `POST /applications/{id}/send` [S05 §7, §10.7] | 1.0 |
| 12 | Create or update a listing | workflow | critical | 3 | Present: `POST /properties`, `PUT /properties/{id}` [S05 §3.3–3.4] | 1.0 |
| 13 | Schedule a showing | workflow | critical | 3 | Present: `POST /showings`, including a waitlist [S05 §4.5–4.6] | 1.0 |
| 14 | Create or update a prospect | workflow | critical | 3 | Present: `POST /applications`, `PATCH /applications/{id}`; `POST /showings` creates or updates the lead [S05 §10.7, §4.5, §4.12] | 1.0 |
| 15 | Cancel or reschedule a showing | lifecycle | important | 2 | Present: `POST /showings/{slot_id}/cancel`, `PUT /showings/{slot_id}/reschedule` [S05 §4.9–4.10] | 1.0 |
| 16 | Activate or deactivate a listing | lifecycle | important | 2 | Present: per-marketplace `enabled: true/false` publishes or unpublishes the listing, and unpublishing can cancel upcoming showings [S05 §3.6]. Archiving the unit record itself is not documented [A-05]. That is a unit-record action, not listing activation | 1.0 |
| 17 | Update a prospect's status | lifecycle | important | 2 | Present: `PATCH /applications/{id}` with `stage`, `decision`, `archived` [S05 §10.7] | 1.0 |
| 18 | Confirm or complete a showing | lifecycle | important | 2 | Present: `POST /showings/{slot_id}/confirm` [S05 §4.11]. "Completed/attended" cannot be written [A-02], but the item is satisfied by confirm | 1.0 |

## Functional coverage map
- Core objects: listings (critical, 3) present; showings (critical, 3) present; prospects/leads (critical, 3) present; units/properties (important, 2) present; showing availability (important, 2) read-only; prospect activity (important, 2) read-only through reports, no messages; agents/users (important, 2) partial; syndication (important, 2) present; access devices (optional, 1) absent; reporting (optional, 1) present; application hand-off links (optional, 1) present.
- Primary operational workflows: create/update a listing; schedule a showing; create/update a prospect. All three are present.
- Lifecycle actions: cancel/reschedule a showing; activate/deactivate a listing; update a prospect's status; confirm a showing. All four (important, 2 each) are present.

## Category 1: Functional Coverage and Usefulness (gate 2)
- C1.1 Object coverage: 81.8% (18.0 of 22) [Documented S05/S07; Live-tested L03–L08, L19–L29]
- C1.2 Write coverage: 100% (9 of 9) [Documented S05 §3.3–3.4, §4.5–4.6, §10.7; S07 POST/PUT/PATCH paths]
- C1.3 Lifecycle coverage: 100% (8 of 8) [Documented S05 §3.6, §4.9–4.11, §10.7]
- C1.4 Change notification: **partial**. [Documented S05 §6.1 events; S05 §5.3 `updated_since`; Live-tested L09, L10, L17, L18 (filter honored), L30 (documented 400)]
  - Webhooks cover listing publish/unpublish, new leads and application stage/decision changes.
  - No showing event exists (scheduled, rescheduled, confirmed, cancelled), and there is no unit created/updated event [A-06]. Push covers well under half of the critical-plus-important state-change weight (the three runs estimated 33%–44%), which is below 0.50.
  - All critical changes (listings, showings, leads) can be detected by efficient incremental polling with `updated_since` plus pagination, verified live. That meets the partial definition.

Gate 2 math: capability coverage = 35.0 ÷ 39 = 89.74% over 39 weight; write coverage 100%; C1.4 partial; critical item scored 0: none; unverified weight: 0%; gate 2 allows: **A**; verification coverage = 4/4 = 100%

What this means for you: the published documentation lets you create and update listings, push them to or pull them from marketplaces, capture and update leads, and book, move, confirm or cancel showings, all by API. The gaps are around the edges:
- The published documentation shows no way to set showing availability by API.
- The published documentation shows no way to manage team members by API, beyond assigning them to a unit.
- The published documentation shows no way to read lead message threads by API.
- The published documentation shows no lockbox or access-code features.
- No documented webhook fires when a showing is booked or cancelled, so your system has to check the showings report for changes.

## Category 2: API Design, Reliability, and Operability (placement)
- **C2.1 Modern API conventions: yes.** REST/JSON with standard verbs (GET/POST/PUT/PATCH/DELETE) and resource paths [Documented S07 path list; Live-tested L01–L34]. Using POST for state transitions (cancel, confirm) is acceptable.
- **C2.2 Consistent typing: no.**
  - Core fields keep legacy text-typed versions on some endpoints while other endpoints type them as numbers:
    - `application_id` and `person_id` are text in `/properties/leads` and `lead.received` but integers in `/applications`.
    - `price`, `bedrooms` and `bathrooms` are text in `/showings/lookup`.
    - `slot_id` is text in the reschedule response.
    - `rent_amount` is text in `/properties/leads`.
    [Documented S05 §1.4 "Older text fields and their `_number` twins"; S07, 9 `deprecated: true` properties]
  - The methodology requires identifiers to keep one type for the same field. These inconsistencies touch core lead and listing fields, so the partial band ("confined to non-core fields") does not apply.
  - Money is also an unscaled JSON number (`type: number`, no format or scale; live `Rent_Amount: 2000.0`, `Amount: 12.0`) [S05 §1.4; S07; L03, L23]. That alone caps this check at partial.
  - Mitigation, noted but not changing the mark: every text field has a typed `_number` twin, and the text fields are deprecated.
- **C2.3 Structured errors: yes.**
  - Every observed error (400, 401, 404) carried `error`, a stable snake_case `code`, `message` and `request_id`, with correct statuses (L12 `application_not_found` 404, L13 `invalid_parameter` 400, L14/L33 `invalid_pagination`, L15 `invalid_updated_since`, L16/L34 `invalid_api_key` 401, L30 `updated_since_not_supported`, L31 `not_found`, L32 `bad_request`) [Live-tested].
  - The schema `ErrorResponse` requires `code` [S07], and S05 §1.5 documents the code's stability [Documented].
  - Limitation noted: one 422 example in S05 §1.5 "Notes" shows no `code` field, which contradicts the schema. It is a documentation example on an unobserved write path.
  - The gateway 403s at the host roots fall outside `/v1` [D01–D03; S05 §1.3].
- **C2.4 Duplicate prevention: yes.** The `Idempotency-Key` header works on every write: responses are stored for 24 h with an `Idempotent-Replayed` flag, a reused key gets 422, and an in-flight duplicate gets 409. It is required for paid screening orders. Natural protection also exists: a duplicate unit name gets 409 with the existing id, and marketplace re-sends are a no-change that is "never billed twice". [Documented S05 §1.7, §10.7–10.9; S07 `IdempotencyKey`]
- **C2.5 Graceful handling under load: partial.**
  - The docs cover 429 `rate_limited` with a `Retry-After` header, explicit backoff guidance (1 s, 2 s, 4 s… up to 60 s) and stated limits (50 req/s, bursts of 100) [Documented S05 §1.4; S07 `RateLimited`].
  - No rate-limit header appeared on any of 37 live responses, and no 429 was met (none was provoked) [Live-tested §8.2; A-13].
  - The documented behavior was never confirmed by an observed signal, so the check is capped at partial.
- **C2.6 Pagination for large collections: yes.**
  - The docs give `page`/`page_size` with `total_rows`, `total_pages` and `has_more`, a documented fixed order per report ("never skips or repeats a row"), and documented caps (5000 on reports, 500 on leasing lists) [Documented S05 §1.4, Part 10].
  - Observed: pages 1→2 (L03, L04) matched the unpaginated order (L19), and the cap was enforced (L33) [Live-tested].
  - Minor gap: `/properties/leads` takes only `limit` (max 500), but leads can be paged in full through `/reports/leads`.
- **C2.7 Bulk or incremental export: yes.** Reports return a full dataset in one call (up to 6 MB, then 413 with a suggested page size) or paginated, with `updated_since` incremental sync on properties, leads, showings, billing and the leasing lists [Documented S05 §1.4, §5.3, §10.6; Live-tested L09, L17, L18, L19].
- **C2.8 Webhook security and delivery reliability: yes.** Deliveries are HMAC-SHA256 signed with Standard Webhooks headers and a timestamp. Failed deliveries are retried (+2 min, +10 min, +30 min, +2 h, 5 attempts, then marked `failed`). Consumers are told to de-duplicate by id/value/`changed_at` and to expect out-of-order and duplicate delivery. A delivery log is readable [Documented S05 §6.1–6.4; S07]. Webhooks were not live-tested (that would need a write).
- **C2.9 Concurrency and conflict control: no.** No ETag, If-Match, 412, record version or optimistic-concurrency mechanism exists in the guide or the OpenAPI file [Documented S05, S07; A-08]. The lease `409 lease_not_editable` rule is a business-state conflict and does not qualify.
- **C2.10 Versioning and backward compatibility: partial.**
  - Present:
    - a version in the path (`/v1`);
    - a written definition of breaking vs additive changes;
    - at least 12 months of `v1` support after a `v2` announcement;
    - dated changelog entries and `deprecated: true` markers.
    [Documented S05 §1.3, §8.6; S07 `info.description`]
  - Missing: the Terms of Service, which cover the API, say Leasey "may stop, suspend or change our Services at any time without prior notice" [Documented S14 §1.5; A-14]. That is a first-party term permitting changes without notice, which the yes definition excludes.
- **C2.11 Request traceability: yes.** `X-Request-Id` was present on all 34 `/v1` responses and matched the body `request_id` on errors [Live-tested L01–L34, §8.2]. The docs say it is on "every response" and to quote it to support [Documented S05 §1.5, §8.5].
- **C2.12 Service availability and status transparency: yes.** A public status page carries uptime figures (100.00% for 24 h, 7 d, 30 d, 1 y and all-time) and response times, with an incident history kept as GitHub Issues (0 incidents recorded; an existing but empty history counts) [Documented S11, S12; A-09]. A contractual SLA exists only on the Custom plan [S02], but the definition is met by uptime information.

Checks earned: 9.0 of 12 applicable; verification coverage = 12/12 = 100%

What this means for you: the API behaves predictably.
- Errors come back with clear codes.
- Every request carries an ID you can quote to support.
- Retries are safe.
- You can page or sync incrementally.
- Webhooks are signed and retried.

The weak spots:
- Some older fields send numbers as text (typed copies exist alongside them).
- Money is a plain decimal number.
- The published documentation shows no protection against two systems overwriting each other's edits.
- The legal terms reserve the right to change the service without notice.
- Rate-limit headers were documented but not seen in practice.

## Category 3: Access Control and Safe Automation (placement)
- **C3.1 Read-only credentials: yes.** Read-only keys can only `GET`, and any write returns 403 `api_key_read_only` [Documented S05 §1.2]. Keys with `"scope": "read"` appear in the account [Live-tested L02].
- **C3.2 Scoped credentials: yes.** Keys can be limited to specific resources (`properties`, `leads`, `showings`, `reports`, `webhooks`, `applications`, `screening`, `leases`, `documents`, `api_keys`), combined with the read/full access level. Other routes return 403 `api_key_resource_not_allowed` [Documented S05 §1.2; S07 `POST /api-keys` `resources`].
- **C3.3 Multiple keys: yes.** Administrators can create several keys, each with a label [Documented S05 §1.2]. The account lists many distinct keys [Live-tested L02].
- **C3.4 Rotation and revocation: yes.** Self-serve: create and revoke in the dashboard, or `POST /api-keys` and `DELETE /api-keys/{key_id}`. The guide documents a rotation procedure, optional expiry, and immediate effect of revocation [Documented S05 §1.2; S07]. Revoked and expired keys appear in the account [Live-tested L02].
- **C3.5 Test environment and isolation: partial.**
  - A full sandbox exists: a separate system with its own credentials and data, Stripe test mode, no live marketplace publishing, and isolated data [Documented S05 §1.3]. Pricing says it is included on every plan [S02]. A sandbox key was rejected by production [Live-tested L34].
  - Limitation: sandbox credentials come through the Leasey technical contact ("Sandbox credentials and the `openapi.yaml` file go through the same channel"), and the sandbox dashboard user is "given at onboarding" [S05 §8.5, §1.3; A-10]. There is no self-serve way to get the sandbox, so it is available only on request.
- **C3.6 Delegated access: no.** No OAuth or other delegated-authorization flow is documented. The OpenAPI file defines only bearer API keys and legacy token/password schemes [Documented S07 `securitySchemes`; S05; A-11]. S20 is a generic blog that does not claim OAuth for Leasey. There is no official MCP server.

Checks earned: 4.5 of 6 applicable; verification coverage = 6/6 = 100%

What this means for you: you can give an AI agent or a reporting tool its own key, set it to read-only, limit it to only leads or only showings, set an expiry, and revoke it yourself at any moment. To get a sandbox you have to go through your Leasey contact. The published documentation shows no "Sign in with Leasey" (OAuth) flow, so third-party apps still need a pasted key.

## Category 4: Documentation and AI-Agent Readiness (placement)
- **C4.1 Complete self-serve reference: yes.** A public reference covers authentication, environments, conventions, errors, every endpoint with parameters, and "the full request and a real response captured from production" for each endpoint, plus tutorials and field catalogs [Documented S05 header and Parts 0–10; S08].
  - Not counted against the reference, but noted: the docs are not linked from the site's header or footer. They were found through `/llms.txt`, the sitemap and the status page.
  - Also noted: a marketing page (S10) contradicts the reference (`POST /v1/listings`, "48+" marketplaces, "real time" webhooks).
- **C4.2 Reliable machine-consumable integration path: yes.** A public OpenAPI 3.0.3 file has 68 operations, typed schemas, an error component, security schemes and deprecation flags. It is kept in step with the guide (`info.version` 3.19, last modified 2026-11-09) and is described as "for Postman, code generators and AI tools" [Documented S07; S04]. No official SDK and no MCP server exist [S13; packet §5.1; A-15].
- **C4.3 AI-readable documentation: yes.** The API-specific `llms.txt` covers auth, errors, pagination, versioning and doc links. `llms-full.txt` holds the complete guide as plain text, byte-identical to the 219 KB Markdown guide, and a per-guide Markdown file is also published [Documented S04, S06, S05]. The OpenAPI file is credited under C4.2, not here.
- **C4.4 Kept current: yes.** A dated changelog runs from 1.0 (2026-08-26) to 3.19 (2026-11-09) with New / Fixed / Docs entries. The OpenAPI `info.version` matches the changelog release, and deprecated fields are flagged in both the guide and the spec [Documented S05 §8.6; S07]. The changelog sits inside the guide, with no standalone `/changelog` URL.
- AI agent path: no official MCP server found (Registry 0 results; `/mcp` and `/.well-known/mcp*` 404; `mcp.leasey.ai` bare 404 with no first-party pointer). There is a public OpenAPI 3.0.3 specification and no official SDK. MCP standard version checked: N-A [packet §5.1, §5.2; A-15]

Checks earned: 4 of 4 applicable; verification coverage = 4/4 = 100%

What this means for you: a developer, or an AI coding tool such as Claude or ChatGPT, can build against this API straight from the published files. There is a full Markdown guide, an `llms-full.txt` copy for AI tools, an OpenAPI file you can load into Postman or a code generator, and a dated changelog. There is no official Leasey MCP server for plugging the account straight into an AI assistant.

## Category 5: Accessibility and Cost (gate 1)
- **C5.1 Self-serve API key: yes.** Company administrators create production keys themselves in the dashboard (Profile → Developers) or with `POST /api-keys`, with no approval step [Documented S05 §1.1–1.2; S04]. Sandbox credentials and the first organization key are issued by Leasey; that test-environment limit is scored in C3.5. Account acquisition goes through "Book a Demo" [S02], which the methodology keeps out of C5.1.
- **C5.2 Not commercially gated: yes.** Pricing says "Every plan includes the full Leasey API (REST endpoints, webhooks and the sandbox) at no extra cost and with no usage quota," with "REST API, webhooks & sandbox included" on Starter ($299), All modules and Custom [Documented S02]. The guide adds "API access is included with every Leasey account, with no usage quota" [S05 §8.5]. A contractual uptime SLA and a named integration contact come only with the Custom reseller plan [S02]. Neither is one of the capability gates C5.2 names; the SLA is considered under C2.12.

Gate 1 allows: **A** (both yes); verification coverage = 2/2 = 100%

What this means for you: if you are a Leasey customer on any plan, the API comes at no extra cost, with no usage cap, and you can create keys yourself. Becoming a customer still starts with a sales demo.

## Grade
- Gate 1, open access: allows A (C5.1 yes, C5.2 yes)
- Gate 2, documented capability: allows A (capability coverage 89.74% ≥ 85%; write coverage 100% ≥ 70%; C1.4 partial; no critical item at 0; 0% unverified weight)
- Letter from the gates: A; binding gate: none (both allow A)
- Placement share: 17.5 of 22 Category 2–4 checks = 79.55% (Category 2: 9.0/12; Category 3: 4.5/6; Category 4: 4/4)
- Score math: 90 + round(6 × 0.795455) = 90 + round(4.7727) = 90 + 5 = **95 (A)**
- Official MCP server (one-step bump): no (none found; packet §5.1, §5.2, A-15). Step not applied.
- Published numeric score: **95 / 100**
- Letter grade: **A**
- Evidence tier: baseline verified (battery steps 1–5 complete)
- Overall verification coverage: 100% (28 of 28 applicable checks scored). Every group is at 100%, so none is Unable to verify. Unverified checklist weight is 0%, and gate 1 is verified.
- Partial-result flag: no
- Unresolved evaluator disagreements: none. All three runs gave 95 (A) independently. The two check-level differences (C2.2, C3.5) were resolved against the packet, and no alternate mark changes the score (see "Grading runs"). The only reading that would change the letter is scoring checklist rows 16 and 18 both at 0.5, which no run did. That would give 87 (B+).

### Arithmetic (computed with code at reconciliation)
```
weight 39 (re-added from the 18 rows; matches the packet), earned 35.0, capability 0.897436
objects 18.0/22 = 0.818182 ; workflows 9.0/9 = 1.0 ; lifecycle 8.0/8 = 1.0
one critical item = 3/39 = 7.6923%
Run1      cat2 9.5 cat3 4.5 cat4 4  share 0.818182  6*share 4.9091  score 95
Run2      cat2 9.0 cat3 4.5 cat4 4  share 0.795455  6*share 4.7727  score 95
Run3      cat2 9.5 cat3 5.0 cat4 4  share 0.840909  6*share 5.0455  score 95
Resolved  cat2 9.0 cat3 4.5 cat4 4  share 0.795455  6*share 4.7727  score 90 + 5 = 95
alt C2.2 partial  share 0.818182 -> 95 ; alt C3.5 yes 0.818182 -> 95 ; both 0.840909 -> 95
sensitivity: rows 16 and 18 both 0.5 -> 33/39 = 0.846154 < 0.85 -> gate 2 B -> 80 + round(9*0.795455 = 7.16) = 87
```

## Good for / Not built for
- Good for:
  - pushing listings to rental marketplaces and turning them on or off;
  - pulling leads into your own CRM or PMS;
  - letting a voice or chat AI agent check availability and book, reschedule, confirm or cancel showings;
  - moving applicants through stages;
  - syncing leasing reports into a dashboard.
- Not built for, per the published documentation:
  - setting showing-availability windows;
  - managing team members;
  - reading lead conversation history;
  - lockbox or self-guided tour access;
  - real-time showing webhooks;
  - "Sign in with Leasey" (OAuth) connections;
  - rent collection or trust accounting.

## Bottom line for a property manager
Leasey's API scores 95 (A) for buildability, near the top of the 90–96 range a vendor can reach without an official MCP server. A property manager can build their own tools on it to list units on marketplaces, capture leads, and let an AI agent book and manage showings. Access is included on every plan, keys can be limited to read-only or to specific areas and revoked self-serve, and the documentation is complete enough for an AI coding tool to work from directly.

The main limits:
- The published documentation shows no way to set showing availability or manage users by API.
- No documented webhook fires for showing changes, so you poll the showings report instead.
- The published documentation shows no OAuth sign-in and no protection against two systems overwriting the same record.
- Sandbox access goes through your Leasey contact.

Leasey is a leasing front end, not a bank, PMS or trust-accounting system. You would still need your property management software (for example Buildium, AppFolio or Rent Manager, which Leasey connects to) as the system of record for leases, rent and owner funds.
