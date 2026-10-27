# Installing AI-PLC in Kiro

## Install

1. Open (or create) the project folder where you want to run AI-PLC.
2. Copy the `.kiro` folder from this package into the project root. If the project already has a `.kiro` folder, merge them. Nothing here overwrites Kiro's own files.
3. Reopen the project in Kiro so it loads the new agents and skills.

## Check it loaded

- In the agent picker (the agent name in the bottom bar of the chat pane), you should see `ai-plc-orchestrator`, `ai-plc-discovery`, `ai-plc-strategy`, `ai-plc-solution`, `ai-plc-viability`, `ai-plc-reviewer`, `ai-plc-outcome` and `ai-plc-delivery`.
- In the steering list you should see `ai-plc`.
- In the CLI, run `/context show` and look for the AI-PLC files.

## Connect your tools (optional)

The package already lists Notion, Atlassian (Jira and Confluence) and Miro under **MCP Servers** in Kiro. Nothing is connected and nothing is signed in until you choose. To use one, click it, choose to connect and sign in in the browser window. Skip this if you do not need it. See `MCP-SETUP.md` for the safe way to try it.

## Run

1. Switch to the `ai-plc-orchestrator` agent.
2. Type `/ai-plc --ideation "<your idea>"`.
3. Answer its questions. It will write `plan.md` and wait for your go.
4. Review each deliverable as it appears in `/product`, then approve it or ask for changes.

## Tips from the first test

- Turn Autopilot off for the first run so you see each change before it is written.
- Tested in Kiro: the orchestrator agent loads with the config in this package, and discovery runs as separate sub-agents (1.2 and 1.3 in parallel).
- Check any key figure against its source link before you approve a deliverable.

## What to watch for, and tell us

- Did the agents and the `/ai-plc` command show up?
- Did the orchestrator find the profile and templates?
- Did it run discovery as a sub-agent, or do the work itself?
- Were the questions the right ones, and were there too many?
- Did the review stops feel natural?
- Anything it got wrong or ignored.

## Status

Tested live in Kiro on a dummy idea through phases 1 to 4, the Outcome Pack and all three delivery adapters (Scrum, plain-markdown, AI-DLC 2.5.67). If something does not load, the likely causes are the steering `inclusion: manual` setting, the `skill://` paths in the agent files, or the sub-agent permissions.

## Using it with AI-DLC

AI-DLC also installs under `.kiro`. Install AI-PLC in a separate test project first so the two do not get mixed up.
