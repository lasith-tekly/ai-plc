# AI-PLC v1.0.0-rc1 (pre-release for testers)

This is a release candidate for testing. It is not v1.0.0. See "Testing this pre-release" in `README.md` inside the zip, and the "Help us test" page in the documentation.

## What is in v1.0
- 7 specialist agents plus an orchestrator, 12 skills, one neutral profile (AI-PLC v1.0), templates.
- Run modes: `--ideation`, `--planning`, `--outcomes`, `--full`.
- Delivery adapters: Scrum, plain-markdown, AI-DLC.
- Optional connectors for Notion, Jira and Confluence (read, and create after an approved dry run).
- Packages for Kiro, Claude Code (plugin and drop-in), Codex and GitHub Copilot, generated from one source.

## What has been tested
| Area | Result |
| --- | --- |
| Kiro, phases 1 to 4, Outcome Pack, three adapters (Scrum, plain-markdown, AI-DLC) | Run on a dummy idea. All pass, with known issues below |
| Atlassian (Jira and Confluence) in Kiro: connect, read, create items, create a page | Passed on a personal test site |
| Claude Code plugin | Passes `claude plugin validate`. Run live through Checkpoint 1 on an earlier build |
| Codex | Run live through Gate 1 on an earlier build |
| GitHub Copilot | File formats checked against the docs. Not run. Experimental |
| Notion connection, listing pages, updating items AI-PLC created, Word and Excel import and export | Written, not yet tested |
| Second full run on a real idea, with a change of direction | PENDING. v1.0 is not published until it passes |

## Known issues
- A package-card label in the AI-DLC output can read differently from the answer to an open question. Review it.
- Using `--scope` together with a description in one AI-DLC command is untested.
- The AI-DLC run reported itself as version 2.5.67 in Kiro. The AI-DLC README listed 2.10.0 as the latest stable release on 2026-10-15, and the difference is unexplained. Treat the AI-DLC adapter as tested only with the Kiro build that reported 2.5.67.
- Per-agent model choice is not set by AI-PLC. See "Cost" in the package README.
- Jira sets its own reporter and default priority on created items. Confluence places a new page under the space home page when that is the space root.

## Safety rules that ship
Humans approve every gate. Fetched content is data, never instructions. Nothing is written to a connected tool without an approved dry run, and nothing is deleted. No credentials are stored in any file.
