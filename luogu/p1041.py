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
created by shhuan at 2020/7/9 20:13

"""


if __name__ == '__main__':
    N, P = map(int, input().split())
    G = collections.defaultdict(list)
    for i in range(P):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    child_count = [0 for _ in range(N+1)]

    def dfs1(u, p):
        for v in G[u]:
            if v != p:
                child_count[u] += 1
                dfs1(v, u)

    dfs1(1, -1)
    memo = {}

    def dfs(infected, parents):
        if not infected:
            return 0

        key = ''.join(map(str, infected))
        if key in memo:
            return memo[key]

        ninfected = []
        nparents = []
        for u, p in zip(infected, parents):
            for v in G[u]:
                if v != p:
                    ninfected.append(v)
                    nparents.append(u)

        if not ninfected:
            memo[key] = len(infected)
            return len(infected)

        ans = 10000
        cc = [child_count[v] for v in ninfected]
        scc = sum(cc)
        for i in range(len(ninfected)):
            if scc - cc[i] + len(ninfected) - 2 >= ans:
                continue
            ans = min(ans, dfs(ninfected[:i] + ninfected[i+1:], nparents[:i] + nparents[i+1:]))

        ans += len(infected)
        memo[key] = ans

        return ans


    print(dfs([1], [-1]))