# Decision points: checkpoints and gates

AI-PLC stops four times and waits for a person to decide. Two are **checkpoints** and two are **gates**.

## Checkpoint or gate?

| | Checkpoint | Gate |
| --- | --- | --- |
| Kind of decision | Product decision | Investment decision |
| The question | "Are we on the right track?" | "Is this worth more money and people?" |
| Usually decided by | You and your product team | The people who fund and prioritise work in your organisation |
| Based on | The deliverables from the phase | A business case, in a short pack |

Who decides depends on your organisation. AI-PLC does not know your approval chain. It prepares the material and records what you report.

## The four stops

| Stop | Comes after | What you are deciding |
| --- | --- | --- |
| Checkpoint 1 | Phase 1: assess market and customers (inside Ideation) | Do we understand the problem, the market and the customers well enough to go on? |
| Gate 1 | Phase 2: define vision and strategy (closes **Ideation**) | Is the **initial business case** strong enough to keep investing? |
| Checkpoint 2 | Phase 3: converge on solution (inside Planning) | Is this the right first solution and MVP scope? |
| Gate 2 | Phase 4: evaluate viability (closes **Planning**) | Is the **final business case** strong enough to commit to building? |

## What happens at each stop

1. A new, separate review agent checks the approved deliverables for unsupported claims, broken sources, inconsistencies and scope problems. It reports findings only.
2. For each medium or high finding you revise the file (a new version) or accept the finding. Accepted findings go into the pack under "Known issues in approved files".
3. A short pack is assembled for you to take to the decision.
4. You report the decision in chat: who decided, the outcome and any feedback.

## The four outcomes of a decision

| Decision | What it means | What AI-PLC does |
| --- | --- | --- |
| Approve | Go ahead | Moves on to the next phase or step |
| Rework | The work needs fixing | Proposes the earliest affected deliverable. You confirm the restart point. That file and everything that depends on it are marked stale and redone |
| Pivot | Change direction | Same as rework, from the point where the direction changes. The pivot is recorded in `memory.md` |
| Stop | Do not continue | Ends the run. Everything so far stays in `/product` |

The decision is saved to `/product/gates/<name>.md` as a record of what you reported. The AI never approves a checkpoint or a gate.
