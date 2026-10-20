"""Generate AI-PLC reference pages from the neutral source. Usage: gen_reference.py SRC OUT_DOCS"""
import sys, re, pathlib, yaml
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
(out/"reference").mkdir(parents=True, exist_ok=True)

def fm(path):
    t = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    return yaml.safe_load(m.group(1)) if m else {}

# agents
rows = []
for f in sorted((src/"agents").glob("*.md")):
    d = fm(f); rows.append((d["name"], d["description"]))
order = ["orchestrator","discovery","strategy","solution","viability","reviewer","outcome","delivery"]
rows.sort(key=lambda r: order.index(r[0].replace("ai-plc-","")))
s = "# Agents (generated)\n\n!!! note\n    This page is generated from `agents/*.md` in the source. Do not edit it by hand.\n\n| Agent | What it does |\n| --- | --- |\n"
for n,d in rows: s += f"| `{n}` | {d} |\n"
(out/"reference/agents.md").write_text(s)

# skills
s = "# Skills (generated)\n\n!!! note\n    This page is generated from `skills/*/SKILL.md`. Do not edit it by hand.\n\n| Skill | Use it when |\n| --- | --- |\n"
for f in sorted((src/"skills").glob("*/SKILL.md")):
    d = fm(f); s += f"| `{d['name']}` | {d['description']} |\n"
(out/"reference/skills.md").write_text(s)

# templates
s = "# Templates (generated)\n\n!!! note\n    This page lists the files in `templates/`. Do not edit it by hand.\n\n| Template | First heading |\n| --- | --- |\n"
for f in sorted((src/"templates").glob("*.md")):
    h = next((l[2:].strip() for l in f.read_text().splitlines() if l.startswith("# ")), "")
    s += f"| `{f.name}` | {h} |\n"
(out/"reference/templates.md").write_text(s)

# profile
p = yaml.safe_load((src/"profiles/ai-plc-v1.0.profile.yaml").read_text())
s = "# Deliverables (generated)\n\n!!! note\n    Generated from `profiles/ai-plc-v1.0.profile.yaml`. Do not edit by hand.\n\n"
s += "Modes: **auto** the tool drafts from the conversation and research. **assist** the tool drafts but you supply inputs or evidence. **human** people outside the tool are needed; the tool gives a template and tracks status.\n\n"
def table(items):
    t = "| ID | Deliverable | Mode | Depends on |\n| --- | --- | --- | --- |\n"
    for i in items:
        dep = ", ".join(i["depends_on"]) or "none"
        extra = f" (feeds {i['feeds'].replace('_',' ')})" if i.get("feeds") else ""
        t += f"| {i['id']} | {i['title']}{extra} | {i['mode']} | {dep} |\n"
    return t + "\n"
for ph in p["phases"]:
    s += f"## Phase {ph['id']}: {ph['name']} ({ph['scope'].title()} stage)\n\n" + table(ph["deliverables"])
s += "## Outcome Definition (after Gate 2)\n\n" + table(p["outcome_definition"]["deliverables"])
for k,v in p["delivery"].items():
    if isinstance(v, list): s += f"## Delivery, `{k}` adapter (`--full` only)\n\n" + table(v)
(out/"reference/deliverables.md").write_text(s)
print("ok")
