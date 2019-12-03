# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/17 10:48

"""

from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a0 = [v for v in nums if v % 3 == 0]
        a1 = [v for v in nums if v % 3 == 1]
        a2 = [v for v in nums if v % 3 == 2]
        a1.sort(reverse=True)
        a2.sort(reverse=True)

        ans = sum(a0 or [0])
        na1 = len(a1)
        if na1 > 0:
            ra1 = na1 % 3 + 3
            ans += sum(a1[:-ra1] or [0])
            a1 = a1[-ra1:]

        na2 = len(a2)
        if na2 > 0:
            ra2 = na2 % 3 + 3
            ans += sum(a2[:-ra2] or [0])
            a2 = a2[-ra2:]

        if len(a1) == len(a2):
            ans += sum(a1 or [0]) + sum(a2 or [0])
        else:
            # ans += a1[0] + a2[0]
            a = a1 + a2
            vis = {0}
            for v in a:
                nvis = {u + v for u in vis}
                vis |= nvis
            vis = list(sorted(vis, reverse=True))
            for v in vis:
                if v % 3 == 0:
                    ans += v
                    break


        return ans


s = Solution()
# print(s.maxSumDivThree([3,6,5,1,8]))
# print(s.maxSumDivThree([4]))
# print(s.maxSumDivThree([1,2,3,4,4]))
print(s.maxSumDivThree([2,3,36,8,32,38,3,30,13,40]))