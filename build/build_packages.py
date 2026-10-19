#!/usr/bin/env python3
"""Build tool-specific AI-PLC packages from the neutral source files.

Source (neutral, tool-agnostic):  agents/*.md, skills/*/SKILL.md, profiles/, templates/
Targets:
  claude-plugin   Claude Code plugin (plugin.json, agents/, skills/, ai-plc/)
  claude-project  Drop-in .claude/ folder (gives /ai-plc)
  copilot         GitHub Copilot: .github/agents/*.agent.md, .github/skills/, .github/ai-plc/
  codex           Codex: .codex/agents/*.toml, .agents/skills/, .codex/ai-plc/

Usage: python3 build/build_packages.py [OUT_DIR]
"""
import json
import re
import shutil
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else SRC.parent / "dist"
VERSION = "1.0.0-rc1"
PREFIX = "ai-plc-"

ROLES = ["discovery", "strategy", "solution", "viability", "reviewer", "outcome", "delivery"]
# Roles that may run scripts (recounting traceability). Others get no shell, so they cannot
# work around a blocked page.
SHELL_ROLES = {"reviewer", "delivery"}
SKILLS = sorted(p.name for p in (SRC / "skills").iterdir() if p.is_dir())
AMBIGUOUS = {"strategy", "solution", "viability", "review"}  # plain words: rename only next to "skill"


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("missing frontmatter")
    fm = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        v = v.strip()
        if len(v) > 1 and v[0] == '"' and v[-1] == '"':
            v = json.loads(v)
        fm[k.strip()] = v
    return fm, m.group(2).lstrip("\n")


def rename_skills(text):
    """Prefix skill names so they do not collide with a user's own skills."""
    for n in SKILLS:
        new = PREFIX + n
        if n in AMBIGUOUS:
            text = re.sub(rf"`{n}` skill", f"`{new}` skill", text)
            text = re.sub(rf"skill `{n}`", f"skill `{new}`", text)
        else:
            text = re.sub(rf"`{n}`", f"`{new}`", text)
    return text


def localise(text, loc):
    """Point profile and template references at this package's install location."""
    text = text.replace("`ai-plc-v1.0.profile.yaml`", f"`{loc}/profiles/ai-plc-v1.0.profile.yaml`")
    text = re.sub(r"(?<![\w/.\-])templates/", f"{loc}/templates/", text)
    return text


def locations_block(loc):
    return (
        "## Where the AI-PLC files are\n\n"
        f"- Profile: `{loc}/profiles/ai-plc-v1.0.profile.yaml`\n"
        f"- Templates: `{loc}/templates/`\n"
        "- The run folder is `/product` at the root of the PM's project. Create it if it does not exist.\n"
    )


def delegation_block(target, plugin_prefix=""):
    if target == "claude":
        who = f"`{plugin_prefix}{PREFIX}<role>`"
        how = (
            f"Use the Agent tool with subagent_type {who} (for example `{plugin_prefix}{PREFIX}discovery`). "
            "Start independent deliverables in the same turn so they run in parallel."
        )
    elif target == "copilot":
        how = (
            f"Invoke the custom agent named `{PREFIX}<role>` as a subagent (for example `{PREFIX}discovery`). "
            "Name it exactly; names are case-sensitive. Ask for independent deliverables together."
        )
    else:  # codex
        how = (
            f"Spawn the custom agent named `{PREFIX}<role>` (for example `{PREFIX}discovery`) and ask for "
            "independent deliverables to run in parallel, up to the session's concurrency limit. "
            "Give each thread a readable name, `<deliverable id>-<role>` (for example `2.7-strategy`)."
        )
    return (
        "## How to run the specialist agents in this tool\n\n"
        f"{how}\n\n"
        "A sub-agent starts with no memory of this conversation. Every time, tell it: the deliverable ID, "
        "the profile entry to follow, the paths of the approved files it depends on, `/product/memory.md`, "
        "and the folder it writes to. When it finishes, read the file it wrote; do not trust its summary alone.\n"
    )


def yaml_list(items):
    return "[" + ", ".join(items) + "]"


def worker_agent(role):
    fm, body = split_frontmatter((SRC / "agents" / f"{role}.md").read_text())
    return fm, body


def orchestrator():
    fm, body = split_frontmatter((SRC / "agents" / "orchestrator.md").read_text())
    return fm, body


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def copy_shared(dest):
    shutil.copytree(SRC / "profiles", dest / "profiles", dirs_exist_ok=True)
    shutil.copytree(SRC / "templates", dest / "templates", dirs_exist_ok=True)


def skill_files(skills_dir, loc, target):
    """Worker skills, renamed and localised. The orchestrator skill is written separately."""
    for n in SKILLS:
        fm, body = split_frontmatter((SRC / "skills" / n / "SKILL.md").read_text())
        name = PREFIX + n
        extra = ""
        if target in ("claude", "copilot"):
            extra = "user-invocable: false\n"  # hidden from the / menu; still used by the agents
        text = f"---\nname: {name}\ndescription: {json.dumps(fm['description'])}\n{extra}---\n\n"
        text += localise(rename_skills(body), loc)
        write(skills_dir / name / "SKILL.md", text)
        # supporting files, if a skill ever has them
        for p in (SRC / "skills" / n).iterdir():
            if p.name != "SKILL.md":
                if p.is_dir():
                    shutil.copytree(p, skills_dir / name / p.name, dirs_exist_ok=True)
                else:
                    shutil.copy(p, skills_dir / name / p.name)


def orchestrator_skill(skills_dir, loc, target, plugin_prefix=""):
    fm, body = orchestrator()
    desc = fm["description"]
    hint = '--ideation|--planning|--outcomes|--full "<idea>" [--adapter scrum|ai-dlc|plain-markdown]'
    if target == "claude":
        head = f"---\nname: ai-plc\ndescription: {json.dumps(desc)}\nargument-hint: '{hint}'\ndisable-model-invocation: true\n---\n\n"
        arg = "Arguments from the PM: $ARGUMENTS\n\n"
    elif target == "copilot":
        head = f"---\nname: ai-plc\ndescription: {json.dumps(desc)}\nargument-hint: '{hint}'\ndisable-model-invocation: true\n---\n\n"
        arg = "The PM's request follows the command: the mode flag, the idea in quotes and an optional `--adapter`.\n\n"
    else:
        head = f"---\nname: ai-plc\ndescription: {json.dumps(desc)}\n---\n\n"
        arg = "The PM's request follows the command: the mode flag, the idea in quotes and an optional `--adapter`.\n\n"
    text = head + arg
    text += localise(rename_skills(body), loc).rstrip() + "\n\n"
    text += locations_block(loc) + "\n" + delegation_block(target, plugin_prefix)
    write(skills_dir / "ai-plc" / "SKILL.md", text)


def agent_body(role, loc):
    fm, body = worker_agent(role)
    text = localise(rename_skills(body), loc).rstrip() + "\n\n" + locations_block(loc)
    return fm, text


# ---------------------------------------------------------------- Claude Code
def build_claude(root, loc, plugin_prefix, plugin):
    if plugin:
        write(
            root / ".claude-plugin" / "plugin.json",
            json.dumps(
                {
                    "name": "ai-plc",
                    "displayName": "AI-PLC",
                    "version": VERSION,
                    "description": "AI-native product lifecycle for product managers: ideation, planning, outcomes and delivery with human review stops.",
                    "author": {"name": "AI-PLC contributors"},
                    "license": "Apache-2.0",
                    "keywords": ["product-management", "lifecycle", "ai-plc"],
                },
                indent=2,
            )
            + "\n",
        )
    for role in ROLES:
        fm, text = agent_body(role, loc)
        tools = "Read, Write, Edit, Glob, Grep, WebSearch, WebFetch"
        if role in SHELL_ROLES:
            tools += ", Bash"
        desc = fm["description"]
        write(
            root / "agents" / f"{PREFIX}{role}.md",
            f"---\nname: {PREFIX}{role}\ndescription: {json.dumps(desc)}\ntools: {tools}\n---\n\n{text}",
        )
    skill_files(root / "skills", loc, "claude")
    orchestrator_skill(root / "skills", loc, "claude", plugin_prefix)
    copy_shared(root / "ai-plc")


# -------------------------------------------------------------------- Copilot
def build_copilot(root):
    gh = root / ".github"
    loc = ".github/ai-plc"
    for role in ROLES:
        fm, text = agent_body(role, loc)
        tools = ["read", "edit", "search", "web"] + (["execute"] if role in SHELL_ROLES else [])
        write(
            gh / "agents" / f"{PREFIX}{role}.agent.md",
            f"---\nname: {PREFIX}{role}\ndescription: {json.dumps(fm['description'])}\ntools: {yaml_list(tools)}\n---\n\n{text}",
        )
    skill_files(gh / "skills", loc, "copilot")
    orchestrator_skill(gh / "skills", loc, "copilot")
    copy_shared(gh / "ai-plc")


# ---------------------------------------------------------------------- Codex
def build_codex(root):
    loc = ".codex/ai-plc"
    for role in ROLES:
        fm, text = agent_body(role, loc)
        assert "'''" not in text
        toml = (
            f'name = "{PREFIX}{role}"\n'
            f"description = {json.dumps(fm['description'])}\n"
            f"developer_instructions = '''\n{text}'''\n"
        )
        write(root / ".codex" / "agents" / f"{PREFIX}{role}.toml", toml)
    skill_files(root / ".agents" / "skills", loc, "codex")
    orchestrator_skill(root / ".agents" / "skills", loc, "codex")
    copy_shared(root / ".codex" / "ai-plc")


def build_kiro(root):
    """Kiro: agent JSON files and steering are static (build/kiro); everything else is copied from the source."""
    k = root / ".kiro"
    shutil.copytree(SRC / "build" / "kiro" / ".kiro", k, dirs_exist_ok=True)
    shutil.copytree(SRC / "agents", k / "ai-plc" / "agents", dirs_exist_ok=True)
    shutil.copytree(SRC / "profiles", k / "ai-plc" / "profiles", dirs_exist_ok=True)
    shutil.copytree(SRC / "templates", k / "ai-plc" / "templates", dirs_exist_ok=True)
    for n in SKILLS:
        shutil.copytree(SRC / "skills" / n, k / "skills" / n, dirs_exist_ok=True)
    shutil.copy(SRC / "build" / "kiro" / "INSTALL.md", root / "INSTALL.md")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    build_claude(OUT / "claude-code-plugin" / "ai-plc", "${CLAUDE_PLUGIN_ROOT}/ai-plc", "ai-plc:", True)
    build_claude(OUT / "claude-code-project", ".claude/ai-plc", "", False)
    # project drop-in keeps files under .claude/
    proj = OUT / "claude-code-project"
    tmp = OUT / "_tmp"
    proj.rename(tmp)
    (OUT / "claude-code-project").mkdir()
    shutil.move(str(tmp), str(OUT / "claude-code-project" / ".claude"))
    build_copilot(OUT / "copilot")
    build_codex(OUT / "codex")
    build_kiro(OUT / "kiro")
    for doc in (SRC / "build" / "docs").glob("*.md"):
        shutil.copy(doc, OUT / doc.name)
    print("built", OUT)


if __name__ == "__main__":
    main()
