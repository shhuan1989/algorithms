# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/25/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

N, M = map(int, input().split())
g = collections.defaultdict(dict)
for _ in range(M):
    u, v, w = map(int, input().split())
    if u == v:
        continue
    if v not in g[u]:
        g[u][v] = w
    else:
        g[u][v] = min(g[u][v], w)
    
    if u not in g[v]:
        g[v][u] = w
    else:
        g[v][u] = min(g[v][u], w)

dists = [float('inf') for _ in range(N+1)]
pre = [-1 for _ in range(N+1)]
q = [(w, v) for v, w in g[1].items()]
for w, v in q:
    pre[v] = 1
    dists[v] = w
dists[1] = 0
heapq.heapify(q)
while q:
    d, u = heapq.heappop(q)
    for v, w in g[u].items():
        nd = d + w
        if nd < dists[v]:
            dists[v] = nd
            pre[v] = u
            heapq.heappush(q, (nd, v))

if dists[N] < float('inf'):
    ans = []
    u = N
    while u > 0:
        ans.append(u)
        u = pre[u]
    print(' '.join(map(str, ans[::-1])))
else:
    print(-1)

