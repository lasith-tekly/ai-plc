---
name: delivery-plain
description: "Produces a readable outcome list with dependencies and drops from an issued AI-PLC Outcome Pack. Use for --full runs with the plain-markdown adapter."
---

# Delivery: plain markdown adapter

## Goal

A single readable list of outcomes a team can work from without any other tooling.

## Steps

1. Check the gate (index `issued`). Read the index, the outcomes, and the pack's dependency map and roadmap (separate files, or sections of the index).
2. Write `/product/delivery/outcome-list.md` (P.1): for each outcome, in delivery order, the statement, metric and target (labelled if SYNTHETIC), drop, dependencies, constraints, risks and open questions, in short form (a few lines each). Add the dependency table and diagram from the map, what can start now and the critical path, and the roadmap from `/product/outcomes/roadmap.md` (drops, timeframes from the PM, what gates each step).
  Open with a Summary for the PM (about 150 words). Keep the body (before the Appendix) to about 2,000 words; put detail in an Appendix. If an outcome spans drops, list it once with its parts labelled by drop.
3. Show it to the PM. Approve, or what to change?

## Quality checks

- Order respects hard dependencies and drops.
- Targets are marked SYNTHETIC or "to be set" where they are.
- Nothing is added that is not in the pack.
- Conditions, guardrails and risks are written with a few words of meaning, not as bare ids (for example "G2: no charge above the confirmed total"). Put lookup tables in the Appendix.
- The critical path follows only declared dependencies. Do not place an outcome after others it does not depend on.
- Keep qualifiers such as "proposed", "to confirm", "accepted, not named" and "not legal advice".
- `updated` is today's date.
