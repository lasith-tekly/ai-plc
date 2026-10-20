# Your first run

Use a dummy idea first. A small, low-stakes one is fine.

## 1. Start

Open your tool in the project folder. In Kiro, switch to the `ai-plc-orchestrator` agent first. Then type the start command for your tool (see [Install](install.md)), for example:

```
/ai-plc --ideation "a short description of your idea"
```

## 2. Answer the questions

The orchestrator explains the mode and which stops you will meet. It asks up to four short questions at a time and says why. If you do not know an answer, say so. It is recorded as an open question.

It also asks which connected sources, if any, to read. Say "none" on your first run.

## 3. Review the plan

It writes `/product/plan.md` and waits. Edit the file if you want. Say go when ready.

## 4. Review every deliverable

Each draft appears under `/product/phase-1/` and so on, with its sources and assumptions. For each one you can approve it, ask for changes, or stop. Check key figures against their source links before approving.

## 5. Checkpoint 1

After phase 1 a new reviewer agent checks the approved files and reports findings. You choose to revise or accept each medium or high finding. A short pack is assembled. You report your decision in chat: **approve, rework, pivot or stop**.

## 6. Carry on

Phase 2 then ends at Gate 1, an investment decision on the initial business case. `--ideation` stops there. See [Choose a run mode](run-modes.md) for the longer ones.

You can close the session at any stop. Next time, run the command again and it resumes from `/product`.
