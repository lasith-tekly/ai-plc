---
name: idea-intake
description: "Turns a raw product idea into an approved problem and opportunity statement (deliverable 1.1) by asking the PM a short set of questions. Use at the start of AI-PLC phase 1."
---

# Idea intake (deliverable 1.1)

## Goal

A clear statement of the customer problem and the opportunity it represents, in the PM's own terms and grounded in what is known. Everything later in the run builds on it.

## Steps

1. Read the idea and `memory.md`. List what the idea already answers.
2. Ask only what is missing, in rounds of up to four questions, saying why each matters:
   - **Scope first**: which customers, which region or market, and what is out of scope for this run (for example consumer or business, one country or global)? Ask this in round one, because it shapes every later deliverable.
   - **Who** has the problem, and in what situation?
   - **What** do they do today, and what goes wrong or costs them?
   - **How do you know** it is a real problem (a conversation, data, a complaint, a hunch)?
   - **Why now**: what has changed that makes this worth solving?
   - **What would success look like** for the customer, in their words?
   - **Limits already known**: budget, deadline, regulation, platform, or things ruled out.
   Keep questions open and neutral. Do not offer example answers that lead the PM toward one view; offer options only when the choice is genuinely a list (for example region).
3. If the PM cannot answer, record it as an open question and carry on.
4. Draft the statement with the sections below. Keep it to one page.
5. Show it to the PM and ask: approve, or what should change? Revise until they decide.

## Output (`/product/phase-1/1.1-problem-opportunity.md`)

Use the standard deliverable frontmatter (`id`, `profile`, `status: draft`, `version`, `updated`, `mode`, `depends_on`, `sources`), then:

```markdown
# 1.1 Problem and opportunity statement

## The problem
Two or three sentences, from the customer's side: who, in what situation, what goes wrong, what it costs them.

## The opportunity
Two or three sentences: what becomes possible or valuable if the problem is solved, and for whom.

## What we know
- <fact, with its source and date, or "from the PM">

## What we are assuming
- <assumption, and how it could be checked>

## Open questions
- <question, and who could answer it>

## Why now
One or two sentences.
```

## Quality checks before showing the PM

- The problem is stated as a customer situation, not as a missing feature or a technology.
- Every fact has a source and date, or is marked "from the PM".
- Nothing in "What we know" is really an assumption.
- The opportunity does not claim a market size; that belongs to 1.2.
