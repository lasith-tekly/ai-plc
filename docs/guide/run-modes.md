# Run modes

Each mode includes the ones before it.

| Command | Runs | Stops at |
| --- | --- | --- |
| `/ai-plc --ideation "<idea>"` | Phases 1 and 2 | Gate 1 |
| `/ai-plc --planning "<idea>"` | Adds phases 3 and 4 | Gate 2 |
| `/ai-plc --outcomes "<idea>"` | Adds Outcome Definition | Outcome Pack issued |
| `/ai-plc --full "<idea>" --adapter scrum` | Adds a delivery adapter | Requirements and user stories, or the adapter's output |

`--adapter` only applies to `--full`. If you leave it out, the orchestrator asks.

## Adapters

| Adapter | Produces |
| --- | --- |
| `scrum` | Requirements, epics, user stories with acceptance criteria, dependency maps and traceability |
| `ai-dlc` | One handoff brief per outcome plus run notes. AI-DLC writes its own requirements and stories |
| `plain-markdown` | A readable outcome list with dependencies and a roadmap |

The Outcome Definition step refuses to run until Gate 2 is approved. Delivery refuses to run until the Outcome Pack index is issued.

## The AI-DLC adapter and versions

In testing, the AI-DLC run in Kiro reported version 2.5.67, while the AI-DLC project listed a newer stable release. The difference is unexplained. Treat the adapter as tested only with that Kiro build, and check the version stated in the run notes.
