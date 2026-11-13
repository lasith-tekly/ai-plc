# Manual install (download and copy)

This works on any computer and needs no terminal. If you are comfortable with a terminal, [one command](install-one-command.md) is quicker.

## Download and unzip

1. Download `ai-plc-packages.zip` from the [Releases page](https://github.com/lasith-tekly/ai-plc/releases). It is listed under **Assets**.
2. Double-click the zip file to unzip it (on Windows, right-click and choose **Extract All**).
3. Open the new `ai-plc-packages` folder. Inside are one folder per tool: `kiro`, `claude-code-plugin`, `claude-code-project`, `codex` and `copilot`, plus a README and some guides.

You only need the folder for the tool you use.

## Copy the files into your project folder

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

The Claude Code plugin works differently: it is installed with a command rather than copied. See [Claude Code](install-claude-code.md).

When the files are in place, follow the page for your tool to check that they loaded: [Kiro](install-kiro.md), [Claude Code](install-claude-code.md), [Codex](install-codex.md) or [GitHub Copilot](install-copilot.md).
