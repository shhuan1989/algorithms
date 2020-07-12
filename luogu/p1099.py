# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/7/11 13:53

"""


if __name__ == '__main__':
    N, S = map(int, input().split())
    if N <= 1:
        print(0)
        exit(0)

    INF = 10**9
    W = [[INF for _ in range(N+1)] for _ in range(N+1)]
    G = collections.defaultdict(list)
    for i in range(N-1):
        u, v, w = map(int, input().split())
        W[u][v] = w
        W[v][u] = w
        G[u].append(v)
        G[v].append(u)


    def dfs1(u, p, path, dist):
        q = path
        d = dist
        for v in G[u]:
            if v != p:
                a, b = dfs1(v, u, path+[v], dist + [W[u][v]])
                if len(a) > len(q):
                    q = a
                    d = b

        return q, d


    p1, d1 = dfs1(1, -1, [1], [])
    p2, d2 = dfs1(p1[-1], -1, [p1[-1]], [])

    path, dist = p2, d2

    disttopath = [INF for _ in range(N+1)]
    jointpoint = [-1 for _ in range(N+1)]
    for v in path:
        disttopath[v] = 0
        jointpoint[v] = v

    for start in path:
        q = [(start, -1, 0)]
        while q:
            nq = []
            for u, p, d in q:
                for v in G[u]:
                    if v != p and v not in path:
                        nd = d + W[u][v]
                        disttopath[v] = nd
                        jointpoint[v] = start
                        nq.append((v, u, nd))
            q = nq

    # print(disttopath)
    # print(jointpoint)

    presum = [0]
    for v in dist:
        presum.append(presum[-1] + v)

    nodeinx = [-1 for _ in range(N+1)]
    for i, u in enumerate(path):
        nodeinx[u] = i
    ans = presum[-1]
    si = 0
    s = 0
    for i, u in enumerate(dist):
        s += u
        while s > S:
            s -= dist[si]
            si += 1

        radius = max(presum[si], presum[-1] - presum[i+1])

        for v in range(1, N+1):
            d = disttopath[v]
            x = jointpoint[v]
            xi = nodeinx[x]
            if si <= xi <= i + 1:
                pass
            elif xi > i + 1:
                d += presum[xi] - presum[i + 1]
            else:
                d += presum[si] - presum[xi]

            radius = max(radius, d)
        # print(path[si: i+2], radius)
        ans = min(ans, radius)

    print(ans)









