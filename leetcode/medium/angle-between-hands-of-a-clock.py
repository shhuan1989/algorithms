# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
    
        b = 360 * minutes / 60
        
        a = 360 * hour / 12 + 360 / 12 * minutes / 60
        
        c = (b-a+360) % 360
        
        return min(c, 360-c)
    

s = Solution()
print(s.angleClock(12, 30))
print(s.angleClock(3, 30))
print(s.angleClock(3, 15))
print(s.angleClock(4, 50))
print(s.angleClock(12, 0))