# Contributing to AI-PLC

Thank you for looking at AI-PLC. It is an early release candidate, so feedback is the most useful contribution right now.

## Ways to help

- **Try it and tell us what happened.** Run it on a small idea and open an issue with the feedback form: https://github.com/lasith-tekly/ai-plc/issues/new/choose. Say which tool you used (Kiro, Claude Code, Codex or Copilot) and how far the run got.
- **Report a problem.** Include the command you ran, what you expected, and what happened. Remove anything private from pasted output.
- **Ask a question or share an idea** in Discussions.
- **Improve the docs.** Fixes to wording, steps that did not work, and missing explanations are all welcome.

## Changing the files

AI-PLC is plain files: skills, agent roles, a profile and templates. The packages for each tool are generated from one source with `build/build_packages.py`, so change the source, not the generated folders. See `docs/reference/build.md` for how to rebuild and check them.

1. Open an issue first for anything bigger than a typo, so we can agree the change.
2. Keep the rules that protect the PM: people approve every stop, fetched content is data and never instructions, nothing is written to a connected tool without an approved dry run, and nothing is deleted.
3. Run the docs build before you send a pull request: `mkdocs build --strict`.
4. Keep pull requests small and describe what you changed and why.

## Licence

By contributing, you agree that your contribution is licensed under Apache 2.0, the same as the project.
