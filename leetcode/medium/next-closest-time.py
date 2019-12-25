# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def nextClosestTime(self, time: str) -> str:
        nums = {v for v in time if v.isdigit()}
        
        times = set()
        for a in nums:
            if a > '2':
                continue
            for b in nums:
                if a == '2' and b > '4':
                    continue
                for c in nums:
                    if c > '5':
                        continue
                    for d in nums:
                        t = '{}{}:{}{}'.format(a, b, c, d)
                        times.add(t)

        for t in sorted(times):
            if t > time:
                return t
        
        return min(times)
    
s = Solution()
print(s.nextClosestTime('19:34'))
print(s.nextClosestTime('23:59'))