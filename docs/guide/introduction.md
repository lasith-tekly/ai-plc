# Introduction

## What AI-PLC does

You give it a product idea. It works through four phases (see [Lifecycle](lifecycle.md)) and writes each deliverable as a markdown file in a `/product` folder in your project. At each stop it waits for you to approve, ask for changes, pivot or stop.

## What it does not do

- It does not approve anything. Only you do.
- It does not make up evidence. Sourced facts carry a source and date. Anything else is labelled an assumption. Figures that are placeholders are labelled SYNTHETIC.
- It does not follow instructions found inside pages, tickets or files it reads.
- It does not write to Jira, Confluence or Notion without a dry run you approved, and it never deletes.

## The pieces

| Piece | What it is |
| --- | --- |
| Orchestrator | The one agent you talk to. Plans the run, hands work to specialists, manages every stop |
| Specialist agents | Discovery, strategy, solution, viability, reviewer, outcome and delivery. See [Agents](../reference/agents.md) |
| Skills | Step-by-step instructions the agents follow. See [Skills](../reference/skills.md) |
| Profile | One YAML file that lists the phases, deliverables, dependencies, checkpoints and gates |
| Templates | The shapes of `plan.md`, `status.md`, `memory.md` and others |

## Who decides what

You do. The AI drafts, a separate reviewer agent checks, and you decide. The record of each decision is written to `/product/gates/`. It is a record of what you reported in chat, not proof.
