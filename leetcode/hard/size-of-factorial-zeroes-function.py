# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/10 19:54

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def f(x):
            y = 5
            ans = 0
            while y <= x:
                ans += x // y
                y *= 5
            return ans


        lo, hi = 0, 10**10
        while lo <= hi:
            m = lo+(hi-lo)//2
            if f(m) >= K:
                hi = m - 1
            else:
                lo = m + 1
        L = lo

        lo, hi = 0, 10**10
        while lo <= hi:
            m = lo + (hi-lo) // 2
            if f(m) <= K:
                lo = m + 1
            else:
                hi = m - 1
        R = hi

        if L <= R:
            return R - L + 1

        return 0




s = Solution()
for i in range(10):
    print(s.preimageSizeFZF(i))