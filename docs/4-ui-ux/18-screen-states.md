---
status: skeleton
---

# Screen States

> **Owns:** What every screen shows when things aren't the happy path: empty, loading, error, and permission-denied states.

## Global patterns
_(empty — the default look for loading, empty, error, and no-permission, so screens only document deviations)_

## Per-screen states
_(empty — one row per screen from 16-screens-and-navigation.md)_

| Screen | Empty state | Loading | Error | No permission |
|--------|-------------|---------|-------|---------------|
| _(empty)_ | | | | |

## Open decisions
- [ ] Skeleton loaders, spinners, or something else for loading?
- [ ] Do empty states include a call to action?
- [ ] When a user lacks permission: hide the screen, or show it with an explanation?
