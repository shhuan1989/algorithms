# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/19 00:03

"""


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if D == 1:
            return sum(weights)

        def check(cap):
            day = 0
            x = 0
            for w in weights:
                if x + w > cap:
                    day += 1
                    if day > D:
                        return False
                    x = w
                else:
                    x += w
            if x > 0:
                day += 1

            return day <= D

        lo, hi = max(weights), sum(weights)
        while lo <= hi:
            m = (lo + hi) // 2
            if check(m):
                hi = m - 1
            else:
                lo = m + 1

        return lo

s = Solution()
print(s.shipWithinDays([1,2,3,1,1], 4))