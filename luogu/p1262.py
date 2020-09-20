# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/12 21:48

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

sys.setrecursionlimit(10000)
MAXN = 10000
MAXM = 10000
head = [-1 for _ in range(MAXN)]
dfn = [-1 for _ in range(MAXN)]
low = [-1 for _ in range(MAXN)]
vis = [False for _ in range(MAXN)]
color = [-1 for _ in range(MAXN)]

to = [-1 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]

tot = [1]

def add(u, v):
    tot[0] += 1
    i = tot[0]
    to[i] = v
    nxt[i] = head[u]
    head[u] = i


if __name__ == '__main__':
    # sys.stdin = open('P1262_2.in', 'r')
    N = int(input())
    P = int(input())

    t =[]
    cost = {}
    for i in range(P):
        a, b = map(int, input().split())
        t.append((b, a))
        cost[a] = b

    ind = [0 for _ in range(N+1)]
    M = int(input())
    for i in range(M):
        u, v = map(int, input().split())
        ind[v] += 1
        add(u, v)

    t.sort()
    root = [-1 for i in range(N+1)]
    for b, a in t:
        if root[a] < 0:
            root[a] = a
            q = [a]
            while q:
                u = q.pop()
                i = head[u]
                while i > 0:
                    v = to[i]
                    if root[v] != a:
                        root[v] = a
                        q.append(v)
                    i = nxt[i]

    for i in range(1, N+1):
        if root[i] < 0:
            print('NO')
            print(i)
            exit(0)

    print('YES')
    print(sum([cost[u] for u in set(root[1:])]))