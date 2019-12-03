# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/29/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

from typing import List

import random

class Solution:
    
    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        blacklist = [v for v in blacklist if 0 <= v < N]
        self.M = N - len(blacklist)
        self.blacklist = list(sorted(blacklist))
    
    def pick(self) -> int:
        v = random.randint(0, self.M-1)
        
        lo, hi = 0, self.N-1
        
        while lo <= hi:
            m = (lo + hi) // 2
            i = bisect.bisect_right(self.blacklist, m)
            
            if m - i >= v:
                hi = m - 1
            else:
                lo = m + 1
                
        return lo
        
    
# s = Solution(1, [])
# for i in range(3):
#     print(s.pick())
#
# s = Solution(2, [])
# for i in range(3):
#     print(s.pick())

s = Solution(3, [2, 0])
for i in range(10):
    print(s.pick())
