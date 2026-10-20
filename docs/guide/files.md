# 7. What gets written, and where

Everything is written inside a `/product` folder in your project. Nothing is written elsewhere.

| Path | What it holds |
| --- | --- |
| `plan.md` | The route for this run: deliverables in order, the agent for each, connected sources, what is ready now. You can edit it |
| `status.md` | Generated from each deliverable's frontmatter. Do not edit by hand |
| `memory.md` | Decisions, constraints, assumptions, terms and rejected options. Read at the start of every session |
| `phase-1/` to `phase-4/` | Phase deliverables |
| `outcomes/` | The Outcome Pack: one file per outcome plus an index |
| `delivery/` | Output of the chosen adapter |
| `reviews/` | Reviewer reports |
| `gates/` | Records of the decisions you reported |
| `inputs/` | Snapshots of connected sources (unreviewed, accepted or discarded) |
| `exports/` | Dry runs and `log.md` for anything sent to a connected tool |

## Deliverable frontmatter

Each deliverable file starts with frontmatter: `id`, `profile`, `status` (draft, reviewed, approved or stale), `version`, `updated`, `mode`, `depends_on` and `sources`. Status lives there and nowhere else. Open `templates/` in the source for exact shapes. See [Templates](../reference/templates.md).

See a real `plan.md` and `status.md` in the [Worked example](worked-example.md).

## Resuming

Run the command again. The orchestrator reads `plan.md`, `status.md` and `memory.md` and resumes. It never redoes an approved deliverable.
