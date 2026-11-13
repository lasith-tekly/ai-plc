# Roadmap

## Where AI-PLC is today
Stage 1 (Product Ideation) and Stage 2 (Product Planning) are automated. Stage 3 (Product Development) is a handover: AI-PLC produces outcomes and delivery material, and your team builds. Stage 4 (Product Launching and Sunsetting) is not built. See [The product lifecycle](guide/lifecycle.md).

## Before v1.0 is published
- Second full run on a real idea, including a change of direction.
- Fixes from that run, then the version moves from release candidate to 1.0.0.

## Untested and to be confirmed
- The Notion connection, listing pages, updating items AI-PLC created, and Word and Excel import and export.
- GitHub Copilot (experimental).

## After v1.0

The order below is a plan, not a promise. Each step uses what the one before it teaches.

1. **Real users first.** Ask product managers to run AI-PLC on a real idea and say what broke or confused them. Their feedback shapes everything after this. Open an [issue](https://github.com/lasith-tekly/ai-plc/issues/new/choose) if you try it.
2. **Easier to adopt.** One-command install is in place for Kiro, Claude Code, Codex and Copilot, with a Claude Code marketplace entry. Next: confirm the Windows install, add a short demo and a browsable sample run, and a Kiro power if testing shows the agents load from it. A **read-only local server** that lets other tools read the `/product` files is also proposed (`proposals/mcp-3-server.md`). Not built.
3. **Close the loop on outcomes.** Today AI-PLC stops at a handover. The next step is bringing actual results back after delivery and comparing them with the outcome targets, so the next round of planning starts from evidence.
4. **Stage 4: Product Launching and Sunsetting.** Bringing the same approach (agents draft, people decide) to release, operation and retirement. Not designed yet, and it starts only once Stages 1 and 2 are in real use.
