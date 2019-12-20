# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/18/19

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
    def numWays(self, n: int, k: int) -> int:
        if n == 0 :
            return 0
        @lru_cache(None)
        def paint(i):
            if i==2:
                return k*k
            if i== 1:
                return k
            return (paint(i-2)+paint(i-1))*(k-1)
        return paint(n)
        

s = Solution()
print(s.numWays(6, 2))
print(s.numWays(4, 3))
print(s.numWays(4, 1))
print(s.numWays(5, 2))
print(s.numWays(3, 2))
print(s.numWays(0, 0))