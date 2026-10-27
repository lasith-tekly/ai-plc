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
s = "# Deliverables (generated)\n\n!!! note\n    Generated from `profiles/ai-plc-v1.0.profile.yaml` and the purposes in `tools/gen_reference.py`. Do not edit by hand.\n\n"
s += "Modes: **auto** the tool drafts from the conversation and research. **assist** the tool drafts but you supply inputs or evidence. **human** people outside the tool are needed; the tool gives a template and tracks status.\n\n"
PURPOSES = {
 "1.1":"The problem and the opportunity, split into known, assumed and open. Everything else builds on it.",
 "1.2":"Market size, trends, segments and competitors, with dated sources. Shows whether there is a real market.",
 "1.3":"Who the customers are, their problem, who pays and who uses it, and who to start with.",
 "1.4":"What research already exists and where it is thin. It asks you for material.",
 "2.1":"Situations where customers would use the product: who, what they do today, what success looks like.",
 "2.2":"The results the product should achieve (not features) and what is out of scope.",
 "2.3":"Compares the use cases with your company's experience or brand principles.",
 "2.4":"Suppliers, platforms and partners the product depends on or could gain from.",
 "2.5":"Onboarding, support, content and human help needed around the product.",
 "2.6":"The skills the scope needs against the skills the team has.",
 "2.7":"Ways of earning money that fit the customers and market. It compares; you choose.",
 "2.8":"The nine canvas blocks, each marked known, assumed or open.",
 "2.9":"Two or three sentences, what the product is not, and two wordings to choose from.",
 "2.10":"The Gate 1 pack. It argues for or against investing in the next phase.",
 "3.1":"What the product needs to do, ranked against criteria stated up front.",
 "3.2":"How similar products solve it, the proposed experience as steps, and design questions to test.",
 "3.3":"A test plan and capture template. It waits for your real results.",
 "3.4":"Who it is for, how it differs from the alternatives, and messages per customer group.",
 "3.5":"How to test with real customers: who, where, how long, and success and stop signals.",
 "3.6":"The smallest set of capabilities that delivers the in-scope outcomes: what is in, out and untested.",
 "4.1":"A list of what needs checking and by whom. The findings come from you.",
 "4.2":"Risks with likelihood and impact, warning signs and responses.",
 "4.3":"Whether the MVP can be built with the known team, skills, partners and time. No estimates of its own.",
 "4.4":"Whether it makes sense as a business, with the strongest reasons for and against.",
 "4.5":"Whether the market is attractive and reachable, with evidence for and against.",
 "4.6":"How each outcome will be measured once the product exists.",
 "4.7":"Value to the customer and the business, split into evidenced, assumed and unknown.",
 "4.8":"Options for how to charge, the evidence for each, and what to test in the pilot.",
 "4.9":"Which services are needed at launch, who runs them, and what is missing.",
 "4.10":"The Gate 2 pack. It updates 2.10 and says what changed since Gate 1.",
 "O.n":"One file per measurable result, with its evidence, limits and risks. The main handover to delivery.",
 "O.M":"Which outcomes must come first (hard) and which would only help (soft).",
 "O.R":"The order of outcomes in drops.",
 "O.I":"The index of the Outcome Pack: counts, order and known issues.",
 "D.1":"What the product must do to deliver each outcome.",
 "D.2":"Which requirements depend on which.",
 "D.3":"Groups of requirements that can be built and released together.",
 "D.4":"The stories a team can pick up, each traced to a requirement and an outcome.",
 "D.5":"Which stories depend on which, and a suggested order.",
 "D.6":"The delivery plan by drop, matching the outcome roadmap.",
 "D.7":"Counts and the trace from outcome to requirement to story.",
 "H.1":"One self-contained brief per outcome, ready for AI-DLC to pick up.",
 "H.2":"The order to hand the briefs over, what waits for what, and run notes.",
 "P.1":"One readable list of outcomes with their dependencies and a roadmap.",
}
def table(items):
    t = "| ID | Deliverable | What it is for | Mode | Depends on |\n| --- | --- | --- | --- | --- |\n"
    for i in items:
        dep = ", ".join(i["depends_on"]) or "none"
        extra = f" (feeds {i['feeds'].replace('_',' ')})" if i.get("feeds") else ""
        assert i["id"] in PURPOSES, "add a purpose for " + i["id"]
        t += f"| {i['id']} | {i['title']}{extra} | {PURPOSES[i['id']]} | {i['mode']} | {dep} |\n"
    return t + "\n"
for ph in p["phases"]:
    s += f"## Phase {ph['id']}: {ph['name']} ({ph['scope'].title()} stage)\n\n" + table(ph["deliverables"])
s += "## Outcome Definition (after Gate 2)\n\n" + table(p["outcome_definition"]["deliverables"])
for k,v in p["delivery"].items():
    if isinstance(v, list): s += f"## Delivery, `{k}` adapter (`--full` only)\n\n" + table(v)
(out/"reference/deliverables.md").write_text(s)
print("ok")
