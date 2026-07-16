---
status: skeleton
---

# State Machines & Transitions

> **Owns:** Every formal state, every transition (with a stable ID), who can trigger it, what it validates, and what side effects it fires.

## State machines
_(empty — one section per entity that has states)_

### States
_(empty — state list with a one-line meaning each)_

### Transitions table
_(empty — one row per transition; `T-` IDs per [00-conventions.md](../00-conventions.md). Cells hold **references**, not definitions: who-can-trigger lives in the permissions matrix, validations in business rules, side effects in notifications/jobs/audit.)_

| ID | From → To | Trigger (PERM refs, or "system") | Preconditions (BR refs) | Side effects (N / JOB / AUD refs) |
|----|-----------|----------------------------------|-------------------------|-----------------------------------|
| _(empty)_ | | | | |

### Diagram
_(empty — state diagram once states/transitions are settled)_

## Open decisions
- [ ] Which entities have state machines?
- [ ] Are any transitions automatic (time- or event-driven) as opposed to user-triggered?
- [ ] Are any transitions reversible? Is there a generic "revert" or only explicit backward transitions?
