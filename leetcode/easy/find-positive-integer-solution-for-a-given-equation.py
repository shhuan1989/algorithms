# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/9/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""

class CustomFunction:
    def f(self, x, y):
        return x + y

class Solution:
    def findSolution(self, customfunction, z: int) -> List[List[int]]:
        ans = []
        tlo, thi = 1, z+1
        for x in range(1, z+1):
            if customfunction.f(x, 1) > z:
                break
            if customfunction.f(x, z) < z:
                continue
            lo, hi = tlo, thi
            while lo <= hi:
                y = (lo + hi) // 2
                pz = customfunction.f(x, y)
                if pz == z:
                    ans.append((x, y))
                    thi = y
                    break
                elif pz > z:
                    hi = y - 1
                else:
                    lo = y + 1
    
        return ans
    
s = Solution()
print(s.findSolution(CustomFunction(), 5))