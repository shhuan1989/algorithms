# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/25

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        
        def check(d):
            c, l, r = 0, 0, 0
            while r < n:
                if bloomDay[r] > d:
                    c += (r - l) // k
                    l = r + 1
                r += 1
            c += (r-l)//k
            return c >= m
        
        lo, hi = 0, max(bloomDay)
        while lo <= hi:
            d = (lo + hi) // 2
            if check(d):
                hi = d - 1
            else:
                lo = d + 1
        
        return lo if lo <= max(bloomDay) else -1


if __name__ == '__main__':
    s = Solution()
    print(s.minDays([7,7,7,7,12,7,7], 2, 3))
    print(s.minDays([1,10,3,10,2], 3, 1))