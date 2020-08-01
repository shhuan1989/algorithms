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
created by shhuan at 2020/7/18 17:39

"""


if __name__ == '__main__':
    N = int(input())
    S = int(input())
    G = collections.defaultdict(list)
    W = collections.defaultdict(int)
    for i in range(N-1):
        u, v, w = map(int, input().strip().split())
        G[u].append(v)
        G[v].append(u)
        W[u, v] = w
        W[v, u] = w


    def dfs(u, p, cost):
        totalCost = cost
        ops = 0
        ends = []
        for v in G[u]:
            if v == p:
                continue
            t, c = dfs(v, u, cost + W[u, v])
            ops += c
            ends.append(t)

        totalCost = max(totalCost, max(ends or [0]))
        ops += sum([totalCost - t for t in ends] or [0])

        return totalCost, ops

    t, c = dfs(S, -1, 0)
    print(c)
