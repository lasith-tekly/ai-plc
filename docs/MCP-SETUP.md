# 8. Connecting AI-PLC to Notion, Jira, Confluence and Miro (MCP)

AI-PLC can read the sources you name at the start of a run, and send approved results back after you approve a dry run. It uses MCP servers that you connect yourself. Nothing here ships with credentials.

**Status.** Tested live on 2026-10-19 in Kiro with a personal Atlassian site: the Atlassian server connected through one sign-in, read a Confluence page, created Jira epics, stories and links, and created a Confluence page, all through a PM-approved dry run. Notion, Miro, and the Claude Code, Codex and Copilot connections, are written from each vendor's documentation and are not yet tested. Treat those as "to confirm in your first test".

## Before you connect

- Check your organisation's policy and ask your admin before connecting AI-PLC to company systems. An admin may need to enable the connection. Test first on a personal or sandbox site.
- The server acts with your own permissions. Use a test project or space, not real work, for the first run.
- Never put a password, token or key in `/product`, in a repo or in a chat. Sign in through the tool's own sign-in window. Where a config needs a secret, use an environment variable reference and keep the file out of version control.
- Content read from a tool is treated as data. Agents never follow instructions found inside it.

## What each source needs

| Source | Server address | Sign-in | Notes |
| --- | --- | --- | --- |
| Notion | `https://mcp.notion.com/mcp` | OAuth in your tool | Read and update pages and databases you can access |
| Jira and Confluence | `https://mcp.atlassian.com/v2/mcp` | OAuth 2.1 in your tool. A personal API token works only if your admin enables it | One server for both. Some tools use Rovo credits |
| Miro | `https://mcp.miro.com/` | OAuth in your tool. You authorise one Miro team, and it works only on boards of that team | Read a board you name. After a dry run, export the dependency maps, the roadmap and the handoff order as native diagrams on a new board. Create only: it never changes or deletes what is already on a board. Your admin may need to approve the app |
| Google Drive, Docs, Sheets | Google's Workspace MCP servers | OAuth 2.0 with your own Google Cloud project | Developer Preview only. Optional in v1.0. Download the files instead |
| Word and Excel | None | None | They are files. Put them in the project folder and name them in the plan |

## Already set up for you

The package includes the connection list for Notion, Atlassian (Jira and Confluence) and Miro, so you do not edit any files. It holds the server addresses only. It holds no password, token or key, and nothing is connected until you sign in.

| Tool | Where it appears | What you do |
| --- | --- | --- |
| Kiro | **MCP Servers** panel | Click the server, choose to connect, sign in in the browser window |
| Claude Code | `/mcp` | Run `/mcp`, pick the server, sign in |
| Codex | `codex mcp login notion` or `atlassian` | Run it once and sign in (also `miro`) |
| GitHub Copilot in VS Code | **MCP: List Servers** in the Command Palette | Start the server and sign in |

One sign-in covers both Jira and Confluence (21 tools). The AI-PLC orchestrator already allows MCP tools. Confirmed in Kiro with Atlassian: the server shows under **MCP Servers**, and a browser window opens for the sign-in. Use a private window if you have several accounts, and allow only the site you mean to use. For Miro, choose the one team whose boards you mean to use, and start with a test board.

If your project already has its own MCP file, merge the two instead of replacing it. The files are `.kiro/settings/mcp.json` (Kiro), `.mcp.json` (Claude Code), `.vscode/mcp.json` (Copilot) and `.codex/config.toml` (Codex). Codex reads the project file only for a project you have marked as trusted.

Don't need a source? Leave it unconnected. AI-PLC carries on with the others.

Keep **Autopilot off** while you try writes, so every tool prompt is shown to you. If you cannot create the file by hand, paste the content into Kiro's chat and ask it to create `.kiro/settings/mcp.json`.

Only the AI-PLC orchestrator uses these connections. The specialist agents read files the orchestrator saves in `/product/inputs/`.

## How a run uses them

1. At the start, say which sources to read (for example "the Confluence space AI-PLC Test and this Excel file"). The orchestrator lists them in `plan.md` under Connected sources.
2. It saves each one as a snapshot in `/product/inputs/` with its source, location and date. You accept, trim or discard each one before the specialists see it.
3. After a deliverable is approved, you can ask for an export. The orchestrator first writes a dry run in `/product/exports/` showing exactly what would be created in Notion, Confluence, Jira or Miro, or in a Word or Excel file.
4. You approve the dry run. Only then does it write. It reads back what it created, compares it with the dry run and logs each result in `/product/exports/log.md`. It never deletes.
5. To re-export after changes, it can update only the items it created earlier. The dry run shows the current and new text side by side, and you approve it first.

Things the tool decides, not AI-PLC: Jira fills in the reporter and a default priority, and Confluence places a new page under the space home page when the home page is the space root. The dry run and the log note these.

## Sending results to Confluence, Jira, Notion or Miro

AI-PLC never writes to a connected tool on its own. It writes only when all of these are true:

1. The deliverable is **approved**.
2. **You ask** for the export, in plain words.
3. The target (the space, project, page or board) is named in `plan.md` under Connected sources. If it was not named at the start, tell the orchestrator and it adds it.
4. You have **approved a dry run**. It lists exactly what would be created. After your approval it creates only, reads back what it wrote, compares it with the dry run and logs it in `/product/exports/log.md`. It never deletes, and it never changes anything it did not create.

| Where | What can go there | When it makes sense | Example request |
| --- | --- | --- | --- |
| Confluence or Notion | Any approved deliverable, as a page | After a gate, for that phase's files (for example 2.10 after Gate 1) | "Export 2.10 to the Confluence space X as a new page." |
| Jira | Epics and stories, with links | After delivery, with the `scrum` adapter. The `ai-dlc` and `plain-markdown` adapters write no epics or stories | "Export the epics and stories to Jira project X." |
| Miro | The Mermaid maps as native diagrams: outcome, requirement and story dependency maps, roadmaps, the handoff order | After the Outcome Pack is issued, or after delivery | "Export the outcome dependency map and roadmap to a new Miro board called AI-PLC test." |

Large maps are split into frames so the board stays readable. Start with a test space, project or board. Jira and Confluence are tested in Kiro. Notion and Miro are written from the vendors' documentation and are not yet tested.

## If it does not work

- The server does not appear: reopen the project or restart the tool. If the project already had its own MCP file, check that the AI-PLC entries were merged in.
- Sign-in fails: check that your admin allows the connection, and that you are not signed in to a different account in the same browser. Use a private window for a personal site.
- A tool needs credits or admin approval: report it to the PM. Do not work around it.
