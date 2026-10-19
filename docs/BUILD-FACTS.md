# What is built and what is tested (fact sheet for the documentation)

Written 2026-10-19 from the AI-PLC build and test records. The documentation must not claim more than this.

## Built (source: this repository)
- Orchestrator plus 7 specialists: discovery, strategy, solution, viability, reviewer, outcome, delivery. Kiro has 8 agent files, including the orchestrator. The other tools run the orchestrator as the main session.
- 12 skills. Neutral names: connectors, delivery-ai-dlc, delivery-plain, delivery-scrum, gate-pack, idea-intake, market-and-customers, outcome-pack, review, solution, strategy, viability. All tools except Kiro prefix them `ai-plc-`.
- One profile: `profiles/ai-plc-v1.0.profile.yaml`. Templates in `templates/`.
- Run modes `--ideation`, `--planning`, `--outcomes`, `--full`. Adapters `scrum`, `ai-dlc`, `plain-markdown`. Two checkpoints, two gates.
- State files in the project's `/product` folder: `plan.md`, `status.md`, `memory.md`, `/inputs`, `/exports`.
- Connectors skill: read sources into snapshots, export after an approved dry run, create only (update rule written, untested), never delete.
- Package builder: `build/build_packages.py` makes folders for Kiro, Claude Code (plugin and drop-in), Codex and Copilot.

## Tested
- Kiro: full run on a dummy idea through phases 1 to 4, the Outcome Pack and all three adapters. Atlassian connection, read, Jira export and Confluence export on a personal test site.
- Claude Code: plugin validates. Run live through Checkpoint 1 on an earlier build.
- Codex: run live through Gate 1 on an earlier build.

## Not tested
- GitHub Copilot (experimental). Notion connection. Listing pages. Updating existing items. Word and Excel import and export. The second full run with a change of direction (pending).

## Tool pages in the docs should say
Kiro: tested. Claude Code and Codex: partly tested on earlier builds. Copilot: not tested. Do not write "supported, tested" for any tool beyond this.

## Source of truth
`RELEASE-NOTES-v1.0.md` and `docs/MCP-SETUP.md` in the release. Update this sheet whenever they change.
