# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


from functools import lru_cache


if __name__ == '__main__':
    # sys.stdin = open('P1352_2.in', 'r')
    # sys.setrecursionlimit(20000)
    N = int(input())
    W = []
    for _ in range(N):
        W.append(int(input()))
    
    g = [[] for _ in range(N)]
    parent = [-1 for _ in range(N)]
    ind = [0 for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[v].append(u)
        parent[u] = v
        ind[v] += 1
    
    q = [v for v in range(N) if ind[v] == 0]
    dp = [[0 for _ in range(2)] for _ in range(N)]
    
    # for u in q:
    #     dp[u][0] = 0
    #
    # for u in range(N):
    #     dp[u][1] = W[u]
    
    ans = 0
    while q:
        nq = []
        for u in q:
            # u = q.popleft()
            dp[u][1] += W[u]
            ans = max(ans, max(dp[u]))
            # print(u, dp[u])
            v = parent[u]
            ind[v] -= 1
            dp[v][0] += max(dp[u])
            dp[v][1] += max(dp[u][0], 0)
            if ind[v] == 0:
                nq.append(v)
                
        q = nq
    print(ans)
    
    
    
    
    
    
    