# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/8 09:49

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

MAXN = 50000
MAXM = 3 * 10**5

INF = 10**9 + 7
head = [0 for _ in range(MAXN)]
vis = [False for _ in range(MAXN)]
pre = [-1 for _ in range(MAXN)]
level = [-1 for _ in range(MAXN)]
curIndex = [0 for _ in range(MAXN)]

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
        curIndex[i] = head[i]


def dfs(curr, end, flow):
    if curr == end or flow <= 0:
        return flow

    ans = 0
    i = curIndex[curr]
    while i > 0 and flow > 0:
        v = to[i]
        curIndex[curr] = i
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
    sys.stdin = open('P3355_3.in', 'r')
    # t0 = time.time()
    N, M = map(int, input().split())

    def getid(x, y):
        return (x-1) * N + y

    start, end = 0, N*N+1
    barrier = [[False for _ in range(N+1)] for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        barrier[x][y] = True

    for r in range(1, N+1):
        for c in range(1, N+1):
            if barrier[r][c]:
                continue
            u = getid(r, c)
            if (r+c) % 2 != 0:
                add(start, u, 1)
                for x, y in [(r - 1, c-2), (r - 2, c - 1), (r - 2, c + 1), (r-1, c + 2), (r + 1, c + 2), (r + 2, c+1),
                             (r + 2, c - 1), (r + 1, c - 2)]:
                    if 1 <= x <= N and 1 <= y <= N and not barrier[x][y]:
                        v = getid(x, y)
                        add(u, v, INF)
            else:
                add(u, end, 1)

    # print('build {}'.format(time.time() - t0))
    f = max_flow_dinic(start, end)
    # print('cal {}'.format(time.time() - t0))
    # print(f)
    print(N*N - M - f)



