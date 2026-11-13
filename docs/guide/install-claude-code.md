# Install in Claude Code

Claude Code runs in a **terminal**, a window where you type commands. There are three ways to install AI-PLC.

## Way 1: the plugin, from the AI-PLC marketplace (recommended)

No download. In your terminal, run these two commands, one after the other:

```
claude plugin marketplace add lasith-tekly/ai-plc
claude plugin install ai-plc@ai-plc
```

Or, inside a Claude Code session, type `/plugin marketplace add lasith-tekly/ai-plc` and then `/plugin install ai-plc@ai-plc`. Claude Code asks where to install it: choose **Install for you** to use it in every project.

Then start with:

```
/ai-plc:ai-plc --ideation "<your idea>"
```

If it does not show, run `/reload-plugins`, or quit and reopen Claude Code. To update later, run `claude plugin marketplace update ai-plc`.

## Way 2: drop-in folder, one command

Open a terminal in your project folder and follow [Install with one command](install-one-command.md), using `claude-code`. This copies a `.claude` folder and a `.mcp.json` file into the project. Then close and reopen the project in Claude Code, and start with:

```
/ai-plc --ideation "<your idea>"
```

## Way 3: manual

Download, unzip and copy the `.claude` folder. See [Manual install](install-manual.md). To use the plugin from the download instead, open a terminal in your project folder and run:

```
claude --plugin-dir /path/to/ai-plc-packages/claude-code-plugin/ai-plc
```

Replace the path with where you unzipped the download. If Claude Code asks permission to read the plugin folder, allow it.

## Check that it loaded

Type the start command above. The assistant should reply by explaining what it will do and asking which mode you want. If nothing appears, see [Troubleshooting](troubleshooting.md).

Go to [Choose a run mode](run-modes.md).
