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



MAXN = 300
MAXM = 100000
INF = 10**9+7


head = [-1 for _ in range(MAXN)]
depth = [-1 for _ in range(MAXN)]

to = [-1 for _ in range(MAXM)]
cap = [0 for _ in range(MAXM)]
flow = [0 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]

tot = [1]


def add_edge(u, v, c):
    tot[0] += 1
    i = tot[0]

    to[i] = v
    cap[i] = c
    nxt[i] = head[u]
    head[u] = i


def add(u, v, c):
    add_edge(u, v, c)
    add_edge(v, u, 0)
    # print(u, v)

def bfs(start, end):
    for i in range(MAXN):
        depth[i] = -1

    q = collections.deque([start])
    depth[start] = 0

    while q:
        u = q.popleft()
        i = head[u]
        while i >= 0:
            v = to[i]
            if depth[v] < 0 and cap[i] - flow[i] > 0:
                depth[v] = depth[u] + 1
                if v == end:
                    return True
                q.append(v)
            i = nxt[i]

    return depth[end] > 0


def dfs(curr, end, add):
    if curr == end or add <= 0:
        return add

    ret = 0
    i = head[curr]
    while i >= 0 and add > 0:
        v = to[i]
        if depth[v] == depth[curr]+1 and cap[i] - flow[i] > 0:
            f = dfs(v, end, min(add, cap[i] - flow[i]))
            if f > 0:
                ret += f
                add -= f
                flow[i] += f
                flow[i ^ 1] -= f
        i = nxt[i]

    return ret


def max_flow(start, end):
    f = 0
    while bfs(start, end):
        f += dfs(start, end, INF)
    return f


if __name__ == '__main__':
    sys.stdin = open('P1401_2.in', 'r')
    t0 = time.time()
    N, M, T = map(int, input().split())

    start, end = 1, N
    edges = []
    for _ in range(M):
        u, v, d = map(int, input().split())
        edges.append((d, u, v))
    edges.sort()

    for d, u, v in edges:
        add(u, v, 1)
        add(v, u, 1)
        f = max_flow(start, end)
        # if f > 0:
        #     print(d, f)
        if f >= T:
            print(d)
            print(time.time() - t0)
            exit(0)
        T -= f
