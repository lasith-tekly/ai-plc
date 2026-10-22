# Connecting AI-PLC to Notion, Jira and Confluence (MCP)

AI-PLC can read the sources you name at the start of a run, and send approved results back after you approve a dry run. It uses MCP servers that you connect yourself. Nothing here ships with credentials.

**Status.** Tested live on 2026-10-19 in Kiro with a personal Atlassian site: the Atlassian server connected through one sign-in, read a Confluence page, created Jira epics, stories and links, and created a Confluence page, all through a PM-approved dry run. Notion, and the Claude Code, Codex and Copilot snippets, are written from each vendor's documentation and are not yet tested. Treat those as "to confirm in your first test".

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
| Google Drive, Docs, Sheets | Google's Workspace MCP servers | OAuth 2.0 with your own Google Cloud project | Developer Preview only. Optional in v1.0. Download the files instead |
| Word and Excel | None | None | They are files. Put them in the project folder and name them in the plan |

## Already set up for you

The package includes the connection list for Notion and Atlassian (Jira and Confluence), so you do not edit any files. It holds the server addresses only. It holds no password, token or key, and nothing is connected until you sign in.

| Tool | Where it appears | What you do |
| --- | --- | --- |
| Kiro | **MCP Servers** panel | Click the server, choose to connect, sign in in the browser window |
| Claude Code | `/mcp` | Run `/mcp`, pick the server, sign in |
| Codex | `codex mcp login notion` or `atlassian` | Run it once and sign in |
| GitHub Copilot in VS Code | **MCP: List Servers** in the Command Palette | Start the server and sign in |

One sign-in covers both Jira and Confluence (21 tools). The AI-PLC orchestrator already allows MCP tools. Confirmed in Kiro with Atlassian: the server shows under **MCP Servers**, and a browser window opens for the sign-in. Use a private window if you have several accounts, and allow only the site you mean to use.

If your project already has its own MCP file, merge the two instead of replacing it. The files are `.kiro/settings/mcp.json` (Kiro), `.mcp.json` (Claude Code), `.vscode/mcp.json` (Copilot) and `.codex/config.toml` (Codex). Codex reads the project file only for a project you have marked as trusted.

Don't need a source? Leave it unconnected. AI-PLC carries on with the others.

Keep **Autopilot off** while you try writes, so every tool prompt is shown to you. If you cannot create the file by hand, paste the content into Kiro's chat and ask it to create `.kiro/settings/mcp.json`.

Only the AI-PLC orchestrator uses these connections. The specialist agents read files the orchestrator saves in `/product/inputs/`.

## How a run uses them

1. At the start, say which sources to read (for example "the Confluence space AI-PLC Test and this Excel file"). The orchestrator lists them in `plan.md` under Connected sources.
2. It saves each one as a snapshot in `/product/inputs/` with its source, location and date. You accept, trim or discard each one before the specialists see it.
3. After a deliverable is approved, you can ask for an export. The orchestrator first writes a dry run in `/product/exports/` showing exactly what would be created in Notion, Confluence or Jira, or in a Word or Excel file.
4. You approve the dry run. Only then does it write. It reads back what it created, compares it with the dry run and logs each result in `/product/exports/log.md`. It never deletes.
5. To re-export after changes, it can update only the items it created earlier. The dry run shows the current and new text side by side, and you approve it first.

Things the tool decides, not AI-PLC: Jira fills in the reporter and a default priority, and Confluence places a new page under the space home page when the home page is the space root. The dry run and the log note these.

## If it does not work

- The server does not appear: reopen the project or restart the tool. If the project already had its own MCP file, check that the AI-PLC entries were merged in.
- Sign-in fails: check that your admin allows the connection, and that you are not signed in to a different account in the same browser. Use a private window for a personal site.
- A tool needs credits or admin approval: report it to the PM. Do not work around it.
