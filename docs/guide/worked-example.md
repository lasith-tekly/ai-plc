# Worked example

This is a real run, shown in short. It was a **dummy run**: the idea was chosen to test AI-PLC, and from phase 3 onwards the inputs are placeholders labelled SYNTHETIC. Nothing here is advice about the product itself. It shows what the files look like and how a run is recorded.

**The idea:** an AI-assisted leisure travel booking platform that plans the whole journey (destination, flights, hotels, car hire and more) from planning through travel to post-trip. First customers: UK families.

**The run:** `--full` with the `ai-dlc` adapter. Phases 1 to 4, all four decision points and the Outcome Pack were done in earlier sessions. This session ran the AI-DLC delivery step.

## plan.md (excerpt)

The orchestrator writes `plan.md` at the start and you may edit it before work starts.

```markdown
---
profile: ai-plc-v1.0
run_mode: full
adapter: ai-dlc
idea: AI-assisted leisure travel booking platform ... First customers: UK families.
created: 2026-10-18
---

# Plan

## Scope
- Run mode: full, with the AI-DLC delivery adapter.
- It stops at: AI-DLC handoff (H.1 and H.2 approved, after a reviewer check).
- Resumed session: phases 1 to 4, all four stops and the Outcome Pack are done.
- Gate check: outcomes/index.md status is `issued`, so delivery may run.
- Dummy run: inputs are SYNTHETIC from phase 3 on. Briefs built on them carry the label.

## Stops
- Review of each delivery deliverable: approve, or what to change.
- Reviewer check of the AI-DLC delivery before the run ends.

## Deliverables

| Order | ID | Deliverable | Mode | Agent | Needs first | Ready now |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | H.1 | AI-DLC handoff briefs (one per outcome) | auto | delivery | Outcome Pack issued | yes |
| 2 | H.2 | Handoff roadmap, order and run notes | auto | delivery | H.1, outcome roadmap | no |
```

Things to notice:

- **Resuming.** The plan starts from what is already approved. Approved work is never redone.
- **The gate check.** Delivery only runs because the Outcome Pack is `issued`.
- **"Ready now".** Only H.1 starts. H.2 waits for H.1.

At the end of the session the orchestrator added a short record of the outcome:

```markdown
## Run outcome
- H.1 approved: nine stand-alone AI-DLC handoff briefs, one per outcome.
- H.2 approved: six hand-over steps, AI-DLC 2.5.67, six known issues carried.
- Reviewer check: checks a to e pass; three medium findings resolved by PM decision, five low findings fixed.
- The full run stopped at the AI-DLC handoff as planned.
```

## status.md (excerpt)

`status.md` is generated from each deliverable's frontmatter. You never edit it.

```markdown
## Where we are
- Run mode: full (adapter: ai-dlc)
- Current stop: full run complete; H.1 and H.2 approved
- Note: this is a dummy run; synthetic data is labelled in each file
- Waiting on the PM: nothing (next step is outside AI-PLC: hand O1 to AI-DLC)

## Deliverables (a few of 41 rows)

| ID | Deliverable | Status | Version | Updated |
| --- | --- | --- | --- | --- |
| 1.1 | Problem and opportunity statement | approved | 1 | 2026-10-15 |
| 2.10 | Initial business case | approved | 1 | 2026-10-15 |
| 3.6 | MVP scope | approved for dummy run (SYNTHETIC inputs) | 1 | 2026-10-15 |
| 4.10 | Final business case | approved for dummy run (SYNTHETIC inputs) | 1 | 2026-10-16 |
| outcome_pack | Outcome Pack: O1 to O9 approved; index issued | issued | 3.0 | 2026-10-16 |
| H.1 | AI-DLC handoff briefs (O1 to O9) | approved | 2-3 | 2026-10-18 |
| H.2 | Handoff roadmap, order and run notes | approved | 2 | 2026-10-18 |

## Checkpoints and gates

| Stop | Decision | Decided by | Date | Feedback |
| --- | --- | --- | --- | --- |
| Checkpoint 1 | approve | PM and senior management | 2026-10-15 | Only leisure travel |
| Gate 1 | approve | Senior management | 2026-10-15 | None reported |
| Checkpoint 2 | approve | Senior management | 2026-10-16 | None (dummy run) |
| Gate 2 | approve | Senior management | 2026-10-16 | None (dummy run) |
```

Things to notice:

- **Who decided.** The four decisions were reported by the PM in chat. The record says who decided, so a gate decided by senior management shows that.
- **Notes on the status.** The status values are draft, reviewed, approved and stale. In this run the status column also carries short notes in brackets, such as "approved for dummy run (SYNTHETIC inputs)", so the SYNTHETIC label travels with the file.
- **Nothing is waiting.** "Waiting on the PM" tells you at a glance whether the next move is yours.

## What a connected source looked like

In the same project the PM also connected a Confluence space and a Jira project on a personal test site. Reading was recorded as a snapshot that stays `unreviewed` until the PM decides. Writing went through a dry run that the PM approved first. See [Connectors](../MCP-SETUP.md).

## Where to look next

- [What gets written](files.md): every file and folder.
- [Decision points](gates.md): what approve, rework, pivot and stop do.
