# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/3/16

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


MAXN = 2 * 10 ** 5 + 5
DP = [0 for _ in range(MAXN)]
A = [0 for _ in range(MAXN)]
G = [[] for _ in range(MAXN)]
ANS = [0 for _ in range(MAXN)]
idx = [0 for _ in range(MAXN)]

def dfs(curr, parent):
    # DP[curr] = A[curr]
    # for to in G[curr]:
    #     if to == parent:
    #         continue
    #     dfs(to, curr)
    #     DP[curr] += max(DP[to], 0)
    
    q = [(curr, parent, 0)]
    while q:
        curr, parent, t = q.pop()
        if t == 0:
            DP[curr] = A[curr]
            q.append((curr, parent, 1))
            for to in G[curr]:
                if to == parent:
                    continue
                q.append((to, curr, 0))
        else:
            for to in G[curr]:
                if to != parent:
                    DP[curr] += max(DP[to], 0)
                
            


def dfs2(curr, parent):
    # ANS[curr] = DP[curr]
    # for to in G[curr]:
    #     if to == parent:
    #         continue
    #     DP[curr] -= max(0, DP[to])
    #     DP[to] += max(0, DP[curr])
    #     dfs2(to, curr)
    #     DP[to] -= max(0, DP[curr])
    #     DP[curr] += max(0, DP[to])
    q = [(curr, parent)]
    while q:
        curr, parent = q.pop()
        if idx[curr] < len(G[curr]):
            ANS[curr] = DP[curr]
            hasMore = False
            for ti in range(idx[curr], len(G[curr])):
                to = G[curr][ti]
                if to != parent:
                    idx[curr] = ti + 1
                    hasMore = True
                    q.append((curr, parent))
                    DP[curr] -= max(0, DP[to])
                    DP[to] += max(0, DP[curr])
                    q.append((to, curr))
                    break
            if not hasMore:
                idx[curr] += 1
                q.append((curr, parent))
        else:
            if parent > 0:
                DP[curr] -= max(0, DP[parent])
                DP[parent] += max(0, DP[curr])
    


N = int(input())
for i, v in enumerate([int(x) for x in input().split()]):
    A[i+1] = v if v == 1 else -1
for i in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(A[1: N+1])
dfs(1, -1)
print(DP[1: N+1])
dfs2(1, -1)
print(' '.join(map(str, ANS[1: N+1])))
        


