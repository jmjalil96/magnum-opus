---
status: skeleton
---

# Audit & History

> **Owns:** What actions get recorded, what each record contains, and who can see the trail.

## What gets audited
_(empty — one `AUD-` entry per audited action/event, referenced from transitions and other docs)_

## Audit record shape
_(empty — what each entry stores: who, what, when, before/after values?)_

## Visibility
_(empty — who can view audit trails, and where in the UI they appear)_

## Retention
Retention policy for all data classes, audit records included, is owned by [21-security-and-privacy.md](21-security-and-privacy.md) — this doc only references it.

## Open decisions
- [ ] Audit everything, or only selected actions?
- [ ] Store before/after values or just "X changed Y"?
- [ ] Who can see the audit trail? Can it ever be deleted?
