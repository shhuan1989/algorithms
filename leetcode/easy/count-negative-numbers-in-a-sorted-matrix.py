
# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/16/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            for v in row:
                ans += 1 if v < 0 else 0
        
        return ans
    
s = Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))