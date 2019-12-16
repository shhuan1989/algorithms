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
created by shhuan at 2019/12/14 14:07

"""

class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def check(val):
            k, s = 0, 0
            for v in sweetness:
                s += v
                if s >= val:
                    s = 0
                    k += 1
                    if k > K:
                        return True
            return k > K

        lo, hi = min(sweetness), sum(sweetness) // (K+1)
        while lo <= hi:
            m = (lo + hi) // 2
            if check(m):
                lo = m + 1
            else:
                hi = m - 1

        return hi

s = Solution()
print(s.maximizeSweetness([1,2,3,4,5,6,7,8,9], 5))
print(s.maximizeSweetness([5,6,7,8,9,1,2,3,4], 8))
print(s.maximizeSweetness([1,2,2,1,2,2,1,2,2], 2))