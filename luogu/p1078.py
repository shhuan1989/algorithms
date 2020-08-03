# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    N, K, M, S, T = map(int, input().split())
    C = [0] + [int(x) for x in input().split()]
    G = collections.defaultdict(list)
    W = collections.defaultdict(int)
    
    E = [[False for _ in range(K+1)] for _ in range(K+1)]
    for i in range(1, K + 1):
        row = [0] + [int(x) for x in input().split()]
        for j in range(1, K+1):
            if row[j] != 0:
                E[i][j] = True
    
    for i in range(M):
        u, v, w = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        W[u, v] = w
        W[v, u] = w

    INF = 10 ** 9 + 7
    DIST = [INF for _ in range(N+1)]
    DIST[S] = 0
    q = [(0, S, {C[S]})]
    while q:
        d, u, visc = heapq.heappop(q)
        for v in G[u]:
            cv = C[v]
            if cv in visc:
                continue
            if any([E[cv][uv] for uv in visc]):
                continue
            
            nd = DIST[u] + W[u, v]
            if nd < DIST[v]:
                DIST[v] = nd
                heapq.heappush(q, (nd, v, visc | {cv}))
    
    ans = DIST[T]
    ans = -1 if ans == INF else ans
    print(ans)
