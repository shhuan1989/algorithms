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

MAXN = 200
MAXM = 10**5

INF = 10**9 + 7
link = [0 for _ in range(MAXN)]
vis = [False for _ in range(MAXN)]
pre = [-1 for _ in range(MAXN)]
level = [-1 for _ in range(MAXN)]

cap = [0 for _ in range(MAXM)]
to = [0 for _ in range(MAXM)]
nxt = [0 for _ in range(MAXM)]


tot = [1]

def add(u, v, w):
    tot[0] += 1
    i = tot[0]
    nxt[i] = link[u]
    cap[i] = w
    to[i] = v
    link[u] = i

def reset():
    for i in range(MAXN):
        pre[i] = -1
        vis[i] = False
        level[i] = -1

def dfs(curr, end, flow):
    if curr == end or flow <= 0:
        return flow

    ans = 0
    i = link[curr]
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
        i = link[u]
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
    match = []

    while bfs(start, end):
        ans += dfs(start, end, INF)

    print(ans)
    for u in range(1, M+1):
        i = link[u]
        while i > 0:
            v = to[i]
            if M+1 <= v <= N and cap[i] == 0:
                match.append((u, v))
            i = nxt[i]
    print('\n'.join(['{} {}'.format(u, v) for u, v in match]))




if __name__ == '__main__':
    # sys.stdin = open('p2756_3.in', 'r')
    M, N = map(int, input().split())

    while True:
        u, v = map(int, input().split())
        if u == -1 and v == -1:
            break
        if 1 <= u <= M and 1 <= v <= N:
            add(u, v, 1)
            add(v, u, 0)

    start, end = 0, N+1
    for i in range(1, M+1):
        add(start, i, 1)
        add(i, start, 0)

    for i in range(M+1, N+1):
        add(i, end, 1)
        add(end, i, 0)

    max_flow_dinic(start, end)