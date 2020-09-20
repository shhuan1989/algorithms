# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/12 21:25

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

MAXN = 2000
MAXM = 10000
head = [-1 for _ in range(MAXN)]

nxt = [-1 for _ in range(MAXM)]
to = [-1 for _ in range(MAXM)]
cost = [-1 for _ in range(MAXM)]

tot = [1]


def add(u, v, w):
    tot[0] += 1
    i = tot[0]

    to[i] = v
    cost[i] = w
    nxt[i] = head[u]
    head[u] = i


if __name__ == '__main__':
    N, M = map(int, input().split())

    for i in range(M):
        u, v, w = map(int, input().split())
        add(v, u, w)

    dist = [float('inf') for _ in range(N+1)]
    inq = [False for _ in range(N + 1)]
    count = [0 for _ in range(N+1)]
    for start in range(1, N+1):
        if dist[start] == float('inf'):
            dist[start] = 0
            q = collections.deque([start])
            while q:
                u = q.popleft()
                inq[u] = False
                i = head[u]
                while i > 0:
                    v = to[i]
                    w = cost[i]
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        if not inq[v]:
                            count[v] += 1
                            if count[v] > N:
                                print('NO SOLUTION')
                                exit(0)
                            inq[v] = True
                            q.append(v)
                    i = nxt[i]

    md = min(dist)
    print('\n'.join(map(str, [v-md for v in dist[1:]])))