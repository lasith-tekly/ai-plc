"""Draw AI-PLC showcase figures from a /product folder.
Usage: build_showcase_figures.py PRODUCT_DIR OUT_DIR
Draws: flow.png (idea to handover) and deliverables.png (dependencies between deliverables)."""
import sys, re, yaml, pathlib, subprocess, shutil, tempfile
prod, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)

def esc(s): return s.replace('"','\\"')
def dot(src, name, dpi=140):
    with tempfile.TemporaryDirectory() as d:
        f = pathlib.Path(d)/'g.dot'; f.write_text(src)
        subprocess.run(['dot','-Tpng',f'-Gdpi={dpi}',str(f),'-o',str(out/name)],check=True)

# ---- deliverables from frontmatter
dl = {}
for f in sorted(prod.glob('phase-*/*.md')):
    t = f.read_text(); m = re.match(r'---\n(.*?)\n---\n', t, re.S)
    if not m: continue
    d = yaml.safe_load(m.group(1))
    if 'id' not in d: continue
    h1 = next((l[2:].strip() for l in t.splitlines() if l.startswith('# ')), str(d['id']))
    title = re.sub(r'^[0-9.]+\s*', '', h1)
    dl[str(d['id'])] = dict(title=title, mode=d.get('mode'), deps=[str(x) for x in (d.get('depends_on') or [])], phase=int(str(d['id']).split('.')[0]))

COL = {'auto':('#dbeafe','#1d4ed8'), 'assist':('#fef3c7','#b45309'), 'human':('#fee2e2','#b91c1c')}
names = {1:'Phase 1: Assess market and customers', 2:'Phase 2: Define vision and strategy', 3:'Phase 3: Converge on solution', 4:'Phase 4: Evaluate viability'}
stops = {1:('CP1','Checkpoint 1'), 2:('G1','Gate 1'), 3:('CP2','Checkpoint 2'), 4:('G2','Gate 2')}
g = ['digraph G { rankdir=LR; compound=true; nodesep=0.25; ranksep=0.55; fontname="Helvetica"; node [fontname="Helvetica", fontsize=11, shape=box, style="rounded,filled", margin="0.12,0.06"]; edge [color="#64748b", arrowsize=0.7];']
for p in (1,2,3,4):
    g.append(f'subgraph cluster_{p} {{ label="{names[p]}"; fontsize=14; style="rounded"; color="#94a3b8"; labeljust=l;')
    for i,d in dl.items():
        if d['phase']==p:
            fc,lc = COL.get(d['mode'],('#f1f5f9','#475569'))
            tt = esc(d['title'])
            if len(tt)>26: 
                w=tt.split(); half=len(w)//2 or 1; tt=' '.join(w[:half])+'\\n'+' '.join(w[half:])
            g.append(f'"{i}" [label="{i}\\n{tt}", fillcolor="{fc}", color="{lc}"];')
    g.append('}')
    sid,sl = stops[p]
    g.append(f'"{sid}" [label="{sl}", shape=diamond, style=filled, fillcolor="#e2e8f0", color="#334155", fontsize=11];')
last = {p:[i for i,d in dl.items() if d['phase']==p][-1] for p in (1,2,3,4)}
for p in (1,2,3,4):
    g.append(f'"{last[p]}" -> "{stops[p][0]}" [ltail=cluster_{p}, style=dashed, color="#334155"];')
for i,d in dl.items():
    for x in d['deps']:
        if x in dl: g.append(f'"{x}" -> "{i}";')
g.append('"OP" [label="Outcome Pack", shape=hexagon, style=filled, fillcolor="#dcfce7", color="#15803d"];')
g.append('"G2" -> "OP" [style=dashed, color="#334155"];')
g.append('}')
dot('\n'.join(g), 'deliverables.png', dpi=110)

# ---- flow: idea to handover
f = '''digraph F { rankdir=LR; nodesep=0.3; ranksep=0.45; node [fontname="Helvetica", fontsize=12, shape=box, style="rounded,filled", margin="0.18,0.1"]; edge [color="#64748b"];
idea [label="Your idea\\n(one command)", fillcolor="#f1f5f9", color="#475569"];
p1 [label="Phase 1\\nAssess market\\nand customers", fillcolor="#dbeafe", color="#1d4ed8"];
cp1 [label="Checkpoint 1", shape=diamond, style=filled, fillcolor="#e2e8f0", color="#334155"];
p2 [label="Phase 2\\nDefine vision\\nand strategy", fillcolor="#dbeafe", color="#1d4ed8"];
g1 [label="Gate 1", shape=diamond, style=filled, fillcolor="#e2e8f0", color="#334155"];
p3 [label="Phase 3\\nConverge\\non solution", fillcolor="#fef3c7", color="#b45309"];
cp2 [label="Checkpoint 2", shape=diamond, style=filled, fillcolor="#e2e8f0", color="#334155"];
p4 [label="Phase 4\\nEvaluate\\nviability", fillcolor="#fef3c7", color="#b45309"];
g2 [label="Gate 2", shape=diamond, style=filled, fillcolor="#e2e8f0", color="#334155"];
op [label="Outcome Pack\\n(measurable results)", shape=hexagon, fillcolor="#dcfce7", color="#15803d"];
dl [label="Delivery material\\nrequirements, epics, stories,\\nor AI-DLC briefs", fillcolor="#dcfce7", color="#15803d"];
dev [label="Development\\n(your team)", fillcolor="#f1f5f9", color="#94a3b8", style="rounded,dashed,filled"];
idea->p1->cp1->p2->g1->p3->cp2->p4->g2->op->dl->dev;
{rank=same; }
}'''
dot(f,'flow.png',dpi=130)
print(len(dl),'deliverables drawn')
