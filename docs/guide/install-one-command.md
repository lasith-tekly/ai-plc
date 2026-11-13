# Install with one command

Instead of downloading, unzipping and copying by hand, you can paste one line into a terminal. It downloads the newest release and copies the right files into your project folder. It never overwrites a file you already have, and it never asks for your password. If anything asks for a password, stop and close the window.

If you would rather read it before you run it, the script is on [GitHub](https://github.com/lasith-tekly/ai-plc/blob/main/install.sh) and is short.

The lines below use `kiro`. Use the name for your tool instead: `kiro`, `claude-code`, `codex` or `copilot`.

## On a Mac

1. **Open the Terminal.** Press **Command + Space**, type `Terminal`, and press **Enter**. A window with a blinking cursor opens. This is where you type or paste commands.
2. **Go to your project folder.** If you made a project folder (for example `my-first-ai-plc-run` in Documents), type this and press **Enter**:

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

Then follow the page for your tool: it says how to check that the files loaded and how to start.

## On Windows

This route has not been tested on Windows yet. If it fails, use the [manual install](install-manual.md) and tell us what happened.

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

??? note "If something goes wrong"

    | What you see | What to do |
    | --- | --- |
    | `download failed` | Check your internet connection. On a work network, a firewall may block the download. Use the [manual install](install-manual.md) instead |
    | `command not found: curl` | Use the [manual install](install-manual.md) |
    | `kept (already exists)` | The folder already had that file, so it was left alone. This is safe. To replace it, add `--force` on a Mac (`-Force` on Windows) |
    | Nothing seems to happen | Wait a few seconds. The download can take a moment |
