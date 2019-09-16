# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/11/19

# f(n, k) = f(n-1, k-1) + f(n-1, k)
"""

import collections
import time
import os
import sys
import bisect
import heapq


N, K = map(int, input().split())
A = [int(x) for x in input().split()]

MOD = 10**9+7
wc = collections.Counter(A)
K = min(K, len(wc.keys()))
    
wc = list(wc.values())
nwc = len(wc)
dp = [[0 for _ in range(K+1)] for _ in range(nwc+1)]
for i in range(nwc+1):
    dp[i][0] = 1
    
for i in range(1, nwc+1):
    for j in range(1, min(i, K)+1):
        dp[i][j] = (dp[i-1][j-1]*wc[i-1] + dp[i-1][j]) % MOD

print(sum(dp[nwc]) % MOD)




