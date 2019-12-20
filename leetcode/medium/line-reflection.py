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


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True
        
        minx = min([x for x, y in points])
        maxx = max([x for x, y in points])
        
        mid = (minx + maxx) / 2
        
        left = {(x, y) for x, y in points if x < mid}
        right = list({(x, y) for x, y in points if x > mid})
        
        if len(left) != len(right):
            return False
        
        mirror = [(int(2 * mid - x), y) for x, y in left]
        mirror.sort()
        right.sort()
        
        return mirror == right
    

s = Solution()
print(s.isReflected([[1,1],[-1,1]]))
print(s.isReflected([[1,1],[-1,-1]]))