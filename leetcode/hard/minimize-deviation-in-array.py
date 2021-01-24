# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/29 11:33

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


from functools import lru_cache
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        nums.sort()
        minvs = []
        for v in nums:
            if v % 2 == 0:
                while v % 2 == 0:
                    minvs.append(v)
                    v //= 2
                minvs.append(v)
            else:
                minvs.append(v)
                minvs.append(v * 2)

        minvs = list(sorted(set(minvs)))


        @lru_cache(maxsize=None)
        def getdiff(minv):
            diff = 0
            for v in nums:
                if v % 2 == 1:
                    if v >= minv:
                        diff = max(diff, v - minv)
                    elif v * 2 >= minv:
                        diff = max(diff, v * 2 - minv)
                    else:
                        return float('inf')
                else:
                    if v < minv:
                        return float('inf')
                    while v % 2 == 0 and v >= minv:
                        v //= 2
                    if v < minv:
                        v *= 2
                    diff = max(diff, v - minv)
            return diff



        ans = max(nums) - min(nums)
        lo, hi = 0, 10**9+7
        while lo < hi - 10:
            d = (hi - lo) // 3
            l, r = lo + d, lo + 2 * d
            a, b, c, d = getdiff(lo), getdiff(l), getdiff(r), getdiff(hi)
            # print(lo, hi)
            if a >= b >= c:
                lo = l
            else:
                hi = r

        print(lo, hi)
        print([getdiff(x) for x in range(lo, hi+10)])
        # print(getdiff(hi))

        ans = min([getdiff(x) for x in range(lo, hi+1)])
        ans = min(ans, getdiff(lo), getdiff(hi))
        return ans





if __name__ == '__main__':
    s = Solution()
    # print(s.minimumDeviation([136,465,87]))
    # print(s.minimumDeviation([1, 2, 3, 4]))
    # print(s.minimumDeviation([10, 4, 3]))
    # print(s.minimumDeviation([3, 5]))
    # print(s.minimumDeviation([4, 1, 5, 20, 3]))
    # print(s.minimumDeviation([2, 10, 8]))
    print(s.minimumDeviation([399,908,648,357,693,502,331,649,596,698]))