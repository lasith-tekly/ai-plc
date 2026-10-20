# Deliverables (generated)

!!! note
    Generated from `profiles/ai-plc-v1.0.profile.yaml`. Do not edit by hand.

Modes: **auto** the tool drafts from the conversation and research. **assist** the tool drafts but you supply inputs or evidence. **human** people outside the tool are needed; the tool gives a template and tracks status.

## Phase 1: Assess market and customers (Ideation stage)

| ID | Deliverable | Mode | Depends on |
| --- | --- | --- | --- |
| 1.1 | Problem and opportunity statement | auto | none |
| 1.2 | Market definition | auto | 1.1 |
| 1.3 | Customer definition | auto | 1.1 |
| 1.4 | Existing research summary | assist | none |

## Phase 2: Define vision and strategy (Ideation stage)

| ID | Deliverable | Mode | Depends on |
| --- | --- | --- | --- |
| 2.1 | Use cases | auto | 1.1, 1.3 |
| 2.2 | Outcome-oriented scope | auto | 1.1, 2.1 |
| 2.3 | Experience strategy fit | assist | 2.1 |
| 2.4 | Partnership consideration | assist | 1.2, 2.1 |
| 2.5 | Services consideration | assist | 2.1 |
| 2.6 | Team skills gaps | assist | 2.2 |
| 2.7 | Pricing and billing model check | assist | 1.2, 1.3 |
| 2.8 | Business model canvas | auto | 1.1, 1.2, 1.3, 2.1 |
| 2.9 | Vision statement | auto | 1.1, 2.1 |
| 2.10 | Initial business case (feeds gate 1) | assist | 1.2, 2.2, 2.7, 2.8, 2.9 |

## Phase 3: Converge on solution (Planning stage)

| ID | Deliverable | Mode | Depends on |
| --- | --- | --- | --- |
| 3.1 | Prioritised capabilities | auto | 2.1, 2.2 |
| 3.2 | Solution research | assist | 3.1 |
| 3.3 | Usability tests | human | 3.2 |
| 3.4 | Early positioning and messaging | auto | 1.2, 2.9 |
| 3.5 | Pilot plan | assist | 3.2, 3.3 |
| 3.6 | MVP scope | auto | 3.1, 3.3 |

## Phase 4: Evaluate viability (Planning stage)

| ID | Deliverable | Mode | Depends on |
| --- | --- | --- | --- |
| 4.1 | Legal | human | 3.6 |
| 4.2 | Risk assessment | assist | 3.6 |
| 4.3 | Implementability | assist | 3.2, 3.6 |
| 4.4 | Product viability | assist | 2.10, 3.6 |
| 4.5 | Market viability | auto | 1.2 |
| 4.6 | Measurement plan | assist | 2.2, 3.6 |
| 4.7 | Value assessment | assist | 4.4, 4.5 |
| 4.8 | Pricing strategy | assist | 2.7, 4.4 |
| 4.9 | Services review | assist | 2.5, 3.6 |
| 4.10 | Final business case (feeds gate 2) | assist | 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9 |

## Outcome Definition (after Gate 2)

| ID | Deliverable | Mode | Depends on |
| --- | --- | --- | --- |
| O.n | Outcomes (one file each) | assist | 3.1, 3.6, 4.2, 4.6, 4.10 |
| O.M | Outcome dependency map | auto | O.n |
| O.R | Outcome roadmap | auto | O.n, O.M |
| O.I | Outcome Pack index | auto | O.n, O.M, O.R |

## Delivery, `scrum` adapter (`--full` only)

| ID | Deliverable | Mode | Depends on |
| --- | --- | --- | --- |
| D.1 | Requirements | assist | outcome-pack |
| D.2 | Requirements dependency map | auto | D.1 |
| D.3 | Epics | auto | D.1, D.2 |
| D.4 | User stories | assist | D.1, D.3 |
| D.5 | Story dependency map and order | auto | D.4 |
| D.6 | Delivery roadmap | auto | D.5, O.R |
| D.7 | Delivery index and traceability | auto | D.6 |

## Delivery, `ai-dlc` adapter (`--full` only)

| ID | Deliverable | Mode | Depends on |
| --- | --- | --- | --- |
| H.1 | AI-DLC handoff briefs (one per outcome) | auto | outcome-pack |
| H.2 | Handoff roadmap | auto | H.1, O.R |

## Delivery, `plain-markdown` adapter (`--full` only)

| ID | Deliverable | Mode | Depends on |
| --- | --- | --- | --- |
| P.1 | Outcome list with dependencies and roadmap | auto | outcome-pack |

