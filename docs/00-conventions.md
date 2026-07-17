---
status: drafted
---

# Spec Conventions

> **Owns:** How this documentation system itself works: ID scheme, reference rules, status gates, and traceability. No app content lives here.

## ID scheme

Every specifiable artifact gets a stable ID. Zero-padded, three digits (`F-001`). IDs are **never renumbered and never reused** — if an artifact is dropped, its ID is retired.

| Prefix | Artifact | Defined in (owning doc) |
|--------|----------|------------------------|
| `F-`   | Feature | [Features & Journeys](1-product/04-features-and-journeys.md) |
| `J-`   | User journey | [Features & Journeys](1-product/04-features-and-journeys.md) |
| `T-`   | State transition | [State Machines & Transitions](2-domain/06-state-machines-and-transitions.md) |
| `BR-`  | Business rule | [Business Rules](2-domain/07-business-rules.md) |
| `PERM-`| Permission row | [Permissions Matrix](2-domain/08-permissions-matrix.md) |
| `API-` | Endpoint | [API Contract](3-backend/10-api-contract.md) |
| `JOB-` | Background job | [Background Jobs](3-backend/13-background-jobs.md) |
| `N-`   | Notification | [Notifications](3-backend/14-notifications.md) |
| `INT-` | Integration | [Integrations & Webhooks](3-backend/15-integrations-and-webhooks.md) |
| `SCR-` | Screen | [Screens & Navigation](4-ui-ux/16-screens-and-navigation.md) |
| `AUD-` | Audited event | [Audit & History](5-cross-cutting/20-audit-and-history.md) |
| `ERR-` | Edge case | [Errors & Edge Cases](5-cross-cutting/22-errors-and-edge-cases.md) |
| `AC-`  | Acceptance criterion | [Acceptance Criteria](6-build-and-operate/26-acceptance-criteria.md) |
| `D-`   | Decision | [Decision Log](decision-log.md) |

## Reference rule

**A fact is defined once, in its owning doc. Everywhere else it appears as an ID reference.**

- A transition row references `PERM-`, `BR-`, `N-`, `JOB-`, `AUD-` IDs; it never restates what those artifacts do.
- When writing an ID in prose (docs or discussion), attach its label for readability: `T-004 (state A → state B)`, `BR-002 (deadline rule)`. The label is a courtesy copy; the owning doc's definition wins.
- If you find the same fact spelled out in two places, that's a bug: pick the owner, replace the other with a reference.

## Status gates

Canonical status lives in each doc's YAML frontmatter (`status:`). The README index is a derived view and may lag.

| Status | Gate to reach it |
|--------|------------------|
| `skeleton` | Structure exists; content empty. |
| `drafted` | Every section has substantive content and no *same-doc* unknowns remain. Cells that reference another doc's IDs (`PERM-`, `N-`, …) may stay TBD while the owning doc hasn't minted them (D-027). |
| `reviewed` | All cross-doc ID references checked and resolving. |
| `final` | No unresolved blocking decisions; acceptance criteria linked where applicable. |

## Open decisions in docs

Each doc carries an "Open decisions" checklist. When a decision is resolved, it gets a `D-` entry in the [Decision Log](decision-log.md) recording context, options, and rationale; the checkbox is checked and annotated with the `D-` ID. Blocking decisions (those that gate `final`) are marked **[blocking]**.

## Traceability matrix

The feature-level traceability matrix (feature → journey → screens → rules/transitions → permissions → API → side effects → acceptance) is a **generated artifact**, extracted from IDs by a validator script (to be built after the first vertical slice). It is never hand-maintained — hand-kept matrices rot silently.
