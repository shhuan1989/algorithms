# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        dp = [[float('inf') for _ in range(n+2)] for _ in range(n+2)]
        for i in range(1, n+1):
            dp[i][1] = 0
            dp[i][0] = 0
            
        for gap in range(2, n+1):
            for start in range(1, n-gap+2):
                for guess in range(start+gap//2-1, start+gap):
                    dp[start][gap] = min(dp[start][gap], guess + max(dp[start][guess-start], dp[guess+1][start+gap-guess-1]))
        
        return dp[1][n]
        
    
    def getMoneyAmount_2(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def guess(l, r):
            if l >= r:
                return 0
            
            ans = float('inf')
            for i in range((l+r)//2, r+1):
                ans = min(i + max(guess(l, i-1), guess(i+1, r)), ans)
            
            return ans
            
        return guess(1, n)
        

s = Solution()
print(s.getMoneyAmount(10))
