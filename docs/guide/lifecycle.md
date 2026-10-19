# Lifecycle

AI-PLC v1.0 has four phases, two checkpoints and two gates, then an Outcome Pack and optional delivery.

| Phase | Name | Ends with |
| --- | --- | --- |
| 1 | Assess market and customers | Checkpoint 1 |
| 2 | Define vision and strategy | Gate 1 (initial business case) |
| 3 | Converge on solution | Checkpoint 2 |
| 4 | Evaluate viability | Gate 2 (final business case) |
| After Gate 2 | Outcome Definition | Outcome Pack issued |
| `--full` only | Delivery adapter | Requirements, briefs or outcome list |

A **checkpoint** is a product decision. A **gate** is a portfolio decision, taken on a business case. See [Checkpoints and gates](gates.md).

## Every deliverable follows the same loop

The tool drafts it, you review it, and its status moves `draft`, `reviewed`, `approved`. Nothing downstream uses a deliverable until you approve it. If an approved file is revised or sent back, files that depend on it become `stale` and are redone.

## Auto, assist, human

- **auto**: drafted from the conversation and sourced research.
- **assist**: drafted, but you must supply inputs or evidence.
- **human**: people outside the tool are needed (for example usability tests and the legal assessment). The tool gives a template and tracks status. It never marks these done.

The full list with dependencies is in [Deliverables](../reference/deliverables.md).
