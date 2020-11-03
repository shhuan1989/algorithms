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
    N, M = map(int, input().strip().split())
    g = collections.defaultdict(list)
    rg = collections.defaultdict(list)
    W = collections.defaultdict(int)
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        rg[v].append(u)
        W[u, v] = w
        
    
    cost = [float('inf') for _ in range(N)]
    cost[0] = 0
    q = collections.deque([0])
    while q:
        u = q.popleft()
        for v in g[u]:
            ncost = cost[u] + W[u, v]
            if ncost < cost[v]:
                cost[v] = ncost
                q.append(v)
    
    ans = sum(cost)
    
    cost = [float('inf') for _ in range(N)]
    cost[0] = 0
    q = collections.deque([0])
    while q:
        u = q.popleft()
        for v in rg[u]:
            ncost = cost[u] + W[v, u]
            if ncost < cost[v]:
                cost[v] = ncost
                q.append(v)
    
    # print(cost)
    # print(sum(cost))
    ans += sum(cost)
    print(ans)
    