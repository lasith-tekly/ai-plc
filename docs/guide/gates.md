# Checkpoints and gates

| Stop | After | Kind | You decide on |
| --- | --- | --- | --- |
| Checkpoint 1 | Phase 1 | Product checkpoint | Whether the problem, market and customers are understood |
| Gate 1 | Phase 2 | Portfolio gate | The initial business case |
| Checkpoint 2 | Phase 3 | Product checkpoint | The solution and MVP scope |
| Gate 2 | Phase 4 | Portfolio gate | The final business case |

## What happens at each stop

1. A new reviewer agent checks the approved deliverables for unsupported claims, broken sources, inconsistencies and scope breaches. It reports findings only.
2. For each medium or high finding you revise the file (a new version) or accept the finding. Accepted findings go into the pack under "Known issues in approved files".
3. A short pack is assembled for you to take to the decision.
4. You report the decision in chat: who decided, the outcome and any feedback.

## The four outcomes

| Decision | What happens |
| --- | --- |
| Approve | The run moves on to the next phase or step |
| Rework | The earliest affected deliverable is proposed. You confirm the restart point. That file and everything depending on it become `stale` and are redone |
| Pivot | Same as rework, from the point where the direction changes. The pivot is recorded in `memory.md` |
| Stop | The run ends. Everything so far stays in `/product` |

The decision is saved to `/product/gates/<name>.md` as a record of what you reported. The orchestrator never approves a checkpoint or a gate.
