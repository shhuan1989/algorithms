# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/16

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List



if __name__ == '__main__':
    N, M = map(int, input().split())
    H = [0] + [int(x) for x in input().split()]
    E = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        E[u].append(v)
        E[v].append(u)
    
    h = max(H)
    if H.count(h) > 1:
        print("Non")
        exit(0)
    
    start = -1
    for i in range(1, N+1):
        if H[i] == h:
            start = i
            break

    vis = [False for _ in range(N + 1)]
    q = collections.deque([start])
    vis[start] = True
    while q:
        u = q.popleft()
        for v in E[u]:
            if H[v] < H[u] and not vis[v]:
                vis[v] = True
                q.append(v)

    if all([vis[u] for u in range(1, N + 1)]):
        print("Oui, j'ai trouve la solution.")
        print(start)
    else:
        print("Non")
