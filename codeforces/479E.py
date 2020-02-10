# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/17/20

convert naive O(N^3)
for k in range(K):
    for x in range(N+1):
        for y in range(x-d, x+d):
            dp[k+1][y] += dp[k][x]

to O(N^2)

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A, B, K):
    MOD = 1000000007
    
    dp = [0 for _ in range(N+1)]
    dp[A] = 1
    for k in range(1, K+1):
        ndp = [0 for _ in range(N+1)]
        for x in range(1, N+1):
            d = abs(x-B)
            if d <= 1:
                continue
            l, r = max(x-d+1, 1), min(x+d, N+1)
            if l < x:
                ndp[l] = (ndp[l] + dp[x]) % MOD
                ndp[x] = (ndp[x] - dp[x]) % MOD
            if x < r:
                if x + 1 <= N:
                    ndp[x+1] = (ndp[x+1] + dp[x]) % MOD
                if r <= N:
                    ndp[r] = (ndp[r] - dp[x]) % MOD
                
        v = 0
        for x in range(N+1):
            v += ndp[x]
            v %= MOD
            ndp[x] = v
        
        dp = ndp
    
    return sum(dp) % MOD


N, A, B, K = map(int, input().split())
print(solve(N, A, B, K))