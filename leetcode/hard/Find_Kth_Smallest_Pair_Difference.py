# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/17 19:37

"""


class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()


        def check(dist):
            c = sum([bisect.bisect_right(nums, v + dist)-i-1 for i, v in enumerate(nums)])
            return c >= k

        lo, hi = 0, max(nums) - min(nums)
        while lo < hi:
            m = (lo + hi) // 2
            if check(m):
                hi = m
            else:
                lo = m + 1

        return lo


s = Solution()
# print(s.smallestDistancePair([1, 3, 1], 1))
print(s.smallestDistancePair([62,100,4], 2))