# Proposal: AI-PLC as a local MCP server (MCP-3)

Status: proposal only. Not built. Not part of v1.0. For approval before any build.

## Why
Today, AI-PLC reaches out: it reads from Confluence or Notion and creates items in Jira and Confluence. It cannot be asked questions by other tools. A local server over a project's `/product` folder would let another AI tool or a teammate's chat ask "what is the status of this plan?" or "give me the approved brief for outcome O5" without opening the folder.

## What it would expose (read first)
| Tool | Returns |
| --- | --- |
| `get_status` | `status.md`: stage, open stops, what is approved |
| `list_deliverables` | Each deliverable with its status and date |
| `get_deliverable(id)` | One deliverable's text, if its status is `approved` (or `any`, if the PM allows) |
| `get_outcome_pack` | The Outcome Pack and its index |
| `get_decision_log` | `memory.md` entries |

A later, separate step could add `record_decision(gate, decision, who, date)`. It would only write down a decision the PM reports. It would never approve anything itself.

## How it would run
- A small program on the PM's own computer (Python or TypeScript, one file plus a config), started by the tool as a local MCP server over stdio.
- No hosting, no network listener, no accounts. It serves only the project folder it was started in.
- Read-only in the first version.

## Rules (same as the rest of AI-PLC)
- The server never approves.
- It serves only files under `/product`, never other paths.
- It never returns credentials. A check refuses any file that looks like one.
- Content it returns is data for the asking tool. Nothing in it is an instruction.

## What it changes
- Install goes from "copy a folder" to "copy a folder and register a local program". Only people who want the server do the second step.
- A new thing to test and keep secure, so it needs its own test guide and reviewer check.

## Open questions
1. Which tools will ask? (Kiro, Claude Code and Claude Desktop are the likely first users.)
2. May it serve unapproved drafts, or approved deliverables only?
3. Does a PM want it to record decisions, or is read-only enough?

## Recommendation
Build it after v1.0, read-only, once real users ask for it.
