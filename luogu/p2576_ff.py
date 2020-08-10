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
flow = [0 for _ in range(MAXN)]
vis = [False for _ in range(MAXN)]
pre = [-1 for _ in range(MAXN)]

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
        # pre[i] = -1
        vis[i] = False
        flow[i] = 0

def max_flow_ford_fulkerson(start, end):
    ans = 0
    match = []

    while True:
        reset()
        q = [start]
        flow[start] = INF
        vis[start] = True
        while q:
            u = q.pop()
            if u == end:
                break
            i = link[u]
            while i > 0:
                v = to[i]
                if not vis[v] and cap[i] > 0:
                    vis[v] = True
                    flow[v] = min(flow[u], cap[i])
                    pre[v] = i
                    q.append(v)
                i = nxt[i]

        if not vis[end]:
            break

        ans += 1
        u = end
        while u != start:
            cap[pre[u]] -= flow[end]
            cap[pre[u] ^ 1] += flow[end]
            u = to[pre[u] ^ 1]

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

    max_flow_ford_fulkerson(start, end)