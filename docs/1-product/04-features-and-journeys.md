---
status: skeleton
---

# Features & User Journeys

> **Owns:** The feature catalog (`F-` IDs) and the end-to-end user journeys (`J-` IDs) — what the user experiences from entry to outcome. This is the spine the other docs hang off: every feature must trace to journeys, screens, rules, and acceptance criteria.

## Feature catalog

| ID | Feature | One-liner | Journeys | Status |
|----|---------|-----------|----------|--------|
| F-001 | Claim submission | Create a claim for an insured (employee or dependent), with documents attached, via any submitting role (D-003, D-006, D-012). | _(TBD)_ | v1 |
| F-002 | Claim processing | Analysts work claims through the lifecycle from received to settled; amounts are recorded, not computed — the insurer adjudicates (D-013). | _(TBD)_ | v1 |
| F-003 | Claim tracking | Scoped read side: employee sees own + dependents', HR their clients', agent their book — all full detail (D-004, D-005, D-009, D-010). | _(TBD)_ | v1 |
| F-004 | Enrollment management | Operations maintains the roster: employees, dependents, policy assignments, effective dates (D-007). | _(TBD)_ | v1 |
| F-005 | Client & catalog administration | Corporate clients, agent↔client links (D-010), insurer catalog (D-011), policies. | _(TBD)_ | v1 |
| F-006 | User & access management | Accounts and invitations for all seven roles; one role per user (D-008). | _(TBD)_ | v1 |
| F-007 | Audit trail | Actions are recorded and reviewable; the read-only `auditor` role (D-001) is its primary consumer. | _(TBD)_ | v1 |
| F-008 | Email notifications | Key claim events notify by email; no in-app notifications in v1 (D-014). | _(TBD)_ | v1 |
| F-009 | Dashboard | Basic per-role counts and aging (e.g. claims by status, time-in-status); no report builder, no exports (D-015). | _(TBD)_ | v1 |

Later versions (explicitly out of v1 — see [PRD non-goals](01-prd.md)): invoicing, resolution center, library, AI chat, accident & life lines, in-app reimbursement calculation, multi-role accounts, in-app notifications, exports.

## Journeys
_(empty — one section per journey, using the template below)_

<!-- Template — copy per journey:

### J-001 — <journey name>

- **Feature:** F-XXX
- **Actor & goal:** <who, trying to achieve what>
- **Entry condition:** <where they start, what must already be true>
- **Happy path:** <numbered steps; reference SCR- and T- IDs>
- **Alternate / failure paths:** <what can diverge and what happens; reference ERR- IDs>
- **Resulting state:** <what is true when the journey ends>
- **Screens:** SCR-XXX, ...
- **Rules & permissions:** BR-XXX, PERM-XXX, ...
- **Acceptance:** AC-XXX, ...
-->

## Open decisions
- [x] **[blocking]** What are the v1 features? → F-001..F-009 above
- [x] Which journey is the core one — the vertical slice that gets specified to full depth first? → The claim lifecycle, submission → settlement (confirmed)
- [ ] Journeys per feature: how many, and which are v1? (To be defined feature by feature.)
