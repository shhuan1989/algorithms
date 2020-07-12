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
created by shhuan at 2020/7/11 19:52

"""



if __name__ == '__main__':
    N, M, K = map(int, input().split())
    G = collections.defaultdict(list)
    for i in range(N):
        row = [int(x) for x in input().split()]

        for j in range(M):
            if row[j] > 0:
                G[row[j]].append((i+1, j+1))

    vs = list(sorted(G.keys(), reverse=True))

    def dfs(x, y, cost, vis, vi, total):
        if cost + x > K:
            return float('-inf')

        ans = total
        val = vs[vi]
        hasmore = False
        for nx, ny in G[val]:
            key = (nx, ny)
            d = abs(x-nx) + abs(y-ny)
            if key not in vis:
                hasmore = True
                ans = max(ans, dfs(nx, ny, cost+d+1, vis | {key}, vi, total + val))

        if not hasmore and vi + 1 < len(vs):
            val = vs[vi+1]
            for nx, ny in G[val]:
                key = (nx, ny)
                d = abs(x-nx) + abs(y-ny)
                if key not in vis:
                    ans = max(ans, dfs(nx, ny, cost+d+1, vis | {key}, vi+1, total + val))

        return ans

    ans = 0
    for x, y in G[vs[0]]:
        ans = max(ans, dfs(0, y, 0, set(), 0, 0))
    print(ans)




