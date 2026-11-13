# Install in GitHub Copilot (experimental)

Copilot support is experimental and has not been run. It was checked against the file formats in Copilot's documentation. Please try it on a test idea and tell us what happens.

## Way 1: one command

Open a terminal in your project folder and follow [Install with one command](install-one-command.md), using `copilot`. This copies a `.github` folder and a `.vscode` folder into the project.

## Way 2: manual

Download, unzip and copy the `.github` folder. See [Manual install](install-manual.md).

## Before your first run

Open Copilot in **Agent mode**, open **Configure Tools** and make sure **Run Subagent** is switched on. If it is off, the orchestrator cannot start the specialists.

Then close and reopen the project, and start with:

```
/ai-plc --ideation "<your idea>"
```

If nothing appears, see [Troubleshooting](troubleshooting.md). Go to [Choose a run mode](run-modes.md).
