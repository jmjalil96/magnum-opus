---
status: drafted
---

# Personas & Roles

> **Owns:** Who uses the app, what each persona is trying to accomplish, and the list of system roles.

## Personas

### Brokerage staff (internal)

- **Admin** — brokerage staff who manage the system itself: users, corporate clients, configuration.
- **Claims Analyst** — brokerage staff who work claims day to day, from submission through settlement.
- **Auditor** — brokerage staff with read-only access; reviews activity and records but changes nothing.
- **Operations** — brokerage staff who manage enrollment (roster of employees/dependents and their policy assignments). No claim edit access. Will also own invoicing in a later version (D-001).

### Portal users (external)

- **HR User** — works at a corporate client; submits claims on behalf of that client's employees and tracks them. Sees full claim detail, including medical information (D-004). One HR user can span several corporate clients — corporate groups/holdings run multiple clients as one program (D-009).
- **Agent** — external sales agent/producer, outside the brokerage, who brought in corporate clients and holds a book of them. Agents and clients relate many-to-many with no limit on either side (D-010). Sees full claim detail for the clients in their book (D-002, D-005).
- **Employee** — an insured employee of a corporate client; submits and tracks their own claims and those of their dependents (D-006).

### Covered but not users

- **Dependent** — a person covered under an employee's policy (e.g. spouse, child). Claims can be for a dependent, but dependents never log in; the employee, HR, or the brokerage submits and tracks on their behalf (D-006).

## Roles

One system role per persona, 7 in total:

| Role | Side | Claim access (summary — enforceable grid lives in [08-permissions-matrix.md](../2-domain/08-permissions-matrix.md)) |
|------|------|------------------------------------------------------------------------------------------------------------------|
| `admin` | Brokerage | Full, plus system management |
| `claims-analyst` | Brokerage | Works claims end to end |
| `auditor` | Brokerage | Read-only, everything |
| `operations` | Brokerage | No claim edit access; manages enrollment |
| `hr` | Portal | Their corporate client's claims, full detail |
| `agent` | Portal | Claims of the clients in their book, full detail |
| `employee` | Portal | Own claims and their dependents' claims |

## Persona → role mapping

1:1 — each persona above maps to exactly one role. **One role per user in v1**: a user account holds a single role; multi-role support (e.g. an HR user who is also an insured employee) is deferred (D-008).

## Open decisions
- [x] Can one HR user span multiple corporate clients? → Yes (D-009). Several HR users per client assumed allowed too — flag if wrong.
- [x] Does a corporate client have exactly one agent, or can several agents share a client? → Many-to-many, no restriction (D-010)
- [x] Does anyone from the insurer ever log in, or is the insurer purely external to the app? → Purely external; catalog entry only (D-011)
- [x] How many distinct personas are there? → 8 (7 user personas + dependent as non-user), see D-001, D-002
- [x] What roles does the system need? Do personas map 1:1 to roles? → 7 roles, 1:1
- [x] Can one user hold multiple roles? → No, one role per user in v1 (D-008)
- [ ] Are there external users (outside the owning organization) with access? → Yes: `hr`, `agent`, `employee`; scoping rules to be locked in the permissions matrix
