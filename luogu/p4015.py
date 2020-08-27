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

MAXN = 2000
MAXM = 10005
INF = 10 ** 9 + 7

head = [-1 for _ in range(MAXN)]
vis = [False for _ in range(MAXN)]
pre = [-1 for _ in range(MAXN)]
incf = [0 for _ in range(MAXN)]
dist = [0 for _ in range(MAXN)]

cap = [0 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]
cost = [-1 for _ in range(MAXM)]
to = [-1 for _ in range(MAXM)]

tot = [1]


def add_edge(u, v, w, c):
    tot[0] += 1
    i = tot[0]
    cap[i] = w
    cost[i] = c
    to[i] = v
    nxt[i] = head[u]
    head[u] = i


def add(u, v, w, c):
    add_edge(u, v, w, c)
    add_edge(v, u, 0, -c)


def spfa(start, end, maxfee):
    for i in range(MAXN):
        pre[i] = -1
        dist[i] = -INF if maxfee else INF
        vis[i] = False
    
    vis[start] = True
    dist[start] = 0
    incf[start] = INF
    q = collections.deque([start])
    while q:
        u = q.popleft()
        i = head[u]
        vis[u] = False
        while i > 0:
            v = to[i]
            f = min(cap[i], incf[u])
            if f <= 0:
                i = nxt[i]
                continue
            
            nd = dist[u] + cost[i]
            if (dist[v] < nd) if maxfee else (dist[v] > nd):
                dist[v] = nd
                pre[v] = i
                incf[v] = f
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
            
            i = nxt[i]
    
    return dist[end] > -INF if maxfee else dist[end] < INF


def max_flow(start, end, maxfee):
    ans = 0
    while spfa(start, end, maxfee):
        u = end
        while u != start:
            ans += incf[end] * cost[pre[u]]
            cap[pre[u]] -= incf[end]
            cap[pre[u] ^ 1] += incf[end]
            u = to[pre[u] ^ 1]
    
    return ans


def solve(N, M, A, B, C, maxfee):
    tot[0] = 1
    for i in range(MAXN):
        head[i] = -1
    for i in range(MAXM):
        cap[i] = 0
        nxt[i] = -1
        cost[i] = -1
        to[i] = -1

    start, end = 0, M + N + 1
    for i in range(1, N + 1):
        add(start, i, A[i - 1], 0)

    for u in range(1, N + 1):
        for v in range(N + 1, N + M + 1):
            add(u, v, B[v - N - 1], C[u - 1][v - N - 1])

    for i in range(N + 1, N + M + 1):
        add(i, end, B[i - N - 1], 0)

    return max_flow(start, end, maxfee)


if __name__ == '__main__':
    # sys.stdin = open('p4015.in', 'r')
    N, M = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = []
    for i in range(N):
        row = [int(x) for x in input().split()]
        C.append(row)
    
    print(solve(N, M, A, B, C, False))
    print(solve(N, M, A, B, C, True))
    
    # x = 0
    # for e in edges[2:tot[0]+1]:
    #     # if e.flow > 0 and e.cost > 0:
    #     x += e.flow * e.cost
    #     print(e.start, e.end, e.cap, e.flow, e.cost)
    #
    # print(x)
    

