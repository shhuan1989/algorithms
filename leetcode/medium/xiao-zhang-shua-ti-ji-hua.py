# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/26

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def minTime(self, cost: List[int], m: int) -> int:
        n = len(cost)
        
        def check(t):
            d = 0
            maxt = 0
            tt = 0
            for i, c in enumerate(cost):
                tt += c
                maxt = max(maxt, c)
                if tt - maxt > t:
                    d += 1
                    tt = c
                    maxt = c
            
            d += 1
            
            return d <= m
        
        lo, hi = 0, max(cost) * n
        while lo <= hi:
            t = (lo + hi) // 2
            if check(t):
                hi = t - 1
            else:
                lo = t + 1
        
        return lo


if __name__ == '__main__':
    s = Solution()
    print(s.minTime([1,2,3,3], 2))
    print(s.minTime([999,999,999], 4))