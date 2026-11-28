import sys, json, re, collections, statistics as st
R = json.load(open(sys.argv[1], encoding='utf-8'))
src = open(sys.argv[2]).read()
T1 = set(re.search(r'T1 = set\("""(.*?)"""', src, re.S).group(1).split('|'))
T2 = set(re.search(r'T2 = set\("""(.*?)"""', src, re.S).group(1).split('|'))
ALT = {'Manacher','Extended KMP','Aho-Corasick','Range Query','Tournament Sort','Algorithm X','Dancing Links','K-D Tree',
       'Binary Lifting','Graph Coloring','A* Search','Heuristic Search','Planar Graph','Triangulation',
       'Persistent Data Structure','Sqrt Decomposition','Cartesian Tree'}
def eff(r):
    ts = set(r['tags']) - ALT
    if {'Kosaraju','Tarjan'} & ts and 'Topological Sort' in ts: ts -= {'Kosaraju','Tarjan'}
    return ts
def tier(ts, raw):
    if 'Pandas' in raw: return 'NONDSA'
    if not raw: return 'NOTAG'
    if ts <= T1: return 'T1'
    if ts <= T1 | T2: return 'T2'
    return 'T3'
D = ['Easy','Medium','Hard']
for mode in ['raw','adj']:
    c = collections.defaultdict(collections.Counter)
    for r in R:
        ts = set(r['tags']) if mode=='raw' else eff(r)
        t = tier(ts, r['tags']); c[r['difficulty']][t] += 1
        if mode=='adj': r['tier_adj'] = t
    tot = {d: sum(v for k, v in c[d].items() if k in ('T1','T2','T3')) for d in D}
    allT = sum(tot.values())
    line = []
    for k in ['T1','T2','T3']:
        s = sum(c[d][k] for d in D)
        line.append(f"{k}: all {s} ({100*s/allT:.1f}%) " + " ".join(f"{d[0]} {c[d][k]} ({100*c[d][k]/tot[d]:.1f}%)" for d in D))
    print(mode, tot, allT); print('   ' + '\n   '.join(line))
low = [r for r in R if r['difficulty']=='Hard' and r['tier_adj']=='T1' and r['rating'] and r['rating'] <= 2150]
skip = {'Array','String','Math','Matrix','Simulation','Enumeration','Counting','Design','Recursion','Brainteaser','Interactive','Data Stream','Iterator'}
nt = collections.Counter(len([t for t in eff(r) if t not in skip]) for r in low)
print('Hard adj-T1 rating<=2150:', len(low), 'tech-tag counts', sorted(nt.items()), 'DP share', sum('Dynamic Programming' in r['tags'] for r in low))
print('notebooks among them', sum(r['status']=='Đã có notebook' for r in low))
H = [r for r in R if r['difficulty']=='Hard' and r['tier_adj']=='T1']
print('Hard adj-T1 total', len(H), 'rated', sum(1 for r in H if r['rating']), 'median', st.median([r['rating'] for r in H if r['rating']]), 'unrated', sum(1 for r in H if not r['rating']))
json.dump(R, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False)
