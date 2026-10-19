---
name: delivery-ai-dlc
description: "Prepares an issued AI-PLC Outcome Pack for AI-DLC: one handoff brief per outcome, in dependency order, plus run notes. AI-DLC writes its own requirements and stories. Use for --full runs with the ai-dlc adapter."
---

# Delivery: AI-DLC adapter

## Goal

Hand outcomes to AI-DLC one at a time, with the context it needs, so it produces its own requirements, design and stories. AI-PLC does not write requirements or stories for this adapter, and does not run AI-DLC. The PM does.

## Steps

1. **Check the gate** (index `issued`). Read the index, the outcomes, the pack's dependency map and roadmap (separate files or index sections) and `memory.md`.
2. **H.1 Handoff briefs.** One brief per outcome at `/product/delivery/ai-dlc/<outcome-id>-brief.md`:
   - the outcome statement, metric, target (labelled if SYNTHETIC) and horizon;
   - evidence, constraints, non-goals, risks and open questions from the outcome file;
   - dependencies (outcomes that must be done first, hard and soft);
   - Gate 2 conditions that apply;
   - a suggested scope note for AI-DLC: what to include, what to bypass, and what the first result should be (the PM can adjust);
   - a ready-to-paste prompt for the PM to give AI-DLC.
3. **H.2 Handoff roadmap, order and run notes** at `/product/delivery/ai-dlc/handoff-order.md`: a roadmap of when each outcome is handed over (using the timeframes in the outcome roadmap, never inventing dates), the order to hand outcomes over (by drop and dependency), what can run in parallel, how to run AI-DLC for each (`aidlc` command, harness and scope mode as the PM's installed version supports), and what to bring back to AI-PLC (for example completed outcomes, so status and the dependency map stay current).
4. Show each deliverable to the PM for review. Approve, or what to change?

## Notes

- Record the AI-DLC version the PM uses in the run notes. If it is unknown, write "version to be confirmed" and do not assert version-specific commands.
- Keep each brief self-contained: AI-DLC should not need to read the rest of `/product`.
- Do not paraphrase risks or conditions away.
- "Decisions already made" in a brief come only from PM decisions recorded in `memory.md`. Wording that appears only in an outcome file is not a decision. If it conflicts with a Gate 2 condition, list it as an open item and quote both.
- Put each Gate 2 condition in every brief that builds what the condition governs, quoted in full, with its source question explained in a few words.
- A hold that covers a whole drop or outcome set (for example "waits for the assistance route") is taken from the index. Show it in H.2 for every outcome it covers, in the diagram, the order table and the roadmap.
- Hand-over holds are written in H.2 only, not in the briefs, so a brief stays an outcome description.
- Open the file with a short Summary for the PM (about 100 words). A brief's body may be about 2,500 words because it must stand alone. Put long tables under an Appendix.

## Quality checks

- One brief per outcome; the roadmap matches `roadmap.md`; order respects hard dependencies and drops.
- Every brief carries constraints, non-goals, risks, conditions and SYNTHETIC labels.
- No requirements or stories written by AI-PLC.
- Decisions already made trace to `memory.md`. Whole-drop holds show for every outcome they cover.
- The run notes state the AI-DLC version or "to be confirmed".
