---
name: delivery-scrum
description: "Turns an issued AI-PLC Outcome Pack into requirements, epics, user stories with acceptance criteria, and requirement and story dependency maps with end-to-end traceability. Use for --full runs with the scrum adapter."
---

# Delivery: Scrum adapter

## Goal

From each outcome, a set of requirements; from requirements, epics and user stories a team can pick up in order, with every item traceable up to its outcome and its dependencies visible.

## Steps

1. **Check the gate** (index `issued`). Read the index, every outcome, `dependency-map.md` and `memory.md`.
2. **Ask for team conventions** through the orchestrator: story format, definition of done, estimation scale (if any), non-functional standards. If none, use the defaults below and say so.
3. **D.1 Requirements.** For each outcome, list what the product must do or satisfy for that outcome to be met. Each requirement is testable. Types: functional, data, security and privacy, legal, accessibility, performance, operational. Carry the outcome's constraints as requirements.
4. **D.2 Requirements dependency map.** Hard and soft dependencies between requirements, same format as the outcome map. Start from the outcome dependencies, then add requirement-level ones from 3.1 and 4.3.
5. **D.3 Epics.** Group requirements into epics by customer value, not by team or layer. Give each epic its outcome(s) and drop.
6. **D.4 User stories.** For each requirement (or small group), write stories a team can finish in one sprint, with acceptance criteria. One file per epic.
7. **D.5 Story dependency map and order.** Dependencies between stories and a suggested order by drop. Show what can start now, parallel groups and the critical path.
8. **D.6 Delivery roadmap.** Order epics and stories over time, by drop and dependency. Use the drops and timeframes from the outcome roadmap. Assign stories to sprints only if the PM supplies sprint length and team capacity; otherwise order by drop and dependency and say "sprints to be set by the PM". Show what gates each drop.
9. **D.7 Delivery index.** Traceability table outcome to requirement to epic to story, counts, carried items, and what is still unknown.
10. Show each deliverable to the PM for review. Approve, or what to change? Approvals follow the standard loop.

## Formats

**Requirements** (`/product/delivery/requirements.md`)
```markdown
| ID | Outcome | Requirement (testable) | Type | Source | Priority | Drop | Notes |
```
IDs: `R-<outcome>-<n>` (for example R-O1-3).

**Requirements dependency map** (`/product/delivery/requirements-dependency-map.md`): a table (Requirement, Depends on, hard/soft, why, source, confirmed by PM), a Mermaid diagram (solid hard, dotted soft), what can start now, critical path, parallel groups, and checks (no loops; drop order respected).

**Epics** (`/product/delivery/epics.md`)
```markdown
| Epic | Title | Outcomes | Requirements | Drop | Depends on |
```

**Stories** (`/product/delivery/stories/E<n>-<slug>.md`, one file per epic)
```markdown
### S-E1-1: <short title>
As a <who>, I want <what>, so that <the outcome result>.
- Outcome: O1 | Requirement: R-O1-2 | Epic: E1 | Drop: 1 | Type: feature
- Depends on: <story ids or none>  (proposed / confirmed)
- Go-live: <the switch-on story this story must wait for, or "none">
- Acceptance criteria:
  - Given <context>, when <action>, then <result>.
- Constraints and risks carried: <ids>
- Estimate: <from the PM's scale, or "not estimated">
- Open questions:
```
Story types: `feature` (family-facing behaviour), `gate` (a legal, commercial or accounting condition; the product part is recording it and holding the switch-on until it is met; the outside work is not sized in sprints) and `enabler` (technical or operational work other stories need).

Defaults if the PM gives no conventions: "As a / I want / so that" format, Given-When-Then criteria, no estimates, definition of done "accepted by the PM against the criteria".

**Story dependency map and order** (`/product/delivery/story-dependency-map.md`): table, Mermaid diagram (by epic if large), suggested order by drop, what can start now, parallel groups, critical path, checks.

**Delivery roadmap** (`/product/delivery/roadmap.md`)
```markdown
## Roadmap by drop
| Drop | Timeframe (from the PM) | Epics | Stories (ids) | Sprints (only if the PM gave capacity) | Needs first |
## Diagram (Mermaid)
## Milestones and gates
## Risks to the roadmap
## What is not scheduled
```
No dates or durations the PM did not set. Must match the story dependency map and the outcome roadmap.

**Delivery index** (`/product/delivery/index.md`): counts, the traceability table, carried items (Gate 2 conditions, unresolved findings, SYNTHETIC labels), assumptions and open questions.

## Quality checks

- Every outcome has at least one requirement; every requirement has a story or a reason it does not; every story traces up to a requirement and outcome.
- No requirement or story without an outcome.
- Acceptance criteria are testable, with no technology or screen detail unless a constraint requires it.
- Stories are small enough for one sprint; if not, split them or flag them.
- Go-live: if the outcome has a switch-on or go-live gate story, every story that only works once it is live names that story in `Go-live`, not only in the build dependency. Build and go-live are separate edges.
- Trigger coverage: for every "Given / when" trigger in a criterion (for example "the whole booking is cancelled"), a story or requirement produces that event. If none does, add it, or write an open question for the PM.
- Testable wording: do not use "plain words", "clear" or "fair" as a pass test. Name the approved wording item it depends on, or state a test (for example a reading-level check), or write an open question.
- One owner per behaviour: when several stories need the same behaviour (for example "no new booking while paused"), one story owns and tests it and the others only trigger it.
- `gate` stories are written in the voice of the person who needs the condition (a family or the PM) but their criteria say what is recorded and what is held; do not present outside work as build work.
- The delivery roadmap respects the story dependencies and the outcome roadmap, and has no invented dates.
- Dependency maps match the `Depends on` fields, have no loops, and respect the drops.
- Constraints, non-goals, risks and SYNTHETIC labels are carried.
- No invented estimates or dependencies.
