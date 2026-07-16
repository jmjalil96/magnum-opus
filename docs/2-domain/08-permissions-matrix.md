---
status: skeleton
---

# Permissions Matrix

> **Owns:** The enforceable role × action grid: exactly who can do what, on which records.

## Matrix
_(empty — one row per action with a `PERM-` ID, one column per role from [02-personas-and-roles.md](../1-product/02-personas-and-roles.md); transitions and screens reference these rows)_

| ID | Action | Role A | Role B | ... |
|----|--------|--------|--------|-----|
| _(empty)_ | | | | |

## Record-level rules
_(empty — when permission depends on the record, not just the role: own records vs anyone's, assignment, state-dependent access)_

## Open decisions
- [ ] Is access purely role-based, or does record ownership/assignment matter?
- [ ] Does any permission depend on the record's current state?
- [ ] Who can manage users and assign roles?
- [ ] Default stance for unlisted actions: deny or allow?
