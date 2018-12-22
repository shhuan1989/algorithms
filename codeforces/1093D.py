<<<<<<< HEAD
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
=======
# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/15 22:57

"""

MOD = 998244353

MAXN = 10**5+10
POW = [0] * MAXN
POW[0] = 1
for i in range(1, MAXN):
    POW[i] = (POW[i-1] * 2) % MOD


def solve(graph, startnode):
    F[startnode] = 2
    q = [startnode]
    f13, f2 = 0, 0
    while q:
        u = q.pop()
        vis[u] = True
        fu = F[u]
        fv = 1 if fu == 2 else 2
        f2 += 1 if fu == 1 else 0
        f13 += 1 if fu == 2 else 0
        for v in graph[u]:
            if F[v] == 0:
                F[v] = fv
                q.append(v)
            elif F[v] != fv:
                return -1

    return (POW[f13] + POW[f2]) % MOD


T = int(input())
ans = []
for ti in range(T):
    N, M = map(int, input().split())
    G = collections.defaultdict(list)
    vis = [False] * (N+1)
    F = [0] * (N + 1)
    for mi in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    valid = True
    count = 1
    for u in range(1, N+1):
        if vis[u]:
            continue
        a = solve(G, u)
        if a < 0:
            valid = False
            break

        count *= a
        count %= MOD
    if valid:
        ans.append(count)
    else:
        ans.append(0)


print('\n'.join(map(str, ans)))
>>>>>>> update
