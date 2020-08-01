# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/7/18 21:37

"""


def dfs(u, n, pre, graph, vis):
    if len(pre) >= n:
        return pre
    for v in graph[u]:
        if v not in vis:
            a = dfs(v, n, pre+[v], graph, vis|{v})
            if a:
                return a

    return []


def bfs(start, size, graph):

    q = [([start], {start}, 0)]
    while q:
        link, vis, t = q.pop()
        if len(link) >= size:
            return link

        u = link[-1]
        for i in range(t, len(graph[u])):
            v = graph[u][i]
            if v not in vis:
                if i + 1 < len(graph[u]):
                    q.append((link, vis, i+1))
                q.append((link + [v], vis | {v}, 0))
                break

    return []


def solve(N, A):
    A.sort()
    ind = collections.defaultdict(int)
    outd = collections.defaultdict(int)
    G = collections.defaultdict(list)
    RG = collections.defaultdict(list)
    for i in range(N):
        ind[A[i][0]] += 1
        outd[A[i][-1]] += 1
        for j in range(N):
            if i != j and A[i][-1] == A[j][0]:
                G[i].append(j)
                RG[i].append(j)
                RG[j].append(i)

    a = len([1 for i in range(N) if outd[i] != ind[i]])
    if a > 2:
        return '***'

    # connected
    vis = [0 for _ in range(N)]
    vis[0] = 1
    q = [0]
    while q:
        u = q.pop()
        for v in RG[u]:
            if vis[v] == 0:
                vis[v] = 1
                q.append(v)
    if sum(vis) != N:
        return '***'

    start = 0
    for i in range(N):
        if ind[A[i][0]] - outd[A[i][0]] == 1:
            start = i
            break

    # ans = dfs(start, N, [start], G, {start})
    ans = bfs(start, N, G)
    if ans:
        return '.'.join([A[i] for i in ans])

    return '***'


if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        A.append(input().strip())

    print(solve(N, A))
