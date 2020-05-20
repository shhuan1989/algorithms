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
    def isPossible(self, target: List[int]) -> bool:
        
        q = [-v for v in target]
        heapq.heapify(q)
        
        s = sum(target)
        while True:
            v = heapq.heappop(q)
            v = -v

            s -= v
            
            if v == 1:
                return True
            if v < 1:
                return False
            
            u = v - s
            if u <= 0:
                return False
            heapq.heappush(q, -u)
            s += u
            # s -= v
            # s += u
        
s = Solution()
print(s.isPossible([9, 3, 5]))
print(s.isPossible([1, 1, 1, 2]))
print(s.isPossible([8, 5]))