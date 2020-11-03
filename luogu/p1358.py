# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache
sys.setrecursionlimit(10000)
if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(x) for x in input().split()]
    MOD = 10007
    
    dp = [[0 for _ in range(101)] for _ in range(N+1)]
    for c in range(N+1):
        dp[c][0] = 1
    
    for c in range(N+1):
        for r in range(1, min(c+1, 101)):
            dp[c][r] += dp[c-1][r-1] + (dp[c-1][r] if r <= c-1 else 0)
            dp[c][r] %= MOD
    
    # @lru_cache(maxsize=None)
    def ncr(c, r):
        if r == 0 or r == c:
            return 1
        if c < r:
            return 0
        
        return dp[c][min(r, c-r)]
        
        # return ncr(c-1, r-1) + ncr(c-1, r)
        
    
    ans = 1
    m = N
    
    for a in A:
        ans *= ncr(m, a)
        ans %= MOD
        m -= a
    print(ans)
    
    
    