# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/24
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


class Solution:
    def keyboard(self, k: int, n: int) -> int:
        
        mod = 10 ** 9 + 7
        maxn = 26*26+1
        fact = [1 for _ in range(maxn)]
        for i in range(1, maxn):
            fact[i] = (i * fact[i-1]) % mod
            
        def inv(x):
            return pow(x, mod-2, mod)
        
        def ncr(c, r):
            if r == 0 or r == c:
                return 1
            if c < r:
                return 0
            if r == 1:
                return c
            
            return (fact[c] * inv(fact[r] * fact[c-r])) % mod
        
        dp = [[0 for _ in range(n+1)] for _ in range(26)]
        for i in range(26):
            dp[i][0] = 1
        
        for i in range(min(k, n)+1):
            dp[0][i] = 1
        
        for i in range(1, 26):
            for j in range(1, n+1):
                for x in range(min(k, j) + 1):
                    dp[i][j] += dp[i-1][j-x] * ncr(j, x)
                    dp[i][j] %= mod
        
        return dp[-1][n]

    
if __name__ == '__main__':
    s = Solution()
    print(s.keyboard(1, 1))
    print(s.keyboard(1, 2))
    print(s.keyboard(5, 50))
