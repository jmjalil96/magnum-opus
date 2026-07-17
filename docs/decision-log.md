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
