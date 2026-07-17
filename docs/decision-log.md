---
status: drafted
---

# Decision Log

> **Owns:** Every resolved decision (`D-` IDs): what was chosen, what was rejected, and why. Docs link here instead of re-explaining rationale.

Decision statuses: `open` → `decided` → `superseded` (by a later `D-` entry, which must reference the old one). Where a decision came out of a depth/scoring ladder (0–10, target, cap), record the ladder result in the Context field.

## Index

| ID | Decision | Status | Date | Docs affected |
|----|----------|--------|------|---------------|
| D-001 | Brokerage internal roles: admin, claims analyst, auditor, operations | decided | 2026-07-16 | 02-personas |
| D-002 | "Agent" = external sales agent/producer with a book of clients | decided | 2026-07-16 | 02-personas, 03-glossary |
| D-003 | Claims submitted by employee, HR, or brokerage `claims-analyst`/`admin` | decided | 2026-07-16 | 02-personas |
| D-004 | HR sees full claim detail, including medical data | decided | 2026-07-16 | 02-personas |
| D-005 | Agent sees full claim detail for their book | decided | 2026-07-16 | 02-personas |
| D-006 | Dependents covered via the employee; no dependent logins | decided | 2026-07-16 | 02-personas, 03-glossary |
| D-007 | Full enrollment management is in v1, owned by operations | decided | 2026-07-16 | 02-personas |
| D-008 | One role per user in v1; multi-role deferred | decided | 2026-07-16 | 02-personas |
| D-009 | One HR user can span multiple corporate clients | decided | 2026-07-16 | 02-personas |
| D-010 | Agents ↔ clients: many-to-many, unrestricted | decided | 2026-07-16 | 02-personas |
| D-011 | Insurer is a catalog entry; no app involvement | decided | 2026-07-16 | 02-personas, 03-glossary |
| D-012 | Claims carry documents, at submission and later | decided | 2026-07-16 | 04-features, 12-files |
| D-013 | Amounts are record-only; the insurer adjudicates | decided | 2026-07-16 | 04-features, 01-prd |
| D-014 | Notifications are email-only in v1 | decided | 2026-07-16 | 04-features, 14-notifications |
| D-015 | v1 reporting = basic dashboard, no exports | decided | 2026-07-16 | 04-features, 01-prd |
| D-016 | Cancellation reachable from any state, terminals included | decided | 2026-07-16 | 06-state-machines |
| D-017 | `settled` = any final insurer outcome (paid/partial/denied) | decided | 2026-07-16 | 06-state-machines |
| D-018 | T-001 gate: linked enrollment + service date in period; portal claims arrive as snapshot | decided | 2026-07-16 | 06-state-machines, 07-business-rules, 03-glossary |
| D-019 | No review → draft return; analysts fix inside review | decided | 2026-07-16 | 06-state-machines |
| D-020 | `not_processed` = died before being sent to the insurer | decided | 2026-07-16 | 06-state-machines |
| D-021 | Cancel: analyst+admin from active states; admin-only from terminals | decided | 2026-07-16 | 06-state-machines |
| D-022 | No direct `pending_information` → `settled`; must return via T-004 | decided | 2026-07-16 | 06-state-machines |
| D-023 | Cancellations and not-processed both require a recorded reason | decided | 2026-07-16 | 06-state-machines |
| D-024 | BR-002: the linked enrollment must belong to the claim's insured | decided | 2026-07-16 | 07-business-rules, 06-state-machines |
| D-025 | T-007: sources restricted to draft/review; triggered by analyst+admin | decided | 2026-07-16 | 06-state-machines |
| D-026 | Dead-end reasons = mandatory category + optional note | decided | 2026-07-16 | 06-state-machines |
| D-027 | `drafted` gate allows TBD cross-doc reference cells, not same-doc unknowns | decided | 2026-07-16 | 00-conventions |
| D-028 | v1 reason category lists for T-006 and T-007 defined | decided | 2026-07-16 | 06-state-machines |
| D-029 | `duplicate` disambiguated by state: draft/review → T-007, later → T-006 | decided | 2026-07-16 | 06-state-machines |

## Entries

### D-001 — Brokerage internal roles

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** v1 needs the brokerage's internal role split before any permission or lifecycle work.
- **Chosen:** Four roles: `admin` (system management), `claims-analyst` (works claims), `auditor` (read-only everything), `operations` (enrollment management, **no claim edit access**; will own invoicing in a later version — invoicing is not v1).
- **Rejected:** Single role; handler+admin; handler+supervisor+admin.
- **Consequences:** Permissions matrix needs four brokerage columns; operations having zero claim-edit rights is a hard line the matrix must enforce.
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md)

### D-002 — "Agent" means external producer

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** "Agent" was ambiguous (broker-side account manager vs external producer vs insurer contact); every doc needs one meaning.
- **Chosen:** An external sales agent/producer, outside the brokerage, who brought in corporate clients and holds a book of them.
- **Rejected:** Broker-side account manager; insurer-side contact.
- **Consequences:** Agents are *external* users whose visibility is scoped by their book; "agent" must never be used for brokerage staff or insurer people in any doc.
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md), [03-glossary.md](1-product/03-glossary.md)

### D-003 — Who can submit a claim

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Submission channel determines journeys and permissions.
- **Chosen:** The insured employee, their corporate client's HR, and on the brokerage side exactly `claims-analyst` and `admin` (e.g. a claim received by email) can submit. `auditor` (read-only) and `operations` (no claim edit) cannot, per D-001.
- **Rejected:** Employee-only; HR-only.
- **Consequences:** At least three submission journeys exist for the same claim entity; the claim must record who submitted it and on whose behalf. The permissions matrix must list the submit action with exactly these four roles: `employee`, `hr`, `claims-analyst`, `admin`. `agent`, `auditor`, and `operations` are excluded — for `agent` that was never on the table and would need its own decision.
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md)

### D-004 — HR visibility: full detail

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Health claims carry medical data; this was flagged as the blocking privacy decision. The privacy-preserving alternatives were considered explicitly.
- **Chosen:** HR sees everything the employee sees: documents, medical information, amounts.
- **Rejected:** Existence+status only; status+amounts; per-claim employee consent.
- **Consequences:** No medical-data firewall between employee and HR needs to be modeled; if this ever changes (regulation, client demand), it becomes a superseding decision with schema and permission impact.
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md)

### D-005 — Agent visibility: full detail

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Same privacy question as D-004, for an *external* party.
- **Chosen:** Agents see full claim detail for corporate clients in their book.
- **Rejected:** Existence+status only; status+amounts.
- **Consequences:** Book membership is the only thing standing between an agent and claim data — the client↔agent relationship must be modeled precisely and kept current.
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md)

### D-006 — Dependents: covered, no login

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Corporate health policies typically cover dependents; the question was whether v1 models them and whether they get access.
- **Chosen:** Claims can be for a dependent; the employee (or HR/brokerage) submits and tracks. Dependents never log in.
- **Rejected:** Employee-only v1; dependent portal accounts.
- **Consequences:** The claim subject ("Insured") is employee-or-dependent, so the data model needs dependents from day one; no auth work for dependents.
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md), [03-glossary.md](1-product/03-glossary.md)

### D-007 — Enrollment management is v1

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Operations' job is enrollment; the question was how much of it lives in-app for v1.
- **Chosen:** Full management: operations maintains the roster in-app — add/remove employees and dependents, manage policy assignments, effective dates.
- **Rejected:** Minimal roster upkeep; imported/seeded data with enrollment deferred.
- **Consequences:** Enrollment is a v1 feature area of its own (catalog, journeys, screens, permissions), not just reference data.
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md)

### D-008 — One role per user in v1

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** The HR-user-who-is-also-an-insured-employee overlap forced the question.
- **Chosen:** A user account holds exactly one role in v1; multi-role support is deferred.
- **Rejected:** Multi-role single account; separate accounts per role as a designed mechanism.
- **Consequences:** Simpler auth and permission model; a person needing two roles is out of scope for v1 and must not be quietly worked around in the design.
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md)

### D-009 — HR user spans multiple corporate clients

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Corporate groups/holdings run several corporate clients but count as one program to the brokerage; their HR needs to see across all of them.
- **Chosen:** HR user ↔ corporate client is a many-per-user relationship; an HR user's scope is the union of their linked clients.
- **Rejected:** One client per HR user.
- **Consequences:** HR scoping is a user↔client link, not a single foreign key. Whether the group/holding ("program") itself becomes a modeled entity is a pending domain-model question.
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md)

### D-010 — Agents ↔ clients: unrestricted many-to-many

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Whether a corporate client can have several agents.
- **Chosen:** Agents and corporate clients are linked many-to-many (join table), no restriction on count in either direction. An agent's "book" is exactly their set of links.
- **Rejected:** Exactly one agent per client.
- **Consequences:** Since agents see full detail (D-005), every link row grants an external party access to a client's claims — creating and removing these links deserves care (permissions, audit).
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md)

### D-011 — Insurer is catalog-only

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Whether insurer staff ever touch the app.
- **Chosen:** The insurer is a catalog entity (referenced by policies/claims); no insurer users, no insurer-facing surface.
- **Rejected:** Insurer-side portal access.
- **Consequences:** No auth, permissions, or screens for insurers in any version currently planned; communication with insurers happens outside the app (or via integrations, if ever, as a separate decision).
- **Docs affected:** [02-personas-and-roles.md](1-product/02-personas-and-roles.md), [03-glossary.md](1-product/03-glossary.md)

### D-012 — Claims carry documents, at submission and later

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Reimbursement claims involve receipts, invoices, medical reports; the question was whether and when files attach.
- **Chosen:** Documents attach at submission and can be added during processing (e.g. when an analyst requests missing paperwork).
- **Rejected:** Submission-only attachment; data-only claims.
- **Consequences:** File upload is v1 core, and the claim lifecycle needs a way to request/receive additional documents mid-processing (a state, a transition, or both — doc 06's call).
- **Docs affected:** [04-features-and-journeys.md](1-product/04-features-and-journeys.md), [12-files-and-documents.md](3-backend/12-files-and-documents.md)

### D-013 — Amounts are record-only

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** The biggest v1 scope question: is the app a workflow tool or a calculation engine?
- **Chosen:** The insurer adjudicates. The app records claimed amounts and, at settlement, what the insurer approved/paid. No coverage math in-app.
- **Rejected:** Assisted estimates from policy rules; full in-app adjudication.
- **Consequences:** v1 needs no coverage-rule modeling (deductibles, copays, limits), which keeps the Policy entity thin; settlement data entry is manual and analyst-owned. If assisted estimates ever come, that's a superseding decision with heavy schema impact.
- **Docs affected:** [04-features-and-journeys.md](1-product/04-features-and-journeys.md), [01-prd.md](1-product/01-prd.md)

### D-014 — Email-only notifications in v1

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Whether v1 notifies at all, and through what.
- **Chosen:** Key events send email; no in-app notification surface in v1.
- **Rejected:** Email + in-app; in-app only; none.
- **Consequences:** v1 needs an email provider (integration doc) and a notification catalog, but no in-app notification UI, unread counts, or preference center.
- **Docs affected:** [04-features-and-journeys.md](1-product/04-features-and-journeys.md), [14-notifications.md](3-backend/14-notifications.md)

### D-015 — v1 reporting is a basic dashboard

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Whether v1 includes reporting beyond filtered lists.
- **Chosen:** Simple per-role counts and aging (claims by status, time-in-status). No report builder, no exports.
- **Rejected:** Nothing; exports only; dashboard + exports.
- **Consequences:** One dashboard feature (F-009) scoped per role; export requests get deferred, not sneaked in as "just a CSV button."
- **Docs affected:** [04-features-and-journeys.md](1-product/04-features-and-journeys.md), [01-prd.md](1-product/01-prd.md)

### D-016 — Cancellation from any state, literally

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Whether "cancelled from any state" includes the terminals.
- **Chosen:** Yes — even `settled` and `not_processed` claims can move to `cancelled` (e.g. data-entry errors). Terminals are soft with respect to cancellation only; `cancelled` itself is final.
- **Rejected:** Non-terminal only; any except settled.
- **Consequences:** Settled figures can change retroactively — dashboards and any future reporting must treat cancellation of settled claims as a real event, not an impossibility. Guarded by D-021 (admin-only from terminals) and D-023 (reason required).
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-017 — `settled` means any final insurer outcome

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** The machine had no home for insurer denials.
- **Chosen:** `settled` = the insurer gave a verdict: paid in full, partial, or denied. Outcome and amounts are fields on the settled claim.
- **Rejected:** Denials as `not_processed`; a separate `denied` state.
- **Consequences:** Settlement data entry (T-005) must capture an outcome type, not just amounts; dashboards must not read `settled` as "money paid."
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-018 — T-001 gate and the portal snapshot

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Who or what validates enrollment, coverage, and dates at `draft` → `review`.
- **Chosen:** The claim must be linked to a real enrollment whose period contains the service date (BR-001). Brokerage-created claims link the enrollment from the start; portal submissions arrive as an unverified **snapshot**, and the brokerage links the real enrollment before T-001.
- **Rejected:** Fully automatic move on submission; purely manual judgment with no enforced rule.
- **Consequences:** The claim model needs both snapshot fields and an enrollment link; BR-001 is the first system-enforced rule; T-001 is a brokerage action, so portal-submitted claims always pass through brokerage hands before `review`.
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md), [07-business-rules.md](2-domain/07-business-rules.md), [03-glossary.md](1-product/03-glossary.md)

### D-019 — No return path from review

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** What happens to incomplete portal submissions that reach `review`.
- **Chosen:** No `review` → `draft` transition. Analysts have edit rights in `review` and fix issues themselves; portal users are never sent back.
- **Rejected:** Return-to-draft loop; dead-ending unfixable claims as the standard path.
- **Consequences:** Analysts need full claim-edit capability in `review`; portal users never see a "returned" claim, so no portal rework flow exists in v1.
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-020 — `not_processed` = never sent

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** With denials landing in `settled` (D-017), what `not_processed` is for.
- **Chosen:** Claims that die before reaching the insurer: abandoned, ineligible, duplicate. `cancelled` = withdrawn/error; `not_processed` = couldn't proceed.
- **Rejected:** Insurer-bounced claims; both combined.
- **Consequences:** Tension flagged in doc 06's open decisions: the original statement allowed `not_processed` from all non-terminal states (including `sent_to_insurer`), which contradicts "never sent" — sources need restricting or the semantics need widening. (Resolved by D-025; duplicate handling refined by D-029.)
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-021 — Who cancels

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** T-006 works from any state (D-016), so its trigger needed care.
- **Chosen:** From active states: `claims-analyst` and `admin`. From `settled`/`not_processed`: `admin` only — cancelling a terminal claim rewrites history.
- **Rejected:** Analyst+admin everywhere; portal users cancelling own drafts.
- **Consequences:** Portal users cannot cancel at all in v1 — they must ask the brokerage; the permissions matrix gets a state-dependent row.
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-022 — Settlement only from `sent_to_insurer`

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Whether a claim can settle straight out of `pending_information`.
- **Chosen:** No — if the insurer settles while information was pending, the analyst records T-004 then T-005. One extra click, cleaner machine.
- **Rejected:** A direct `pending_information` → `settled` transition.
- **Consequences:** Exactly one path into `settled`; time-in-state metrics for `pending_information` stay honest.
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-023 — Reasons required for both dead-ends

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Whether T-006/T-007 record why.
- **Chosen:** Both cancellation and not-processed require a recorded reason — nothing dies silently.
- **Rejected:** Reason on cancellation only; optional notes.
- **Consequences:** Both transitions carry a mandatory reason field; whether it's free text or categories is an open decision in doc 06.
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-024 — BR-002: enrollment must belong to the insured

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Review finding: BR-001 alone lets an analyst link any enrollment with a matching period — wrong person, wrong corporate client — and advance the claim.
- **Chosen:** A separate rule BR-002: the linked enrollment must belong to the claim's insured (and therefore the correct corporate client). Enforced at T-001 alongside BR-001.
- **Rejected:** Folding it into BR-001 (distinct failure mode deserves a distinct, referenceable rule).
- **Consequences:** T-001 now cites BR-001 + BR-002. Whether the insured is derived from the enrollment (making BR-002 structural) is an open domain-model decision.
- **Docs affected:** [07-business-rules.md](2-domain/07-business-rules.md), [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-025 — T-007 resolved: draft/review only, analyst+admin

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** D-020's "never sent" semantics contradicted the original "from all non-terminal states" statement.
- **Chosen:** Semantics win. T-007 sources are `draft` and `review` only; a claim already at the insurer ends via `settled` or `cancelled`. Triggered by `claims-analyst` or `admin`.
- **Rejected:** Widening `not_processed` to mean "ended without a verdict"; admin-only triggering.
- **Consequences:** The machine has no dead-end from `sent_to_insurer`/`pending_information` except cancellation — dashboards can treat those states as "insurer has it."
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-026 — Dead-end reasons: category + optional note

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** D-023 required reasons but left the format open.
- **Chosen:** A mandatory category from a fixed list, plus an optional free-text note — countable on dashboards, flexible in detail.
- **Rejected:** Free text only; categories only.
- **Consequences:** Two category lists (cancellation, not-processed) must be defined — open decision in doc 06; the claim model carries category + note fields for its dead-end.
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-027 — `drafted` gate refined

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Review finding: doc 06 was `drafted` with TBDs. Strictly, no doc could reach `drafted` while referencing IDs another doc hasn't minted — circular waiting between docs.
- **Chosen:** `drafted` = every section has substantive content and no *same-doc* unknowns; cross-doc reference cells may stay TBD until the owning doc mints the IDs. `reviewed` still requires all references to resolve.
- **Rejected:** Strict gate (doc 06 back to skeleton); a new intermediate status.
- **Consequences:** Doc 06 legitimately holds `drafted` now that T-007 is resolved; the future validator checks same-doc completeness for `drafted` and reference resolution for `reviewed`.
- **Docs affected:** [00-conventions.md](00-conventions.md)

### D-028 — Reason category lists (v1)

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** D-026 mandated categories but the lists didn't exist — the last same-doc unknown blocking doc 06's `drafted` status.
- **Chosen:** T-006: `withdrawn_by_claimant`, `duplicate`, `created_in_error`, `administrative`. T-007: `ineligible`, `duplicate`, `abandoned`, `out_of_submission_window`. Free-text note optional with any category.
- **Rejected:** Moving list ownership to another doc to dodge the status gate.
- **Consequences:** Both lists are v1-frozen; adding a category is a decision-log event. Spanish UI labels for the categories join the copy work later.
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)

### D-029 — `duplicate` disambiguated by state

- **Status:** decided
- **Date:** 2026-07-16
- **Context:** Review finding: `duplicate` on both reason lists (D-028) conflicted with D-020's "duplicates are `not_processed`", making terminal-state selection ambiguous.
- **Chosen:** State decides, never the user: a duplicate discovered in `draft`/`review` must exit via T-007 with `duplicate`; one discovered in `sent_to_insurer`/`pending_information` (or found on a terminal claim) exits via T-006 with `duplicate`, since T-007 is unavailable there (D-025). Refines D-020's "cancelled = withdrawn/error" to include late-found duplicates.
- **Rejected:** Removing `duplicate` from T-006 (late-found duplicates would be mislabeled `created_in_error`/`administrative`, losing the count).
- **Consequences:** Dashboard counts stay meaningful: `not_processed`+`duplicate` = caught before sending; `cancelled`+`duplicate` = caught after. The rule is mechanically enforceable — no state offers both paths.
- **Docs affected:** [06-state-machines-and-transitions.md](2-domain/06-state-machines-and-transitions.md)
