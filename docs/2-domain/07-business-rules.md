---
status: skeleton
---

# Business Rules

> **Owns:** Every rule with an "if/then" that isn't a state transition — calculations, validations, deadlines, limits. Each rule gets a `BR-` ID, referenced from transitions, endpoints, and acceptance criteria.

## Calculations
_(empty — formulas and derived values: inputs, formula, rounding, edge cases)_

## Validations
_(cross-field and cross-entity rules; single-field constraints live in 09-database-schema.md)_

### BR-001 — Service date within enrollment period
The claim's service date must fall within the period of the enrollment linked to the claim. Enforced at T-001 (`draft` → `review`) — a claim cannot enter `review` without passing it. Source: D-018.

### BR-002 — Enrollment belongs to the insured
The enrollment linked to a claim must belong to the claim's insured (the Employee or Dependent the claim is for), and therefore to the correct Corporate Client. Without this, any enrollment with a matching period would satisfy BR-001. Enforced at T-001, together with BR-001. Source: D-024.

## Deadlines & time rules
_(empty — anything driven by dates or elapsed time)_

## Limits & quotas
_(empty — maximums, minimums, rate-style limits)_

## Open decisions
- [ ] What values does the system calculate rather than store as input?
- [ ] Are there deadlines or time-based rules? What happens when they're missed?
- [ ] Are there per-user, per-account, or per-plan limits?
