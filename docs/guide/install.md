# Install

1. Download `ai-plc-packages.zip` from the latest [Release](https://github.com/lasith-tekly/ai-plc/releases) and unzip it.
2. Copy the folder for your tool into your project folder.

| Folder in the package | Tool | Notes |
| --- | --- | --- |
| `kiro/.kiro` | Kiro | Reopen the project afterwards. Skills have no prefix |
| `claude-code-plugin/ai-plc` | Claude Code, as a plugin | Skills are prefixed `ai-plc-` |
| `claude-code-project/.claude` | Claude Code, drop-in folder | |
| `codex/.codex` and `codex/.agents` | Codex | |
| `copilot/.github` | GitHub Copilot | Experimental, not run |

3. Check that it loaded. In Kiro, the agent picker should list `ai-plc-orchestrator` and the seven specialists, and the steering list should show `ai-plc`.

Each package folder has its own install notes. `TEST-GUIDE.md` in the package has a short checklist you can follow on a dummy idea.

## Turn Autopilot off for the first run

In Kiro, keep Autopilot off so every change and every tool call is shown to you before it happens.

## Model and cost

The agent files do not choose a model. The model you select in your tool's chat is used. Cost depends on that choice and on how much research a deliverable needs. In Kiro, single steps cost roughly 1.6 to 12.4 credits in testing. Use a stronger model for strategy and viability if your tool lets you choose per agent, and a cheaper one for the rest.
