---
name: market-and-customers
description: "Drafts the market definition (1.2), customer definition (1.3) and existing research summary (1.4) for AI-PLC phase 1, using web search and any research the PM supplies. Use after the problem and opportunity statement (1.1) is approved."
---

# Market and customers (deliverables 1.2, 1.3 and 1.4)

## Goal

Show whether the problem sits in a real market with identifiable customers, using evidence rather than assumptions. 1.2 and 1.3 can be drafted in parallel once 1.1 is approved.

## Evidence rules

- Search the web first. Also use any research the PM uploads, and name it as a source.
- Every figure, trend or claim from outside carries a source (URL or document name) and a date.
- Prefer original sources (reports, filings, official statistics) over summaries.
- When sources disagree, show both and say so.
- Never invent a number. If it cannot be found, write "unknown" and add an open question.
- Keep quotes short and paraphrase the rest.
- If a page cannot be fetched with the normal fetch tool (blocked, paywalled, sign-in), record the source as "not confirmed" and move on. Do not work around it: no browser spoofing, no cached or mirror copies, no scripts to get past the block.
- Use at most about 12 sources per deliverable, original sources first. Stop when more sources would repeat the same point.
- Mark sponsored or vendor-published content as such, and flag figures published by a company that sells the thing measured.
- 1.4 summarises research the PM supplied or that is already public and about the problem. It does not size the market or analyse competitors; that belongs to 1.2.

## 1.2 Market definition

`/product/phase-1/1.2-market-definition.md`

```markdown
# 1.2 Market definition

## Market in one paragraph
What market this is, and where the product would sit in it.

## Size and growth
| Measure | Value | Source and date |
| --- | --- | --- |

## Trends
- <trend, with source and date>

## Segments
| Segment | Description | Why it matters |
| --- | --- | --- |

## Alternatives and competitors
| Alternative | What it does | Gap or weakness |
| --- | --- | --- |

## What we are assuming
## Open questions
```

## 1.3 Customer definition

`/product/phase-1/1.3-customer-definition.md`

```markdown
# 1.3 Customer definition

## Customer groups
| Group | Who they are | The problem they have | How often | Evidence |
| --- | --- | --- | --- | --- |

## Who benefits most, and why
Which group to start with, and the reason. This is a draft for the PM to decide.

## Buyers and users
If the person who pays differs from the person who uses it, say who is who.

## What we are assuming
## Open questions
```

## 1.4 Existing research summary (assist)

`/product/phase-1/1.4-existing-research.md`

The PM supplies the research. Ask for it plainly: interviews, surveys, analytics, support tickets, earlier studies. For each item record what it is, its date and what it shows, then summarise what the evidence says about the problem and the customers, and where it is thin. If the PM has none, say so in the file and list what would be worth gathering.

## Frontmatter

Use the standard deliverable frontmatter (`id`, `profile`, `status: draft`, `version`, `updated`, `mode`, `depends_on`, `sources`). 1.2 and 1.3 depend on `["1.1"]`; 1.4 depends on nothing.

## Quality checks before showing the PM

- Every number has a source and a date, or says "unknown".
- Segments and customer groups are about people and situations, not product features.
- Competitors and alternatives include what customers do today, including doing nothing.
- Known, assumed and open items are kept apart.
