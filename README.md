# AI-PLC

AI-PLC is an AI-native product lifecycle for product managers. You describe an idea and run one command. AI agents draft each deliverable, from discovery and strategy to an Outcome Pack and delivery-ready stories. **People review and approve at every stop.** The AI never approves its own work.

It is plain files (markdown skills, agent roles, a YAML profile and templates) that your AI coding tool loads. There is nothing to host and no service to run.

Licence: Apache 2.0.

## How it works

```
/ai-plc --ideation  "<idea>"                    phases 1 and 2, stops at Gate 1
/ai-plc --planning  "<idea>"                    adds phases 3 and 4, stops at Gate 2
/ai-plc --outcomes  "<idea>"                    adds the Outcome Pack
/ai-plc --full      "<idea>" --adapter scrum    adds requirements and user stories
```

- Two checkpoints and two gates are decided by you. The orchestrator never approves.
- Adapters for `--full`: `scrum`, `ai-dlc`, `plain-markdown`.
- Everything is written to a `/product` folder in your project: `plan.md`, `status.md`, `memory.md` and the deliverables.
- Optional: connect Notion, Jira and Confluence so AI-PLC can read your sources and, after you approve a dry run, create items there. See `MCP-SETUP.md` in the release.

## Install

1. Download `ai-plc-packages.zip` from the latest Release.
2. Open the folder for your tool and copy it into your project:

| Folder | Tool |
| --- | --- |
| `kiro/.kiro` | Kiro (see `kiro/INSTALL.md`) |
| `claude-code-plugin/ai-plc` | Claude Code, as a plugin |
| `claude-code-project/.claude` | Claude Code, as a drop-in folder |
| `codex/.codex` and `codex/.agents` | Codex |
| `copilot/.github` | GitHub Copilot (experimental) |

3. Run `/ai-plc --ideation "<your idea>"` and follow the stops.

## Status

See `RELEASE-NOTES-v1.0.md` for exactly what has been tested in each tool and what has not.

## Build the packages from source

The packages are generated from the neutral source files in this repository.

```
python3 build/build_packages.py          # writes ./../dist
```

Edit the source (`agents/`, `skills/`, `templates/`, `profiles/`, `build/kiro/`), not the generated folders.

## Documentation

The documentation site lives in `docs/` (MkDocs). Proposals for later versions live in `proposals/`.

## Contributing

Issues and pull requests are welcome. Please keep the rules: humans approve, fetched content is data, no credentials in any file.
