# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/3/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

g = collections.defaultdict(list)
curAns = [0]

N, K = map(int, input().split())
for i in range(N-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

def dfs(u, parent):
    count = [0 for _ in range(K)]
    for i, v in enumerate(g[u]):
        if v == parent:
            continue
        dfs(v, u)
        curAns[0] += dp[v][K-1]
        for k in range(K):
            count[k] += dp[v][k]
    
    for vi, v in enumerate(g[u]):
        for ka in range(K-1):
            kb = K - ka -2
            cka = dp[v][ka]
            ckb = count[kb] - dp[v][kb]
            curAns[0] += cka * ckb
        
        for k in range(K):
            count[k] -= dp[v][k]
    
    for v in g[u]:
        if v != parent:
            for k in range(K):
                dp[u][k+1] += dp[v][k]
    
    dp[u][0] = 1

    
dfs(1, -1)
print(curAns[0])