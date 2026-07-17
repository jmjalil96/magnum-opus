---
status: skeleton
---

# Domain Model

> **Owns:** The entities of the system, their relationships, and the lifecycle of each — stack-independent.

## Entities
_(empty — one subsection per entity: purpose, key attributes at concept level, who owns/creates it)_

## Relationships
_(empty — how entities relate: one-to-many, many-to-many, ownership, required vs optional)_

## Entity lifecycles
_(empty — for each entity: how it's created, changed, archived/deleted; entities with formal states point to 06-state-machines-and-transitions.md)_

## Open decisions
- [ ] What are the top-level entities?
- [ ] Is a corporate group/holding ("one program, several corporate clients", see D-009) a modeled entity, or is it represented only by the HR-user ↔ client links?
- [ ] Is the claim's insured *derived* from the linked enrollment (pick the enrollment → the insured follows, making BR-002 structurally unviolable), or stored independently and validated by BR-002 at T-001?
- [ ] Which entity is the "center of gravity" the rest hang off?
- [ ] Which entities have a formal state machine vs a simple active/archived flag?
- [ ] Can entities be deleted, or only archived?
