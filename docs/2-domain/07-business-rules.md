---
status: skeleton
---

# Business Rules

> **Owns:** Every rule with an "if/then" that isn't a state transition — calculations, validations, deadlines, limits. Each rule gets a `BR-` ID, referenced from transitions, endpoints, and acceptance criteria.

## Calculations
_(empty — formulas and derived values: inputs, formula, rounding, edge cases)_

## Validations
_(empty — cross-field and cross-entity rules; single-field constraints live in 09-database-schema.md)_

## Deadlines & time rules
_(empty — anything driven by dates or elapsed time)_

## Limits & quotas
_(empty — maximums, minimums, rate-style limits)_

## Open decisions
- [ ] What values does the system calculate rather than store as input?
- [ ] Are there deadlines or time-based rules? What happens when they're missed?
- [ ] Are there per-user, per-account, or per-plan limits?
