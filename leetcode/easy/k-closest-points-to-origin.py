# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/6/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ds = [(x**2+y**2, x, y) for x, y in points]
        ds.sort()

        return [(x, y) for d, x, y in ds[:K]]
    
s = Solution()
print(s.kClosest(points = [[1,3],[-2,2]], K = 1))
print(s.kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2))