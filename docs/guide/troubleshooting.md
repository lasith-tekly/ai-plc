# Troubleshooting

| Problem | What to try |
| --- | --- |
| Agents or `/ai-plc` do not show up | Check you copied the right folder for your tool to the project root, then reopen the project |
| Orchestrator does not find the profile or templates | Confirm the whole package folder was copied, not part of it |
| A source page could not be read | The research agents never work around blocked pages. It is recorded as "not confirmed". Download the file and name it in the plan |
| Connected tool will not sign in | See [Connectors](../MCP-SETUP.md). Use a private browser window if you have several accounts |
| A figure looks wrong | Open its source link. Ask the orchestrator to send it back to the owning agent |
| Jira shows a reporter or priority you did not set | The tool sets these defaults. The dry run and the export log note it |
| Confluence page is not where you expected | If the space home page is the space root, the page is placed under it |
| AI-DLC package-card label differs from the answer to an open question | Known issue. Review it |
| AI-DLC version differs from 2.5.67 | The adapter was tested with 2.5.67. See [Run modes](run-modes.md) |

Known issues for each release are in the [release notes](https://github.com/lasith-tekly/ai-plc/blob/main/RELEASE-NOTES-v1.0.md).
