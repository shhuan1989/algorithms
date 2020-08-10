# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/3 19:11

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

MAXN = 5000
MAXM = 10**5

INF = 10**9 + 7
head = [0 for _ in range(MAXN)]
vis = [False for _ in range(MAXN)]
pre = [-1 for _ in range(MAXN)]
level = [-1 for _ in range(MAXN)]

cap = [0 for _ in range(MAXM)]
to = [0 for _ in range(MAXM)]
nxt = [0 for _ in range(MAXM)]


tot = [1]

def add_edge(u, v, w):
    tot[0] += 1
    i = tot[0]
    nxt[i] = head[u]
    cap[i] = w
    to[i] = v
    head[u] = i

def add(u, v, w):
    add_edge(u, v, w)
    add_edge(v, u, 0)

def reset():
    for i in range(MAXN):
        pre[i] = -1
        vis[i] = False
        level[i] = -1

def dfs(curr, end, flow):
    if curr == end or flow <= 0:
        return flow

    ans = 0
    i = head[curr]
    while i > 0 and flow > 0:
        v = to[i]
        if level[v] == level[curr] + 1:
            f = dfs(v, end, min(cap[i], flow))
            if f > 0:
                cap[i] -= f
                cap[i ^ 1] += f
                ans += f
                flow -= f
        i = nxt[i]

    return ans


def bfs(start, end):
    reset()
    q = collections.deque([start])
    level[start] = 0
    while q:
        u = q.popleft()
        i = head[u]
        while i > 0:
            v = to[i]
            if level[v] < 0 and cap[i] > 0:
                vis[v] = True
                level[v] = level[u] + 1
                q.append(v)
            i = nxt[i]

    return level[end] > 0


def max_flow_dinic(start, end):
    ans = 0
    while bfs(start, end):
        ans += dfs(start, end, INF)

    return ans


if __name__ == '__main__':
    # sys.stdin = open('p2762_2.in', 'r')
    N, M = map(int, input().split())
    start, end = 0, N+M+1
    profit = 0
    for i in range(N):
        row = [int(x) for x in input().split()]
        profit += row[0]
        add(start, i+1, row[0])
        for v in row[1:]:
            add(i+1, v+N, INF)

    cost = [int(x) for x in input().split()]
    for i in range(M):
        add(i+1+N, end, cost[i])

    flow = max_flow_dinic(start, end)
    exp = [u for u in range(1, N+1) if level[u] > 0]
    print(' '.join(map(str, exp)))
    ins = [u-N for u in range(N+1, N+M+1) if level[u] > 0]
    print(' '.join(map(str, ins)))
    print(profit - flow)