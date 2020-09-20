# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/18 10:08

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

MAXN = 50000

head = [-1 for _ in range(MAXN)]
cost = [-1 for _ in range(MAXN)]
nxt = [-1 for _ in range(MAXN)]
to = [-1 for _ in range(MAXN)]
fee = [-1 for _ in range(MAXN)]
isleaf = [False for _ in range(MAXN)]
usercount = [0 for _ in range(MAXN)]

tot = [1]

def add(u, v, w):
    tot[0] += 1
    i = tot[0]
    cost[i] = w
    to[i] = v
    nxt[i] = head[u]
    head[u] = i

def dfs1(curr):
    if isleaf[curr]:
        usercount[curr] = 1
        return 1

    i = head[curr]
    c = 0
    while i > 0:
        v = to[i]
        c += dfs1(v)
        i = nxt[i]
    usercount[curr] = c
    return c


def dfs(curr, dist):
    if isleaf[curr]:
        return fee[curr] - dist


    i = head[curr]
    profit = float('-inf')
    while i > 0:
        v = to[i]
        for uc in range(usercount[v] + 1):
            dfs(v, classmethod)

        profit = max(profit, dfs(to[i], ))
        i = nxt[i]


if __name__ == '__main__':
    N, M = map(int, input().split())
    for u in range(1, N-M+1):
        row = [int(x) for x in input().split()]
        for ri in range(1, len(row), 2):
            v, w = row[ri], row[ri+1]
            add(u, v, w)
    line = [int(x) for x in input().split()]
    for i in range(M):
        fee[N-M+i+1] = line[i]
        isleaf[N-M+i+1] = True


