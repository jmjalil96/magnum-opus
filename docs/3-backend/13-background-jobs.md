---
status: skeleton
---

# Background Jobs & Scheduled Tasks

> **Owns:** Every piece of work that runs without a user clicking something: scheduled tasks, queued jobs, retries. Each job gets a `JOB-` ID, referenced from transitions and integrations.

## Scheduled tasks
_(empty — one entry per task: schedule, what it does, what it touches)_

## Queued / event-driven jobs
_(empty — work triggered by events but executed asynchronously)_

## Failure handling
_(empty — retries, dead-letter behavior, who gets told when a job fails)_

## Open decisions
- [ ] Does anything need to run on a schedule?
- [ ] Which operations are too slow or unreliable to run inside a request and need a queue?
- [ ] What happens when a job fails repeatedly?
