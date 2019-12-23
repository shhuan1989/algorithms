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
created by shhuan at 2019/12/22 20:15

"""


class Solution:

    def __init__(self, w: List[int]):
        psum = []
        t = 0
        for v in w:
            t += v
            psum.append(t)
        self.psum = psum
        self.total = t

    def pickIndex(self) -> int:
        target = random.randint(0, self.total-1)

        lo, hi = 0, len(self.psum) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if target >= self.psum[mid]:
                lo = mid + 1
            else:
                hi = mid

        return hi

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()