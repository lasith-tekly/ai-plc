# AI-PLC v1.0.0-rc3

See "Before you start, and how to give feedback" in `README.md` inside the zip, and the "Feedback" page in the documentation.

## New in rc3
- **Easier install.** One command for Kiro, Claude Code, Codex and GitHub Copilot (`install.sh` on Mac and Linux; `install.ps1` on Windows, not yet tested on Windows). It previews first and never overwrites a file you already have.
- **Kiro power.** Import the AI-PLC power from GitHub inside Kiro, then ask Kiro to "set up AI-PLC".
- **Claude Code marketplace.** Install the plugin with `claude plugin marketplace add lasith-tekly/ai-plc` and `claude plugin install ai-plc@ai-plc`.
- **Install guide split by tool**, with a manual route for anyone who does not use a terminal.
- **Miro tested** for connecting and creating diagrams from the Mermaid maps.
- Packages carry the maintainer name as author.

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
| One-command install (`install.sh`) in Kiro on a Mac | Passed. Files copied, project opened in Kiro |
| AI-PLC Setup power in Kiro (import from GitHub, then "set up AI-PLC") | Passed. Preview shown, files checked, existing files kept |
| Claude Code marketplace install (`ai-plc@ai-plc`) | Validates and installs in a clean setup: 13 skills, 7 agents, 3 connections load. Not yet run end to end in Claude Code |
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
