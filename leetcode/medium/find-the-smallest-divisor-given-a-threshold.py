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
created by shhuan at 2019/12/8 10:35

"""


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def check(m):
            s = sum([x//m if x % m == 0 else x//m + 1 for x in nums])
            return s <= threshold

        lo, hi = 1, 10**6
        while lo <= hi:
            m = (lo+hi) // 2
            if check(m):
                hi = m - 1
            else:
                lo = m + 1

        return lo

s = Solution()
print(s.smallestDivisor(nums = [1,2,5,9], threshold = 6))
print(s.smallestDivisor(nums = [2,3,5,7,11], threshold = 11))
print(s.smallestDivisor(nums = [19], threshold = 5))