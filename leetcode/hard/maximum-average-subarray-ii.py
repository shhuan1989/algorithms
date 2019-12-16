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
created by shhuan at 2019/12/13 19:37

"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        presum = [0] * (n + 1)

        def check(avg):
            presum[0] = 0
            for i, v in enumerate(nums):
                presum[i+1] = presum[i] + v - avg

            minLeft = 0
            for i in range(k, len(nums)+1):
                if presum[i] >= minLeft:
                    return True
                minLeft = min(minLeft, presum[i-k+1])

            return False

            # postmax[-1] = n-1
            # maxval, maxi = presum[-1], n-1
            # for i in range(n-2, -1, -1):
            #     v = presum[i+1]
            #     if v > maxval:
            #         maxval = v
            #         maxi = i
            #     postmax[i] = maxi
            #
            #     if i <= n-k:
            #         j = postmax[i+k-1]
            #         if presum[j+1] - presum[i] > 0:
            #             return True
            #
            # return False

        lo, hi = min(nums), max(nums)
        while abs(lo-hi) > 1e-5:
            m = (lo + hi) / 2
            if check(m):
                lo = m
            else:
                hi = m

        return hi