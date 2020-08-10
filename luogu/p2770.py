# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/6 21:18

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


class Node:
    def __init__(self, u, v, cap, flow, cost):
        self.u = u
        self.v = v
        self.cap = cap
        self.flow = flow
        self.cost = cost
        self.nxt = -1

INF = 10**9+7
MAXN = 1000
MAXM = 10**5

edges = [Node(0, 0, 0, 0, 0) for _ in range(MAXM)]
head = [-1 for _ in range(MAXN)]
incf = [0 for _ in range(MAXN)]
vis = [0 for _ in range(MAXN)]
pre = [0 for _ in range(MAXN)]
dist = [0 for _ in range(MAXN)]
tot = [1]


def add_edge(u, v, w, c):
    tot[0] += 1
    i = tot[0]
    edges[i].u = u
    edges[i].v = v
    edges[i].cap = w
    edges[i].cost = c
    edges[i].nxt = head[u]
    head[u] = i


def add(u, v, w, c):
    add_edge(u, v, w, c)
    add_edge(v, u, 0, -c)


def spfa(start, end):
    for i in range(MAXN):
        incf[i] = 0
        vis[i] = False
        pre[i] = -1
        dist[i] = -INF

    q = collections.deque([start])
    vis[start] = True
    dist[start] = 0
    incf[start] = INF
    while q:
        u = q.popleft()
        i = head[u]
        vis[u] = False
        while i > 0:
            e = edges[i]
            v = e.v
            if e.cap - e.flow > 0:
                nd = dist[u] + e.cost
                if nd > dist[v]:
                    dist[v] = nd
                    pre[v] = i
                    incf[v] = min(e.cap-e.flow, incf[u])
                    if not vis[v]:
                        vis[v] = True
                        q.append(v)
            i = e.nxt

    return dist[end] > 0


def mcmf(start, end):
    ans = 0
    # paths = []
    while spfa(start, end):
        ans += incf[end]
        u = end
        path = []
        while u != start:
            e = edges[pre[u]]
            # path.append(e.v)
            # ans += e.cost * incf[end]
            e.flow += incf[end]
            edges[pre[u] ^ 1].flow -= incf[end]
            u = e.u
        # print(path[::-1])
        # paths.append(path[::-1])
    return ans


def getpath(curr, end, path):
    if curr == end:
        return path

    i = head[curr]
    while i > 0:
        e = edges[i]
        v = e.v
        if e.flow == 1:
            p = getpath(v, end, path + [v])
            if p:
                e.flow = 0
                return p
        i = e.nxt
    return []

if __name__ == '__main__':
    # sys.stdin = open('p2770.in', 'r')
    N, M = map(int, input().split())
    via, vib = {}, {}
    direct = False
    cities = ['']
    for i in range(N):
        name = input().strip()
        cities.append(name)
        via[name] = i + 1
        vib[name] = N + i + 1
    start, end = 0, N+N+1

    add(start, 1, 2, 0)
    add(N+N, end, 2, 0)

    for i in range(2, N):
        add(i, i+N, 1, 1)
    add(1, 1+N, 2, 1)
    add(N, N+N, 2, 1)

    for i in range(M):
        a, b = input().strip().split()
        u, v = via[a], via[b]
        if u > v:
            u, v = v, u
        if u == 1 and v == N:
            direct = True

        add(u+N, v, 1, 0)

    flow = mcmf(start, end)
    if flow < 2:
        if direct:
            print(2)
            print(cities[1])
            print(cities[N])
            print(cities[1])
        else:
            print('No Solution!')
    else:
        iva = {i: v for v, i in via.items()}
        path = [cities[1]]
        path += [iva[i] for i in getpath(N+1, N, []) if 1 <= i <= N]
        path += [iva[i] for i in reversed(getpath(N+1, N, [])) if 1 <= i < N]
        path += [cities[1]]
        print(len(path) - 1)
        print('\n'.join(path))


