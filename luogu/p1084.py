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
created by shhuan at 2020/7/11 20:59

"""

if __name__ == '__main__':
    N = int(input())
    G = collections.defaultdict(list)
    W = collections.defaultdict(int)
    for i in range(N-1):
        u, v, w = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        W[u, v] = w
        W[v, u] = w

    M = 1
    while 2 ** M <= N:
        M += 1
    M += 1
    INF = 10**9 + 7
    PARENTS = [[-1 for _ in range(M)] for _ in range(N + 1)]
    DIST = [[INF for _ in range(M)] for _ in range(N + 1)]
    ISLEAF = [True if len(G[i]) == 1 else False for i in range(N + 1)]
    LEAFS = [i for i in range(1, N + 1) if ISLEAF[i]]

    K = int(input())
    ARMY = collections.Counter([int(x) for x in input().split()])
    NECKS = [v for v in G[1]]
    NECK = [-1 for _ in range(N+1)]

    def dfs(u, p, neck):
        PARENTS[u][0] = p
        if p > 0:
            DIST[u][0] = W[u, p]

        neck = neck if p != 1 else u
        NECK[u] = neck
        for i in range(1, M):
            PARENTS[u][i] = PARENTS[PARENTS[u][i - 1]][i - 1]
            DIST[u][i] = DIST[u][i-1] + DIST[PARENTS[u][i - 1]][i - 1]

        for v in G[u]:
            if v != p:
                dfs(v, u, neck)

    dfs(1, -1, -1)


    def getparentindist(u, d):
        while u > 1:
            pi = 0
            while pi < M and DIST[u][pi] <= d:
                pi += 1
            pi -= 1
            if pi < 0:
                return u, d

            if pi == 0:
                return PARENTS[u][0], d - DIST[u][0]

            d -= DIST[u][pi]
            u = PARENTS[u][pi]

        return 1, d


    def findstop(u, c, ps):
        if u in ps:
            return u

        if u == 1:
            return c

        return findstop(PARENTS[u][0], u, ps)

    def check(cost):
        cks = collections.defaultdict(list)
        for army, count in ARMY.items():
            stop, rest = getparentindist(army, cost)
            if stop == 1:
                rest += DIST[NECK[army]][0]
                cks[NECK[army]].append((rest, count))
            else:
                cks[stop].append((rest, count))

        checkpoints = set(cks.keys())
        needs = {findstop(u, -1, checkpoints) for u in LEAFS}

        over = collections.defaultdict(int)
        for k, rcs in cks.items():
            if k in needs:
                if NECK[k] == k:
                    cks[k].sort()
                    r, c = cks[k][0]

                    if c > 1:
                        nd = r - DIST[k][0]
                        if nd > 0:
                            over[nd] += c-1
                    for r, c in cks[k][1:]:
                        nd = r - DIST[k][0]
                        if nd > 0:
                            over[nd] += c
            else:
                if NECK[k] == k:
                    for r, c in cks[k]:
                        nd = r - DIST[k][0]
                        if nd > 0:
                            over[nd] += c
            needs.discard(k)

        neckdist = [DIST[NECK[u]][0] for u in needs]
        neckdist.sort()

        overd = list(sorted(over.keys()))
        oi = 0
        for d in neckdist:
            while oi < len(overd) and (overd[oi] < d or over[overd[oi]] <= 0):
                oi += 1

            if oi >= len(overd):
                return False
            over[overd[oi]] -= 1

        return True


    lo, hi = 0, INF

    while lo <= hi:
        m = (lo + hi) // 2
        if check(m):
            hi = m - 1
        else:
            lo = m + 1

    print(lo if lo < INF else -1)
