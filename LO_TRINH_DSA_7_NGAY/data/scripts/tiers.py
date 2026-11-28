import sys, json, collections, statistics as st
R = json.load(open(sys.argv[1], encoding='utf-8'))
T1 = set("""Array|String|Hash Table|Math|Dynamic Programming|Sorting|Greedy|Binary Search|Depth-First Search|Bit Manipulation|Matrix|Prefix Sum|Tree|Two Pointers|Breadth-First Search|Heap (Priority Queue)|Simulation|Counting|Graph|Stack|Binary Tree|Sliding Window|Enumeration|Design|Backtracking|Union Find|Linked List|Monotonic Stack|Divide and Conquer|Trie|Queue|Recursion|Memoization|Binary Search Tree|Shortest Path|Topological Sort|Monotonic Queue|Data Stream|Iterator|Brainteaser|Parentheses|Doubly-Linked List|Counting Sort|Bucket Sort|Quickselect|Merge Sort|Quick Sort|Knapsack|0-1 Knapsack|Unbounded Knapsack|Longest Increasing Subsequence|Longest Common Subsequence|Dijkstra|Directed Acyclic Graph|Floyd Cycle Detection|Hash Function|Interactive|Boyer-Moore Voting|Boyer–Moore|Bubble Sort|Lowest Common Ancestor|Bipartite Graph|Tree DP|Radix Sort|Newton's Method|Brute-Force Search|Heap|Sort|Timsort""".split('|'))
T2 = set("""Bitmask|Ordered Set|Number Theory|Combinatorics|Game Theory|Geometry|Greatest Common Divisor|Euclidean Algorithm|Sieve|Sieve of Eratosthenes|Prime Factorization|Primality Test|Least Common Multiple|Randomized|Reservoir Sampling|Rejection Sampling|Bidirectional Search|Minimax|Zero-Sum Game|Nim Game|Impartial Game|Rolling Hash|String Matching|KMP|Binary Indexed Tree|Minimum Spanning Tree|Kruskal|Prim|Borůvka|Probability and Statistics|Pigeonhole Principle|0-1 BFS|Inclusion-Exclusion|Ternary Search|Polygon|Floyd–Warshall|Bellman–Ford|Sweep Line|Binary Lifting|Mixed Knapsack|Bounded Knapsack|Linear Algebra|Extended Euclidean Algorithm|Bézout's Identity|Euler's Totient Function|Euler's Theorem|Fermat's Little Theorem|Cartesian Tree""".split('|'))
NONDSA = {'Pandas'}
alltags = collections.Counter(t for r in R for t in r['tags'])
T3 = set(alltags) - T1 - T2 - NONDSA
print('T3 tags:', sorted(T3))
def tier(r):
    ts = set(r['tags'])
    if ts & NONDSA: return 'NONDSA'
    if not ts: return 'NOTAG'
    if ts <= T1: return 'T1'
    if ts <= T1 | T2: return 'T2'
    return 'T3'
c = collections.Counter(); cd = collections.defaultdict(collections.Counter)
for r in R:
    t = tier(r); r['tier'] = t; c[t] += 1; cd[r['difficulty']][t] += 1
print('overall', dict(c))
for d in ['Easy','Medium','Hard']:
    n = sum(cd[d].values()); print(d, n, {k: f"{v} ({100*v/n:.0f}%)" for k, v in cd[d].items()})
# ratings by tier for Hard
for t in ['T1','T2','T3']:
    rs = [r['rating'] for r in R if r['difficulty']=='Hard' and r['tier']==t and r['rating']]
    if rs: print('Hard', t, 'rated', len(rs), 'median', st.median(rs))
# per-tag median rating (rated problems), tags with >=15 rated
print('\nPer-tag median rating (>=15 rated):')
tr = collections.defaultdict(list)
for r in R:
    if r['rating']:
        for t in r['tags']: tr[t].append(r['rating'])
rows = sorted([(st.median(v), t, len(v)) for t, v in tr.items() if len(v) >= 15])
for m, t, n in rows: print(f"  {t:28s} median {m:6.0f}  n={n}")
# Hard in T1 with rating <= 2150 or unrated classic
H = [r for r in R if r['difficulty']=='Hard' and r['tier']=='T1']
low = [r for r in H if r['rating'] and r['rating'] <= 2150]
print('\nHard T1:', len(H), 'rated<=2150:', len(low), 'unrated:', sum(1 for r in H if not r['rating']))
combo = collections.Counter()
skip = {'Array','String','Math','Matrix','Simulation','Enumeration','Counting','Design','Recursion','Brainteaser','Interactive','Data Stream','Iterator'}
for r in low:
    k = tuple(sorted(t for t in r['tags'] if t not in skip))
    combo[k] += 1
print('Top technique combos among Hard T1 rating<=2150:')
for k, v in combo.most_common(25): print(f"  {v:3d}  {' + '.join(k)}")
pair = collections.Counter()
for r in low:
    ks = sorted(t for t in r['tags'] if t not in skip)
    for i in range(len(ks)):
        for j in range(i+1, len(ks)): pair[(ks[i], ks[j])] += 1
print('Top technique pairs:')
for k, v in pair.most_common(20): print(f"  {v:3d}  {k[0]} + {k[1]}")
json.dump(R, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False)
