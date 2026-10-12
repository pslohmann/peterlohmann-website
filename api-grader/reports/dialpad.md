# API Report Card: Dialpad — Dialpad Public API (v2)

## Run metadata
- Methodology version: 1.1
- Evaluating model: Claude Opus 4.8 (claude-opus-4-8)
- Date run: 2026-10-11
- Provisional evidence-packet: DIALPAD-PKT-v1.0 (documentation tier)
- Final evidence-packet: **DIALPAD-PKT-v1.1** (v1.0 documentation + read-path live amendment, frozen 2026-10-11)
- Evidence-discovery mode: tool-enabled discovery + one controlled verification pass (OpenAPI spec downloaded and parsed firsthand)
- Evidence tier: **Baseline verified** (read-path live; write-path documentation-graded)
- Live-write method and safety: **none — write-path checks documentation-graded.** No writes performed against the live account; nothing created, sent, charged, or mutated. Operator ran read-only GETs in his own terminal; the API key was never transmitted to the evaluator or pulled from Vercel.
- Minimum live-test battery: **complete.** Steps 1–5 performed live; step 7 (idempotency) **N-A** (no idempotency documented); steps 6 (create/update) & 8 (webhook delivery) **not run** (write-path) and graded from documentation.
- Live tests performed: authenticate (200); paginated read + cursor traversal (page 1→2); filtered query (`state=active`/`suspended`) honored; deliberate errors (404 + 401, structured); response-header/traceability inspection.
- Live tests not possible / not run: write create/update (step 6), idempotency (step 7 — N-A), webhook delivery (step 8) — all documentation-graded.
- Documentation-graded checks (Baseline verified): **C1.2, C1.3, C2.4, C2.8** (write/lifecycle/idempotency/webhook-delivery graded from the OpenAPI spec + first-party docs rather than live writes).

## Final evidence packet manifest (first-party)
- developers.dialpad.com/llms.txt; /docs/{welcome, getting-started, authentication-basics, oauth, api-key-generation, rate-limits, event-subscriptions, event-subscriptions-via-websocket, call-events, access-control-policies, sms-api, stats-api-dialpad-analytics, getting-help}.md
- developers.dialpad.com/reference/{userslist, usersupdate, smssend, webhookscreate, accesscontrolpoliciesassign, oauth2tokenpost, webhookslist}.md
- developers.dialpad.com/changelog (latest: "Recently Launched (July 2025)")
- github.com/dialpad/dialpad-python-sdk + dialpad_api_spec.json (OpenAPI, parsed firsthand: 120 paths / 193 operations); PyPI python-dialpad
- dialpad.com/, /pricing/, /faq/, /industry/real-estate/, /mcp/; status.dialpad.com
- Live read-path observations, 2026-10-11 (operator-executed; see packet v1.1)
- Inaccessible: help.dialpad.com (HTTP 403 to automated fetch; "Create an API Key" article read via browser). Not located: developers.dialpad.com/openapi.json, /reference/download-api-collection, llms-full.txt (all 404).

## Evidence-amendment log
- Controlled verification: downloaded + parsed the OpenAPI spec firsthand (confirmed 191/193 ops document only 200; 0 error responses; 0 idempotency/ETag/If-Match params; cursor on 31 ops; security schemes api_key_in_url + bearer_token) — affects C1.1–C1.3, C2.1–C2.4, C2.6, C2.9, C2.11.
- Live amendment (read-path battery): **C2.3** no→yes (structured Google-format error with machine-readable `reason` observed); **C2.11** no→partial (`x-cloud-trace-context` per-request ID observed, undocumented); **C2.5** confirmed no (no rate-limit headers); **C2.2** confirmed partial (live `id` string); **C2.6** confirmed partial (cursor traversal works).

## API eligibility
- Qualifying API: **yes**
- API operator: **Dialpad, Inc.** [status.dialpad.com; API served from dialpad.com; OAS `servers`]
- Access / credential issuer: **Dialpad, Inc.** — admin-created API keys (api-key-generation.md: Admin Settings → My Company → Authentication → API Keys → Add Key) and registered OAuth 2.0 apps (oauth.md)
- Eligibility basis: first-party REST API at `/api/v2` exposing Dialpad's own telephony/messaging/contact-center functions; access self-authorized by company admins (API key) or via Dialpad-approved OAuth apps. Confirmed live: operator's key authenticated (HTTP 200).

## Context
- Software category: **Other (business communications / UCaaS + CCaaS)**
- What the API is for: Dialpad's API exposes its cloud phone/contact-center/messaging platform — users/seats, phone numbers, calls (history + control), SMS/MMS, call centers/departments/offices/IVRs, contacts, rooms/devices, recordings/transcripts/AI recaps, analytics exports, and event subscriptions. Core objects are users, numbers, calls, and messages; core workflows are reading those records, sending messages / placing calls, and provisioning/assigning users and numbers.

## Provider and property-management fit
- What this product is: an AI-powered business communications platform (cloud phone, contact center, sales dialer, SMS, meetings, AI). [dialpad.com]
- Bank status: **N-A** (not a financial institution). [dialpad.com]
- Who provides any bank/regulated service: **none / N-A.**
- What the customer receives: software/service access to a cloud communications platform and its API; no account/ledger/fund-holding relationship.
- Property-management fit: **general-purpose.** [dialpad.com/industry/real-estate names "property managers" in marketing copy but ties no API or workflow to PM]
- Documented PM-specific workflows: **none found.** The real-estate page is generic UCaaS marketing.
- Trust/fiduciary workflow support: **N-A** (no fund-holding or trust-accounting functionality).
- Operational role and dependencies: a communications layer a property manager could build on for prospect/tenant/vendor calls and texts and call-center routing; it would sit alongside (not replace) a PMS, accounting/trust system, and any payments provider.

## Coverage classification (fixed before inspection; "Other" category → derived from the communications-platform domain)
| Object or workflow | Class | Weight | Present / read-only / absent |
|---|---|---|---|
| Users / operators | Critical | 3 | Present (full CRUD + lifecycle) |
| Phone numbers | Critical | 3 | Present (list/assign/swap/unassign/release; no net-new DID purchase) |
| Calls (records + control) | Critical | 3 | Present (read + initiate + control) |
| Messages (SMS/MMS) | Critical | 3 | Present but send-only via REST (history is event-driven) |
| Contacts | Important | 2 | Present (CRUD + upsert) |
| Call centers / departments / offices | Important | 2 | Present (CRUD + operators) |
| Webhooks / event subscriptions | Important | 2 | Present (CRUD) |
| Recordings / transcripts / AI | Important | 2 | Present (read + sharelinks; AI via events) |
| Rooms / devices | Optional | 1 | Present |
| Stats / analytics exports | Optional | 1 | Present (async CSV export) |
| Fax / voicemail / settings | Optional | 1 | Partial (fax assign; settings read) |
| WF: read core records | Critical | 3 | Present (verified live: users/calls) |
| WF: send SMS / initiate call | Critical | 3 | Present (POST /sms, POST /call) |
| WF: create/update/assign users & numbers | Critical | 3 | Present |
| Lifecycle: assign/unassign, (de)activate, transfer/hangup, delete, disable | Important | 2 | Present |

## Functional coverage map
- Core objects: Users ✅, Numbers ✅ (assign/swap/release; no purchase), Calls ✅, Messages ⚠️ (send-only via REST; inbound/history via SMS events), Contacts ✅, Call centers/departments/offices ✅, Webhooks/subscriptions ✅, Recordings/transcripts/AI ✅, Rooms/devices ✅, Stats ✅, Fax/settings ⚠️.
- Primary operational workflows: read core records ✅ (live), send SMS ✅, initiate/transfer/hang up calls ✅, create/update/assign users ✅, assign/swap/release numbers ✅, manage routing (call routers/IVRs) ✅, async analytics export ✅.
- Principal lifecycle changes: number assign/unassign/swap/delete ✅, user status/DND/deactivate/delete ✅, call transfer/hangup/unpark ✅, delete contact/room/channel/IVR/call center/department ✅, subscription create/disable/delete ✅.

---

## Category 1: Functional Coverage and Usefulness: 15.0/15
- **C1.1 Object coverage: yes** — weighted coverage ≈ **91%** (21.0/23), no critical object absent. Users/Calls/Contacts/CC/offices/webhooks/recordings/rooms/stats = 1.0; Messages = 0.5 (REST send-only, history via events); Fax/settings = 0.5. [OAS path list; packet C1]
- **C1.2 Core operational actions: yes** — weighted ≈ 100%; create/update present for every critical write workflow: POST /sms, POST /call, POST+PATCH /users, POST /numbers/assign, plus broad POST/PATCH across resources (OAS: 56 POST / 24 PATCH). *(documentation/OAS-graded — writes not executed live)* [OAS; packet C1]
- **C1.3 Delete or lifecycle actions: yes** — weighted ≈ 100%; all principal lifecycle actions present (26 DELETE ops + status/transfer/hangup/assign/unassign). *(documentation/OAS-graded)* [OAS; packet C1]
- **C1.4 Change notification: yes** — event subscriptions cover call / sms / contact / agent_status + a `changelog` catch-all, with rich call-event states; ≥ 0.85 weighted of critical+important state changes. [event-subscriptions.md; call-events.md]

Score math: earned 4.0 of 4 applicable; fraction 1.000; category = **15.0/15**; verification coverage 4/4 = 100%.
What this means for you: Dialpad's API exposes essentially the entire communications platform — you can read users/calls, send texts, place/transfer/end calls, provision and assign numbers, manage call routing, and subscribe to real-time events. For automations and AI agents around phone/text workflows, the surface is broad and mature. The one gap: you read inbound SMS through event webhooks, not a REST message-history endpoint.

## Category 2: API Design, Reliability, and Operability: 5.0/10
- **C2.1 Modern conventions: yes** — REST, resource-oriented, standard verbs, JSON, `/api/v2`. [OAS; reference pages; live 200]
- **C2.2 Consistent typing: partial** — schemas typed, but core `id` fields are inconsistent: live `id` returns as a **string** while the OAS types several IDs int64, and ID typing varies across objects (ContactProto.id string vs ActiveCallProto.id int64). [smssend.md; webhookscreate.md; OAS parse; live step 2]
- **C2.3 Structured errors: yes** — live 404/401 return a structured body with `error.code`, human-readable `error.message`, and machine-readable `error.errors[].reason` (`notFound`/`required`), correct HTTP status, consistent across cases. *(Observed behavior; note: the docs document no errors — this does not rescue C4.1.)* [live step 4]
- **C2.4 Duplicate prevention: no** — no idempotency keys/headers anywhere (OAS: 0); POST /sms and POST /call (consequential writes) can duplicate on retry; only contacts PUT is naturally idempotent. *(documentation-graded)* [OAS parse; packet C2.4]
- **C2.5 Graceful handling under load: no** — numeric limits are published, but there is no documented 429, no `Retry-After`, no backoff guidance, and live responses carry **no** `X-RateLimit-*` headers. [rate-limits.md; live step 5]
- **C2.6 Pagination: partial** — cursor pagination works (traversal verified live, page 1→2), but no documented stable-ordering guarantee, no total-count, and a ≤100 cap. [getting-started.md; OAS; live steps 2–3]
- **C2.7 Bulk or incremental export: partial** — async CSV export exists (Stats API) but covers only call records/stats; no updated-since/delta sync; other objects via cursor lists only. [stats-api-dialpad-analytics.md]
- **C2.8 Webhook security and delivery reliability: partial** — JWT HS256 signed payloads (shared secret), but no documented retry policy, no replay/dedup guidance, and events may arrive out of order. *(documentation-graded)* [event-subscriptions.md; webhookscreate.md; call-events.md]
- **C2.9 Concurrency and conflict control: no** — no ETag/If-Match/version fields and no 409 semantics (OAS: 0); last-write-wins. [OAS parse; usersupdate.md]
- **C2.10 Versioning and backward compatibility: partial** — explicit `/api/v2` path version + per-endpoint "added on" notes and a v1 archive, but no formal backward-compatibility policy or defined deprecation window. [packet C2.10]
- **C2.11 Request traceability: partial** — every response carries a unique `x-cloud-trace-context` identifier, but it is **undocumented** by Dialpad and not referenced in the support flow (which asks for the key's last 4). [live step 1/5; getting-help.md]
- **C2.12 Service availability and status transparency: yes** — public Statuspage with a dedicated "API Platform" component, incident history, and published uptime (e.g., Calling 99.999%/30d). No SLA, but uptime present. [status.dialpad.com]

Score math: earned 6.0 of 12 applicable (yes×3 = C2.1/C2.3/C2.12; partial×6 = C2.2/C2.6/C2.7/C2.8/C2.10/C2.11; no×3 = C2.4/C2.5/C2.9); fraction 0.500; category = **5.0/10**; verification coverage 12/12 = 100%.
What this means for you: the API is a clean, predictable REST interface, errors are structured and actionable, and uptime is transparent — all good for building. The weak spots are reliability-engineering guarantees: no idempotency (retrying a failed "send SMS" can double-send), no concurrency control (last write wins), no documented rate-limit recovery contract, and webhook delivery has signatures but no documented retry/ordering guarantees. Build in your own dedup, backoff, and webhook reconciliation.

## Category 3: Access Control and Safe Automation: 3.5/5
- **C3.1 Read-only credentials: no** — no read-only credential mode; scopes are action/export-oriented and endpoint access is gated by a user/admin role flag, not a read-only grant; admin keys act across all users. [oauth.md; api-key-generation.md]
- **C3.2 Scoped credentials: partial** — per-key/token scope selection (Dialpad-approved) + Access Control Policies, but ACPs bind to **users, not API credentials**, their permission sets are write-only and AI-contact-center-scoped, and OAuth has an undefined basic-access floor. [api-key-generation.md; access-control-policies.md; accesscontrolpoliciesassign.md]
- **C3.3 Multiple keys: yes** — multiple named API keys in the admin "API Keys" list. [api-key-generation.md; Help Center]
- **C3.4 Rotation and revocation: yes** — self-serve key expiration set at creation + OAuth `POST /oauth2/deauthorize` revocation. [api-key-generation.md; oauth.md]
- **C3.5 Test and production isolation: yes** — separate sandbox host and credentials (sandbox.dialpad.com vs dialpad.com), confirmed in OAS `servers`. [authentication-basics.md; OAS]

Score math: earned 3.5 of 5 applicable; fraction 0.700; category = **3.5/5**; verification coverage 5/5 = 100%.
What this means for you: you can issue multiple keys, scope them somewhat, rotate/revoke them, and keep a separate sandbox — solid basics. But you cannot mint a guaranteed read-only key, so handing a limited key to an AI agent or third party carries more blast radius than ideal; compensate with a dedicated scoped OAuth app and tight monitoring.

## Category 4: Documentation and AI-Agent Readiness: 3.8/5
- **C4.1 Complete self-serve reference: partial** — ~200 public reference pages with typed params + 200-response examples + schemas, but no request/code samples and no documented error responses (confirmed: live errors exist but are undocumented). [userslist.md; live step 4]
- **C4.2 Reliable machine-consumable path: yes** — OpenAPI 3.x spec (Dialpad GitHub, auto-generated from live OAS) + actively maintained official Python SDK (`python-dialpad`, updated 2026-03-31) + a first-party MCP server. [github.com/dialpad/dialpad-python-sdk; dialpad.com/mcp]
- **C4.3 AI-readable documentation: yes** — comprehensive `llms.txt` index + clean per-endpoint Markdown (`.md` twin on every page). [llms.txt; packet C4.3]
- **C4.4 Kept current: partial** — on-site changelog is ~15 months stale (latest July 2025) and irregular, though the SDK/OAS pipeline is current and endpoints carry version-added notes; no formal deprecation policy. [developers.dialpad.com/changelog]

Score math: earned 3.0 of 4 applicable; fraction 0.750; category = **3.8/5** (3.75); verification coverage 4/4 = 100%.
What this means for you: an AI coding tool can consume this API well — the OpenAPI spec, maintained Python SDK, `llms.txt`, and per-endpoint Markdown are genuinely strong. The reference lacks copy-paste request examples and (notably) documents none of the error responses your code will actually hit, and the public changelog looks neglected.

## Category 5: Accessibility and Cost: 11.3/15
- **C5.1 Self-serve API key: yes** — a company admin creates keys in-product (name, expiration, scopes) with no sales call or approval for key creation itself. [api-key-generation.md]
- **C5.3 Not commercially gated: partial** — API access is tier-gated with inconsistent first-party sources: FAQ ("Enterprise plans include Admin and Reporting APIs"), help docs (reportedly Pro+), dev docs (silent), pricing page (no mention of API). Not on the entry Standard tier. The operator's own key authenticated live, confirming API access is enabled on his plan (tier not disclosed). [dialpad.com/faq; dialpad.com/pricing; live step 1]

Score math: earned 1.5 of 2 applicable; fraction 0.750; category = **11.3/15** (11.25); verification coverage 2/2 = 100%.
What this means for you: once you're on an entitled plan, getting a key is instant and self-serve — no gatekeeping. The catch is the entitlement: API access isn't on the cheapest tier and the exact plan requirement is stated inconsistently across Dialpad's own pages, so confirm your tier includes it before you build (yours evidently does, since your key works).

## Total
- Raw: **38.50 / 50**
- Normalized before rounding: **77.00 / 100**
- Published numeric score: **77 / 100**
- Letter grade: **C+**
- Evidence tier: **Baseline verified** (read-path live; write-path documentation-graded)
- Overall verification coverage: **100%** (27/27 applicable checks verified; no category below 0.70; none "Unable to verify"; gate passes)
- Partial-result flag: no (battery steps 1–5 complete; publishable)
- Independent-run reconciliation: 3 independent runs on the frozen packet agreed on **24 of 27** checks. Post-live reconciled = 77 (C+). (Documentation-tier run values were 75/71/74; live upgrades to C2.3/C2.11 lifted the reconciled result to 77.)
- Unresolved evaluator disagreements and possible score effect:
  - **C1.1 object coverage (yes vs partial)** — hinges on scoring the Numbers object 1.0 vs 0.5 (net-new DID purchase absent). Resolved **yes** (2 of 3 runs + merits). If partial → 73 (C). *One-band sensitivity.*
  - **C5.3 commercial gating (partial vs no)** — all three runs chose partial, but "no" is defensible if API access is effectively Enterprise-gated. If no → 70 (C-). *Largest downside; your plan tier would settle it.*
  - Minor: C2.2 (partial vs no → 76 vs 77); C3.1 (no vs yes), C3.2 (partial vs yes), C3.4 (yes vs partial) — each ±0.5 within Category 3.

## Bottom line for a property manager
Dialpad has a genuinely strong, buildable communications API: near-complete coverage of calls, texts, users, numbers, routing, and real-time events, a maintained OpenAPI spec and Python SDK, clean AI-readable docs, and transparent uptime — you (or an AI agent) can automate prospect/tenant/vendor calling and texting workflows on it today. It earns a **C+ (77/100, Baseline verified)**: the drag is reliability-engineering maturity — no idempotency, no concurrency control, no documented rate-limit recovery, webhook delivery without retry/ordering guarantees, no read-only credential, and errors that work at runtime but aren't documented. None of that is a dealbreaker; it just means you own the retry/dedup/reconciliation logic. Practically, Dialpad is a **communications layer, not a property-management system** — there is no dedicated PM offering and no trust/fiduciary functionality, so it sits alongside your PMS, accounting/trust system, and payments provider rather than replacing any of them. Before building, confirm your plan tier includes API access (yours does) — that's the single biggest swing in this grade.
