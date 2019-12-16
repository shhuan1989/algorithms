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
created by shhuan at 2019/12/15 18:09

"""

class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:

        def check(val):
            if val <= 0:
                return False
            count = 0
            for a, b in zip(stations[:-1], stations[1:]):
                d = b - a
                needs = int(math.ceil(d/val)) - 1
                count += needs
                if count > K:
                    return False
            return True

        N = len(stations)
        lo, hi = 0, max([stations[i]-stations[i-1] for i in range(1, N)])
        while hi - lo >= 1e-5:
            m = (lo + hi) / 2
            if check(m):
                hi = m
            else:
                lo = m

        return lo

s = Solution()
print(s.minmaxGasDist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))