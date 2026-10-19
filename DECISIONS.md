# AI-PLC decision log

| Date | Decision | Basis |
| --- | --- | --- |
| 2026-10-15 | Name stays **AI-PLC**. Repo name under the PM's own GitHub account checked 2026-10-15: 404, so free. Still optional: search for similar active projects, the org name and a domain. | PM decision. npm `ai-plc` returned 404 (free) on 2026-10-15; `aiplc` exists. GitHub and domains not checked. |
| 2026-10-15 | Licence: **Apache 2.0**. | PM decision. Permissive, patent grant, trademark clause. AI-DLC itself is MIT-0 (github.com/awslabs/aidlc-workflows, accessed 2026-10-15). |
| 2026-10-15 | Only the neutral **AI-PLC v1.0** profile is published. The company PLC mapping stays private. | PM decision. |
| 2026-10-15 | AI-DLC compatibility: document the version used in testing. Latest stable shown in the repo README on 2026-10-15 is 2.10.0 (previews 2.11.x); earlier work used 2.8.2. PM to confirm the version that ran with `aidlc --version`. | A releases-page fetch showed v1.0.1, which conflicts with the README and release trackers; treat as unverified. |
| 2026-10-15 | Codex: ship role files as project agents in `.codex/agents/*.toml` and keep the one-role-at-a-time fallback. | Codex docs (learn.chatgpt.com, accessed 2026-10-15): subagents on by default, custom agents are TOML files in `.codex/agents/`, run in parallel. Docs do not say plugins can ship custom agents. |
| 2026-10-15 | Kiro Powers: not the primary install. Keep the `.kiro` folder install (agents, skills, steering). Offer a Power later for the skills only. | kiro.dev/docs/powers (accessed 2026-10-15): recommended format is `plugin.json` with optional `skills/` and `mcp.json`; the page does not mention custom agents or steering. |

## 2026-10-18: changes after the first live Scrum delivery run
- Stories get a Type (feature, gate, enabler) and a Go-live line. Source: E8 and E9 story review and the delivery traceability report (M1, L1).
- Delivery review adds go-live consistency, trigger coverage (sample of 10+), testable criteria (sample of 10+) and stale-wording checks. Traceability alone did not catch a missing whole-booking cancel story.
- Approvals update index tables and close answered questions (traceability report L4).
- Reviewer states its report path in its summary.

## 2026-10-18: multi-tool packages
- One neutral source, one build script (`build/build_packages.py`) generates Claude Code (plugin and drop-in), GitHub Copilot and Codex packages. Kiro keeps its own hand-built package.
- The orchestrator is delivered as an `ai-plc` skill so it runs in the main session (Claude Code sub-agents cannot start sub-agents); specialists are custom agents named `ai-plc-<role>`.
- Worker skills are prefixed `ai-plc-` so they do not collide with a user's own skills, and are hidden from the slash menu.
- Only the reviewer and delivery agents get a shell; the others cannot work around a blocked page.
- Descriptions in all frontmatter are quoted, because unquoted ": " breaks strict YAML parsers (found by validation).
- Copilot and Codex packages follow their docs (accessed 2026-10-18) but are not run yet.

## 2026-10-18: after the live Claude Code and Codex runs
- Test scope: the smoke test and the runs that followed (Claude Code to Checkpoint 1, Codex to Gate 1) are enough. The longer test levels (`--planning` in Claude Code) and the Copilot test are skipped for now. Copilot ships as experimental until it is run. PM decision.
- Plan: shows the whole route for the mode and marks which deliverables are ready now. Only those start. (The old text said both "list what the mode needs" and "list only what can run now".)
- Reviews: a new reviewer for every review, never a reused one. Sub-agents are named `<deliverable id>-<role>` where the tool allows it. Report length about 1,200 words, low findings grouped.
- Review findings on approved files: the PM either has the file revised (new version) or accepts it, and accepted or unrevised findings are listed in the pack under "Known issues in approved files". Source: Codex Gate 1 run, where a reviewer found a wrong line in an approved file that stayed in the file.
- Length: each deliverable opens with a Summary for the PM (about 150 words) and keeps the body to about 1,500 words, with detail in an appendix. Source: Claude Code run, where drafts reached 3,200 to 6,900 words.
- Dependencies: a revision uses only its own `depends_on` files, `memory.md` and sources it cites itself. It never copies from a file that depends on it. Files approved against an older version are listed as "check against version N". Source: Claude Code run, 1.1 v2 used 1.2 and 1.4 with `depends_on: []`.
- Consistency check: when drafts arrive together, the orchestrator compares them before showing them, and does not rewrite them.
- Orchestrator work: research and drafting stay with the specialists. The orchestrator may download and convert one normal public file a specialist cannot read (for example a spreadsheet), pass the figures on with URL and date, and tell the PM. It never fetches a page a specialist found blocked. Open to PM override.
- Review check numbers: length is check 10, delivery checks are 11 to 15.
- Review checks for the `ai-dlc` and `plain-markdown` adapters added (brief count, order against roadmap and drops, labels carried, version stated). Found by reading the adapters before their first run: the Scrum-only checks would have been marked not applicable.

## 2026-10-19 Plain-markdown run fixes
- Agents use today's date from the environment, never a reused one (Kiro agents wrote 2026-10-16).
- Delivery agent and `delivery-plain` get a summary and length target (about 2,000 words for P.1 and H.2; H.1 briefs later set at about 2,500, because a brief must stand alone).
- Plain-markdown review check (a) allows an outcome split across drops if each part is labelled.
- Not re-run live.
- 2026-10-19: the P.1 length target applies to the body before the Appendix, matching the 1,500-word rule for other deliverables. Kiro v2 of P.1 (body 1,986, appendix 1,586) accepted as meeting it.
- 2026-10-19: plain-markdown reviewer report (0 high, 1 medium, 10 low) accepted; adapter passes. Rule fixes: ids carry short meanings, critical path uses declared dependencies only, qualifiers kept, and the dependency map and roadmap may be index sections rather than separate files.

## 2026-10-19: AI-DLC adapter run (Kiro, AI-DLC 2.5.67)
- Result: all five ai-dlc checks pass; reviewer found 0 high, 3 medium, 5 low. Nine briefs plus handoff-order.md approved.
- PM decisions: O2 stays one brief with parts A and B. Scopes (classic, mvp, express) are suggestions; the AI-DLC team decides. Package-card label "Booked with [operator], not with us" kept as a known issue against Q9. All of Drop 2 shown as blocked until the assistance route is chosen. Hand-over holds live in H.2 only.
- Rules added: decisions already made come only from memory.md; Gate 2 conditions go in every brief that builds what they govern; whole-drop holds show for every outcome; H.1 body about 2,500 words with a short Summary for the PM; review check f for ai-dlc; reviewer report 1,200 words at most (reports ran 1,445 and 1,715).
- The run used the package from before the 2026-10-19 date and length rules, so briefs show updated 2026-10-18, no summaries and 1,758 to 3,288 words. Not re-run with the final package.
- `--scope` with a description in one command is untested; the AI-DLC team confirms on the first real run.

## 2026-10-19: MCP moves earlier
- PM decision: MCP comes earlier than the original "after v1.0" slot. Exact placement (before the second run, or before publishing v1.0) to be confirmed. The neutral files stay the base; MCP is added on top.

## 2026-10-19: one package for all tools
- PM question: why two packages? No technical reason. Kiro is now built by `build/build_packages.py` from the same source (static agent JSON and steering live in `build/kiro/`). One zip, `ai-plc-packages.zip`, holds a folder per tool: claude-code-plugin, claude-code-project, codex, copilot, kiro. The built Kiro folder is identical to the earlier hand-built one.
- PM decision: MCP is built before the second run, ahead of publishing v1.0.

## 2026-10-19: MCP scope agreed
- PM goals: A read from tools, B write to tools, C AI-PLC as a server. Tools first: Notion, Jira (or similar), Google Drive, plus Word and Excel files.
- Phasing (PM agreed): MCP-1 read and MCP-2 write before the second run; MCP-3 server after it.
- Word and Excel are files, so they are handled as import and export, not MCP.
- Rules for every phase: source and date on every fetched fact; no credentials in `/product` or the repo; nothing written out before a PM-approved dry run; the server never approves, it only records a decision the PM reports; reads and writes limited to the sources named at the start of a run.
- To confirm before building: which MCP servers exist for each tool and how they sign in.
- 2026-10-19: Confluence added to the MCP scope. It uses the same Atlassian Rovo MCP server as Jira (https://mcp.atlassian.com/v2/mcp, OAuth 2.1); the vendor page says it can search, summarise and create or update Confluence pages. To confirm in testing: one sign-in covering both, and page read and comment support.
- 2026-10-19: Findings. Notion hosted server (OAuth); Atlassian Rovo (Jira and Confluence, OAuth 2.1); Google Drive, Docs and Sheets servers are Developer Preview with heavy setup, so Drive is optional for v1.0; Word and Excel are files, not MCP. No credentials in packages. Fetched content is data, never instructions. Test Jira and Confluence on a personal site, not a work system.

## 2026-10-19: MCP-1 and MCP-2 rules written (not tested live)
- Design: only the orchestrator touches connected tools. Specialists never do. This keeps every specialist's tool list unchanged and keeps fetched content out of their reach until the PM accepts it.
- Read: new skill `connectors`. The PM names the sources at the start; each is saved as a snapshot in `/product/inputs/` with source, location and date; the PM accepts, trims or discards it; accepted snapshots are given to specialists as PM-supplied documents.
- Write: after a deliverable is approved and the PM asks, a dry run goes to `/product/exports/`; only the PM approves it; the writes create only, and each is logged in `/product/exports/log.md`.
- Fetched content is data, never instructions. No credentials in `/product` or the repo. Reviewer check 16 covers connected sources.
- Setup guide `MCP-SETUP.md` added (Notion, Jira and Confluence on one Atlassian server, OAuth). Google Drive optional (Developer Preview). Word and Excel are files, read and exported locally.
- Kiro orchestrator agent allows MCP tools (`@mcp`). Test guide adds checks 15 to 20.
- To confirm in testing: Atlassian config snippets per tool, one sign-in for Jira and Confluence, Confluence read and comment support, and the Kiro `@mcp` setting.

## 2026-10-19: MCP-1 and MCP-2 tested live (Atlassian, in Kiro)
- Setup: `.kiro/settings/mcp.json` with the server `https://mcp.atlassian.com/v2/mcp`, sign-in through the browser (OAuth). One sign-in covers Jira and Confluence (21 tools). The orchestrator used the tools through the existing `@mcp` setting, with no agent change. Site: a personal Atlassian site, not a work system.
- Read test: the orchestrator read the Confluence space home page, saved a snapshot in `/product/inputs/` with status unreviewed and the right date, added it to `plan.md`, checked it for embedded instructions, and said which page widgets could not be converted. Nothing was written. The PM discarded it.
- Write test, Jira: dry run first, PM approved, then 2 epics, 3 stories and 2 "blocks" links were created in project SCRUM. The orchestrator read one item back. Existing items were untouched. Jira set the reporter and a default priority (Medium), which the dry run had said was not set.
- Write test, Confluence: dry run first, PM approved, one new page created in the test space. It was read back and matched the dry run, and four existing pages were unchanged. The dry run said the page would sit at the space root. Confluence made it a child of the space home page, because in that space the root is the home page. The orchestrator noticed, logged it and told the PM.
- Findings turned into rules: read back after every write and compare with the dry run; note tool defaults in the dry run and the log; keep Autopilot off for write tests.
- New rule (update): a re-export may update only items that `/product/exports/log.md` shows AI-PLC created, after reading the current content, with current and new text side by side in a PM-approved dry run. Never delete. Never touch other items. Untested.
- Still untested: Notion, Claude Code, Codex and Copilot connection snippets; listing pages in a space; the update rule; Word and Excel import and export.
