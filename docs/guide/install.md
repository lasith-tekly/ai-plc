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

## Faster: one command (skips steps 2 and 3)

Instead of downloading, unzipping and copying by hand, you can paste one line into the Terminal. It downloads the newest release and copies the right files into your project folder. It never overwrites a file you already have, and it never asks for your password. If anything asks for a password, stop and close the window.

If you would rather read it before you run it, the script is on [GitHub](https://github.com/lasith-tekly/ai-plc/blob/main/install.sh) and is short.

### On a Mac

1. **Open the Terminal.** Press **Command + Space**, type `Terminal`, and press **Enter**. A window with a blinking cursor opens. This is where you type or paste commands.
2. **Go to your project folder.** If you made the folder in step 1 (for example `my-first-ai-plc-run` in Documents), type this and press **Enter**:

    ```
    cd ~/Documents/my-first-ai-plc-run
    ```

    No folder yet? This makes one and goes into it:

    ```
    mkdir -p ~/Documents/my-first-ai-plc-run && cd ~/Documents/my-first-ai-plc-run
    ```

    A folder somewhere else? Type `cd` and a space, then drag the folder from Finder into the Terminal window, and press **Enter**.
3. **Preview first (optional).** This shows what would be copied and changes nothing. Paste it and press **Enter**:

    ```
    curl -fsSL https://raw.githubusercontent.com/lasith-tekly/ai-plc/main/install.sh | sh -s -- kiro --dry-run
    ```

4. **Install.** Paste this and press **Enter**:

    ```
    curl -fsSL https://raw.githubusercontent.com/lasith-tekly/ai-plc/main/install.sh | sh -s -- kiro
    ```

    Replace `kiro` with `claude-code`, `codex` or `copilot` if you use one of those tools. It prints which version it downloads, then a line like `Done: 38 file(s) copied, 0 kept.`
5. **Check the files are there.** Type `ls -a` and press **Enter**. You should see `.kiro` (or `.claude`, `.codex` and `.agents`, or `.github`, for the other tools). In Finder, press **Command + Shift + .** to show hidden files.

!!! warning "Restart or reload if the tool does not see the files"
    Tools read their files when a project opens. If the project was already open when you ran the command, close and reopen the project. If AI-PLC or its connections still do not show, quit the tool completely and open it again. The new agents appear after the tool has re-read the folder.

Then carry on at [step 4](#step-4-open-the-project-in-your-tool).

### On Windows

This route has not been tested on Windows yet. If it fails, use steps 2 and 3 below and tell us what happened.

1. **Open PowerShell.** Click the Start menu, type `PowerShell`, and press **Enter**.
2. **Go to your project folder.** This makes one in Documents and goes into it:

    ```
    mkdir $HOME\Documents\my-first-ai-plc-run; cd $HOME\Documents\my-first-ai-plc-run
    ```

3. **Install.** Paste this and press **Enter**:

    ```
    & ([scriptblock]::Create((irm https://raw.githubusercontent.com/lasith-tekly/ai-plc/main/install.ps1))) kiro
    ```

    Replace `kiro` with `claude-code`, `codex` or `copilot` if you use one of those tools. Add `-DryRun` at the end to preview without changing anything.
4. **Check the files are there.** Type `dir -Force` and press **Enter**. You should see `.kiro` (or the folders for your tool).

### If something goes wrong

| What you see | What to do |
| --- | --- |
| `download failed` | Check your internet connection. On a work network, a firewall may block the download. Use steps 2 and 3 below instead |
| `command not found: curl` | Use steps 2 and 3 below |
| `kept (already exists)` | The folder already had that file, so it was left alone. This is safe. To replace it, add `--force` on a Mac (`-Force` on Windows) |
| Nothing seems to happen | Wait a few seconds. The download can take a moment |

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

Open your tool, then open your project folder in it (usually **File**, then **Open Folder**). If the project was already open when you copied the files, or when you ran the one-command install, close it and open it again so the tool notices them. If the agents or connections still do not show, quit the tool completely and open it again.

## Step 5: check that it loaded

**In Kiro:** in the chat panel, click the agent name in the bar at the bottom. You should see `ai-plc-orchestrator` and seven more agents whose names start with `ai-plc-`: discovery, strategy, solution, viability, reviewer, outcome and delivery. Choose `ai-plc-orchestrator`.

**In other tools:** type the start command from the table below. The assistant should reply by explaining what it will do and asking which mode you want.

If nothing appears, see [Troubleshooting](troubleshooting.md).

## Step 6: switch Autopilot off

Some tools have an **Autopilot** setting that lets the AI make changes without asking. For your first run, make sure it is **off**, so every change is shown to you first. In Kiro, find the Autopilot switch in the chat panel and turn it off.

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
