# Agents (generated)

!!! note
    This page is generated from `agents/*.md` in the source. Do not edit it by hand.

| Agent | What it does |
| --- | --- |
| `ai-plc-orchestrator` | Entry point for AI-PLC. Reads the run mode, plans the run, assigns work to the specialist agents, tracks status and manages every review stop, checkpoint and gate. Use when the PM runs /ai-plc. |
| `ai-plc-discovery` | Phase 1 agent for AI-PLC. Drafts the problem and opportunity statement, market definition, customer definition and existing research summary. Used by the orchestrator. |
| `ai-plc-strategy` | Phase 2 agent for AI-PLC. Drafts use cases, outcome-oriented scope, strategy considerations, pricing check, business model canvas, vision statement and the initial business case. Used by the orchestrator. |
| `ai-plc-solution` | Phase 3 agent for AI-PLC. Drafts prioritised capabilities, solution research and design, usability test plan, positioning and messaging, pilot plan and MVP scope. Used by the orchestrator. |
| `ai-plc-viability` | Phase 4 agent for AI-PLC. Drafts the legal and security assessment template, risk assessment, implementability, product and market viability, measurement plan, value assessment, pricing strategy, services review and final business case. Used by the orchestrator. |
| `ai-plc-reviewer` | Independent review agent for AI-PLC. Checks approved deliverables before a checkpoint or gate for unsupported claims, broken sources, inconsistencies and scope breaches. Reports findings only. Used by the orchestrator. |
| `ai-plc-outcome` | Outcome Definition agent for AI-PLC. After Gate 2 is approved, turns the approved evidence into an Outcome Pack: one file per outcome plus an index. Used by the orchestrator. |
| `ai-plc-delivery` | Delivery agent for AI-PLC --full runs. After the Outcome Pack is issued, produces requirements, epics, user stories and their dependency maps (Scrum), AI-DLC handoff briefs, or a plain outcome list. Used by the orchestrator. |
