# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/1/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        
        
        
        # f(a,b) = 0.25(f(a-100, b) + f(a-75, b-25) + f(a-50, b-50) + f(a-25, b-75))
        
        memo = {}
        q = [(N, N)]
        
        while q:
            a, b = q.pop()
            
            if a <= 0 and b <= 0:
        
        
        
        
        
        memo = {}
        
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            
            key = (a, b)
            
            if key in memo:
                return memo[key]
            
            ans = 0.25 * (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b - 50) + dfs(a - 25, b - 75))
            
            memo[key] = ans
            
            return ans
        
        return dfs(N, N)




s = Solution()
print(s.soupServings(10**8))