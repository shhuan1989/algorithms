# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/13/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def redOfTree(node, parent, g):
    count = 0
    for v, c in g[node]:
        if v != parent:
            count += c + redOfTree(v, node, g)
    return count


def solve(N, A):
    INF = N+100
    flips = [INF for _ in range(N + 1)]
    q = [(1, 0, 0)]
    redCount = 0
    flips[1] = 0
    while q:
        nq = []
        for node, red, dist in q:
            for v, c in A[node]:
                if flips[v] == INF:
                    redCount += c
                    ndist, nred = dist + 1, red + c
                    flips[v] = ndist - 2 * nred
                    nq.append((v, nred, ndist))
        q = nq


    # def dfs(node, parent, red, dist):
    #     x = dist - 2 * red
    #     flips[node] = x
    #     ans = x
    #
    #     for v, c in A[node]:
    #         if v != parent:
    #             ans = min(ans, dfs(v, node, red + c, dist + 1))
    #
    #     return ans
    #
    # mf = dfs(1, -1, 0, 0)
    mf = min(flips)
    # redCount = redOfTree(1, -1, A)
    vertex = [i for i, v in enumerate(flips) if v == mf]
    # print(redCount)
    # print(flips)
    # print(vertex)
    print(redCount + mf)
    print(' '.join(map(str, vertex)))


N = int(input())
A = [[] for _ in range(N+1)]
for i in range(N - 1):
    u, v = map(int, input().split())
    A[u].append((v,  0))
    A[v].append((u, 1))

solve(N, A)