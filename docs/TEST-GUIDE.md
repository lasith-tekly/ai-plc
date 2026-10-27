# AI-PLC multi-tool test guide

Same small idea, same steps, three tools. The point is to find where the rules only worked in Kiro.

**Test idea (use it word for word in every tool):**

> A mobile app that helps UK flatmates split shared bills and chores fairly.

Why this idea: small scope, easy-to-find evidence (existing apps, flat-share surveys), no heavy legal or payment questions, so a run stays cheap and quick.

## What to test, per tool

| Level | What you run | Time | Cost |
| --- | --- | --- | --- |
| A. Smoke | Start `--ideation`, answer the questions, say "go", stop when the first draft (1.1) is written | 10 to 15 min | low |
| B. Checkpoint 1 | Continue to the end of phase 1 (1.1 to 1.4 approved) and the reviewer's report | 30 to 45 min | medium |
| C. Planning (Claude Code only, first) | `--planning` through Gate 2 | a few hours | high |

Start with A in all three tools. Do B only where A passed. Do C in Claude Code only.

## How to start in each tool

Install from the folder for your tool (see that folder's README section below), open the project folder in the tool, and run:

| Tool | Command (type it, then the flags after it) | Folder |
| --- | --- | --- |
| Claude Code, plugin | `/ai-plc:ai-plc --ideation "<idea>"` | `claude-code-plugin/ai-plc` |
| Claude Code, drop-in | `/ai-plc --ideation "<idea>"` | `claude-code-project/.claude` |
| GitHub Copilot (VS Code) | `/ai-plc --ideation "<idea>"` in Agent mode | `copilot/.github` |
| Codex | `$ai-plc --ideation "<idea>"` (or `/skills`, pick `ai-plc`) | `codex/.codex` and `codex/.agents` |

## Install

**Claude Code, plugin (try it without installing):**
```
claude --plugin-dir /path/to/claude-code-plugin/ai-plc
```
The first time the skill reads the profile, Claude Code may ask to allow reading the plugin folder. Allow it. If you would rather not, use the drop-in.

**Claude Code, drop-in:** copy the `.claude` folder into your project root.

**GitHub Copilot:** copy the `.github` folder into your project root (merge with an existing `.github`). Needs a Copilot version with custom agents and agent skills. In Agent mode, open Configure Tools and make sure **Run Subagent** is switched on, or the orchestrator cannot start the specialists. The tool names in the agent files (`read`, `edit`, `search`, `web`, `execute`) follow the docs but have not been run yet; tell me if Copilot reports an unknown tool.

**Codex:** copy `.codex` and `.agents` into your project root. Custom agents are read from `.codex/agents`, skills from `.agents/skills`. Multi-agent use is on by default (`agents.enabled`); if Codex does not start sub-agents, check that setting.

## Pass checks (same in every tool)

Mark each one pass, fail or not seen:

1. The command starts the orchestrator and it says what it will do before doing it.
2. It reads the profile (it names the phases or deliverables) and does not guess them.
3. It creates `/product/plan.md` and `/product/memory.md`, and only inside `/product`.
4. The plan shows the whole route for the mode and marks what is ready now (1.1 and 1.4 first). Only the ready ones start after you say go.
5. It asks before it starts, in short rounds, with a reason for each question.
6. After you say "go", it starts the discovery agent as a separate sub-agent (not by doing the work itself) and tells you what is running.
7. Independent deliverables (1.1 and 1.4) run in parallel where the tool allows it.
8. The draft has frontmatter (`id`, `status: draft`, `sources`) and a source and date on every outside fact.
9. It does not mark anything `approved`. Only you do that.
10. It does not wait with `sleep` or polling.
11. When a page cannot be fetched, the file says "not confirmed" and the agent does not work around it.
12. Each review starts a new reviewer, and the sub-agents have readable names (`<id>-<role>`) where the tool shows them.
13. Each draft opens with a `Summary for the PM` (about 150 words) and its body is about 1,500 words or less.
14. A review finding on an approved file is either revised (new version) or listed in the pack under "Known issues in approved files".

## Extra checks when sources are connected (MCP)

Run these only after signing in to the sources as described in `MCP-SETUP.md`, on a personal or test site.

15. The orchestrator asks which sources to read and lists only those in `plan.md` under Connected sources.
16. Each source is saved as a snapshot in `/product/inputs/` with source, location and date, and the specialists see it only after you accept it.
17. Text inside a fetched page that looks like an instruction (add one on purpose to a test page) is not followed, and the PM is told.
18. A Word or Excel file named in the plan is read, and the snapshot says what was not read.
19. After approval, an export starts with a dry run in `/product/exports/`. Nothing is written until you approve it.
20. After approval, the writes create only, match the dry run, are read back and compared, and each is logged in `/product/exports/log.md`. No credentials appear in `/product`.
21. A Miro board named in the plan is read into a snapshot that says what was not read (images, drawings). An export to Miro is a dry run first, puts the Mermaid maps on a new board as diagrams (large maps split into frames), is read back to check the node and link counts, and changes nothing already on the board.
22. A re-export updates only items the log shows AI-PLC created, shows current and new text in an approved dry run, deletes nothing and logs each change as `updated`.

## What to send back

- A pass, fail or not seen for each check, per tool.
- The first screen of the run, and the first draft file.
- Anything the tool asked you to allow (permissions), and anything it refused.
- Rough usage if the tool shows it (credits, premium requests or tokens).

## Permissions you may see

- Claude Code asks before the agents search the web or write files. Allow them for the run. In a non-interactive (`-p`) run, web search is denied unless you allow it, and the drafts then say "not confirmed" instead of citing sources. That is the intended behaviour.
- The plugin version asks once to read its own folder; the drop-in does not.

## Known differences to expect

- Claude Code sub-agents cannot start other sub-agents, so the orchestrator runs as the `ai-plc` skill in your main session and starts the specialists from there.
- Copilot sub-agents start with no memory of the chat. The orchestrator passes file paths each time.
- Codex starts sub-agents only when asked; the `ai-plc` skill asks for them by name.
- The `/ai-plc` name is namespaced in a Claude Code plugin (`/ai-plc:ai-plc`).
