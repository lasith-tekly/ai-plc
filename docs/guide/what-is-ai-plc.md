# What is AI-PLC?

AI-PLC stands for **AI-native Product Lifecycle**. It is a way of taking a product idea from "we think there is something here" to "here is what to build, and why", with AI doing the drafting and you making every decision.

## The problem it solves

Early product work is slow and uneven. Someone has to research the market, define the customer, write the business case, check the risks and turn it all into something a delivery team can build. It is usually done in documents that drift apart, and the reasoning behind a decision gets lost.

AI-PLC runs that work as one connected flow. Each piece of work is a **deliverable**: a short document such as a market definition, a vision statement or a risk assessment. Each deliverable is drafted by an AI agent, checked, and then reviewed and approved by you. Later deliverables are built only from approved earlier ones, so the thread of evidence stays intact.

## The idea in one picture

```
Idea  ->  Understand the problem  ->  Decide what is worth doing  ->  Shape the solution  ->  Test if it can work  ->  Outcomes  ->  Delivery material
              (phase 1)                     (phase 2)                     (phase 3)               (phase 4)            (after approval)     (optional)
                       \                          |                            |                          |
                    decision                  decision                     decision                   decision
```

There are four working phases. After each one, work **stops** and waits for a person to decide. Nothing moves on without that decision.

## The four phases, in plain words

| Phase | The question it answers | What you get |
| --- | --- | --- |
| 1. Assess market and customers | Is there a real problem, for real people, in a market worth entering? | Problem statement, market definition, customer definition, summary of existing research |
| 2. Define vision and strategy | What would we offer, and does the business case make sense? | Use cases, scope, vision, business model, an initial business case |
| 3. Converge on solution | What exactly will we build first? | Prioritised capabilities, positioning, pilot plan, MVP scope |
| 4. Evaluate viability | Can this actually work: legally, financially, practically? | Risk, pricing, measurement plan, a final business case |

After phase 4 and your approval, AI-PLC can also write an **Outcome Pack** (the results the product must achieve, each with a measure) and, if you ask, **delivery material** such as requirements and user stories.

## Decision points

There are four stops where a person must decide. Two are **checkpoints** and two are **gates**. See [Decision points](gates.md) for what each means. In short:

- A **checkpoint** is a product decision, usually yours and your team's: "are we on the right track?"
- A **gate** is an investment decision about the business case: "should we keep putting money and people into this?" It is usually taken by the people who fund the work, so AI-PLC prepares a short pack for you to take to them.

## What the AI does and does not do

The AI drafts, researches and checks. A separate review agent looks for unsupported claims and inconsistencies before each decision point. **The AI never approves anything.** Every figure that is a placeholder is labelled SYNTHETIC, and every claim has a source or is labelled an assumption.

## What it is made of

Plain files that your AI coding tool loads: instructions for each agent, one profile that lists the phases and deliverables, and templates. There is nothing to host. See [Install](install.md).

## Where to go next

- [Choose a run mode](run-modes.md): how far do you want to go?
- [Install](install.md) and [Your first run](first-run.md)
