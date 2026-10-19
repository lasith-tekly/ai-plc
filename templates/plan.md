---
profile: ai-plc-v1.0
run_mode: <ideation | planning | outcomes | full>
adapter: <none | scrum | ai-dlc | plain-markdown>   # only for full
idea: <the PM's idea in one line>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# Plan

Written by the orchestrator at the start of a run. The PM may edit it before work starts.

## Scope
- Run mode: <mode>, covering phases <list>.
- It stops at: <gate 1 | gate 2 | outcome pack issued | user stories>.

## Connected sources
- <system, location and why, or "none">. Only these are read. Anything written out needs a PM-approved dry run.

## Stops
- Review of each deliverable, as it is drafted.
- Product checkpoint after phase 1 (and after phase 3 if in scope).
- Gate 1 after phase 2 (and Gate 2 after phase 4 if in scope).

## Deliverables

| Order | ID | Deliverable | Mode | Agent | Needs first | Runs in parallel with | Ready now |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.1 | Problem and opportunity statement | auto | discovery | nothing | 1.4 | yes |
| 1 | 1.4 | Existing research summary | assist | discovery | nothing | 1.1 | yes |
| 2 | 1.2 | Market definition | auto | discovery | 1.1 | 1.3 | no |
| 2 | 1.3 | Customer definition | auto | discovery | 1.1 | 1.2 | no |

The table is the whole route for this mode. Only the rows marked "Ready now" start after the PM says go; the rest wait for their dependencies to be approved.

## Already approved (not redone)
- <none yet>

## Notes for the PM
- <anything the PM should supply, such as research documents or access to a tool>
