---
status: skeleton
---

# Integrations & Webhooks

> **Owns:** Every external system the app talks to, in both directions, and what happens when the other side fails. Each integration gets an `INT-` ID.

## Outbound integrations
_(empty — one section per external service: purpose, what data crosses, auth, failure behavior)_

## Inbound (webhooks the app exposes)
_(empty — endpoints external systems call, verification, idempotency)_

## Failure behavior
_(empty — timeouts, retries, what the user sees when an external service is down)_

## Open decisions
- [ ] Which external services does v1 depend on?
- [ ] For each: what happens when it's unavailable — block, queue, or degrade?
- [ ] Does anything external push data into the app?
