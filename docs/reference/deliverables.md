# Deliverables (generated)

!!! note
    Generated from `profiles/ai-plc-v1.0.profile.yaml` and the purposes in `tools/gen_reference.py`. Do not edit by hand.

Modes: **auto** the tool drafts from the conversation and research. **assist** the tool drafts but you supply inputs or evidence. **human** people outside the tool are needed; the tool gives a template and tracks status.

## Phase 1: Assess market and customers (Ideation stage)

| ID | Deliverable | What it is for | Mode | Depends on |
| --- | --- | --- | --- | --- |
| 1.1 | Problem and opportunity statement | The problem and the opportunity, split into known, assumed and open. Everything else builds on it. | auto | none |
| 1.2 | Market definition | Market size, trends, segments and competitors, with dated sources. Shows whether there is a real market. | auto | 1.1 |
| 1.3 | Customer definition | Who the customers are, their problem, who pays and who uses it, and who to start with. | auto | 1.1 |
| 1.4 | Existing research summary | What research already exists and where it is thin. It asks you for material. | assist | none |

## Phase 2: Define vision and strategy (Ideation stage)

| ID | Deliverable | What it is for | Mode | Depends on |
| --- | --- | --- | --- | --- |
| 2.1 | Use cases | Situations where customers would use the product: who, what they do today, what success looks like. | auto | 1.1, 1.3 |
| 2.2 | Outcome-oriented scope | The results the product should achieve (not features) and what is out of scope. | auto | 1.1, 2.1 |
| 2.3 | Experience strategy fit | Compares the use cases with your company's experience or brand principles. | assist | 2.1 |
| 2.4 | Partnership consideration | Suppliers, platforms and partners the product depends on or could gain from. | assist | 1.2, 2.1 |
| 2.5 | Services consideration | Onboarding, support, content and human help needed around the product. | assist | 2.1 |
| 2.6 | Team skills gaps | The skills the scope needs against the skills the team has. | assist | 2.2 |
| 2.7 | Pricing and billing model check | Ways of earning money that fit the customers and market. It compares; you choose. | assist | 1.2, 1.3 |
| 2.8 | Business model canvas | The nine canvas blocks, each marked known, assumed or open. | auto | 1.1, 1.2, 1.3, 2.1 |
| 2.9 | Vision statement | Two or three sentences, what the product is not, and two wordings to choose from. | auto | 1.1, 2.1 |
| 2.10 | Initial business case (feeds gate 1) | The Gate 1 pack. It argues for or against investing in the next phase. | assist | 1.2, 2.2, 2.7, 2.8, 2.9 |

## Phase 3: Converge on solution (Planning stage)

| ID | Deliverable | What it is for | Mode | Depends on |
| --- | --- | --- | --- | --- |
| 3.1 | Prioritised capabilities | What the product needs to do, ranked against criteria stated up front. | auto | 2.1, 2.2 |
| 3.2 | Solution research | How similar products solve it, the proposed experience as steps, and design questions to test. | assist | 3.1 |
| 3.3 | Usability tests | A test plan and capture template. It waits for your real results. | human | 3.2 |
| 3.4 | Early positioning and messaging | Who it is for, how it differs from the alternatives, and messages per customer group. | auto | 1.2, 2.9 |
| 3.5 | Pilot plan | How to test with real customers: who, where, how long, and success and stop signals. | assist | 3.2, 3.3 |
| 3.6 | MVP scope | The smallest set of capabilities that delivers the in-scope outcomes: what is in, out and untested. | auto | 3.1, 3.3 |

## Phase 4: Evaluate viability (Planning stage)

| ID | Deliverable | What it is for | Mode | Depends on |
| --- | --- | --- | --- | --- |
| 4.1 | Legal | A list of what needs checking and by whom. The findings come from you. | human | 3.6 |
| 4.2 | Risk assessment | Risks with likelihood and impact, warning signs and responses. | assist | 3.6 |
| 4.3 | Implementability | Whether the MVP can be built with the known team, skills, partners and time. No estimates of its own. | assist | 3.2, 3.6 |
| 4.4 | Product viability | Whether it makes sense as a business, with the strongest reasons for and against. | assist | 2.10, 3.6 |
| 4.5 | Market viability | Whether the market is attractive and reachable, with evidence for and against. | auto | 1.2 |
| 4.6 | Measurement plan | How each outcome will be measured once the product exists. | assist | 2.2, 3.6 |
| 4.7 | Value assessment | Value to the customer and the business, split into evidenced, assumed and unknown. | assist | 4.4, 4.5 |
| 4.8 | Pricing strategy | Options for how to charge, the evidence for each, and what to test in the pilot. | assist | 2.7, 4.4 |
| 4.9 | Services review | Which services are needed at launch, who runs them, and what is missing. | assist | 2.5, 3.6 |
| 4.10 | Final business case (feeds gate 2) | The Gate 2 pack. It updates 2.10 and says what changed since Gate 1. | assist | 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9 |

## Outcome Definition (after Gate 2)

| ID | Deliverable | What it is for | Mode | Depends on |
| --- | --- | --- | --- | --- |
| O.n | Outcomes (one file each) | One file per measurable result, with its evidence, limits and risks. The main handover to delivery. | assist | 3.1, 3.6, 4.2, 4.6, 4.10 |
| O.M | Outcome dependency map | Which outcomes must come first (hard) and which would only help (soft). | auto | O.n |
| O.R | Outcome roadmap | The order of outcomes in drops. | auto | O.n, O.M |
| O.I | Outcome Pack index | The index of the Outcome Pack: counts, order and known issues. | auto | O.n, O.M, O.R |

## Delivery, `scrum` adapter (`--full` only)

| ID | Deliverable | What it is for | Mode | Depends on |
| --- | --- | --- | --- | --- |
| D.1 | Requirements | What the product must do to deliver each outcome. | assist | outcome-pack |
| D.2 | Requirements dependency map | Which requirements depend on which. | auto | D.1 |
| D.3 | Epics | Groups of requirements that can be built and released together. | auto | D.1, D.2 |
| D.4 | User stories | The stories a team can pick up, each traced to a requirement and an outcome. | assist | D.1, D.3 |
| D.5 | Story dependency map and order | Which stories depend on which, and a suggested order. | auto | D.4 |
| D.6 | Delivery roadmap | The delivery plan by drop, matching the outcome roadmap. | auto | D.5, O.R |
| D.7 | Delivery index and traceability | Counts and the trace from outcome to requirement to story. | auto | D.6 |

## Delivery, `ai-dlc` adapter (`--full` only)

| ID | Deliverable | What it is for | Mode | Depends on |
| --- | --- | --- | --- | --- |
| H.1 | AI-DLC handoff briefs (one per outcome) | One self-contained brief per outcome, ready for AI-DLC to pick up. | auto | outcome-pack |
| H.2 | Handoff roadmap | The order to hand the briefs over, what waits for what, and run notes. | auto | H.1, O.R |

## Delivery, `plain-markdown` adapter (`--full` only)

| ID | Deliverable | What it is for | Mode | Depends on |
| --- | --- | --- | --- | --- |
| P.1 | Outcome list with dependencies and roadmap | One readable list of outcomes with their dependencies and a roadmap. | auto | outcome-pack |

