# API Report Card: Rentvine Open API (manager API) and Rentvine MCP

**Published score: 87 / 100 — B+** (85, B, before the MCP step). Evidence tier: baseline verified.

## Run metadata
- Methodology version: 1.2
- Grading model (fixed for this version): Claude Opus 5.5 (`claude-opus-5-5`). All three runs were launched at high effort. Run 3 said in its own report that it believed it ran at a lower effort setting; this could not be independently confirmed, and its result matches the other two runs.
- Date run: 2026-11-17
- Provisional evidence-packet version or ID: RV-EP-2026-11-17-P1
- Final evidence-packet version or ID: RV-EP-2026-11-17-F1 (frozen 2026-11-17 17:55 UTC)
- Evidence-discovery mode: supplied final packet. The grading runs did no discovery, opened no links and made no API calls.
- Evidence tier: baseline verified
- Credential: account API key and secret (HTTP Basic) for a Rentvine demo/test account. The tester's evidence session used it for read calls only. The key does not appear in the packet or in this report.
- Minimum live-test battery: complete (steps 1–5; packet §7)
- Live tests performed (packet §8, 2026-11-17):
  - T1, T2a–T2d: authentication and properties paging, including a page past the end and `pageSize=500`
  - T2e: lease export
  - T3a–T3h: property export with `dateTimeModifiedMin/Max`, the `isActive=0` filter, and transactions search with `dateTimeModifiedMin`
  - T4a–T4d: deliberate errors (nonexistent ID, non-numeric ID, invalid parameters, wrong key)
  - T5a: accounts; T6a: leases; T6b: work orders
  - T0: API root and `/.well-known/api-catalog`
  - T7: MCP `initialize` handshake only, rejected with 400; no tool was called
- Documentation-graded checks: the write-path checks C1.2, C1.3, C2.4, C2.8 and C2.9; the credential controls C3.1–C3.4; also C1.4 (push side), C2.10, C2.12, C3.5, C3.6, C4.1–C4.4, C5.1 and C5.2.
- Checks applicable: 28 of 28 (no N-A, no unverified)

## Final evidence packet manifest
All sources are first-party and were accessed 2026-11-17.
- S1 https://www.rentvine.com/open-api [Documented]
- S2 https://docs.rentvine.com/ — Redoc "Rentvine API Docs" 1.0.0 with a downloadable OpenAPI 3.1.0 spec, 143 paths / 205 operations, SHA-256 `7a6b21bf…ddbca`; full operation index in packet Appendix A [Documented]
- S3 https://www.rentvine.com/features/mcp [Documented]
- S4 https://www.rentvine.com/features/mcp/setup [Documented]
- S5 https://www.rentvine.com/features/mcp/cookbook [Documented]
- S6 https://help.rentvine.com/en/articles/17219935-the-rentvine-mcp [Documented]
- S7 https://www.rentvine.com/terms-of-service-mcp-addendum (last modified 2026-09-21) [Documented]
- S8 https://www.rentvine.com/terms (last modified 2026-10-14) [Documented]
- S9 https://help.rentvine.com/en/articles/16575275-tip-of-the-week-30-guide-to-rentvines-open-api [Documented]
- S10 https://help.rentvine.com/en/articles/16574284-how-to-add-webhooks, with screenshot transcriptions (A8) [Documented]
- S11 https://help.rentvine.com/en/articles/16574157-user-roles [Documented]
- S12 https://www.rentvine.com/pricing [Documented]
- S13 https://status.rentvine.com, including /history, /uptime and the JSON API [Documented]
- S14 https://www.rentvine.com/blog/expands-ai-leadership-with-rentvine-cru-and-mcp (2026-10-22) [Documented]
- S15 https://mcp.rentvine.ai — root, /docs, /openapi.json, and `/.well-known/oauth-protected-resource/mcp` [Documented]
- S16 https://www.rentvine.com/llms.txt [Documented]
- S17 https://help.rentvine.com/llms.txt [Documented]
- S18 https://www.rentvine.com/sitemap.xml [Documented]
- S19 https://help.rentvine.com/en/collections/19753996-release-notes [Documented]
- S20 rentvine.com homepage, /integrations, /ai-assistant, /blog/what-is-mcp-property-management-software, /digital-terms-of-use [Documented]
- A1–A7 blog and help pages added during verification [Documented]; A8 S10 screenshot transcription [Documented]; A9 targeted searches (nothing found); A10 re-scan of S2
- T0–T7 live tests [Live-tested, 2026-11-17]
- Standard locations checked (packet §3, all 2026-11-17):
  - www.rentvine.com: /llms.txt 200 (marketing content, no API content); /llms-full.txt, /openapi.json, /openapi.yaml, /swagger.json, /changelog, /.well-known/api-catalog, /.well-known/mcp.json all 404; /sitemap.xml 200; /release-notes redirects to the help-center release notes (200)
  - status.rentvine.com: 200 (Atlassian Statuspage)
  - docs.rentvine.com: / 200 (Redoc); /llms.txt, /llms-full.txt, /openapi.*, /swagger.json, /sitemap.xml, /changelog, /release-notes, /.well-known/api-catalog, /robots.txt all 403
  - help.rentvine.com: /llms.txt 200 (help-article index with per-article .md files); /sitemap.xml 200
  - mcp.rentvine.ai: / 200; /docs and /openapi.json 200 (a "Rentvine AI" service, not an MCP tool list); OAuth protected-resource metadata 200 (scopes `mcp:read`, `mcp:write`); other well-known paths, /llms.txt, /sitemap.xml 404
  - Account API host: root 404 JSON; /.well-known/api-catalog returns the web-app HTML shell
  - MCP standard version: not stated on any public page and not observed (T7)
  - Documentation-home sequence (packet §2): the vendor's /open-api page links to docs.rentvine.com (found at step 1); common hosts and searches were also run and recorded. MCP Registry: 0 servers. GitHub org: one `practice-sandbox` repo, no SDK. npm: 0 packages.

## Evidence-amendment log
Recorded in the packet during the evidence session's single verification pass. The grading runs added nothing.
- A1 Zapier how-to blog (C2.5, C3.2, C3.4, C5.2): generic rate-limit advice only; cost "may depend on your Rentvine plan and configuration".
- A2 open-api-integration blog (C5.1, C5.2): no special approval needed; included at no additional cost.
- A3 MCP Tip of the Week #38 (C3.6, C4.2): closed beta then rollout; MCP actions tagged by "the MCP key" in the work-order timeline.
- A4 MCP conference recap: context only.
- A5 "MCP is here" blog (C3.6, C5.2): sign in with normal Rentvine login; included with every plan; financials read-only.
- A6 general API article: no bearing.
- A7 release notes weeks 42/44/46 (C4.4): product-level notes; none mentions API endpoint changes.
- A8 webhook screenshot transcription (C1.4, C2.8).
- A9 targeted searches (C2.4, C2.5, C2.8–C2.11, C3.5, C4.4): no first-party page on rate limits/429, idempotency, concurrency control, versioning/deprecation, request IDs, webhook retries/signature format, or a sandbox.
- A10 spec re-scan (checklist items 7, 13, 16, 17, 22, 27, 28, 30, 32; C2.6).

## Grading runs
- Evidence session (tester: discovery, verification, live battery, packet frozen): 2026-11-17
- Runs 1–3 (PLM; methodology prompt and the frozen packet only; no vendor-specific guidance; run in parallel as separate agents): 2026-11-17
- Results: Run 1 87 (B+), Run 2 87 (B+), Run 3 87 (B+). All three: 85 (B) before the MCP step.
- Coverage map: all 32 checklist items scored identically in all three runs (capability coverage 83.33% in each).
- Check-level agreement: **25 of 28 checks unanimous.**

| Check | Run 1 | Run 2 | Run 3 | Resolved | Basis |
|---|---|---|---|---|---|
| C2.7 Bulk or incremental export | partial | yes | yes | **yes** | The yes definition includes "documented incremental sync via updated-since plus pagination" that retrieves a full dataset without per-record calls. `dateTimeModifiedMin/Max` with paging is documented on 17 operations, including the four export endpoints, transactions, entries, journal entries, ledgers, accounts, tenants, owners and vendors (S2.2), and was honored live (T3a–T3h). Work orders, bills and deposits lack the filter but can be paged in full, not read record by record. Run 1's reading ("export covers only some resources") applies to a dedicated export path, which the rubric does not require for yes. |
| C3.6 Delegated access | partial | yes | yes | **yes** | The rubric states that a hosted, official MCP server where "the operator signs in and approves scopes instead of pasting a key" qualifies. The official MCP uses OAuth sign-in (S4, S6 "leave Authentication set to OAuth"), with documented scopes `mcp:read`/`mcp:write` and authorization server `account.rentvine.com` (S15), per-tool approval (S4), and the addendum assigns OAuth-token revocation to the client (S7 §3). Run 1's concern (no documented Rentvine-side screen for revoking grants; the S5 sentence about API keys) is noted but does not outweigh the explicit rule. |
| C4.4 Kept current | no | no | partial | **no** | The check asks for reliable visibility into changes to the API reference and machine-consumable resources. No API changelog exists on any first-party host (S19, A9); the 2026 release notes are product-level and none mentions an API change (A7); the spec stays at 1.0.0 with no change history (S2). Run 3 counted the current product release notes and MCP activity-feed note as thin currency information. |

- Score effect of the disagreements: none. The code checked every combination of the three disputed marks: placement share ranges from 11.0/22 to 12.5/22, and every combination gives 85 (B) before the MCP step and 87 (B+) after it.
- Unresolved disagreements: none.
- Sensitivity shared by all three runs (not a disagreement): capability coverage is 1.15 weight points short of 0.85. If checklist item 6 (General ledger) or item 7 (Bank accounts) were scored 1.0 instead of 0.5, gate 2 would allow an A and the score would be 93 (A), then 97 (A+) after the MCP step. All three runs scored both at 0.5 on the same evidence (read-only, with no documented create/update; S2.5).

## API eligibility
- Qualifying API: yes
- Interface label: none
- API operator: Rentvine, LLC [S2 server `https://{account}.rentvine.com/api/manager`; S8 §8a API license] [Documented]
- Access or credential issuer: Rentvine. The customer's own users create keys in Settings > Users, Roles and API > API [S2.1; S9] [Documented]
- Eligibility basis: a public OpenAPI 3.1 reference of 205 operations on Rentvine's own manager API, with HTTP Basic key/secret authentication [S2], confirmed live with 200 responses [T1, Live-tested]. Rentvine also runs an official hosted MCP server [S3, S4, S6, S15].

## Context
- Product type: Accounting/PMS
- What the API is for: programmatic access to a property manager's system of record with trust accounting. Core objects are properties, units, leases, tenants, lease ledgers, the general ledger and bank accounts, plus owners, vendors, bills, deposits, work orders, screening applications and messaging. Core workflows are reading records, posting lease charges and payments, and creating and updating leases through move-out.

## Provider and property-management fit
- What this product is: cloud property-management software for professional managers (single-family, multifamily, commercial), with trust accounting, owner/tenant portals, leasing, maintenance and reporting [S16; S12] [Documented]
- Bank status: not a bank. The reviewed materials describe software and do not name Rentvine as a bank [S16; packet §4 provider context] [Documented]
- Who provides any bank account or regulated banking service: unclear; no banking provider is named in the packet. Bank accounts appear only as chart-of-account records [S2.5] [Documented]
- What the customer actually receives: a PMS and trust-accounting software subscription priced per active unit, with the Open API and MCP connection included [S12; S1; S3] [Documented]
- Property-management fit: PM-specialized [S16; S1; S2 tag groups Leases, Properties, Screening, Maintenance, Portfolios] [Documented]
- Documented PM-specific workflows [S2.4; Appendix A] [Documented]:
  - lease creation (including from an application), lease status through move-out, recurring charges
  - lease charges and tenant payments
  - owner statements and statement batches; owner ACH details
  - work orders with vendor assignment
  - screening application status and screening report orders
  - property, unit, tenant and owner deactivation; deposit-level reconciliation
- Trust or fiduciary workflow support: limited. The API documents escrow flags on accounts (`isEscrow`), diagnostics (escrow mismatch, reserve not met, prepayment mismatch, manager ledger balance, bank-account reconciliation lapse), security-deposit fields, and a readable "Lease Deposit Release Credit" transaction type [S2.5; Appendix A rows 38–48]. The published documentation shows no way to apply, release or refund a deposit, create an owner distribution, post a journal entry or run a full bank reconciliation [S2.5].
- Operational role and dependencies: Rentvine is itself the PMS and trust ledger; the operator still needs its own bank for the trust accounts, and a webhook receiver or polling job to react to changes.

## Coverage classification (fixed before inspection)
- Checklist: Accounting/PMS published list, no deviation (packet §1, recorded 2026-11-17 17:41:26 UTC)
- Size (weights re-added in code; matches the packet's stated totals): 32 items, total weight 69 (objects 22 items / weight 46 · workflows 3 / 9 · lifecycle actions 7 / 14)
- One missing critical item = 3 ÷ 69 = 4.35% of capability coverage

| # | Item | Kind | Class | Weight | State | Score |
|---|---|---|---|---|---|---|
| 1 | Properties | object | critical | 3 | present: list/search/get/create/update/delete/activate/deactivate/export (App. A 114–122, 203); live T1–T3 | 1.0 |
| 2 | Units | object | critical | 3 | present: list/create/view/update/delete/activate/deactivate/export (App. A 123–129, 204) | 1.0 |
| 3 | Leases | object | critical | 3 | present: list/create/view/update/delete/status/export, lease tenants (App. A 159–168, 202); live T2e, T6a | 1.0 |
| 4 | Tenants | object | critical | 3 | present: list/search/get/create/update/delete/activate/deactivate (App. A 64–71) | 1.0 |
| 5 | Lease ledgers / transactions | object | critical | 3 | present: transaction and entry search by type/void/date; create lease charge and payment (App. A 27–31); live T3e–f | 1.0 |
| 6 | General ledger | object | critical | 3 | partial: accounts, ledgers, entries and journal entries read/search only; no journal-entry or account create/update (S2.5) | 0.5 |
| 7 | Bank accounts | object | critical | 3 | partial: no dedicated resource; read-only as chart-of-account records; no create/update; no documented balance read (S2.5; T5a) | 0.5 |
| 8 | Owners | object | important | 2 | present: CRUD plus activate/deactivate (App. A 56–63) | 1.0 |
| 9 | Bills | object | important | 2 | present: list/create/get/update/void/approve/print, payables search (App. A 4–10, 33) | 1.0 |
| 10 | Payments | object | important | 2 | present: create lease payment and other payment; read via transaction search (App. A 29, 31; S2.4) | 1.0 |
| 11 | Applicants | object | important | 2 | present: list/get/summary/export, applicant tab, status update, order screening reports (App. A 181–186, 205) | 1.0 |
| 12 | Work orders / tasks | object | important | 2 | present: CRUD, status CRUD, inspections (App. A 131–148) | 1.0 |
| 13 | Reconciliation | object | important | 2 | partial: deposit-level reconcile/unreconcile and `reconciliationID` filters only (S2.4, S2.5) | 0.5 |
| 14 | Vendors | object | important | 2 | present: CRUD plus activate/deactivate, vendor trades (App. A 72–79, 142–145) | 1.0 |
| 15 | Recurring charges | object | important | 2 | present: full CRUD (App. A 169–173) | 1.0 |
| 16 | Security deposits (hold, apply, refund) | object | important | 2 | partial: held as a move-in charge or field; release type readable; no apply/release/refund operation (S2.5) | 0.5 |
| 17 | Owner distributions or statements | object | important | 2 | present (statements): search/list/get/download, batches (App. A 108–113); generated statements need no write | 1.0 |
| 18 | Files | object | optional | 1 | partial: upload only; no list/get/delete (S2.4) | 0.5 |
| 19 | Communications | object | optional | 1 | present: email send/list/get, chat create/list, SMS send/list (App. A 49–55) | 1.0 |
| 20 | Custom fields | object | optional | 1 | present: categories create, values get/save (App. A 187–191) | 1.0 |
| 21 | Associations | object | optional | 1 | present: CRUD plus activate/deactivate (App. A 80–87) | 1.0 |
| 22 | Inventory | object | optional | 1 | partial: materials and labor-rate CRUD; appliances read-only as an include (S2.5) | 0.5 |
| 23 | Read core records | workflow | critical | 3 | present (S2 index; live battery T1–T6) | 1.0 |
| 24 | Post ledger charges and payments | workflow | critical | 3 | present: `POST /accounting/leases/{leaseID}/charges`, `/payments`, `POST /accounting/other-payments` (S2.4) | 1.0 |
| 25 | Create and update leases | workflow | critical | 3 | present: `POST /leases`, `POST /leases/{leaseID}` (S2.4) | 1.0 |
| 26 | Change lease status through move-out | lifecycle | critical | 3 | present: `POST /leases/{leaseID}/status` with notice, move-out and closed dates (S2.4) | 1.0 |
| 27 | Void or reverse a posted lease-ledger transaction | lifecycle | important | 2 | absent (S2.5) | 0.0 |
| 28 | Record a returned or refunded payment | lifecycle | important | 2 | absent; return types readable only (S2.5) | 0.0 |
| 29 | Void a bill | lifecycle | important | 2 | present: `DELETE /accounting/{billID}` (S2.4) | 1.0 |
| 30 | Finalize or undo a bank reconciliation | lifecycle | important | 2 | partial: single-deposit reconcile/unreconcile only, "as opposed to a full bank statement reconciliation" (S2.4) | 0.5 |
| 31 | Deactivate or archive a property, unit, tenant, or owner | lifecycle | important | 2 | present: `/deactivate` on all four (S2.4) | 1.0 |
| 32 | Delete or archive optional records | lifecycle | optional | 1 | partial: custom-field values clear with null; no file delete; no notes endpoint (S2.4, S2.5) | 0.5 |

## Functional coverage map
- Core objects:
  - Present: properties, units, leases, tenants, lease transactions (critical, 3 each); owners, bills, payments, applicants, work orders, vendors, recurring charges, owner statements (important, 2 each); communications, custom fields, associations (optional, 1 each).
  - Partial or read-only: general ledger, bank accounts (critical, 3 each); reconciliation, security deposits (important, 2 each); files, inventory (optional, 1 each).
  - Absent: none.
- Primary operational workflows: read core records; post lease charges and payments; create and update leases. All present.
- Lifecycle actions:
  - Present: lease status through move-out (critical, 3); void a bill, deactivate records (important, 2 each).
  - Partial: bank reconciliation (important, 2); optional-record delete (optional, 1).
  - Absent: void/reverse a lease transaction, record a returned or refunded payment (important, 2 each).

## Category 1: Functional Coverage and Usefulness (gate 2)
- C1.1 Object coverage: **86.96%** (40.0 / 46) [Documented S2, S2.4, S2.5, App. A; Live-tested T1–T6]
- C1.2 Write coverage: **100%** (rows 24 and 25, 6 / 6; read-only row 23 excluded) [Documented S2.4 createLeaseCharge, createLeasePayment, createOtherPayment, createLease, updateLease]
- C1.3 Lifecycle coverage: **60.71%** (8.5 / 14) [Documented S2.4 updateLeaseStatus, voidBill, deactivate, reconcile/unreconcile; S2.5 no void/return/refund operations]
- C1.4 Change notification: **partial** [Documented; Live-tested]
  - Push: webhooks are visible only for Work Order, Lease and Property Created/Updated (the dropdown scrolls; no full event list is published) [S10; A8]. That is well under 0.50 of critical-plus-important weight.
  - Polling: `dateTimeModifiedMin/Max` with paging is documented on the lease, property, unit and application exports and on accounting, tenant, owner and vendor searches [S2.2]; the lease export's modified timestamp updates on status changes, move-out and lease transactions [S2.2]. Honored live: 13 → 1 → 12 → 0 items on the property export; 0 of 4 transactions after the cutoff [T3a–T3h, T3e/f].

Gate 2 math: capability coverage = 83.33% over 69 weight (57.5 / 69); write coverage 100%; C1.4 partial; critical item scored 0: none; unverified weight: 0%; gate 2 allows: **B** (below 0.85); verification coverage = 100% (4 / 4)

What this means for you: you can read nearly everything and do the core day-to-day writes: create leases, post rent charges and tenant payments, run move-outs, void bills, deactivate records and run work orders. The published documentation shows no way to void or reverse a posted charge or payment, record a returned (NSF) payment, apply or refund a security deposit, post a journal entry or run a full bank reconciliation. Those stay in the Rentvine web app. Webhooks cover only leases, properties and work orders, so other changes need a scheduled "what changed since" check.

## Category 2: API Design, Reliability, and Operability (placement)
- **C2.1 Modern API conventions: yes** [Documented S2, S2.2; Live-tested T1]. Resource-oriented REST over JSON with an OpenAPI 3.1 spec; updates by POST and voids by DELETE are accepted conventions.
- **C2.2 Consistent typing: no** [Documented S2.3; Live-tested T2e, T3a]. ID fields are integer in 61 schema properties and string in 81; `is*` flags are boolean in 38, integer in 21 and string in 46; `isDeposit` is typed both boolean and "1"/"0" string; money is mostly decimal strings but `number`/`double` in 15 places. Live, `isActive` is the string "1" on properties but the integer 1 inside the export's owners array.
- **C2.3 Structured errors: partial** [Documented S2.2; Live-tested T4a–T4d]. The documented schema is `{"error": string}` with no machine code. Observed shapes vary: a not-found returned as 400 (T4a); a 404 with `code` as a string (T4b); a 401 with `code` as a number (T4d); invalid query values returned a 500 with an empty HTML body (T4c). Usable messages, but no stable machine code.
- **C2.4 Duplicate prevention: no** [Documented S2.2 "idempot" count 0; A9]. No idempotency key or equivalent is documented for charges, payments, bills or deposits.
- **C2.5 Graceful handling under load: partial** [Live-tested T1 and all reads; Documented S2.2, A1, A9]. `RateLimit-Policy` and `RateLimit` headers (account, user and api-key quotas) appear on ordinary reads, but no 429, `Retry-After` or backoff behavior is documented. Observed signals with no documented behavior.
- **C2.6 Pagination: partial** [Documented S2.2; Live-tested T1–T2d]. `page`/`pageSize` with total-items, total-pages and next-page headers are documented and observed. Limits: no stable-ordering guarantee on `GET /properties` and most lists (non-ID order observed, T2d); maximum page size enforced but unpublished; `Pagination-Next-Page` returns the last page number instead of the documented null (T2b, T2c).
- **C2.7 Bulk or incremental export: yes** [Documented S2.2, App. A 202–205; Live-tested T3a–T3h]. Dedicated export endpoints for leases, properties, units and applications, plus documented updated-since filtering with paging on 17 operations; honored live. (Resolved from a 2–1 split; see "Grading runs".)
- **C2.8 Webhook security and delivery reliability: partial** [Documented S10, A8, A9]. A resettable signing key "used to sign all HTTP payloads" exists; no signature algorithm or header, retry policy or replay guidance is documented.
- **C2.9 Concurrency and conflict control: no** [Documented S2.2 counts 0; A9]. No ETag, If-Match, 412/409 or version-token mechanism.
- **C2.10 Versioning and backward compatibility: no** [Documented S2, S2.2, S8 §8c]. No version identifier in path or header (`/api/manager`; 1.0.0 is only the document version), no deprecation policy, and the terms allow API changes "with or without notice".
- **C2.11 Request traceability: partial** [Live-tested T1–T6; Documented S2.2]. No Rentvine request ID is documented or returned; the only per-request identifier is CloudFront's `X-Amz-Cf-Id`, undocumented and not shown to be usable with support.
- **C2.12 Service availability and status transparency: yes** [Documented S13]. Public Statuspage with an "API" component, monthly incident history with Atom/RSS feeds, and uptime history (100% Sept–Nov 2026). No SLA is published (S8 §1); not required for yes.
- Evidence parity: C2.3, C2.5, C2.6 and C2.11 were observed live; each is partial on the merits, so parity did not change a mark.

Checks earned: 5.5 of 12 applicable; verification coverage = 100%

What this means for you: the API is easy to call and page through, shows your rate-limit budget on every response, and has export endpoints that return only what changed. Build defensively, though: values come back as text and inconsistently typed, errors lack codes, the published documentation shows nothing that stops a retried payment from posting twice or one tool from overwriting another's edit, and there is no versioning promise.

## Category 3: Access Control and Safe Automation (placement)
- **C3.1 Read-only credentials: yes** [Documented S2.1, S9, S11, S2.4]. Each key is assigned a role built from per-action permission toggles, and write operations are documented as requiring named permissions ("Update Lease", ApproveBill, ModifyDeposit). A role with no modify toggles yields a read-only key. (All three runs agreed; S11 does not name a "read-only" role as such.)
- **C3.2 Scoped credentials: yes** [Documented S9, S11]. Keys inherit fine-grained action toggles from their role and can be associated with a pod; least privilege is recommended.
- **C3.3 Multiple keys: yes** [Documented S2.1, S9]. "New API Key" with a reference name; each key is labeled and managed separately.
- **C3.4 Rotation and revocation: yes** [Documented S9]. Self-serve "regenerate the secret", change role, or "delete the key".
- **C3.5 Test environment and isolation: no** [Documented S2.2 "sandbox" count 0; A9; packet §2]. No sandbox, test mode or test-account offering is documented. The `practice-sandbox` GitHub repo is not an API test environment, and the tester's demo account has no first-party documentation.
- **C3.6 Delegated access: yes** [Documented S4, S6, S15, S7 §3]. The official hosted MCP uses OAuth sign-in with a Rentvine account, with scopes `mcp:read`/`mcp:write`, per-tool approval, and client-side token revocation. The REST API itself offers only HTTP Basic keys. (Resolved from a 2–1 split; see "Grading runs".)

Checks earned: 5 of 6 applicable; verification coverage = 100%

What this means for you: you can give each app or AI agent its own key limited to exactly the permissions it needs, and rotate or delete it yourself. AI assistants connect by signing in, not by pasting a key. The published documentation shows no test environment, so automations get tested against a live account.

## Category 4: Documentation and AI-Agent Readiness (placement)
- **C4.1 Complete self-serve reference: partial** [Documented S2, S2.1, S2.2, S2.4]. Public reference with auth instructions, a curl example, 205 operations, parameters and response examples. Gaps: `POST /accounting/bills` and `POST /properties` list no request fields; "Related endpoints" text cites `PUT` paths that do not exist; webhooks are absent from the reference; no error-code catalog.
- **C4.2 Reliable machine-consumable integration path: yes** [Documented S2]. A downloadable OpenAPI 3.1.0 spec covering all 205 operations. The official MCP is also noted (writes for work orders, notes, prospects and inspections; financials read-only) [S3, S5]. No official SDKs [packet §2].
- **C4.3 AI-readable documentation: no** [Documented S16, S17; packet §3]. The www llms.txt is marketing content; the help-center llms.txt indexes product how-tos with no endpoint reference; docs.rentvine.com/llms.txt returns 403; no documentation-search MCP.
- **C4.4 Kept current: no** [Documented S19, A7, A9, S2]. No API changelog on any first-party host; current release notes are product-level and none mentions an API change; the spec stays at 1.0.0 with no change history. (Resolved from a 2–1 split; see "Grading runs".)
- AI agent path: official MCP (read-write; financial records read-only), hosted at `https://mcp.rentvine.ai/mcp` with OAuth sign-in, "90+ governed tools" [S3, S4, S6, S14, S15]; plus a public OpenAPI 3.1 spec [S2]; no SDKs. MCP standard version checked: not stated on any public page and not observed (T7 was rejected for a missing, undocumented `x-rentvine-account` header) [packet §3; T7].

Checks earned: 1.5 of 4 applicable; verification coverage = 100%

What this means for you: a developer or AI coding tool can load the OpenAPI file and get most of the way. A few create endpoints are under-documented, there's no AI-ready copy of the API docs, and no API changelog warns you when something changes.

## Category 5: Accessibility and Cost (gate 1)
- **C5.1 Self-serve API key: yes** [Documented S2.1, S9, A2]. Customers create keys themselves in Settings > Users, Roles and API > API; "Any developer can access the API without needing special approval from our team."
- **C5.2 Not commercially gated: yes** [Documented S12, S9, A2, S3, S4, S6, A5]. One plan lists "Fully Open API & Integrations" and "Native MCP" as included; the API has no usage restrictions or extra charges; the MCP is "Not an add-on" and free with every plan. The addendum's "where identified as such on the Order Form, an Add-On Service" (S7 §1) and A1's "may depend on your Rentvine plan" are generic hedges, not evidence of an actual charge. Claude or ChatGPT plan requirements are third-party costs.

Gate 1 allows: **A** (both yes); verification coverage = 100%

What this means for you: any Rentvine customer can create an API key today and connect the AI (MCP) connector, with no sales call, upgrade or extra fee.

## Grade
- Gate 1, open access: allows **A** (C5.1 yes, C5.2 yes)
- Gate 2, documented capability: allows **B** (capability coverage 83.33%, below 85%; write coverage 100%; C1.4 partial; no critical item at 0)
- Letter from the gates: **B**; binding gate: **gate 2**
- Placement share: 12.0 of 22 Category 2–4 checks = 54.55% (Cat 2 5.5/12; Cat 3 5/6; Cat 4 1.5/4)
- Score math: 80 + round(9 × 0.545455 = 4.909) = 80 + 5 = **85 (B)**
- Official MCP server (one-step bump): **yes** — Rentvine's vendor-hosted MCP at mcp.rentvine.ai reads and acts on account data and has been generally available to every customer since 2026-10-22 [S3, S4, S6, S14, S15]. After the step: **87 (B+)**
- **Published numeric score: 87 / 100**
- **Letter grade: B+**
- Evidence tier: baseline verified
- Overall verification coverage: 100% (28 / 28). No group is Unable to verify; unverified checklist weight 0% (limit 30%); overall ≥ 80%.
- Partial-result flag: no
- Unresolved evaluator disagreements: none (three split checks resolved; none changes the score)

Calculation (computed with code, re-run on the resolved marks):
```
objects    22 items, weight 46, earned 40.0, coverage 0.8696
workflows   3 items, weight  9, earned  9.0, coverage 1.0000
lifecycle   7 items, weight 14, earned  8.5, coverage 0.6071
total weight 69, earned 57.5, capability coverage 0.833333
C1.2 write coverage 1.0
one critical item = 4.3478%;  gap to 0.85 = 1.15 weight points
RESOLVED: share 12.0/22 = 0.545455 -> 80 + round(4.909091) = 85
Run1 share 11.0/22 = 0.500000 -> 85
Run2 share 12.0/22 = 0.545455 -> 85
Run3 share 12.5/22 = 0.568182 -> 85
every combination of disputed marks gives pre-MCP score: [85]
MCP step: B (85) -> B+ (87)
```

## Good for / Not built for
- **Good for:** syncing properties, units, leases, tenants, owners, vendors and transactions into your own tools; creating leases and recurring charges; posting rent charges and tenant payments; running move-outs; managing work orders, bills and screening status; sending tenant emails and texts; pulling owner statements; and letting Claude or ChatGPT work on your Rentvine data through the official MCP.
- **Not built for:** voiding or reversing posted charges and payments, recording returned (NSF) payments, applying or refunding security deposits, posting journal entries, sending owner distributions, or running a full bank reconciliation. The published documentation shows no way to do these through the API.

## Bottom line for a property manager
Rentvine is property-management software with its own trust accounting, not a bank, and every customer gets its API and official AI (MCP) connector at no extra cost, with keys you create yourself. Today you can build automations that read almost everything, create leases, post charges and payments, run move-outs, and manage work orders, bills and tenant messages, with each key limited to exactly what that tool needs. The biggest strength is breadth plus open access: 205 documented operations, "changed since" export endpoints, fine-grained per-key roles, and an included AI connector. The biggest limitations are engineering polish and the correction side of accounting: the published documentation shows no protection against double-posting on retries, no versioning promise, no test environment, and no way to reverse ledger entries, record returned payments, refund deposits or reconcile a full bank statement, and values come back as inconsistently typed text. You still need your own bank for the trust accounts, and those accounting corrections stay inside the Rentvine app. Rentvine is 1.15 weight points short of an A gate: a documented write path for the general ledger (journal entries) or bank accounts would move it to 97 (A+).
