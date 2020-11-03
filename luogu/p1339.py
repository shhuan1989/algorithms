# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/14

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, M, S, T = map(int, input().split())
    g = collections.defaultdict(list)
    W = collections.defaultdict(int)
    for i in range(M):
        u, v, w = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
        W[u, v] = w
        W[v, u]  = w
        
    q = collections.deque([S])
    INF = float('inf')
    dist = [INF for _ in range(N+1)]
    dist[S] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] > dist[u] + W[u, v]:
                dist[v] = dist[u] + W[u, v]
                q.append(v)
    
    print(dist[T])