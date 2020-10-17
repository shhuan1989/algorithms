# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/17 11:03

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List



MAXN = 500
MAXM = 100000
INF = 10**9+7


head = [-1 for _ in range(MAXN)]
depth = [-1 for _ in range(MAXN)]

to = [-1 for _ in range(MAXM)]
cap = [0 for _ in range(MAXM)]
flow = [0 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]
dist = [-1 for _ in range(MAXM)]

tot = [1]


def add_edge(u, v, d, c):
    tot[0] += 1
    i = tot[0]

    to[i] = v
    cap[i] = c
    dist[i] = d
    flow[i] = 0
    nxt[i] = head[u]
    head[u] = i


def add(u, v, d, c):
    add_edge(u, v, d, c)
    add_edge(v, u, d, 0)
    # print(u, v)


def bfs(start, end, maxd):
    for i in range(MAXN):
        depth[i] = -1

    q = collections.deque([start])
    depth[start] = 0

    while q:
        u = q.popleft()
        i = head[u]
        while i >= 0:
            v = to[i]
            if dist[i] <= maxd and depth[v] < 0 and cap[i] - flow[i] > 0:
                depth[v] = depth[u] + 1
                q.append(v)
            i = nxt[i]

    return depth[end] > 0


def dfs(curr, end, add, maxd):
    if curr == end or add <= 0:
        return add

    ret = 0
    i = head[curr]
    while i >= 0 and add > 0:
        v = to[i]
        if dist[i] <= maxd and depth[v] == depth[curr]+1 and cap[i] - flow[i] > 0:
            f = dfs(v, end, min(add, cap[i] - flow[i]), maxd)
            if f > 0:
                ret += f
                add -= f
                flow[i] += f
                flow[i ^ 1] -= f
        i = nxt[i]

    return ret


def max_flow(start, end, maxd):
    f = 0
    for i in range(MAXM):
        flow[i] = 0
    while bfs(start, end, maxd):
        f += dfs(start, end, INF, maxd)
    return f


if __name__ == '__main__':
    sys.stdin = open('P1401_2.in', 'r')
    N, M, T = map(int, input().split())

    start, end = 1, N
    width = set()
    # add(start, 1, 0, INF)
    # add(N, end, 0, INF)
    for _ in range(M):
        u, v, d = map(int, input().split())
        # if d <= INF:
        add(u, v, d, 1)
            # print(u, v, d)
        width.add(d)

    print(max_flow(start, end, INF))
    width = list(sorted(width))

    lo, hi = 0, len(width)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        f = max_flow(start, end, width[mid])
        print(width[mid], f)
        if f >= T:
            hi = mid - 1
        else:
            lo = mid + 1

    print(width[lo] if lo < len(width) else -1)

