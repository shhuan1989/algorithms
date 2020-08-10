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
    # sys.stdin = open('p2763.in', 'r')
    K, N = map(int, input().split())
    start, end = 0, N+K+1
    wanted = [int(x) for x in input().split()]
    for i in range(K):
        add(i+N+1, end, wanted[i])

    for i in range(N):
        d = [int(x) for x in input().split()]
        for c in d[1:]:
            add(i+1, N+c, 1)

    for i in range(1, N+1):
        add(start, i, 1)

    flow = max_flow_dinic(start, end)
    if flow != sum(wanted):
        print('No Sulution!')
    else:
        for c in range(1, K+1):
            u = c + N
            i = head[u]
            p = []
            while i > 0:
                if 1 <= to[i] <= N and cap[i] > 0:
                    p.append(to[i])
                i = nxt[i]
            print('{}: {}'.format(c, ' '.join(map(str, sorted(p)))))