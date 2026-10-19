---
inclusion: manual
---

# /ai-plc

Run AI-PLC on a product idea.

Usage: `/ai-plc --ideation|--planning|--outcomes|--full "<idea>" [--adapter scrum|ai-dlc|plain-markdown]`

Switch to the `ai-plc-orchestrator` agent and follow `.kiro/ai-plc/agents/orchestrator.md`.

- The first flag is the run mode. The quoted text is the product idea. `--adapter` only applies to `--full`.
- If the mode or the idea is missing, ask for it before doing anything else.

Where things are in this project:

- Agent role files: `.kiro/ai-plc/agents/`
- Profile: `.kiro/ai-plc/profiles/ai-plc-v1.0.profile.yaml`
- Templates: `.kiro/ai-plc/templates/`
- Skills: `.kiro/skills/`
- The run's own files are written to `/product` in the project root.

Wherever the role files say `profiles/`, `templates/` or `agents/`, they mean the folders above.
