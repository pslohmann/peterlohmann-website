# API Report Card: Latchel (Partner API, Webhooks, Latchel MCP)

**Published score: 87 / 100 · Letter grade: B+** (gates allow B → placement 84 B → official MCP step → 87 B+)

## Run metadata
- Methodology version: 1.2
- Grading model (fixed for this version): Claude Opus 5.5 (`claude-opus-5-5`) at high effort, for all three grading runs
- Date run: 2026-11-17
- Provisional evidence-packet version or ID: LATCHEL-EV-20261117-P1
- Final evidence-packet version or ID: LATCHEL-EV-20261117-F1 (frozen 2026-11-17)
- Evidence-discovery mode: supplied final packet (three independent grading runs; no discovery, no live calls, no sources added)
- Evidence tier: baseline verified
- Credential: sandbox / development API key (accepted only by the documented testing/development host `https://latchel-demo.com/v1`; rejected by production, L-01 vs L-04), used for read calls only
- Minimum live-test battery: complete (all five steps run against the documented sandbox host; packet section 8). Production behavior was not observed.
- Live tests performed: L-01…L-21. Authenticate (`GET /me`, L-01, L-04). Read and paginate `/jobs` (L-05…L-08), read a single job (L-09), its state history (L-10) and invoices (L-11). Incremental and filtered queries: `updated_at_start_date` on jobs (L-12) and properties (L-15, L-16), `in_states` (L-13). Deliberate errors: wrong key (L-02, L-21), no key (L-03), nonexistent ID (L-17, L-18), invalid parameter (L-19, L-20). Rate-limit and traceability headers recorded on every response.
- Documentation-graded checks: C1.1, C1.2, C1.3, C1.4 (webhooks), C2.1, C2.2 (with live corroboration), C2.4, C2.7 (with live corroboration), C2.8, C2.9, C2.10, C2.12, C3.1–C3.6, C4.1–C4.4, C5.1, C5.2
- Checks applicable: 28 of 28 (no N-A checks; no unverified checks)

## Final evidence packet manifest
- S-01 https://latchel.com/ [Documented]
- S-02 https://latchel.com/llms.txt [Documented]
- S-03 https://latchel.com/llms-full.txt [Documented]
- S-04 https://latchel.com/robots.txt [Documented]
- S-05 https://latchel.com/sitemap.xml [Documented]
- S-06 https://latchel.com/claude-mcp-connector/ [Documented]
- S-07 https://latchel.com/latchel-everywhere-product-launch/ [Documented]
- S-08 https://latchel.com/integrations/ [Documented]
- S-09 https://latchel.com/reporting-and-analytics/ [Documented; added in verification]
- S-10 https://latchel.com/terms-of-use/ [Documented]
- S-11 https://latchel.com/terms-of-use-msa/ [Documented]
- S-12 https://latchel.com/team/ [Documented]
- S-13 https://latchel.com/faq/ [Documented]
- S-14 https://help.latchel.com/llms.txt and /_llms/help-center-guides.txt [Documented]
- S-15 https://help.latchel.com/sitemap.xml [Documented]
- S-16 https://help.latchel.com/s/topic/0TO5e000000h9wqGAA/API-Docs [Documented]
- S-17 https://help.latchel.com/s/topic/0TO5e000000h9wqGAA/How-to-Generate-an-API-Key (with screenshot transcriptions) [Documented]
- S-18 https://help.latchel.com/s/topic/0TO5e000000h9wqGAA/The-Webhook-Subscription (with screenshot transcriptions) [Documented]
- S-19 https://help.latchel.com/reference/introduction [Documented]
- S-20 https://help.latchel.com/reference/payload-format [Documented]
- S-21 Help Center webhook reference pages (job, tenant, portfolio) [Documented]
- S-22 https://help.latchel.com/s/topic/0TO5e000000h9wqGAA/latchel-mcp-ai-assistants [Documented]
- S-23 Help Center Product Updates / release notes 2025–2026 [Documented]
- S-24 Help Center export guides [Documented]
- S-25 https://papi.latchel.com/api-docs/papi/ (ReDoc shell) [Documented]
- S-26 / Appendix A https://papi.latchel.com/api-docs/papi/papi.yaml (OpenAPI 3.0.0, sha256 b868232e…) [Documented]
- S-27 / Appendix B https://papi.latchel.com/api-docs/webhooks/webhooks.yaml + 22 referenced files (OpenAPI 3.1.0) [Documented]
- S-28 https://help.latchel.com/mcp (documentation-search MCP server) [Documented]
- S-29 https://status.latchel.com/ redirect chain [Documented observation]
- S-30 GitHub, npm, MCP Registry listings (search records)
- S-31 https://help.latchel.com/s/topic/0TO5e000000h9wqGAA/How-to-Change-the-Service-Provider-on-a-Work-Order-New-Experience [Documented; added in verification]
- S-32 Web search records (2026-11-17)
- S-33 Pages checked in verification with no API evidence (on-call rotation page, pricing page, integration guides) [Documented; added in verification]
- L-01…L-21 live read requests, 2026-11-17 19:27:34–19:28:37 UTC [Live-tested]
- Standard locations checked (packet section 5):
  - **latchel.com:** `/llms.txt` 200 (marketing index); `/llms-full.txt` 200 (marketing prose); `/openapi.json`, `/openapi.yaml`, `/swagger.json` 404; `/sitemap.xml` 200; `/changelog`, `/release-notes` 404; `/.well-known/api-catalog` 404.
  - **status.latchel.com:** redirects to Atlassian's marketing page; no Latchel status content.
  - **help.latchel.com:** `/llms.txt` 200; `/llms-full.txt` 200 (no Partner API endpoint reference); per-page `.md` available; `/openapi.*`, `/swagger.json`, `/changelog`, `/release-notes` redirect to a login page; `/mcp` is a docs-search server (protocol 2025-06-18).
  - **papi.latchel.com:** standard locations 404, except `/api-docs/papi/papi.yaml` 200 and the webhook spec files 200.
  - **latchel-demo.com:** standard locations 404.
  - **Documentation-host subdomains** (`docs.`, `developer.`, `developers.`, `api.`, `api-docs.`, `dev.`, `mcp.`): connections timed out.
  - **Registries:** MCP Registry, not listed; npm, 0 packages; GitHub, no SDK repository.

## Evidence-amendment log
- As recorded by the tester in packet section 9 (V-01…V-13):
  - S-09 added (commercial-gating search, C5.2).
  - S-31 added (vendor reassignment, checklist row 19).
  - S-33 added (status/SLA and pricing searches, C2.12, C5.2).
  - S-17 and S-18 screenshot transcriptions added (C3.1–C3.4, C2.8).
  - S-10 and S-11 excerpts extended (C2.10).
- No source was removed, and the coverage table was unchanged. The grading runs added nothing.

## Grading runs
- Evidence session (tester: discovery, verification, live battery, packet frozen): 2026-11-17
- Runs 1–3 (PLM; this prompt and the frozen packet only; no vendor-specific guidance; each run graded the packet once, in parallel, as separate agents on Claude Opus 5.5 at high effort): all 2026-11-17
- Run results before reconciliation: Run 1 **87 (B+)** · Run 2 **97 (A+)** · Run 3 **87 (B+)**
- Check-level agreement: **24 of 28 checks unanimous**. All 22 placement checks (Categories 2–4) agreed except C2.7 and C3.6. C1.3, C1.4, C5.1 and C5.2 agreed. C1.1 and C1.2 differed because the checklist rows under them differed. Checklist rows: 13 of 20 unanimous.

| Check / row | Run 1 | Run 2 | Run 3 | Resolved | Basis |
|---|---|---|---|---|---|
| Row 2 Status transitions (critical, 3) | 0.5 | 1.0 | 0.5 | **0.5** | The Partner API reads state and state history and can cancel, approve and deny. `Job_Updatable` has no `state_id` and there is no completion endpoint [Appendix A; V-11]. Run 2's 1.0 relied on MCP-only actions (see the MCP note below). |
| Row 3 Vendor/technician assignment (critical, 3) | 1.0 | 0.5 | 0.5 | **0.5** | `vendor_id` is settable only in `Job_Creatable`, not `Job_Updatable` [Appendix A], so a vendor cannot be assigned to an existing job through the API. The MCP "can't find or assign a service provider" [S-22]. The assignment is present but materially limited. |
| Row 5 Scheduling/appointments (important, 2) | 0.5 | 1.0 | 0.5 | **0.5** | `scheduled_start`/`scheduled_end` are readable, but `Job_Updatable` has no scheduling fields [Appendix A; V-11]. "Schedule or reschedule" is documented only for the MCP [S-22]. |
| Row 12 Estimates (optional, 1) | 0.5 | 1.0 | 1.0 | **0.5** | `estimate`/`estimate_note` appear only on the Job response schema, not in `Job_Creatable`/`Job_Updatable` [Appendix A], and are "only filled in while the work order is waiting on approval" [S-16]. Approve/deny is scored separately in row 20, and "add an estimate" is MCP-only [S-22]. Read-only and transient, so 0.5. Effect: 1.1 points of capability coverage; no grade effect. |
| Row 13 Invoices (optional, 1) | 1.0 | 1.0 | 0.5 | **1.0** | `GET /invoices`, `GET /invoices/{id}` [Appendix A; L-11] plus the `invoice_mutated` webhook [Appendix B]. Invoices are vendor-submitted financial records, and reading them is the operations the item requires. No grade effect. |
| Row 14 Owner approval (optional, 1) | 0.5 | 1.0 | 0.5 | **0.5** | The API has owners CRUD and budget approve/deny [Appendix A], but no owner-approval record. "Record an owner's approval or denial" is MCP-only [S-22]. |
| Row 17 Transition its status to completion (critical, 3) | 0.0 | 1.0 | 0.0 | **0.0** | No completion endpoint, and `Job_Updatable` lacks `state_id` [Appendix A; S-26 inventory; V-11]. "Confirm completion" is MCP-only [S-22]. |
| C1.1 Object coverage | 83.9% | 91.1% | 78.6% | **78.6%** | Follows from the resolved rows (22 / 28) |
| C1.2 Write coverage | 50.0% | 83.3% | 50.0% | **50.0%** | Follows from the resolved rows (4.5 / 9) |
| C2.7 Bulk or incremental export | yes | yes | partial | **yes** | The check's "yes" expressly includes "documented incremental sync via updated-since plus pagination". The spec documents "Delta Sync" with `updated_at_start_date` and `per_page` up to 500 [Appendix A `info.description`], confirmed live [L-12, L-15, L-16]. Score effect: none (84 either way). |
| C3.6 Delegated access | yes | yes | partial | **yes** | The official hosted MCP uses "standard OAuth" sign-in with the user's own account, and the user approves the connection after seeing "what the connector can reach" [S-22; S-06 steps 2–3]. This matches the methodology's qualifying MCP case. Operator-side grant revocation is not separately described. Score effect: none (84 either way). |

- **The main disagreement: does the AI connector count in Category 1?** Run 2 credited actions that are documented only for the official Latchel MCP connector (completion, scheduling, owner approval, adding an estimate) to the coverage map. Runs 1 and 3 did not. It was resolved against counting them, on the methodology's text:
  - Gate 2 and Core rule 1 credit what is available "through the API".
  - The methodology names where an official MCP server earns credit: "C3.6, C4.2, and C4.3, where the MCP rule assigns it", plus the MCP step. The final integrity check repeats this ("credited where the MCP rule assigns it (C3.6, C4.2, C4.3) and, by design, also through the MCP step").
  - "Grade it on every check, the same as an API" appears only under MCP-only vendors (Step 0), and Latchel has a public API.
  - Latchel's own FAQ points autonomous agents to the Partner API instead, because the MCP supports only interactive sign-in [S-22 FAQ].
- **Unresolved disagreements:** none at the check level. **Disclosed sensitivity:** the methodology does not say outright whether an official MCP's documented actions count toward the Category 1 checklist when a public API also exists. If they did count (Run 2's reading), capability coverage would be 86.36%, write coverage 83.3%, and no critical item would score 0. Gate 2 would then allow an A, giving 93 (A) before the MCP step and an **alternate published score of 97 (A+)**. This should be clarified in the next methodology version so it applies to every vendor.

## API eligibility
- Qualifying API: yes
- Interface label: none (a public Partner API exists, so "MCP only" does not apply)
- API operator: Latchel, Inc., a Delaware corporation [S-10 Terms of Use, opening paragraph; Appendix A `info.contact` tech@latchel.com] [Documented]
- Access or credential issuer: Latchel; a property-manager user generates the key in the Latchel dashboard (Account Settings → Integrations → API Key → Generate) [S-17 steps 1–4] [Documented]
- Eligibility basis: The Latchel Partner API is a documented REST/JSON interface that reads and writes Latchel's own work orders, properties, residents, vendors, files and invoices [S-16; Appendix A `info`, `servers`, `paths`, `securitySchemes`]. It has a production base (`https://papi.latchel.com/v1`), a sandbox base (`https://latchel-demo.com/v1`) and an `x-api-key` header. Webhooks [Appendix B] and an official MCP server [S-06, S-22] are additional first-party interfaces. Confirmed live with `GET /me` 200 [L-04].

## Context
- Product type: Maintenance/operations
- What the API is for and its core objects and workflows: Latchel coordinates residential maintenance alongside a PMS: intake, troubleshooting, vendor dispatch, scheduling, approvals, invoices and after-hours emergencies. Its API exposes work orders ("jobs") with their states and state history, vendor companies and their priority rules, properties, portfolios, residents, owners, job files, invoices, inbound calls, on-call emergency alerts and intake-session transcripts. The core workflows are creating a work order, getting it assigned and moving it to completion.

## Provider and property-management fit
- What this product is: An AI maintenance-coordination and AI call-center platform for residential property managers, "not a property management system (PMS). It sits alongside one." [S-02] [Documented]
- Bank status, when relevant: N-A (not a bank or payments provider; no banking materials found) [packet section 2; S-02] [Documented]
- Who provides any bank account or regulated banking service: N-A [packet section 2]
- What the customer actually receives: Software plus a service, quoted as a per-door subscription: 24/7 maintenance intake and troubleshooting, vendor dispatch and coordination, an AI call center, and vendor invoice collection [S-02; S-03; S-33] [Documented]
- Property-management fit: PM-specialized [S-02 "the AI front office for residential property managers"; S-08] [Documented]
- Documented PM-specific workflows: [S-02 "Product" and "Integrations" lists; S-08] [Documented]
  - maintenance intake and troubleshooting
  - vendor dispatch and scheduling
  - budget approval and invoice collection
  - after-hours emergency on-call
  - resident benefits
  - PMS integrations (AppFolio, Rentvine, Buildium, Rent Manager, Propertyware, Yardi and others)
- Trust or fiduciary workflow support, when relevant: not documented. The API has owner payment-method links and vendor invoices [Appendix A `/portfolios/{id}/create-payment-method-link`, `/invoices`], but no trust-accounting, security-deposit or client-fund workflow appears in the packet [packet section 2].
- Operational role and dependencies: Latchel runs the maintenance and call-center layer, while the operator's PMS stays the system of record [S-08].

## Coverage classification (fixed before inspection)
- Checklist: Maintenance/operations published list, used verbatim; no deviation recorded (packet section 3). The tester disclosed that the table was written into the packet after the spec was downloaded. Its content is the published list verbatim, so it does not depend on the API.
- Size (re-added with code): 20 items, total weight 44.
  - By kind: objects 14 items (weight 28); workflows 3 items (weight 9); lifecycle actions 3 items (weight 7).
  - By class: critical 7 items (weight 21); important 10 (weight 20); optional 3 (weight 3).
  - These match the packet's stated totals.
- One missing critical item = 3 / 44 = **6.82%** of capability coverage
- Interfaces counted in this map: the Partner API and its webhooks (see "Grading runs" for why MCP-only actions were not counted)

| # | Item | Kind | Class | Weight | Present / partial / alert-only / absent | Score |
|---|---|---|---|---|---|---|
| 1 | Work orders | object | critical | 3 | present (list, create, read, update, cancel) | 1.0 |
| 2 | Status transitions | object | critical | 3 | partial (state, history and events readable; only cancel/approve/deny writable) | 0.5 |
| 3 | Vendor/technician assignment | object | critical | 3 | partial (vendor_id settable only at creation; priority rules writable) | 0.5 |
| 4 | Vendors | object | important | 2 | present (vendor companies CRUD, vendor users, service zip codes) | 1.0 |
| 5 | Scheduling/appointments | object | important | 2 | partial (scheduled window and resident availability read-only) | 0.5 |
| 6 | Residents | object | important | 2 | present (list, read, create in property, update, move dates) | 1.0 |
| 7 | Units/properties | object | important | 2 | present (list, create, read, update, merge, portfolios) | 1.0 |
| 8 | Photos or attachments on a work order | object | important | 2 | present (list, upload, read, reclassify) | 1.0 |
| 9 | Messages or comments on a work order | object | important | 2 | partial (intake transcript read-only; no notes/messages endpoint) | 0.5 |
| 10 | Links to PMS records | object | important | 2 | present (ref_job_id, ref_property_id, ref_unit_id, ref_user_id writable) | 1.0 |
| 11 | Entry permission and access instructions | object | important | 2 | present (enter_permission, access_instructions, property defaults writable) | 1.0 |
| 12 | Estimates | object | optional | 1 | partial (read-only, only while awaiting approval) | 0.5 |
| 13 | Invoices | object | optional | 1 | present (list, read, webhook) | 1.0 |
| 14 | Owner approval | object | optional | 1 | partial (owners CRUD and budget approve/deny; no owner-approval record) | 0.5 |
| 15 | Create a work order | workflow | critical | 3 | present | 1.0 |
| 16 | Assign it | workflow | critical | 3 | partial (assignable only at creation) | 0.5 |
| 17 | Transition its status to completion | workflow | critical | 3 | absent from the API | 0.0 |
| 18 | Cancel a work order | lifecycle | critical | 3 | present (state-restricted) | 1.0 |
| 19 | Reassign the vendor or technician | lifecycle | important | 2 | absent from the API (UI only) | 0.0 |
| 20 | Approve or reject an estimate or invoice | lifecycle | important | 2 | present (budget approve/deny) | 1.0 |

## Functional coverage map
- Core objects:
  - Work orders (critical, 3), present: `GET/POST /jobs`, `GET/PUT /jobs/{job_id}`, `POST /jobs/{job_id}/cancel` [Appendix A paths; S-26 inventory]; list and read observed live [L-05…L-09] [Documented, Live-tested]
  - Status transitions (critical, 3), partial: every job carries `state_id`/`state`, and `GET /jobs/{job_id}/history/state` returns its history [Appendix A; L-10]. The job `updated` webhook carries `state_id` [S-20; Appendix B job.yaml]. Writes are limited to cancel, approve and deny; `Job_Updatable` has no `state_id` [Appendix A] [Documented, Live-tested]
  - Vendor/technician assignment (critical, 3), partial: `vendor_id` and `manually_assign_vendor` are in `Job_Creatable` only, not `Job_Updatable` [Appendix A]. Per-property and per-portfolio vendor priority rules are writable (`POST/PATCH/DELETE /properties|portfolios/{id}/vendor-companies`) [Appendix A]. A vendor change fires the job webhook [S-20] [Documented]
  - Vendors (important, 2), present: `/vendor-companies` GET/POST/PATCH/DELETE, `/vendor-companies/prioritized`, `/vendors/{user_id}`, service zip codes [Appendix A] [Documented]
  - Scheduling/appointments (important, 2), partial and read-only: Job `scheduled_start`/`scheduled_end` and Tenant `availability` are readable [Appendix A; L-06], but `Job_Updatable` has no scheduling fields [Appendix A; V-11] [Documented, Live-tested]
  - Residents (important, 2), present: `/tenants` GET, `/tenants/{user_id}` GET/PUT, `/properties/{id}/tenants` GET/POST/PUT, and adding a tenant to a property with move dates [Appendix A] [Documented]
  - Units/properties (important, 2), present: `/properties` GET/POST, `/properties/{id}` GET/PUT, merge, subscriptions, warranties; `/portfolios` [Appendix A; L-14] [Documented, Live-tested]
  - Photos or attachments (important, 2), present: `/jobs/{job_id}/files` GET/POST (multipart, with classifications including Before/After Image) and `/jobs/{job_id}/files/{file_id}` GET/PATCH [Appendix A] [Documented]
  - Messages or comments (important, 2), partial: intake-session transcripts are readable via `/intake-sessions` and `/jobs/{job_id}/intake-session` [Appendix A], but there is no endpoint to read or post work-order notes or messages [V-11] [Documented]
  - Links to PMS records (important, 2), present: `ref_job_id`, `ref_property_id`, `ref_unit_id`, `ref_user_id`, `ref_service_request_id` [Appendix A, B] [Documented]
  - Entry permission and access instructions (important, 2), present: `enter_permission` and `access_instructions` in `Job_Updatable`, plus `default_access_instructions` on property and portfolio [Appendix A] [Documented]
  - Estimates (optional, 1), partial: Job `estimate`/`estimate_note` exist only on the response schema and are "only filled in while the work order is waiting on approval" [S-16; Appendix A] [Documented]
  - Invoices (optional, 1), present (read role): `GET /invoices`, `GET /invoices/{id}` [Appendix A; L-11] and the invoice webhook [Appendix B] [Documented, Live-tested]
  - Owner approval (optional, 1), partial: `/owners` GET/POST/PUT and `/jobs/{id}/approve|deny` ("Approve a jobs budget") exist [Appendix A], but there is no owner-approval record [Documented]
- Primary operational workflows:
  - create a work order (`POST /jobs`): present
  - assign it (`vendor_id` on creation only): partial
  - transition to completion: absent from the API
- Lifecycle actions:
  - Cancel a work order (critical, 3): present. `POST /jobs/{id}/cancel`, restricted to pre-dispatch and approval states [Appendix A].
  - Reassign the vendor (important, 2): absent from the API. `Job_Updatable` has no `vendor_id`, and S-31 documents reassignment as a dashboard action.
  - Approve or reject an estimate (important, 2): present. `POST /jobs/{id}/approve` (note, max_cost) and `/deny` [Appendix A].

## Category 1: Functional Coverage and Usefulness (gate 2)
- C1.1 Object coverage: **78.6%** (22 / 28) [Documented, Live-tested] [Appendix A paths and schemas cited per row above; L-05…L-14]
- C1.2 Write coverage: **50.0%** (4.5 / 9) [Documented] [Appendix A `requestBodies.JobCreate`, `JobUpdate`; V-11]
  - create a work order: 1.0
  - assign it: 0.5
  - completion: 0.0
- C1.3 Lifecycle coverage: **71.4%** (5 / 7) [Documented] [Appendix A `/jobs/{job_id}/cancel`, `/approve`, `/deny`; S-31]
  - cancel: 1.0
  - reassign: 0.0
  - approve/reject: 1.0
- C1.4 Change notification: **yes** [Documented] [Appendix B `webhooks.yaml`; S-20 "What Triggers an Updated Webhook"; S-18]
  - Webhooks fire on create and update for jobs, tenants, portfolios, invoices, properties, files, owners and on-call instances.
  - They cover 37 / 41 = 90.2% of the critical-plus-important checklist weight. The uncovered rows are Vendors and Messages.
  - Incremental polling also works: `updated_at_start_date` on jobs, properties and tenants [Appendix A; L-12, L-15].

Gate 2 math: capability coverage = **71.59%** (31.5 / 44) over 44 weight; write coverage 50.0%; C1.4 yes; critical item scored 0: **Transition its status to completion**; unverified weight: 0%; **gate 2 allows: B** (coverage ≥ 0.60; A blocked by coverage < 0.85, write coverage < 0.70, and the critical zero); verification coverage = 100% (4 / 4)

What this means for you:
- Through the API you can push work orders into Latchel from your own system and keep properties, residents, owners and vendors in sync.
- You can also set preferred-vendor rules, attach photos, cancel early-stage jobs and approve or deny budgets.
- Webhooks tell you when jobs, residents, properties, invoices or files change.
- The published documentation shows no API way to mark a job complete, schedule it, change the vendor after creation, or read and post work-order notes. Those happen in the Latchel app, and some can be done through Latchel's MCP connector in Claude or ChatGPT.

## Category 2: API Design, Reliability, and Operability (placement)
- C2.1 Modern API conventions: **yes** [Documented, Live-tested]
  - Resource-oriented REST/JSON with GET/POST/PUT/PATCH/DELETE and an OpenAPI 3.0 spec [Appendix A paths]; JSON responses observed [L-04…L-20].
- C2.2 Consistent typing: **partial** [Documented, Live-tested]
  - Identifiers are integers and flags are 0/1 integers consistently on core records, and live reads match [L-05…L-16].
  - Work-order money fields `max_cost` and `estimate` are binary `float` [Appendix A; L-05, L-09], which caps this check at partial.
  - Invoice `total`/`price` are `float` in the API but `string` in webhooks [Appendix A `Invoice`; Appendix B invoice.yaml].
  - File `author` is an object in the API but an integer in webhooks [Appendix A `JobFile`; Appendix B file.yaml].
  - Job timestamps come back as `"2026-09-10 16:09:17"` with no timezone, while other endpoints return RFC 3339 [L-05 vs L-10, L-14].
  - Some schema type keywords are invalid (`float`, `string|null`, `json`).
- C2.3 Structured errors: **partial** [Live-tested, Documented]
  - Responses use correct status codes with a JSON `{"errors":["..."]}` body and usable messages: 401 no key [L-03], 403 bad key [L-02, L-21], 404 "Record not found." [L-17, L-18], 422 validation [L-19, L-20].
  - No stable machine-readable error code is documented or returned [Appendix A `ValidationErrors`].
- C2.4 Duplicate prevention: **no** [Documented]
  - No idempotency key or other duplicate protection is documented for `POST /jobs` or other creates [V-01; Appendix A].
  - Two sandbox jobs share `ref_job_id` "APITEST-REF-001" [L-07, jobs 22900 and 22901], so the reference ID does not stop duplicates.
- C2.5 Graceful handling under load: **yes** [Documented, Live-tested]
  - Documented limit of 600 requests per key per 10 minutes, with 429, `Retry-After` and `X-RateLimit-Reset` [Appendix A `info.description` "Request Limits"; S-16].
  - `x-ratelimit-limit` and `x-ratelimit-remaining` observed on ordinary reads [L-04…L-20]. No 429 was provoked.
- C2.6 Pagination for large collections: **partial** [Live-tested, Documented]
  - `page`/`per_page` (1–500) with `links.next` are documented [Appendix A; L-05].
  - Following `links.next` exactly as returned drops `per_page`, so a client silently skipped records 3–10 [L-05 → L-07].
  - `/jobs` documents no ordering and returns no total or last page [L-05, L-08].
- C2.7 Bulk or incremental export: **yes** [Documented, Live-tested]
  - Documented "Delta Sync" with `updated_at_start_date` plus pagination up to 500 per page [Appendix A `info.description`; S-16], confirmed live [L-12, L-15, L-16].
  - No async export job; CSV exports exist in the app only [S-24]. Run 3 marked this partial; no score effect.
- C2.8 Webhook security and delivery reliability: **partial** [Documented]
  - A static per-account UUID is sent in the body `secret` and the `x-api-key` header, and is obtained by contacting Latchel Engineering [S-20 "Authentication"]. It is not a signature.
  - No retry policy and no replay guidance are documented [V-10; S-18].
- C2.9 Concurrency and conflict control: **no** [Documented]
  - No ETag/If-Match, version field or 409/412 behavior [V-02; Appendix A].
  - The `Contact` schema warns that a PUT without the full array removes contacts, i.e. the last write wins [Appendix A].
- C2.10 Versioning and backward compatibility: **partial** [Documented]
  - Path `/v1` and `info.version: 1.0.0` [Appendix A].
  - No breaking-change definition, deprecation notice period or deprecation signal [V-03].
  - Terms §22 allow changes "without notice" [S-10]. MSA §7.d gives 90 days' notice only for discontinuing the Services [S-11].
- C2.11 Request traceability: **no** [Live-tested, Documented]
  - No request or correlation ID header on any of the 21 responses (packet section 8), and none is documented [V-04].
- C2.12 Service availability and status transparency: **no** [Documented]
  - `status.latchel.com` redirects to Atlassian's marketing page [S-29].
  - No SLA or uptime commitment and no availability page were found [S-11; V-05; S-33].

Checks earned: 5.5 of 12 applicable; verification coverage = 100% (12 / 12)

What this means for you:
- This is a normal, well-structured REST API with clear rate limits and a documented "only what changed" sync, which suits a nightly sync into a spreadsheet, database or Zapier flow.
- Be careful with retries and paging. The published documentation shows no protection against creating the same work order twice and no overwrite protection.
- Following the API's own "next page" link can skip records unless you add the page size back yourself.
- There is no public status page and no request ID to quote in support tickets.

## Category 3: Access Control and Safe Automation (placement)
- C3.1 Read-only credentials: **no** [Documented]
  - "API keys have full access to your account" [S-16].
  - The key panel has no read-only option [S-17 screenshot].
- C3.2 Scoped credentials: **no** [Documented]
  - There is one all-powerful company key, with no scope or permission controls [S-16; S-17 screenshots].
- C3.3 Multiple keys: **no** [Documented]
  - The panel shows one key and "Re-generate Api Key", with no way to add a second key [S-17; V-06].
- C3.4 Rotation and revocation: **yes** [Documented]
  - Self-serve "Re-Generate API Key"; "Re-generating a key immediately invalidates the old one" [S-17; S-16].
- C3.5 Test environment and isolation: **partial** [Documented, Live-tested]
  - A sandbox host with separate keys and data exists [S-16; Appendix A `servers`], and the supplied development key worked only there [L-01 vs L-04].
  - No first-party page explains how an operator gets a development key, and webhook staging secrets require contacting Latchel Engineering [S-20; V-07].
- C3.6 Delegated access: **yes** [Documented]
  - The official hosted Latchel MCP connects through "standard OAuth": the user signs in with their own Latchel account and approves the connection after seeing "what the connector can reach", with "no API keys to manage" [S-22; S-06 steps 2–3]. This matches the methodology's MCP qualifying case.
  - The Partner API itself has no OAuth [V-08]. Run 3 marked this partial; no score effect.

Checks earned: 2.5 of 6 applicable; verification coverage = 100% (6 / 6)

What this means for you:
- You can't give an app or AI agent a limited, read-only or second key through the Partner API. There is one full-access key per company, and replacing it breaks every integration using it.
- You can rotate the key yourself.
- You can connect Claude or ChatGPT through Latchel's sign-in instead of sharing the key.
- A sandbox exists, but the documentation doesn't say how to get its key.

## Category 4: Documentation and AI-Agent Readiness (placement)
- C4.1 Complete self-serve reference: **partial** [Documented]
  - A public ReDoc reference, backed by a complete OpenAPI file, covers every endpoint with auth, parameters, request bodies and field-level examples [S-25, S-26, Appendix A].
  - There are no worked request/response examples beyond the field examples.
  - Error responses are undocumented for most endpoints.
  - There are some schema defects, e.g. `GET /owners` returns a single `Owner`, and `GET /jobs/{job_id}/files/{file_id}` lists 201 as its success code.
- C4.2 Reliable machine-consumable integration path: **yes** [Documented]
  - A published, maintained OpenAPI 3.0.0 spec for the full Partner API (last-modified 2026-11-17) [S-26], plus an OpenAPI 3.1.0 webhooks spec [S-27].
  - Also an official read-write MCP server [S-06 "Fourteen tools. Read and write."; S-22].
  - No SDKs.
- C4.3 AI-readable documentation: **partial** [Documented]
  - The Help Center has `llms.txt`, `llms-full.txt`, per-page Markdown and a docs-search MCP server [S-14, S-28].
  - They cover only the API overview, key and webhook pages, not the Partner API endpoint reference [packet section 5; V-12].
- C4.4 Kept current: **partial** [Documented]
  - Biweekly product release notes mention some API changes (Nov 2, 2026; Aug 10, 2026; Dec 1, 2025; Mar 9, 2026) [S-23], and the spec is freshly dated [S-26].
  - There is no API changelog, and several spec changes (on-call instances, intake sessions, warranties, delta sync) do not appear in the release notes.
- AI agent path: official MCP (read-write), plus a public OpenAPI specification (Partner API and webhooks); no SDKs; also an official docs-search MCP.
  - MCP standard version: not stated for the data MCP server (`app.latchel.com/mcp/user-tools`) [S-22; packet section 5].
  - The docs-search server reports protocol `2025-06-18` [S-28].

Checks earned: 2.5 of 4 applicable; verification coverage = 100% (4 / 4)

What this means for you:
- An AI coding tool can load Latchel's OpenAPI file and build against the whole API.
- Latchel's own connector lets Claude or ChatGPT read and act on work orders.
- The AI-friendly help files leave out the endpoint reference itself.
- API changes are announced inside general product newsletters, not a dedicated API changelog.

## Category 5: Accessibility and Cost (gate 1)
- C5.1 Self-serve API key: **yes** [Documented]
  - "Latchel Property Managers can generate (for the first-time) or regenerate an API key right from the Latchel console" [S-17].
- C5.2 Not commercially gated: **yes** [Documented]
  - API and MCP access are presented to Latchel property managers with no plan condition [S-16, S-17, S-06 "Anyone who can sign in to Latchel"].
  - The verification search found no statement that the API, webhooks, sandbox or MCP are tier-gated or paid [V-09].
  - The only separately priced add-on found, Analytics+, is not an API feature [S-03].

Gate 1 allows: A (both yes); verification coverage = 100% (2 / 2)

What this means for you: If you're a Latchel customer, you can create your API key yourself today, and nothing in Latchel's published materials says the API costs extra.

## Grade
- Gate 1, open access: allows A (C5.1 yes, C5.2 yes)
- Gate 2, documented capability: allows **B**
  - capability coverage 71.59%
  - write coverage 50.0%
  - C1.4 yes
  - critical item scored 0: transition to completion
- Letter from the gates: **B**; binding gate: **gate 2**
- Placement share: 10.5 of 22 Category 2–4 checks = 47.73%
- Score math: 80 + round(9 × 0.477273) = 80 + round(4.295) = **84 (B)** (computed with code)
- Official MCP server (one-step bump): yes. Latchel's official, Latchel-hosted MCP server reads and acts on work orders, tasks, properties and residents [S-06; S-22]. After the step: **87 (B+)**
- Published numeric score: **87 / 100**
- Letter grade: **B+**
- Evidence tier: baseline verified
- Overall verification coverage: 100% (28 / 28) (gate: no group Unable to verify; unverified checklist weight 0% ≤ 30%; overall ≥ 80%)
- Partial-result flag: no. The live battery ran on the documented sandbox host; production behavior was not observed because the supplied key is a development key.
- Unresolved evaluator disagreements: none at the check level. Disclosed methodology sensitivity: if MCP-only actions counted in Category 1, the alternate score would be 97 (A+) (see "Grading runs").

## Good for / Not built for
- Good for: pushing work orders into Latchel from your own system, syncing properties, residents, owners and vendors, setting preferred-vendor rules, attaching photos, approving or denying budgets, cancelling early-stage jobs, and getting webhooks or a delta sync of what changed.
- Not built for: closing out, scheduling or reassigning work orders, or reading and posting work-order notes, through the API; giving an app a limited or read-only key.

## Bottom line for a property manager
Latchel is a maintenance-coordination and AI call-center service that sits alongside your PMS. It is not a PMS, a bank or a trust-accounting system, and your PMS stays the system of record. Its Partner API is a clean, self-serve REST API with an OpenAPI file, a "what changed since" sync and webhooks. You can build intake flows that create work orders, keep your property, resident and vendor lists in sync, and pipe job updates into your own reports or automations. The biggest limitation is that the published documentation shows no API way to mark a work order complete, schedule it, or change its vendor. Those steps stay in the Latchel app, or partly in Latchel's Claude/ChatGPT connector, which needs a person to sign in. Plan for one all-access key per company, no duplicate protection on creates, and a "next page" link that drops your page size, and handle those in your build.
