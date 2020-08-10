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

MAXN = 5000
MAXM = 2 * 10**5

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
    # sys.stdin = open('P2766_7.in', 'r')
    N = int(input())
    A = []
    while len(A) < N:
        A += [int(x) for x in input().split()]

    if N == 1:
        print(1)
        print(1)
        print(1)
        exit(0)

    dp = [1 for i in range(N)]
    for i in range(N):
        for j in range(i):
            if A[j] <= A[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    maxf = max(dp)
    print(maxf)

    fi = collections.defaultdict(list)
    for i in range(N):
        fi[dp[i]].append(i+1)


    def getid(u, k):
        return u + k * N

    start, end = 0, getid(N, 1)+1
    for v in fi[1]:
        add(start, getid(v, 0), 1)

    for v in range(1, N+1):
        add(getid(v, 0), getid(v, 1), 1)

    for i in range(1, maxf):
        for u in fi[i]:
            for v in fi[i+1]:
                if u < v and A[u-1] <= A[v-1]:
                    add(getid(u, 1), getid(v, 0), 1)
    for v in fi[maxf]:
        add(getid(v, 1), end, 1)

    f = max_flow_dinic(start, end)
    print(f)

    add(start, getid(1, 0), INF)
    add(getid(1, 0), getid(1, 1), INF)

    if dp[N-1] == maxf:
        add(getid(N, 0), getid(N, 1), INF)
        add(getid(N, 1), end, INF)

    f += max_flow_dinic(start, end)
    print(f)



