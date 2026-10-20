# 2. Install

This page takes you from the download to a project that is ready for your first run. No coding is needed. Allow some time to read it through once before you start.

## What you need

| You need | Why | Where to get it |
| --- | --- | --- |
| An AI coding tool | AI-PLC is a set of files that a tool loads and follows. The tool is the app you will chat with | [Kiro](https://kiro.dev) is the easiest to start with and the most tested. Others are listed below |
| The AI-PLC download | The files for each tool | The [Releases page](https://github.com/lasith-tekly/ai-plc/releases) on GitHub. Download `ai-plc-packages.zip` |
| An empty folder for your test project | AI-PLC writes its work into a `product` folder inside your project, and nowhere else | You make it in step 1 |

## Step 1: make a project folder

A **project folder** is just a normal folder on your computer where AI-PLC will keep your work. Make a new one, for example `my-first-ai-plc-run` in your Documents folder. Keep it empty for now. Use a new folder for each idea.

## Step 2: unzip the download

1. Download `ai-plc-packages.zip` from the [Releases page](https://github.com/lasith-tekly/ai-plc/releases). It is listed under **Assets**.
2. Double-click the zip file to unzip it (on Windows, right-click and choose **Extract All**).
3. Open the new `ai-plc-packages` folder. Inside are one folder per tool: `kiro`, `claude-code-plugin`, `claude-code-project`, `codex` and `copilot`, plus a README and some guides.

You only need the folder for the tool you use.

## Step 3: copy the files into your project folder

The files you copy have names that start with a dot, such as `.kiro`. Computers hide these by default, so you may think they are missing. Show them first:

- **Mac:** open the folder in Finder and press **Command + Shift + .** (full stop). Press it again to hide them.
- **Windows:** in File Explorer choose **View**, then **Show**, then **Hidden items**.

Then copy for your tool:

| Tool | Open this folder in the download | Copy this into your project folder |
| --- | --- | --- |
| **Kiro** (recommended) | `kiro` | the `.kiro` folder |
| Claude Code, drop-in | `claude-code-project` | the `.claude` folder |
| Codex | `codex` | both the `.codex` and the `.agents` folders |
| GitHub Copilot | `copilot` | the `.github` folder |

Copy the **whole folder**, not what is inside it. Your project folder should now contain, for example, a folder called `.kiro`. If your project already has a folder with the same name, choose to merge. Nothing in AI-PLC overwrites the tool's own files.

The Claude Code plugin works differently: it is loaded with a command rather than copied. See [Claude Code plugin](#claude-code-plugin) below.

## Step 4: open the project in your tool

Open your tool, then open your project folder in it (usually **File**, then **Open Folder**). If the project was already open when you copied the files, close it and open it again so the tool notices them.

## Step 5: check that it loaded

**In Kiro:** in the chat panel, click the agent name in the bar at the bottom. You should see `ai-plc-orchestrator` and seven more agents whose names start with `ai-plc-`: discovery, strategy, solution, viability, reviewer, outcome and delivery. Choose `ai-plc-orchestrator`.

**In other tools:** type the start command from the table below. The assistant should reply by explaining what it will do and asking which mode you want.

If nothing appears, see [Troubleshooting](troubleshooting.md).

## Step 6: switch Autopilot off

Some tools have an **Autopilot** setting that lets the AI make changes without asking. For your first run, make sure it is **off**, so every change is shown to you first. In Kiro, find the Autopilot switch in the chat panel and turn it off.

## The start command for your tool

You type this in the chat. It is the same idea everywhere, with a small difference in the first characters:

| Tool | Status | Start command |
| --- | --- | --- |
| Kiro | Tested | `/ai-plc` |
| Claude Code, drop-in | Run to Checkpoint 1 on an earlier build | `/ai-plc` |
| Claude Code, plugin | Run to Checkpoint 1 on an earlier build | `/ai-plc:ai-plc` |
| Codex | Run to Gate 1 on an earlier build | `$ai-plc` |
| GitHub Copilot | Not run. Experimental | `/ai-plc` |

Everywhere else in this guide the command is written as `/ai-plc`. Use the one for your tool.

## Claude Code plugin

Claude Code runs in a **terminal**, a window where you type commands. If you have not used one, use Kiro or the drop-in folder instead. If you are comfortable, open a terminal in your project folder and run:

```
claude --plugin-dir /path/to/ai-plc-packages/claude-code-plugin/ai-plc
```

Replace the path with where you unzipped the download. If Claude Code asks permission to read the plugin folder, allow it.

## GitHub Copilot

Copilot is experimental and has not been run. After copying `.github`, open Copilot in **Agent mode**, open **Configure Tools** and make sure **Run Subagent** is switched on. If it is off, the orchestrator cannot start the specialists.

## Cost and model

The AI-PLC files do not choose an AI model. Your tool uses the model you select in its chat. In testing, single steps in Kiro cost roughly 1.6 to 12.4 Kiro credits, and a long run costs more. Start with `--ideation`, which costs the least. If strategy or review output reads thin, try a stronger model.

## Ready?

Go to [Choose a run mode](run-modes.md).
