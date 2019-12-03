# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/30 16:34

"""

R, C, N = map(int, input().split())

fields = set()
for i in range(N):
    r, c = map(int, input().split())
    fields.add((r, c))

parent = {}


def find(u):
    v = u if u not in parent or parent[u] == -1 or parent[u] == u else find(parent[u])
    parent[u] = v
    return v


def union(u, v):
    if u == v:
        return
    pu, pv = find(u), find(v)
    parent[pu] = pv


def xy2index(x, y):
    return x * R + y

for x, y in fields:
    ixy = xy2index(x, y)
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if (nx, ny) in fields:
            inxy = xy2index(nx, ny)
            union(ixy, inxy)

groups = collections.defaultdict(list)
for x, y in fields:
    ixy = xy2index(x, y)
    groups[find(ixy)].append((x, y))

print(groups)
ans = 0
for g in groups.values():
    count = 0
    for x, y in g:
        s = 4
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if (nx, ny) in fields:
                s -= 1
        count += s
    ans = max(ans, count)

print(ans)