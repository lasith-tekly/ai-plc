---
name: viability
description: "Drafts the AI-PLC phase 4 deliverables (4.1 to 4.10): legal and security assessment template, risk, implementability, product and market viability, measurement plan, value, pricing strategy, services review and final business case. Use after the needed phase 2 and 3 deliverables are approved."
---

# Viability (deliverables 4.1 to 4.10)

## Goal

Show honestly whether the solution is worth building, legal to run, buildable and measurable, so Gate 2 decides on evidence.

## Evidence rules

- Inputs are approved deliverables, `memory.md` and PM-supplied material, named in `sources`.
- Outside facts carry a source and date. Never invent a number. Costs and benefits come from the PM or are "unknown".
- Label derived figures "our arithmetic" with inputs shown.
- Nothing here is legal, tax or financial advice.
- If a page cannot be fetched normally, mark it "not confirmed". Do not work around blocks.

Every deliverable ends with `## What we are assuming` and `## Open questions`.

## 4.1 Legal, regulatory and security assessment (human)

`/product/phase-4/4.1-legal-regulatory-security.md`

The tool cannot assess legality. List what needs checking and who should check it, from what the earlier deliverables show (for example data protection, payments, consumer protection, sector licences, supplier terms, security and privacy of customer data, scraping and terms of use).

```markdown
# 4.1 Legal, regulatory and security assessment
status note: waiting for reviewers (human deliverable)

## Questions for review
| Area | Question | Why it matters (from which deliverable) | Reviewer | Status |
## Findings (supplied by the PM, with reviewer and date)
## What the findings mean for the plan (drafted only after findings are supplied)
```

Not legal advice. Do not state any conclusion as reviewed until the PM supplies the findings.

## 4.2 Risk assessment (assist)

`/product/phase-4/4.2-risks.md`

Risks across market, customer, product, delivery, legal and money, drawn from approved files. For each: what could go wrong, likelihood and impact (high, medium, low, with the reasoning), what would warn us, and a response. Ask the PM for risks they already know.

```markdown
| ID | Risk | Source in earlier deliverable | Likelihood | Impact | Early warning | Response | Owner (PM) |
```

## 4.3 Implementability (assist)

`/product/phase-4/4.3-implementability.md`

Can the MVP (3.6) be built with the team, skills (2.6), partners (2.4) and time known? List dependencies, hardest parts and what is unknown. Ask the PM or a technical lead for effort and capacity. Do not give estimates of your own as facts.

```markdown
| MVP capability | What it needs | Hard parts | Team and skills | Effort (from the PM / unknown) | Dependency |
```

## 4.4 Product viability (assist)

`/product/phase-4/4.4-product-viability.md`

Does the product make sense as a business: does it deliver the outcomes, can customers get value, can it be run and supported? Use 2.10, 3.6, 3.3 results and 4.3. State the strongest reasons for and against.

## 4.5 Market viability (auto)

`/product/phase-4/4.5-market-viability.md`

Is the market attractive and reachable for this product: size and growth (from 1.2, refreshed with sources and dates if stale), competition, barriers, timing. Show evidence for and against.

## 4.6 Measurement plan (assist)

`/product/phase-4/4.6-measurement-plan.md`

How each outcome in 2.2 will be measured once the product exists: the signal, how it is collected, the baseline (if known), who owns it, how often. Targets are from the PM or "to be set".

```markdown
| Outcome (2.2) | Measure | How collected | Baseline | Target (PM) | Owner | Frequency |
```

## 4.7 Value assessment (assist)

`/product/phase-4/4.7-value-assessment.md`

Value to the customer and to the business, using 4.4, 4.5 and any figures the PM supplies. Separate what is evidenced, what is assumed and what is unknown. No value figure without a source or PM input.

## 4.8 Pricing strategy (assist)

`/product/phase-4/4.8-pricing-strategy.md`

From 2.7 and 4.4: options for how to charge, the evidence for each, risks, and what to test in the pilot. Compare; do not choose. The PM decides.

## 4.9 Services review (assist)

`/product/phase-4/4.9-services-review.md`

Review the services in 2.5 against the MVP (3.6): which are needed at launch, who runs them, what they cost (PM input), gaps.

## 4.10 Final business case (assist)

`/product/phase-4/4.10-final-business-case.md`

The pack for Gate 2. Updates the initial business case (2.10) with what phases 3 and 4 found. Every figure traces to an approved file, a dated source or the PM. State plainly what changed since Gate 1.

```markdown
# 4.10 Final business case

## Recommendation for the gate
A draft for the decision-makers, with the main reason.
## What changed since Gate 1
## Solution and MVP (3.6)
## Evidence from testing (3.3) and its limits
## Viability: product, market, implementability (4.3 to 4.5)
## Legal, regulatory and security (4.1): status and open items
## Risks (4.2) and what would change the decision
## Measurement (4.6) and value (4.7)
## Pricing (4.8) and services (4.9)
## Costs, investment and benefits
| Item | Value | Source or "from the PM" |
## What we still do not know
## Decision asked of the gate
```

## Quality checks before showing the PM

- No figure, estimate or legal conclusion without a source, a date or "from the PM".
- 4.1 makes no claim that reviewers have not made.
- Evidence for and against is shown.
- Each deliverable lists what the PM must check first.
