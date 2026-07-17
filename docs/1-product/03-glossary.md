---
status: skeleton
---

# Glossary

> **Owns:** One canonical name per domain concept, used consistently across all docs, code, and UI.

## Terms

| Term | Definition | Do not call it | Spanish UI label |
|------|-----------|----------------|------------------|
| Brokerage | The insurance broker company operating the app; its staff are the internal users. | broker (for the org), agency | _(TBD)_ |
| Corporate Client | A company whose employees are covered; the brokerage's customer. | company, account, group | _(TBD)_ |
| Employee | A person employed by a Corporate Client and covered under its policy; portal user. | member, worker | _(TBD)_ |
| Dependent | A person covered through an Employee (e.g. spouse, child). Never logs in. | beneficiary, family member | _(TBD)_ |
| Insured | The person a claim is for: an Employee or a Dependent. | patient, member | _(TBD)_ |
| HR User | A Corporate Client's HR person with portal access; submits and tracks claims for that client's employees. | HR manager, client user | _(TBD)_ |
| Agent | External sales agent/producer who holds a book of Corporate Clients; portal user with visibility into their book. | broker, producer, account manager | _(TBD)_ |
| Claim | A request for reimbursement of a health expense, from submission to settlement. Health only in v1. | case, ticket, request | _(TBD)_ |
| Enrollment | Managing the roster: which Employees and Dependents are covered and their policy assignments, with effective dates. | registration, onboarding | _(TBD)_ |
| Insurer | The insurance company that ultimately pays. A catalog entry in the app; insurer people never use it (D-011). | carrier, company | _(TBD)_ |
| Policy | _(definition pending — how policies, plans, and coverage are modeled is not yet decided)_ | plan (until decided) | _(TBD)_ |
| Service Date | The date the medical service behind a claim was provided; must fall within the linked enrollment's period (BR-001). | claim date, event date | _(TBD)_ |
| Snapshot | The unverified insured/enrollment data a portal-submitted claim carries in `draft`, before the brokerage links the real enrollment (D-018). | — | _(TBD)_ |

## Open decisions
- [ ] Spanish UI label for every term (single canonical label each; the UI is Spanish-only).
- [ ] How is "Policy" modeled — per corporate client? per insured? plan tiers? (blocks the Policy definition)
- [ ] Is "Insured" the right umbrella term for "Employee or Dependent as claim subject"? (introduced by Claude — veto freely)
