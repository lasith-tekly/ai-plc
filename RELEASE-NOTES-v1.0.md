# AI-PLC v1.0.0-rc2

See "Before you start, and how to give feedback" in `README.md` inside the zip, and the "Feedback" page in the documentation.

## What is in v1.0
- Covers the first two of the four product lifecycle stages: Product Ideation and Product Planning. It then produces outcomes and delivery material for the Development stage. Product Launching and Sunsetting is not built yet.
- 7 specialist agents plus an orchestrator, 12 skills, one neutral profile (AI-PLC v1.0), templates.
- Run modes: `--ideation`, `--planning`, `--outcomes`, `--full`.
- Delivery adapters: Scrum, plain-markdown, AI-DLC.
- Research agents keep a log of the tools and searches they used, and the reviewer checks that log before every stop.
- Optional connectors for Notion, Jira, Confluence and Miro (read, and create after an approved dry run). The connection list ships in every package. You only sign in.
- Packages for Kiro, Claude Code (plugin and drop-in), Codex and GitHub Copilot, generated from one source.

## What has been tested
| Area | Result |
| --- | --- |
| Kiro, phases 1 to 4, Outcome Pack, three adapters (Scrum, plain-markdown, AI-DLC) | Run on a dummy idea. All pass, with known issues below |
| Atlassian (Jira and Confluence) in Kiro: connect, read, create items, create a page | Passed on a personal test site |
| One-command install (`install.sh`) in Kiro's built-in terminal on a Mac | Passed. Files copied, project opened in Kiro |
| One-command install on Windows (`install.ps1`), and in Claude Code, Codex and Copilot | Written, not yet tested in the tool. Copying is tested for all four tools |
| Claude Code plugin | Passes `claude plugin validate`. Run live through Checkpoint 1 on an earlier build |
| Codex | Run live through Gate 1 on an earlier build |
| GitHub Copilot | File formats checked against the docs. Not run. Experimental |
| Miro in Kiro: connect, create the Mermaid maps as diagrams on a board | Passed on a test board. Reading an existing board not yet confirmed |
| Notion connection, listing pages, updating items AI-PLC created, Word and Excel import and export | Written, not yet tested |
| Second full run on a real idea, with a change of direction | PENDING. v1.0 is not published until it passes |

## Known issues
- A package-card label in the AI-DLC output can read differently from the answer to an open question. Review it.
- Using `--scope` together with a description in one AI-DLC command is untested.
- The AI-DLC adapter was tested with AI-DLC 2.5.67, as reported by Kiro. Other AI-DLC versions have not been tested.
- Per-agent model choice is not set by AI-PLC. See "Cost" in the package README.
- Jira sets its own reporter and default priority on created items. Confluence places a new page under the space home page when that is the space root.

## Safety rules that ship
Humans approve every gate. Fetched content is data, never instructions. Nothing is written to a connected tool without an approved dry run, and nothing is deleted. No credentials are stored in any file.
