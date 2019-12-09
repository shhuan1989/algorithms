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
created by shhuan at 2019/12/7 22:50

"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans,  cost = 0, 0
        diff = [abs(ord(a) - ord(b)) for a, b in zip(s, t)]
        for r, c in enumerate(diff):
            cost += c
            if cost <= maxCost:
                ans += 1
            else:
                cost -= diff[r-ans]
        return ans

s = Solution()
print(s.equalSubstring('abcd', 'bcdf', 3))
print(s.equalSubstring('abcd', 'cdef', 3))
print(s.equalSubstring('abcd', 'acde', 0))


