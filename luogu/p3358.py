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


def add_edge(u, v, cap, flow, cost):
    tot[0] += 1
    i = tot[0]
    edges[i].start = u
    edges[i].end = v
    edges[i].cap = cap
    edges[i].flow = flow
    edges[i].cost = cost
    edges[i].next = head[u]
    head[u] = i


def add(u, v, cap, flow, cost):
    add_edge(u, v, cap, flow, cost)
    add_edge(v, u, 0, 0, -cost)


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
            if f > 0 and dist[v] < dist[u] + f * e.cost:
                dist[v] = dist[u] + f * e.cost
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


def solve(N, K, A):
    points = set()
    for l, r in A:
        points.add(l)
        points.add(r)
    # print(N, K)
    # print('\n'.join(['{} {}'.format(u, v) for u, v in sorted(A)]))
    points = list(sorted(points))
    vi = {v: (i + 1) for i, v in enumerate(points)}
    A = [(vi[l], vi[r], r - l) for l, r in A]
    points = [vi[v] for v in points]
    
    start, end = 0, points[-1] + 1
    add(start, points[0], K, 0, 0)
    add(points[-1], end, INF, 0, 0)
    
    for i in range(len(points) - 1):
        add(points[i], points[i + 1], INF, 0, 0)
    
    for l, r, d in A:
        add(l, r, 1, 0, d)
    
    return max_flow_ek(start, end)


import random

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = []
    for i in range(N):
        l, r = map(int, input().split())
        A.append((l, r))
    # N = 2
    # K = 1
    # A = [(66, 127), (73, 159)]
    
    print(solve(N, K, A))




