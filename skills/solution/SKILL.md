---
name: solution
description: "Drafts the AI-PLC phase 3 deliverables (3.1 to 3.6): prioritised capabilities, solution research and design, usability test plan, positioning and messaging, pilot plan and MVP scope. Use after the needed phase 2 deliverables are approved."
---

# Solution (deliverables 3.1 to 3.6)

## Goal

Move from "what outcomes we want" to "what we would build and test first", with every choice traceable to evidence.

## Evidence rules

- Inputs are approved deliverables, `memory.md` and PM-supplied material, named in `sources`.
- Outside facts carry a source and date. Never invent a number, a quote or a test result.
- Label estimates "our arithmetic" and show inputs. Figures from the PM are "from the PM".
- If a page cannot be fetched normally, mark it "not confirmed". Do not work around blocks.

Every deliverable ends with `## What we are assuming` and `## Open questions`.

## 3.1 Prioritised capabilities (auto)

`/product/phase-3/3.1-prioritised-capabilities.md`

List the capabilities the product needs to deliver the outcomes in 2.2 and the use cases in 2.1, then rank them. State the ranking criteria first (for example value to the customer, evidence, effort, risk) and score each capability against them. Show the scoring so the PM can change it.

```markdown
# 3.1 Prioritised capabilities

## Ranking criteria
## Capabilities
| Rank | Capability | Outcomes (2.2) | Use cases (2.1) | Value | Evidence | Effort (to confirm) | Risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
```

Capabilities describe what the product can do for the customer, not technology. Effort is "to confirm" until the PM or a technical person supplies it.

## 3.2 Solution research, design and content (assist)

`/product/phase-3/3.2-solution-design.md`

For the top capabilities: how similar products solve it (sourced), the proposed experience as steps the customer takes, the content needed, and design questions to test. Ask the PM for existing designs, brand rules or constraints.

```markdown
# 3.2 Solution research, design and content

## Approaches seen elsewhere
| Product | How it handles this (source, date) | What to learn |
## Proposed experience
Numbered steps from the customer's side, per top use case.
## Content needed
## Design questions to test
```

## 3.3 Usability tests (human)

`/product/phase-3/3.3-usability-tests.md`

The tool cannot run tests with real people. Write the test plan and the capture template, then wait for the PM to supply results.

```markdown
# 3.3 Usability tests
status note: waiting for results from people (human deliverable)

## What we want to learn
## Who to test with (from 1.3), how many, how to recruit
## Tasks to give them
## Capture template
| Participant | Group | Task | Completed? | Where they struggled | Quote (as said) |
## Results (supplied by the PM, with dates)
## What the results say (drafted only after results are supplied)
```

Do not fill results. Without evidence the deliverable stays `draft`.

## 3.4 Early positioning and messaging (auto)

`/product/phase-3/3.4-positioning.md`

From 1.2 and 2.9: who it is for, the problem, what is different from the alternatives in 1.2, and draft messages per customer group. Offer two wordings of the main message. Claims about competitors must be sourced.

```markdown
# 3.4 Early positioning and messaging

## Positioning statement
## Differences from alternatives (sourced)
## Messages by customer group
## Proof we have, proof we need
```

## 3.5 Pilot plan (assist)

`/product/phase-3/3.5-pilot-plan.md`

How to test the product with real customers before a full launch: who, where, for how long, what to measure, what would make the pilot a success or a failure, and what it needs. Ask the PM for limits (region, budget, time).

```markdown
# 3.5 Pilot plan

## Goal and questions the pilot answers
## Who, where and how long
## Success and stop signals
## What it needs (people, access, partners, money: "to confirm" where unknown)
## Risks
```

## 3.6 MVP scope (auto)

`/product/phase-3/3.6-mvp-scope.md`

The smallest set of capabilities from 3.1 that delivers the in-scope outcomes, informed by 3.3 results. Show what is in, what is out for now, and why. If 3.3 has no results, say the scope is untested.

```markdown
# 3.6 MVP scope

## In the MVP
| Capability | Outcome it delivers | Why it is in |
## Not in the MVP (and when it might be)
## What is untested
## Constraints respected (from memory.md)
```

## Quality checks before showing the PM

- Every ranking, claim and quote is traceable to an approved file or a dated source.
- No test result is made up.
- Scope respects `memory.md`.
- Each deliverable lists what the PM must check first.
