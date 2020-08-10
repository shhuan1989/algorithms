# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/5

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import math


class Node:
    def __init__(self, start, end, cap, flow, cost):
        self.start = start
        self.end = end
        self.cap = cap
        self.flow = flow
        self.cost = cost
        self.next = -1


MAXN = 2000
MAXM = 100000
INF = 10 ** 9 + 7

vis = [False for _ in range(MAXN)]
pre = [-1 for _ in range(MAXN)]
incf = [0 for _ in range(MAXN)]
head = [-1 for _ in range(MAXN)]
dist = [-1 for _ in range(MAXN)]
edges = [Node(0, 0, 0, 0, 0) for _ in range(MAXM)]
tot = [1]


def add_edge(u, v, cap, cost):
    tot[0] += 1
    i = tot[0]
    edges[i].start = u
    edges[i].end = v
    edges[i].cap = cap
    edges[i].cost = cost
    edges[i].next = head[u]
    head[u] = i


def add(u, v, cap, cost):
    add_edge(u, v, cap, cost)
    add_edge(v, u, 0, -cost)


def spfa(start, end):
    for i in range(MAXN):
        vis[i] = False
        pre[i] = -1
        incf[i] = 0
        dist[i] = -1

    q = collections.deque([start])
    vis[start] = True
    incf[start] = INF
    dist[start] = 0
    while q:
        u = q.popleft()
        vis[u] = False
        i = head[u]
        while i > 0:
            e = edges[i]
            v = e.end
            f = min(e.cap - e.flow, incf[u])
            if f > 0 and dist[v] < dist[u] + e.cost:
                dist[v] = dist[u] + e.cost
                incf[v] = f
                pre[v] = i
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
            i = e.next

    return incf[end] > 0


def max_flow_ek(start, end):
    ans = 0
    while spfa(start, end):
        u = end
        while u != start:
            edges[pre[u]].flow += incf[end]
            edges[pre[u] ^ 1].flow -= incf[end]
            ans += incf[end] * edges[pre[u]].cost
            u = edges[pre[u]].start

    return ans


def distance(x0, y0, x1, y1):
    return int(math.floor(math.sqrt((x1-x0)**2 + (y1-y0)**2)))


def solve(N, K, A):
    points = set()
    B = []
    for x0, y0, x1, y1, d in A:
        l = x0 * 2
        r = x1 * 2
        if x0 == x1:
            r += 1
        else:
            l += 1
        points.add(l)
        points.add(r)
        B.append((l, r, d))

    points = list(sorted(points))
    vi = {v: (i + 1) for i, v in enumerate(points)}
    B = [(vi[l], vi[r], d) for l, r, d in B]
    M = len(points)
    start, end = 0, M + 1
    add(start, 1, K, 0)
    add(M, end, INF, 0)

    for i in range(M+1):
        add(i, i+1, INF, 0)

    for l, r, d in B:
        add(l, r, 1, d)

    return max_flow_ek(start, end)


if __name__ == '__main__':
    # sys.stdin = open('p3357.in', 'r')
    N, K = map(int, input().split())
    A = []
    for i in range(N):
        x0, y0, x1, y1 = map(int, input().split())
        if x0 > x1:
            x0, y0, x1, y1 = x1, y1, x0, y0
        A.append((x0, y0, x1, y1, distance(x0, y0, x1, y1)))

    print(solve(N, K, A))




