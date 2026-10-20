# Install

1. Download `ai-plc-packages.zip` from the latest [Release](https://github.com/lasith-tekly/ai-plc/releases) and unzip it.
2. Set up the folder for your tool, as below.
3. Check that it loaded, then go to [Choose a run mode](run-modes.md).

## Steps by tool

| Tool | Status | Do this | Start command |
| --- | --- | --- | --- |
| Kiro | Tested | Copy `kiro/.kiro` into your project folder (merge with an existing `.kiro`), then reopen the project | `/ai-plc` |
| Claude Code, plugin | Run to Checkpoint 1 on an earlier build | To try it without installing: `claude --plugin-dir /path/to/claude-code-plugin/ai-plc`. Allow Claude Code to read the plugin folder if it asks | `/ai-plc:ai-plc` |
| Claude Code, drop-in | Run to Checkpoint 1 on an earlier build | Copy `claude-code-project/.claude` into your project folder | `/ai-plc` |
| Codex | Run to Gate 1 on an earlier build | Copy `codex/.codex` and `codex/.agents` into your project folder | `$ai-plc` (or `/skills`, then pick `ai-plc`) |
| GitHub Copilot | Not run. Experimental | Copy `copilot/.github` into your project folder (merge with an existing `.github`). In Agent mode, open Configure Tools and switch **Run Subagent** on, or the orchestrator cannot start the specialists | `/ai-plc` |

Everywhere in this guide the command is written as `/ai-plc`. Use the start command for your tool from the table.

## Check it loaded

In Kiro the agent picker should list `ai-plc-orchestrator` and the seven specialists, and the steering list should show `ai-plc`. In the other tools, type the start command and the orchestrator should answer by saying what it will do.

`TEST-GUIDE.md` in the package has a short checklist you can follow on a dummy idea.

## Turn Autopilot off for the first run

In Kiro, keep Autopilot off so every change and every tool call is shown to you before it happens.

## Model and cost

The agent files do not choose a model. The model you select in your tool's chat is used. Cost depends on that choice and on how much research a deliverable needs. In Kiro, single steps cost roughly 1.6 to 12.4 credits in testing. Start with a mid-tier model. If strategy, viability or review output reads thin, try a stronger model for those agents if your tool lets you choose per agent.
