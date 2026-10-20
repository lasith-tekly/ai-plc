# 3. Choose a run mode

A run mode is how far you want AI-PLC to take your idea in one go. You choose it when you start. If you are not sure what the phases are, read [What is AI-PLC?](what-is-ai-plc.md) first.

You can always stop at a decision point and carry on later. You can also start small and run a bigger mode afterwards. Approved work is kept and never redone.

## How the modes relate to the lifecycle stages

| Mode | Covers |
| --- | --- |
| `--ideation` | Stage 1, Product Ideation |
| `--planning` | Stages 1 and 2: Ideation, then Planning |
| `--outcomes` | Stages 1 and 2, then the Outcome Pack for the Development stage |
| `--full` | All of the above, then requirements and user stories (or the adapter's output) to feed Development |

Stages 3 (running the build) and 4 (Launching and Sunsetting) are not run by AI-PLC. See [The product lifecycle](lifecycle.md).

## Which one do I need?

| I want to... | Use | You get | It stops when |
| --- | --- | --- | --- |
| Find out whether an idea is worth pursuing | `--ideation` | Problem, market, customers, use cases, vision, initial business case | The initial business case is ready for an investment decision (Gate 1) |
| Plan the solution and test whether it can work | `--planning` | Everything above, plus the solution, MVP scope, risks, pricing and a final business case | The final business case is ready for an investment decision (Gate 2) |
| Turn an approved plan into measurable results | `--outcomes` | Everything above, plus an Outcome Pack: each outcome with its measure, dependencies and a roadmap | The Outcome Pack is issued |
| Hand a delivery team something to build from | `--full` | Everything above, plus requirements and user stories (or the format your delivery method uses) | The delivery material is ready for review |

Each mode includes the ones before it. For example, `--planning` does what `--ideation` does and then continues.

## How to run each one

These use the `/ai-plc` form. In the Claude Code plugin it is `/ai-plc:ai-plc`, and in Codex it is `$ai-plc`. See [Install](install.md).

```
/ai-plc --ideation "<your idea>"
/ai-plc --planning "<your idea>"
/ai-plc --outcomes "<your idea>"
/ai-plc --full     "<your idea>" --adapter scrum
```

## What the stopping points mean

The "stops when" column refers to the four decision points: two checkpoints (product decisions) and two gates (investment decisions). Every mode also stops at the checkpoints it passes. See [Decision points](gates.md).

## Delivery formats for `--full`

`--adapter` only applies to `--full`. If you leave it out, AI-PLC asks. It chooses how the Outcome Pack is turned into something a team can build.

| Adapter | Choose it if | You get |
| --- | --- | --- |
| `scrum` | Your team works in sprints with backlogs | Requirements, epics, user stories with acceptance criteria, and how they depend on each other |
| `ai-dlc` | Your team builds with AI-DLC (an AI-driven development method) | One handoff brief per outcome. AI-DLC writes its own requirements and stories |
| `plain-markdown` | You just want a readable list | Outcomes in order, with dependencies and a roadmap |

## Order matters

The Outcome step will not run until the final business case (Gate 2) is approved. Delivery will not run until the Outcome Pack is issued. If you ask for a mode that needs something not yet approved, AI-PLC runs up to that point and stops.

## About the AI-DLC adapter and its version

The AI-DLC adapter was tested with the AI-DLC version that Kiro reported, **2.5.67**. The run notes state the version that was installed in your workspace when they were written. If you use a different AI-DLC version, check that the briefs still suit it.
