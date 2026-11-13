# Install in Kiro

Kiro is the easiest tool to start with and the most tested. Choose one of three ways. All three end with the same files in your project.

## Way 1: the AI-PLC power, from inside Kiro

No terminal and no download. The power asks Kiro to install AI-PLC for you, shows a preview first, and waits for your approval.

1. Open your project folder in Kiro (a new, empty folder is best for a first try).
2. In the left bar, open the **Powers** panel.
3. Under **Installed**, click **Add Custom Power**, then **Import power from GitHub**.
4. Paste this address, then click **Install**:

    ```
    https://github.com/lasith-tekly/ai-plc/tree/main/powers/ai-plc
    ```

5. Open a chat and type: `set up AI-PLC`.
6. Kiro runs a preview and shows what it would copy. Read it, then say yes.
7. Close and reopen the project so Kiro loads the new agents. If they still do not show, quit Kiro completely and open it again.

## Way 2: one command

Open the terminal in Kiro (or any terminal) in your project folder and follow [Install with one command](install-one-command.md), using `kiro`.

## Way 3: manual

Download, unzip and copy the `.kiro` folder. See [Manual install](install-manual.md).

## Check that it loaded

In the chat panel, click the agent name in the bar at the bottom. You should see `ai-plc-orchestrator` and seven more agents whose names start with `ai-plc-`: discovery, strategy, solution, viability, reviewer, outcome and delivery. Choose `ai-plc-orchestrator`.

## Before your first run

Switch **Autopilot** off. It lets the AI make changes without asking. With it off, every change is shown to you first. Find the switch in the chat panel.

Then start with:

```
/ai-plc --ideation "<your idea>"
```

Go to [Choose a run mode](run-modes.md). If nothing appears, see [Troubleshooting](troubleshooting.md).
