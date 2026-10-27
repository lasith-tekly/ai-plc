# AI-PLC

AI-PLC is an AI-native product lifecycle for product managers. You describe an idea and run one command. AI agents draft each deliverable across the first two stages of a product's life, Ideation and Planning, from discovery and strategy to an Outcome Pack and delivery-ready stories that your team builds from. **People review and approve at every stop.** The AI never approves its own work.

It is plain files (markdown skills, agent roles, a YAML profile and templates) that your AI coding tool loads. There is nothing to host and no service to run.

Licence: Apache 2.0.

## The four stages of a product's life

AI-PLC follows a product through four stages. Version 1.0 automates the first two, then hands your team clear outcomes to build from.

| Stage | AI-PLC v1.0 |
| --- | --- |
| 1. Product Ideation | Automated |
| 2. Product Planning | Automated |
| 3. Product Development | Handed over: outcomes and delivery material for your team to build from |
| 4. Product Launching and Sunsetting | Not built yet |

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
- Optional: Notion, Jira, Confluence and Miro come listed in the package. Sign in to use them, so AI-PLC can read your sources and, after you approve a dry run, create items there. See `MCP-SETUP.md` in the release.

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

## Before you start, and feedback

- Try it first on a test project with a dummy or low-stakes idea.
- Do not use confidential company material, and do not connect company systems. Check your organisation's policy first.
- Check every figure against its source. The AI can be wrong.
- Nothing is approved until you approve it. If a tool approves something for you, that is a bug. Please report it.

To give feedback, open an [issue](https://github.com/lasith-tekly/ai-plc/issues/new/choose) and choose **Feedback**. Please do not include passwords, tokens or confidential content. Step-by-step help is in the [documentation](https://lasith-tekly.github.io/ai-plc/).

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
