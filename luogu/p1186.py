# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/24

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    INF = 10 ** 9 + 7
    edges = []
    G = collections.defaultdict(list)
    W = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for i in range(M):
        u, v, w = map(int, input().split())
        edges.append((u, v))
        G[u].append(v)
        G[v].append(u)
        W[u][v] = w
        W[v][u] = w
    for i in range(N+1):
        W[i][i] = 0

    dist = [INF for _ in range(N + 1)]
    pre = [-1 for _ in range(N+1)]
    inq = [False for _ in range(N + 1)]
    dist[1] = 0
    q = collections.deque([1])
    inq[1] = True
    while q:
        u = q.popleft()
        d = dist[u]
        inq[u] = False
        for v in G[u]:
            nd = d + W[u][v]
            if nd < dist[v]:
                dist[v] = nd
                if not inq[v]:
                    inq[v] = True
                    q.append(v)
                pre[v] = u
    
    path = []
    u = N
    while u > 0:
        path.append((u, pre[u]))
        u = pre[u]
        
    ans = 0
    for a, b in path:
        dist = [INF for _ in range(N+1)]
        dist[1] = 0
        q = collections.deque([1])
        inq[1] = True
        while q:
            u = q.popleft()
            d = dist[u]
            inq[u] = False
            for v in G[u]:
                if (u, v) == (a, b) or (u, v) == (b, a):
                    continue
                nd = d + W[u][v]
                if nd < dist[v]:
                    dist[v] = nd
                    if not inq[v]:
                        inq[v] = True
                        q.append(v)
        ans = max(ans, dist[N])

    print(ans)