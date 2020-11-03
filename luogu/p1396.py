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
    # sys.stdin = open('P1396_1.in', 'r')
    N, M, S, T = map(int, input().split())
    E = [[] for _ in range(N+1)]
    W = {}
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        E[u].append(v)
        E[v].append(u)
        W[(u, v)] = min(W.get((u, v), float('inf')), w)
        W[(v, u)] = min(W.get((v, u), float('inf')), w)
        
    dist = [float('inf') for _ in range(N+1)]
    dist[S] = 0
    q = collections.deque([S])
    inq = [False for _ in range(N+1)]
    inq[S] = True
    
    while q:
        u = q.popleft()
        inq[u] = False
        
        for v in E[u]:
            nd = max(dist[u], W[(u, v)])
            if dist[v] > nd:
                dist[v] = nd
                if not inq[v]:
                    inq[v] = True
                    q.append(v)
    

    # print(dist)
    print(dist[T])