# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/17/18

"""

import collections
import time
import os
import sys
import bisect
import heapq

MOD = 998244353
MAXN = 3 * 10 ** 5 + 10
POW = [0] * MAXN
POW[0] = 1
for i in range(1, MAXN):
    POW[i] = (POW[i - 1] * 2) % MOD
    

VIS = [False] * MAXN
GRAPH = [[] for _ in range(MAXN)]
COLOR = [0] * MAXN


def dfs(start):
    # 0 means put 2 in vertex, else means put 1, 3 in vertext
    q = [start]
    f = [0] * 2
    VIS[start] = True
    COLOR[start] = 0
    while q:
        u = q.pop()
        c = COLOR[u]
        f[c] += 1
        nv = c ^ 1
        for w in GRAPH[u]:
            if not VIS[w]:
                VIS[w] = True
                COLOR[w] = nv
                q.append(w)
            elif COLOR[w] != nv:
                    return 0
    
    return sum([POW[x] for x in f]) % MOD


def solve():
    N, M = map(int, input().split())
    for i in range(N+1):
        COLOR[i] = 0
        VIS[i] = False
        GRAPH[i] = []
    
    for mi in range(M):
        u, v = map(int, input().split())
        GRAPH[u].append(v)
        GRAPH[v].append(u)
    
    counts = 1
    for u in range(1, N + 1):
        if VIS[u]:
            continue
        
        counts *= dfs(u)
        counts %= MOD
        if counts == 0:
            return 0

    return counts


T = int(input())
ans = []
for ti in range(T):
    ans.append(solve())

print('\n'.join(map(str, ans)))