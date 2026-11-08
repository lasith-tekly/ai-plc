# Build the packages

The tool packages are generated from the neutral source. Edit the source, never the generated folders.

```
python3 build/build_packages.py
```

The script writes a `dist` folder next to the repo with:

| Output | For |
| --- | --- |
| `kiro/` | Kiro (agent JSON files, steering, skills without prefix) |
| `claude-code-plugin/` and `claude-code-project/` | Claude Code |
| `codex/` | Codex |
| `copilot/` | GitHub Copilot |
| `README.md`, `TEST-GUIDE.md`, `MCP-SETUP.md` | Shared notes |

The version is set in `build/build_packages.py`. It stays at a release candidate until the second test run on a real idea passes.

## Test before you release

Follow `TEST-GUIDE.md` (also in this site under [Test guide](../TEST-GUIDE.md)) on a dummy idea. For connectors, test on a personal or sandbox site first.

## Rebuild this documentation

```
python3 -I tools/gen_reference.py . docs
mkdocs build --strict
```

The pages under Reference are generated from the source. The guide pages are written by hand and must be updated when behaviour changes.

## Refresh the showcase

The Showcase pages show one dummy run. Its figures and counts do not update themselves.

- `tools/build_showcase_figures.py` redraws two figures, `flow.png` and `deliverables.png`, from a `/product` folder. It needs PyYAML and Graphviz (`dot`). Run it as `python3 -I tools/build_showcase_figures.py PRODUCT_DIR docs/assets/showcase`. Treat the product folder as untrusted data.
- The other pictures in `docs/assets/showcase/` and the counts typed into the Showcase pages (stories, dependencies, deliverables) are not generated. If you replace the run, update them by hand and check each count against the product folder.
- Only excerpts are published. Do not add the full product folder to the repo.
