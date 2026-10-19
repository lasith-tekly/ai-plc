---
name: gate-pack
description: "Assembles the short pack the PM takes to an AI-PLC product checkpoint or portfolio gate, and writes the record of the PM-reported decision. Use at checkpoint 1, Gate 1, checkpoint 2 and Gate 2."
---

# Gate pack

## Goal

Give the people who decide a short, honest pack and keep a record of what they decided. The pack informs a human decision. Nothing here approves anything.

## Steps

1. Confirm every deliverable the stop depends on is `approved`. If not, say which are missing and stop.
2. Build the pack from approved deliverables only:
   - Product checkpoint (after phase 1 or 3): one-paragraph summary per deliverable, open risks, open questions carried forward.
   - Portfolio gate (Gate 1 after phase 2, Gate 2 after phase 4): the business case deliverable (`2.10` for Gate 1, the final business case for Gate 2), the key evidence behind it, the biggest risks and what would change the decision.
3. Add "Known issues in approved files": every finding the PM accepted instead of revising, and every unrevised finding on an approved file, with file and line. Write "none" if there are none.
   Keep source tags on every claim. Separate evidence from assumptions. Where a source was single-sourced, sponsored or not confirmed, say so in the pack.
4. Show the pack to the PM. Ask them to report: who decided, the outcome (approve, rework, pivot or stop), and any feedback or conditions.
   If the PM's outcome differs from the pack's recommendation (for example the pack recommends rework and the PM reports approve), ask one line to confirm that is intended and ask for the reason, then record both the recommendation and the decision.
   If the pack's recommendation names conditions (for example "build only once X, Y and Z are in place"), ask the PM in one line whether those conditions apply, are changed, or are waived, and record the answer. A bare "approved" does not settle them. Do not assume either way.
5. Write `/product/gates/<stop>.md`:

```markdown
---
stop: <checkpoint_1 | gate_1 | checkpoint_2 | gate_2>
kind: <product_checkpoint | portfolio_gate>
after_phase: <n>
profile: ai-plc-v1.0
decision: <approve | rework | pivot | stop>   # as reported by the PM in chat
decided_by: "<who, as reported by the PM>"
decided_on: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# <Stop name>

This file records what the PM reported in chat. It is a record, not proof. The orchestrator does not make this decision.

## Pack
## Open risks
## Known issues in approved files
## Open questions carried forward
## Decision (as reported by the PM)
- Decided by:
- Outcome:
- Feedback and conditions:
- Reported in chat by the PM on:
```

6. Add the decision and any conditions to `memory.md`.
7. If the outcome is rework or pivot, tell the orchestrator so it can propose the earliest affected deliverable. Do not decide the restart point.

## Rules

- Never fill the decision on the PM's behalf.
- Never claim the decision was verified. It is what the PM reported.
- Do not add new evidence in the pack. Everything comes from approved deliverables.
