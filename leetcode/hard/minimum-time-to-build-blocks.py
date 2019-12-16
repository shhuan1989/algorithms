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
created by shhuan at 2019/12/16 23:16

"""

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        N = len(blocks)
        blocks.sort(reverse=True)

        def check(cost):
            startime = [cost-v for v in blocks]
            if any([v < 0 for v in startime]):
                return False

            x = 1
            built = 0
            currenttime = 0
            while built < N:
                if x <= 0:
                    return False
                if x >= N - built:
                    return True
                y = bisect.bisect_right(startime, currenttime + split - 1)
                if y >= built:
                    y -= built
                if y > x:
                    return False

                x -= y
                built += y
                x *= 2
                currenttime += split

            return True

        lo, hi = max(blocks), 10 * split + max(blocks)
        while lo <= hi:
            cost = (lo + hi) // 2
            if check(cost):
                hi = cost - 1
            else:
                lo = cost + 1

        return lo


s = Solution()
# print(s.minBuildTime([1,1,1,1], 100))
print(s.minBuildTime([1], 1))
# print(s.minBuildTime([1, 2], 5))
# print(s.minBuildTime([1, 2, 3], 1))
print(s.minBuildTime([94961,39414,41263,7809,41473], 90))