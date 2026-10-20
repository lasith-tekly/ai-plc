# The product lifecycle

AI-PLC follows the life of a product in four stages. Most teams already work this way, whatever they call the stages.

| Stage | The question | Where AI-PLC v1.0 stands |
| --- | --- | --- |
| 1. Product Ideation | Is there something worth pursuing? | **Automated.** Phases 1 and 2, ending at Gate 1 |
| 2. Product Planning | What exactly will we build first, and can it work? | **Automated.** Phases 3 and 4, ending at Gate 2 |
| 3. Product Development | Build it | **Handed over.** AI-PLC produces outcomes and delivery material. Your team builds, for example with AI-DLC or Scrum |
| 4. Product Launching and Sunsetting | Release it, run it, and retire it when its time comes | **Not built yet.** On the [roadmap](../roadmap.md) |

Between Planning and Development sits one more step: **Outcome Definition**. It turns the approved business case into **outcomes**: measurable results the product must achieve. Outcomes are the single handover. Whatever method your team builds with, it starts from them.

## Inside Ideation and Planning: four phases

Each of the first two stages has two phases. Each phase ends with a stop where a person decides.

| Stage | Phase | The question it answers | Ends with |
| --- | --- | --- | --- |
| Ideation | 1. Assess market and customers | Is there a real problem, for real people, in a market worth entering? | Checkpoint 1 |
| Ideation | 2. Define vision and strategy | What would we offer, and does the business case make sense? | Gate 1 |
| Planning | 3. Converge on solution | What exactly will we build first? | Checkpoint 2 |
| Planning | 4. Evaluate viability | Can it work: legally, financially, practically? | Gate 2 |

A **checkpoint** is a product decision. A **gate** is an investment decision, taken on a business case. Each gate closes a stage. See [Decision points](gates.md).

## After Planning

- **Outcome Pack.** After Gate 2 is approved, one file per outcome, with a dependency map and a roadmap.
- **Delivery material (`--full`).** Requirements and user stories (Scrum), handoff briefs (AI-DLC), or a plain outcome list. Running the build itself is your team's job, outside AI-PLC.

## Every deliverable follows the same loop

The tool drafts it, you review it, and its status moves `draft`, `reviewed`, `approved`. Nothing downstream uses a deliverable until you approve it. If an approved file is revised or sent back, files that depend on it become `stale` and are redone.

## Auto, assist, human

- **auto**: drafted from the conversation and sourced research.
- **assist**: drafted, but you must supply inputs or evidence.
- **human**: people outside the tool are needed (for example usability tests and the legal assessment). The tool gives a template and tracks status. It never marks these done.

The full list with dependencies is in [Deliverables](../reference/deliverables.md).
