# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/3 21:04

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



if __name__ == '__main__':
    N, M = map(int, input().split())
    fix = [[] for _ in range(N+1)]
    for _ in range(M):
        t, a, b = input().strip().split()
        t = int(t)
        u, v = 0, 0
        for i, c in enumerate(a):
            if c == '+':
                fix[i].append((a, b, t))
        if '+' not in a:
            fix[N].append((a, b, t))

    def check(bug, patch):
        for i, v in enumerate(patch):
            if v == '+':
                if bug & (1 << i) <= 0:
                    return False
            elif v == '-':
                if bug & (1 << i) > 0:
                    return False
        return True

    def apply(bug, patch):
        for i, v in enumerate(patch):
            if v == '+':
                bug |= 1 << i
            elif v == '-':
                bug |= 1 << i
                bug ^= 1 << i
            else:
                pass
        return bug

    INF = 10**9+7
    dist = [INF for _ in range(2**N)]
    start, end = 2**N-1, 0
    dist[start] = 0
    q = collections.deque([start])
    inq = [False for _ in range(2**N)]
    while q:
        u = q.popleft()
        inq[u] = False
        for i in range(N+1):
            if i == N or u & (1 << i) > 0:
                for a, b, t in fix[i]:
                    if check(u, a):
                        v = apply(u, b)
                        if dist[u] + t < dist[v]:
                            dist[v] = dist[u] + t
                            if not inq[v]:
                                inq[v] = True
                                q.append(v)

    print(dist[0] if dist[0] < INF else 0)




