# AI-PLC: multi-tool packages (release candidate)

AI-PLC is an AI-native product lifecycle for product managers. A PM runs one command, the AI drafts each deliverable, and humans review and approve at every stop. These packages load the same neutral files into four tools.

| Folder | Tool | What you get |
| --- | --- | --- |
| `claude-code-plugin/ai-plc` | Claude Code | A plugin: 7 agents, 12 skills, the `/ai-plc:ai-plc` command |
| `claude-code-project/.claude` | Claude Code | The same, as a drop-in folder, command is `/ai-plc` |
| `copilot/.github` | GitHub Copilot | 7 custom agents (`.agent.md`), 12 skills, the `/ai-plc` skill command |
| `codex/.codex` + `codex/.agents` | Codex | 7 custom agents (`.toml`), 12 skills, the `$ai-plc` skill |
| `kiro/.kiro` | Kiro | 8 agents (`.json`), 12 skills, the `/ai-plc` steering command. See `kiro/INSTALL.md` |


Connecting to Notion, Jira and Confluence is optional. See `MCP-SETUP.md`.

## Run it

```
/ai-plc --ideation  "<idea>"                       phases 1 and 2, stops at Gate 1
/ai-plc --planning  "<idea>"                       adds phases 3 and 4, stops at Gate 2
/ai-plc --outcomes  "<idea>"                       adds the Outcome Pack
/ai-plc --full      "<idea>" --adapter scrum       adds requirements and user stories
```

Adapters for `--full`: `scrum`, `ai-dlc`, `plain-markdown`. Everything is written to `/product` in your project. Nothing is approved until you approve it.

## Status

| Tool | Status |
| --- | --- |
| Kiro | Tested live on a dummy idea through phases 1 to 4, the Outcome Pack and all three delivery adapters (Scrum, plain-markdown, AI-DLC 2.5.67) |
| Claude Code | Plugin passes `claude plugin validate`. Tested live on a dummy idea through Checkpoint 1 (4 deliverables, reviewer report) |
| Codex | Tested live on a dummy idea through Gate 1 (14 deliverables, 2 reviews, checkpoint and gate records) |
| GitHub Copilot | File formats checked against the docs; not run yet. Experimental |

See `TEST-GUIDE.md` for the shared test and the pass checks.

## Cost

AI-PLC does not set a model. Each tool uses the model you choose in its own model menu, and the same applies to every specialist agent. This is guidance from our own test runs, not a measured rule.

- **Start small.** `--ideation` stops at Gate 1 and costs the least. A `--full` run costs the most. Run the earlier modes first and stop where you have enough.
- **Default to a mid-tier model** for the orchestrator and the specialists. In our Kiro tests, single steps used about 1.6 to 12.4 Kiro credits, and the largest were the delivery agent's long briefs.
- **Spend more only where judgement matters.** If the strategy, viability or reviewer output reads thin, switch just those agents to a stronger model and compare. Tell us what you find.
- **Keep Autopilot off** (in tools that have it) while you try connectors and writes. You see every prompt, and nothing runs that you did not mean.
- **Read only what you need.** Name the sources to read at the start. Every page read is more to process.

## Rebuild

The packages are generated from the neutral source files by `build/build_packages.py`. Edit the source, not the generated folders.

Licence: Apache 2.0.
