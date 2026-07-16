---
status: skeleton
---

# Errors & Edge Cases

> **Owns:** The catalog of things that go wrong outside normal validation: concurrency, stale data, expired sessions, deleted references. Each case gets an `ERR-` ID, referenced from journeys and acceptance criteria.

## Concurrency
_(empty — two users editing the same record, acting on a record whose state just changed)_

## Stale & deleted references
_(empty — acting on something that was deleted/archived by someone else)_

## Session & auth edge cases
_(empty — session expires mid-action, permissions revoked while logged in)_

## Data edge cases
_(empty — very long values, zero items, huge lists, unusual characters)_

## Open decisions
- [ ] Concurrent edits: last-write-wins, optimistic locking, or explicit locking?
- [ ] What should a user see when their session expires mid-form?
- [ ] What happens to in-progress work when a referenced record is archived?
