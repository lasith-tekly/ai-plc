---
name: strategy
description: "Drafts the AI-PLC phase 2 deliverables (2.1 to 2.10) from approved phase 1 evidence: use cases, scope, strategy fit, partnerships, services, skills, pricing, business model canvas, vision and initial business case. Use after the needed phase 1 deliverables are approved."
---

# Strategy (deliverables 2.1 to 2.10)

## Goal

Turn what we know about the problem, market and customers into a direction a business can decide on at Gate 1. Every deliverable shows what is known, what is assumed and what is open.

## Evidence rules

- Inputs are approved deliverables, `memory.md` and PM-supplied material. Name them in `sources`.
- Outside facts carry a source and date. Never invent a number. If it cannot be found, write "unknown" and add an open question.
- A figure the PM gives is "from the PM". An estimate is labelled "our arithmetic" with its inputs shown.
- If a page cannot be fetched normally, mark it "not confirmed". Do not work around blocks. About 12 sources at most per deliverable.

## Common sections

Every deliverable ends with:

```markdown
## What we are assuming
## Open questions
```

## 2.1 Use cases (auto)

`/product/phase-2/2.1-use-cases.md`

From 1.1 and 1.3, write the situations in which the customer would use the product. For each use case: who, the situation, what they want to get done, what they do today, what success looks like, and the customer group from 1.3.

```markdown
# 2.1 Use cases

| ID | Customer group | Situation | What they want to get done | Today | Success looks like |
| --- | --- | --- | --- | --- | --- |

## Priority view
Which use cases matter most and why. A draft for the PM to decide, with the evidence from 1.3 and 1.4.
```

Keep to the customer's situation, not features. Aim for 5 to 10 use cases.

## 2.2 Outcome-oriented scope (auto)

`/product/phase-2/2.2-outcome-scope.md`

State what the product should achieve for the customer and the business, and what is out of scope. Outcomes are results (a customer or business change that can be observed), not features.

```markdown
# 2.2 Outcome-oriented scope

## Outcomes in scope
| ID | Outcome (a result, not a feature) | For whom | How we would know | Use cases |
| --- | --- | --- | --- | --- |

## Out of scope
- <item, and why>

## Scope decisions already made
- <from memory.md, with date>
```

Do not write measurement targets as facts. "How we would know" names the signal, not a number, unless the PM supplied a target.

## 2.3 Experience strategy fit (assist)

`/product/phase-2/2.3-experience-strategy-fit.md`

Ask the PM for the company's experience or brand principles and any existing customer journey standards. Then compare the use cases to them. If none exist, say so, state the experience principles the use cases imply, and mark them as proposed.

```markdown
# 2.3 Experience strategy fit

## Company principles supplied
## Fit by use case
| Use case | Fits the principles? | Gap or tension |
| --- | --- | --- |
```

## 2.4 Partnership consideration (assist)

`/product/phase-2/2.4-partnerships.md`

From 1.2 and 2.1, list the partners the product would depend on or gain from (suppliers, platforms, data or payment providers). Ask the PM about existing relationships.

```markdown
# 2.4 Partnership consideration

| Partner type | Examples | Why needed | Risk or dependency | Status (PM) |
| --- | --- | --- | --- | --- |
```

## 2.5 Services consideration (assist)

`/product/phase-2/2.5-services.md`

What the customer needs around the product to get value: onboarding, support, content, operations, human help. Ask the PM which services the company can run.

```markdown
# 2.5 Services consideration

| Service | Needed for use case | Who would run it | Open question |
| --- | --- | --- | --- |
```

## 2.6 Team skills gaps (assist)

`/product/phase-2/2.6-team-skills-gaps.md`

Ask the PM for the skills the team has. Compare them with the skills 2.2 implies. If the PM does not know the team, give the template and mark the status human-to-complete.

```markdown
# 2.6 Team skills gaps

| Skill needed | For outcome | Available today (PM) | Gap | Ways to close it |
| --- | --- | --- | --- | --- |
```

## 2.7 Pricing and billing model check (assist)

`/product/phase-2/2.7-pricing-billing.md`

Check which ways of earning money fit the customers and the market. Use 1.2 for how competitors charge and 1.3 for who pays. Ask the PM about constraints (existing pricing, regulation, payment methods). Compare options; do not pick one.

```markdown
# 2.7 Pricing and billing model check

| Option (for example commission, subscription, fee per use, advertising) | How competitors do it (source, date) | Fit with the customers | Risks |
| --- | --- | --- | --- |

## Billing considerations
Payments, currencies, refunds, taxes, regulation that apply. Mark anything unverified.

## What the PM needs to decide
```

## 2.8 Business model canvas (auto)

`/product/phase-2/2.8-business-model-canvas.md`

Fill the nine blocks from approved inputs. Mark each block as known, assumed or open.

```markdown
# 2.8 Business model canvas

| Block | Content | Known / assumed / open |
| --- | --- | --- |
| Customer segments | | |
| Value propositions | | |
| Channels | | |
| Customer relationships | | |
| Revenue streams | | |
| Key resources | | |
| Key activities | | |
| Key partners | | |
| Cost structure | | |
```

## 2.9 Vision statement (auto)

`/product/phase-2/2.9-vision.md`

A short vision (two or three sentences) and a one-line statement of what the product is not. Offer two alternative wordings so the PM can choose.

```markdown
# 2.9 Vision statement

## Vision
## What this product is not
## Alternative wording
```

## 2.10 Initial business case (assist)

`/product/phase-2/2.10-initial-business-case.md`

The pack for Gate 1. It argues for or against investing in the next phase using the approved evidence. No figure without a source or an input from the PM. Where numbers are missing, say what is needed and from whom.

```markdown
# 2.10 Initial business case

## Recommendation for the gate
One paragraph. State it as a draft for the decision-makers, with the main reason.

## Problem and opportunity (from 1.1)
## Market and competition (from 1.2)
## Customers and who goes first (from 1.3)
## Scope and outcomes (from 2.2)
## How it earns money (from 2.7 and 2.8)

## Costs and investment
| Item | Value | Source or "from the PM" |
| --- | --- | --- |
Unknown items are written "unknown" and listed in open questions.

## Benefits
| Benefit | How it would be measured | Value | Source |
| --- | --- | --- | --- |

## Risks and what would change the decision
## What we still do not know
## Decision asked of the gate
Approve, rework, pivot or stop, and what the decision-makers need to see to approve.
```

## Quality checks before showing the PM

- Nothing is written as fact without a source, date or "from the PM".
- Scope decisions in `memory.md` are respected.
- Use cases and outcomes are about the customer, not features.
- Where evidence conflicts, both sides are shown.
- Each deliverable lists what the PM must check first.
