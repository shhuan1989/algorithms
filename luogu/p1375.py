# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N = int(input())
    MOD = 10**9 + 7
    
    pii = [1 for _ in range(2*N+1)]
    for i in range(2, 2*N+1):
        pii[i] = i * pii[i-1]
        pii[i] %= MOD
    
    
    def getinv(x):
        return pow(x, MOD-2, MOD)
    
    inv = [getinv(x) for x in pii]
    
    
    ans = pii[2*N]*inv[N]*inv[N+1]
    ans %= MOD
    print(ans)
    # dp = [0 for _ in range(N+1)]
    # dp[0] = 1
    # for n in range(1, N+1):
    #     for a in range(n):
    #         dp[n] += dp[a] * dp[n-a-1]
    #         dp[n] %= MOD
    # print(dp[-1])