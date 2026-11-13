---
name: ai-plc-setup
description: Install AI-PLC into the current Kiro project. Use when the user asks to set up, install or add AI-PLC, or to get started with AI-PLC product ideation and planning.
---

# Set up AI-PLC in this project

AI-PLC is an open-source set of agents, skills and templates that takes a product idea through ideation and planning. A product manager leads it and approves every stop. This skill installs the AI-PLC files for Kiro into the current project. It does not run AI-PLC.

## Before you start

- Tell the user which folder you will install into (the current project folder) and ask them to confirm it. Suggest a new, empty test project for a first try.
- Remind them not to use confidential company material and not to connect company systems. Check their organisation's policy first.

## Steps

1. **Preview.** Run the installer in preview mode and show the user the full output. It changes nothing.
   - Mac or Linux: `curl -fsSL https://raw.githubusercontent.com/lasith-tekly/ai-plc/main/install.sh | sh -s -- kiro --dry-run`
   - Windows PowerShell: `& ([scriptblock]::Create((irm https://raw.githubusercontent.com/lasith-tekly/ai-plc/main/install.ps1))) kiro -DryRun`
   The script is public and short: https://github.com/lasith-tekly/ai-plc/blob/main/install.sh
2. **Ask for approval.** Say what will be copied (the `.kiro` folder: agents, skills, steering, templates and the connection list) and that existing files are never overwritten. Wait for a clear yes.
3. **Install.** Run the same command without the preview flag.
4. **Report.** Show the result line (for example "Done: 38 file(s) copied, 0 kept"). If files were kept because they already existed, say so.
5. **Tell the user what to do next.**
   - Close and reopen the project so Kiro loads the new agents. If they still do not show, quit Kiro completely and open it again.
   - In the chat panel, choose the agent `ai-plc-orchestrator`.
   - Switch Autopilot off for the first run, so every change is shown first.
   - Start with: `/ai-plc --ideation "<your idea>"`
   - Connections to Notion, Jira, Confluence and Miro are optional. Setup is in `MCP-SETUP.md` in the docs: https://lasith-tekly.github.io/ai-plc/

## Rules

- Never use `--force` or `-Force` unless the user asks for it and understands that existing files will be replaced.
- Never ask for, store or print passwords or tokens. The installer needs none.
- If the download fails, show the error as it appears and point the user to the manual steps: https://lasith-tekly.github.io/ai-plc/guide/install/
- Do not edit files inside `.kiro` after installing. Report problems on https://github.com/lasith-tekly/ai-plc/issues
