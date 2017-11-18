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
created by shhuan at 2017/11/18 22:07

"""

N, M = map(int, input().split())

E = collections.defaultdict(set)
W = collections.defaultdict(list)
A = [(-1, -1, -1)]
for i in range(M):
    u, v, w = map(int, input().split())
    E[u].add(v)
    E[v].add(v)
    W[w].append((u, v))
    W[w].append((v, u))
    A.append((u, v, w))


def dfs(u, fa, vis, e):
    for v in e[u]:
        if v != fa:
            if v in vis:
                return True
            else:
                return dfs(v, u, vis | {v}, e)

    return False

def cycle(e):

    for u in s:
        if dfs(u, -1, set(), e):
            return True

    return False


def transform(u, fa, e, vis):
    pass

Q = int(input())
for qi in range(Q):
    q = [int(x) for x in input().split()]

    minw = float('inf')
    for i in q[1:]:
        u, v, w = A[i]
        minw = min(minw, w)

    e = collections.defaultdict(set)
    s = set()
    for w in range(minw):
        for u, v in W[w]:
            e[u].add(v)
            e[v].add(u)
            s.add(u)
            s.add(v)
    # if cycle(e):
    #     print("NO")
    #     exit(0)

    group = {}
    num = N+1
    for u in s:
        if u not in group:
            p = [u]
            while p:
                v = p.pop()
                group[v] = num
                for w in e[v]:
                    if w not in group:
                        p.append(w)
            num += 1
    e = collections.defaultdict(set)
    s = set()
    for i in q[1:]:
        u, v, w = A[i]
        if u in group:
            u = group[u]
        if v in group:
            v = group[v]
        e[u].add(v)
        e[v].add(u)
        s.add(u)
        s.add(v)

    if not cycle(e):
        print("YES")
    else:
        print("NO")




