# 2. Install

This page helps you pick your tool and get a project ready for your first run. No coding is needed. Each tool has its own page with the steps.

## What you need

| You need | Why | Where to get it |
| --- | --- | --- |
| An AI coding tool | AI-PLC is a set of files that a tool loads and follows. The tool is the app you will chat with | [Kiro](https://kiro.dev) is the easiest to start with and the most tested |
| An empty folder for your test project | AI-PLC writes its work into a `product` folder inside your project, and nowhere else | You make it below |

## Make a project folder

A **project folder** is just a normal folder on your computer where AI-PLC will keep your work. Make a new one, for example `my-first-ai-plc-run` in your Documents folder. Keep it empty for now. Use a new folder for each idea.

## Choose your tool

| Your tool | Easiest way to install | Steps |
| --- | --- | --- |
| **Kiro** (recommended) | Install the AI-PLC power from inside Kiro | [Install in Kiro](install-kiro.md) |
| Claude Code | Two commands from the AI-PLC marketplace | [Install in Claude Code](install-claude-code.md) |
| Codex | One command | [Install in Codex](install-codex.md) |
| GitHub Copilot (experimental) | One command | [Install in GitHub Copilot](install-copilot.md) |

Other ways, for any tool:

- [Install with one command](install-one-command.md) on a Mac or Windows. You paste one line into a terminal.
- [Manual install](install-manual.md): download, unzip and copy. No terminal needed.

## The start command for your tool

You type this in the chat. It is the same idea everywhere, with a small difference in the first characters:

| Tool | Start command |
| --- | --- |
| Kiro | `/ai-plc` |
| Claude Code, drop-in | `/ai-plc` |
| Claude Code, plugin | `/ai-plc:ai-plc` |
| Codex | `$ai-plc` |
| GitHub Copilot | `/ai-plc` |

Everywhere else in this guide the command is written as `/ai-plc`. Use the one for your tool.

If the tool does not show AI-PLC after you install, close and reopen the project. If it still does not show, quit the tool completely and open it again.

## Cost and model

The AI-PLC files do not choose an AI model. Your tool uses the model you select in its chat. In testing, single steps in Kiro cost roughly 1.6 to 12.4 Kiro credits, and a long run costs more. Start with `--ideation`, which costs the least. If strategy or review output reads thin, try a stronger model.

## Ready?

Go to [Choose a run mode](run-modes.md).
