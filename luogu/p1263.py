# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

INF = 10 ** 9 + 7
MAXN = 40000
MAXM = 2 * 10 ** 5 + MAXN

head = [-1 for _ in range(MAXN)]
level = [-1 for _ in range(MAXN)]

cap = [-1 for _ in range(MAXM)]
flow = [0 for _ in range(MAXM)]
to = [-1 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]

tot = [1]


def add_edge(u, v, w):
    tot[0] += 1
    i = tot[0]
    cap[i] = w
    to[i] = v
    nxt[i] = head[u]
    head[u] = i


def add(u, v, w):
    add_edge(u, v, w)
    add_edge(v, u, 0)


def bfs(start, end):
    for i in range(MAXN):
        level[i] = -1
    
    level[start] = 0
    q = collections.deque([start])
    while q:
        u = q.pop()
        i = head[u]
        while i > 0:
            v = to[i]
            if level[v] < 0 and cap[i] - flow[i] > 0:
                level[v] = level[u] + 1
                q.append(v)
            i = nxt[i]
    
    return level[end] > 0


def dfs(curr, end, add):
    if curr == end or add <= 0:
        return add
    
    x = 0
    i = head[curr]
    while i > 0 and add > 0:
        v = to[i]
        if level[v] == level[curr] + 1 and cap[i] - flow[i] > 0:
            f = dfs(v, end, min(add, cap[i] - flow[i]))
            if f > 0:
                add -= f
                x += f
                flow[i] += f
                flow[i ^ 1] -= f
        i = nxt[i]
    
    return x


def dinic(start, end):
    ans = 0
    while bfs(start, end):
        ans += dfs(start, end, INF)
    
    return ans


def draw():
    g = collections.defaultdict(list)
    for u in range(MAXN):
        i = head[u]
        while i > 0:
            if cap[i] > 0:
                g[u].append((to[i], cap[i]))
            i = nxt[i]
    
    # print(len(g))
    for u, vs in g.items():
        for v, w in vs:
            # ru, cu = (u-1)//(M+1), (u-1) % (M+1)
            # rv, cv = (v - 1) // (M + 1), (v - 1) % (M + 1)
            # print('{}-{} {}-{} {}'.format(ru, cu, rv, cv, w))
            print('{} {}'.format(u, v))


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        row = [int(x) for x in input().split()]
        A.append(row)
    
    xymap = {}
    
    
    def getid(r, c, t):
        v = r * (M + 1) + c + 1 + t * (N + 2) * (M + 2)
        xymap[v] = (r, c)
        return v
    
    
    start, end = 0, getid(N, M, 1) + 1
    
    for c in range(M):
        wall = N
        vis = set()
        # add(start, getid(wall, c), 1)
        for r in range(N - 1, -1, -1):
            if A[r][c] == 2:
                wall = r
                # add(start, getid(wall, c), 1)
            elif A[r][c] == 0:
                if wall not in vis:
                    add(start, getid(wall, c, 0), 1)
                    vis.add(wall)
                add(getid(wall, c, 0), getid(r, c, 0), 1)
            else:
                pass
    
    for r in range(N):
        wall = M
        vis = set()
        for c in range(M - 1, -1, -1):
            if A[r][c] == 2:
                wall = c
            elif A[r][c] == 0:
                if wall not in vis:
                    add(getid(r, wall, 1), end, 1)
                    vis.add(wall)
                add(getid(r, c, 0), getid(r, wall, 1), 1)
    
    # draw()
    print(dinic(start, end))
    
    ans = []
    for u in range(MAXN):
        i = head[u]
        while i > 0:
            v = to[i]
            if flow[i] == 1 and v in xymap:
                r, c = xymap[v]
                if 0 <= r < N and 0 <= c < M and A[r][c] == 0:
                    ans.append((r + 1, c + 1))
                    # print('({}, {}, {}) -> ({}, {}, {})'.format(xymap[u][0], xymap[u][1], u, r, c, v))
            i = nxt[i]
    
    # print(len(ans))
    print('\n'.join(['{} {}'.format(r, c) for r, c in ans]))
    
    # draw()




