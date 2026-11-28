import sys, json, collections, re
R = json.load(open(sys.argv[1], encoding='utf-8'))
ALT = {'Manacher','Extended KMP','Aho-Corasick','Range Query','Tournament Sort','Algorithm X','Dancing Links','K-D Tree','Binary Lifting','Graph Coloring','A* Search','Heuristic Search','Planar Graph','Triangulation','Persistent Data Structure','Sqrt Decomposition','Cartesian Tree'}
for r in R:
    ts = set(r['tags']) - ALT
    if {'Kosaraju','Tarjan'} & ts and 'Topological Sort' in ts: ts -= {'Kosaraju','Tarjan'}
    r['eff'] = ts
L = [
 ("L0 Nền tảng", "Array|String|Math|Simulation|Matrix|Enumeration|Brainteaser|Interactive|Iterator|Newton's Method|Brute-Force Search"),
 ("L1 Bảng băm & kỹ thuật mảng", "Hash Table|Counting|Hash Function|Sorting|Sort|Timsort|Counting Sort|Bucket Sort|Radix Sort|Bubble Sort|Quick Sort|Quickselect|Prefix Sum|Two Pointers|Sliding Window|Boyer-Moore Voting|Boyer–Moore|Greedy"),
 ("L2 Tìm kiếm nhị phân", "Binary Search"),
 ("L3 Tuyến tính & heap", "Stack|Monotonic Stack|Queue|Monotonic Queue|Linked List|Doubly-Linked List|Parentheses|Floyd Cycle Detection|Heap (Priority Queue)|Heap|Data Stream|Design"),
 ("L4 Đệ quy & cây", "Recursion|Tree|Binary Tree|Binary Search Tree|Depth-First Search|Breadth-First Search|Lowest Common Ancestor|Trie|Divide and Conquer|Merge Sort"),
 ("L5 Quay lui & bit", "Backtracking|Bit Manipulation"),
 ("L6 Đồ thị", "Graph|Topological Sort|Directed Acyclic Graph|Union Find|Shortest Path|Dijkstra|Bipartite Graph"),
 ("L7 QHĐ", "Dynamic Programming|Memoization|Knapsack|0-1 Knapsack|Unbounded Knapsack|Longest Increasing Subsequence|Longest Common Subsequence|Tree DP"),
]
cum = set(); D = ['Easy','Medium','Hard']
tot = collections.Counter(r['difficulty'] for r in R if r['tags'] and 'Pandas' not in r['tags'])
print('denominator (tagged DSA):', dict(tot), sum(tot.values()))
for name, tags in L:
    cum |= set(tags.split('|'))
    c = collections.Counter(r['difficulty'] for r in R if r['tags'] and 'Pandas' not in r['tags'] and r['eff'] <= cum)
    allc = sum(c.values())
    print(f"{name:32s} all {allc:5d} ({100*allc/sum(tot.values()):4.1f}%)  " + "  ".join(f"{d[0]} {100*c[d]/tot[d]:4.1f}%" for d in D))
# title keywords
kw = {'interval': r'interval|meeting', 'stock': r'stock', 'LIS': r'increasing subsequence', 'palindrom': r'palindrom', 'island': r'island', 'subarray': r'subarray', 'substring': r'substring', 'subsequence': r'subsequence', 'k-th/top k': r'\bkth\b|k-th|top k|\bk closest|\bk largest|\bk smallest', 'parenthes': r'parenthes', 'matrix/grid': r'matrix|grid'}
print()
for k, p in kw.items():
    rs = [r for r in R if re.search(p, r['title'], re.I)]
    c = collections.Counter(r['difficulty'] for r in rs)
    print(f"title~{k:12s} {len(rs):4d}  E{c['Easy']} M{c['Medium']} H{c['Hard']}")
