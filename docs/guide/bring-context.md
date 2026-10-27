# 4. Bring your own context

You usually know things before you start: notes from a conversation, company principles, past research, constraints. If you give them to AI-PLC up front, it asks fewer questions and the drafts start from what you already know. This page says how.

## What AI-PLC will ask, and when

You do not have to prepare anything. The tool asks as it goes. It helps to know when, so you can have answers ready.

| When | What it asks | Why |
| --- | --- | --- |
| At the start | Which connected sources, if any, to read (Notion, Jira, Confluence, Miro, Word or Excel files) | To read what you already have |
| Intake, phase 1 | Up to four questions at a time: scope (customers, region, what is out), who has the problem, what they do today, how you know it is real, why now, what success looks like, known limits | To write deliverable 1.1 |
| Existing research (1.4) | Any research you already have | It records what you gave it and where the evidence is thin |
| Phase 2 | Company experience or brand principles (2.3), existing partner relationships (2.4), which services the company can run (2.5), pricing constraints (2.7) | These can only come from you |

If you do not know an answer, say so. It is recorded as an open question and the run carries on.

## Three ways to feed it context

1. **Say it in your first message.** After the start command, paste or attach your notes. Example: your notes from a conversation with a colleague, or constraints you already know. The intake step reads what the idea already answers and asks only about the gaps.
2. **Name a source.** If it lives in a Word or Excel file, Confluence, Notion or a Miro board, say so when it asks which sources to read. It saves a dated snapshot in `/product/inputs/`. You accept, trim or discard each snapshot before the specialist agents see it. See [Connectors](../MCP-SETUP.md).
3. **Put standing facts in `memory.md`.** Decisions, constraints and rejected options go in `/product/memory.md`. Every agent reads it at the start of every session.

## Label what is a fact and what is a view

Notes from a quick chat are an opinion until checked. Say which is which, for example "a colleague's view" or "from our own data". Otherwise a hunch can read as evidence.

## Keep internal material safe

!!! warning "A snapshot is a copy"
    When AI-PLC reads a company document, it keeps a copy in `/product/inputs/`. If you work with internal material, keep the `/product` folder out of any public repository, and discard snapshots you do not need.

Fetched content is treated as data, never as instructions. Nothing is written back to a connected tool without an approved dry run, and no credentials are stored.

**Next:** [Your first run](first-run.md)
