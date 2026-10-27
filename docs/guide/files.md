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

## The three working files

- **`plan.md`** is written at the start of a run, and you can edit it before anything starts. It lists the run mode, where the run stops, the connected sources and targets you named, and every deliverable in order, with its agent, what it needs first, what can run in parallel and whether it is ready now. Only the rows marked ready start after you say go. If you want to send results to Confluence, Jira, Notion or Miro later, the target has to be named here.
- **`status.md`** is the dashboard. It shows where you are, who the run is waiting on, each deliverable's status and version, and the outcome of each checkpoint and gate as you reported it. It is regenerated after every change, so do not edit it.
- **`memory.md`** is the run's memory: decisions you made, constraints, assumptions, terms and rejected options, each with a date and source. The agents read it at the start of every session and do not ask you again what is recorded. You can read and correct any entry.

The other folders: `reviews/` holds the reviewer's report before each checkpoint and gate, `gates/` holds what you reported at each stop, `inputs/` holds snapshots of sources you named, and `exports/` holds the dry runs and the log of anything sent to a connected tool. For what each deliverable is for, see [Deliverables](../reference/deliverables.md).

## Deliverable frontmatter

Each deliverable file starts with frontmatter: `id`, `profile`, `status` (draft, reviewed, approved or stale), `version`, `updated`, `mode`, `depends_on` and `sources`. Status lives there and nowhere else. Open `templates/` in the source for exact shapes. See [Templates](../reference/templates.md).

See a real `plan.md` and `status.md` in the [Worked example](worked-example.md).

## Resuming

Run the command again. The orchestrator reads `plan.md`, `status.md` and `memory.md` and resumes. It never redoes an approved deliverable.
