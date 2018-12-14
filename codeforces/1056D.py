# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/13 20:13

"""


N = int(input())
p = [int(x) for x in input().split()]

G = collections.defaultdict(list)
for i, v in enumerate(p):
    u = i + 2
    G[u].append(v)
    G[v].append(u)


root = 1
vis = [False] * (N+1)
vis[1] = True
leafs = []
parents = [0] * (N+1)

q = [1]
while q:
    u = q.pop(0)
    childcount = 0
    for v in G[u]:
        if not vis[v]:
            vis[v] = True
            parents[v] = u
            q.append(v)
            childcount += 1
    if childcount == 0:
        leafs.append(u)

print(parents)
print(leafs)
counts = [0] * (N+1)
q = {u for u in leafs}
vis = [False] * (N+1)
while q:
    nq = set()
    for node in q:
        if vis[node]:
            continue
        counts[node] += 1
        vis[node] = True
        parent = parents[node]
        if parent > 0:
            nq.add(parent)
        while parent > 0:
            counts[parent] += 1
            parent = parents[parent]
    q = nq

ans = [0] * (N+1)
for k in range(1, len(leafs) + 1):
    ans[k] = 1


nodes = {parents[node] for node in leafs}

k = len(leafs)
while k < N:
    child_count = [counts[u] for u in nodes]
    child_count.sort()
    n = len(child_count)

    for i in range(n):
        ans[k+i+1] = child_count[i] - 1

    for node in nodes:
        counts[parents[node]] += counts[node] + 1

    k += n

    nodes = {parents[node] for node in nodes}

print(' '.join(map(str, ans[1:])))




