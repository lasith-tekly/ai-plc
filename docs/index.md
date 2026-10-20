# AI-PLC

AI-PLC is an AI-native product lifecycle for product managers. You describe an idea and run one command. AI agents draft each deliverable across the Ideation and Planning stages, from market and customer discovery to an Outcome Pack and delivery-ready stories. **You review and approve at every stop.** The AI never approves its own work.

It is plain files: markdown skills, agent roles, a YAML profile and templates that your AI coding tool loads. There is nothing to host and no service to run. Licence: Apache 2.0.

## The four stages of a product's life

AI-PLC follows a product through four stages. Version 1.0 automates the first two, then hands your team clear outcomes to build from.

| Stage | AI-PLC v1.0 |
| --- | --- |
| 1. Product Ideation | Automated |
| 2. Product Planning | Automated |
| 3. Product Development | Handed over: outcomes and delivery material for your team to build from |
| 4. Product Launching and Sunsetting | Not built yet |

See [The product lifecycle](guide/lifecycle.md).

## Where to start

- New here? Follow [Start here](guide/start-here.md): eight short steps from "what is this" to your first run.
- Want to know what it covers? See [The product lifecycle](guide/lifecycle.md) and [Deliverables](reference/deliverables.md).
- Connecting Jira, Confluence or Notion? See [Connectors](MCP-SETUP.md).

## Which tools work today

| Tool | Status in v1.0 release candidate |
| --- | --- |
| Kiro | Tested end to end: phases 1 to 4, Outcome Pack, all three adapters, and Atlassian connectors |
| Claude Code (plugin and drop-in folder) | Passes plugin validation. Run live through Checkpoint 1 on an earlier build |
| Codex | Run live through Gate 1 on an earlier build |
| GitHub Copilot | Formats checked against its documentation. Not run. Experimental |

Not yet tested: the Notion connection, updating items AI-PLC created earlier, and Word and Excel import and export. The exact list is in the [release notes](https://github.com/lasith-tekly/ai-plc/blob/main/RELEASE-NOTES-v1.0.md).
