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
created by shhuan at 2020/7/24 19:14

"""

MAXN = 400005

class Node:
    def __init__(self):
        self.to = 0
        self.next = 0

E = [Node() for _ in range(MAXN)]
head = [0 for _ in range(MAXN)]
ecount = 1


def add(u, v, index):
    E[index].to = v
    E[index].next = head[u]
    head[u] = index



if __name__ == '__main__':
    N, M= map(int, input().split())

    # G = collections.defaultdict(list)
    for i in range(M):
        u, v = map(int, input().split())
        # G[u].append(v)
        # G[v].append(u)
        ecount += 1
        add(u, v, ecount)
        ecount += 1
        add(v, u, ecount)


    K = int(input())
    destroy = []
    merged = [True for _ in range(N)]
    for i in range(K):
        u = int(input())
        destroy.append(u)
        merged[u] = False

    parent = [i for i in range(N)]
    rank = [1 for i in range(N)]
    def find(u):
        pu = parent[u]
        if pu == u:
            return pu
        parent[u] = find(pu)
        return parent[u]

    def union(u, v):
        pu, pv = find(u), find(v)
        if pu == pv:
            return False

        if rank[pu] > rank[pv]:
            parent[pv] = pu
            rank[pu] += rank[pv]
        else:
            parent[pu] = pv
            rank[pv] += rank[pu]
        return True


    c = N - len(destroy)
    for u in range(N):
        if not merged[u]:
            continue
        vi = head[u]
        while vi > 0:
            v = E[vi].to
            if merged[v]:
                c -= 1 if union(u, v) else 0
            vi = E[vi].next
    ans = [c]
    for u in reversed(destroy):
        c = ans[-1] + 1
        add = []
        vi = head[u]
        while vi > 0:
            v = E[vi].to
            if merged[v]:
                add.append(v)
                c -= 1 if union(u, v) else 0
            vi = E[vi].next

        ans.append(c)
        merged[u] = True

    print('\n'.join(map(str, reversed(ans))))
