---
id: outcome-pack
profile: ai-plc-v1.0
status: draft          # draft | issued | stale
version: 1.0
updated: <YYYY-MM-DD>
product: <product or idea name>
gate_1: <approved on date, decided by name>
gate_2: <approved on date, decided by name>   # the pack is issued only after this
---

# Outcome Pack: <product name>

## Summary
Two or three sentences: the problem, who has it, and what success looks like.

## Outcomes

| ID | Outcome | Metric | Baseline | Target | Horizon | Priority | MVP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| O1 | <title> | <metric> | <value> | <value> | <when> | 1 | yes |
| O2 | <title> | <metric> | <value> | <value> | <when> | 2 | yes |

Each outcome has its own file in this folder: `O1-<slug>.md`, `O2-<slug>.md`, and so on.

## Dependency map
See `dependency-map.md`: hard and soft dependencies, what can start now, the critical path to the MVP and parallel groups.

## Roadmap
See `roadmap.md`: outcomes by drop and timeframe, what gates each step, and when each result can first be measured.

## Traceability

| Outcome | Capabilities (3.1) | Use cases (2.1) | Evidence |
| --- | --- | --- | --- |
| O1 | <ids> | <ids> | <deliverable ids or sources> |

## Carried items (Gate 2 conditions and unresolved review findings)

| Item | Source | Outcomes affected |
| --- | --- | --- |
| <condition or finding> | <gate-2 or review id> | O1, O3 |

## Assumptions
- <what the pack assumes to be true>

## Out of scope for the whole pack
- <what this pack does not cover>

## Source deliverables
- Problem and opportunity statement (1.1), market definition (1.2), customer definition (1.3)
- Use cases (2.1), vision statement (2.9), initial business case (2.10)
- Prioritised capabilities (3.1), MVP scope (3.6)
- Measurement plan (4.6), final business case (4.10)
- Risk assessment (4.2), implementability (4.3)
