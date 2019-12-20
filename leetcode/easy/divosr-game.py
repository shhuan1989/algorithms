# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/20/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache
import math

class Solution:
    def divisorGame(self, N: int) -> bool:
        def mex(x):
            i = 0
            while i in x:
                i += 1
            
            return i
        
        @lru_cache(maxsize=None)
        def dfs(n):
            if n <= 1:
                return 0
            
            vis = set()
            for i in range(1, min(int(math.sqrt(n))+1, n-1) + 1):
                if n % i == 0:
                    vis.add(dfs(n-i))
            
            return mex(vis)
        
        return dfs(N) > 0


s = Solution()
print(s.divisorGame(2))
print(s.divisorGame(3))