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
created by shhuan at 2019/12/4 23:56

"""

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        ans = 0
        wc = collections.Counter(nums)
        counts = collections.defaultdict(int)
        for l in wc.values():
            counts[l] += 1

        N = len(nums)
        for i in range(N-1, -1, -1):
            if len(counts) == 2:
                a, b = list(counts.keys())
                if abs(b-a) == 1 and counts[max(a, b)] == 1:
                    ans = i+1
                    break
                if 1 in counts and counts[1] == 1:
                    ans = i+1
                    break
            elif len(counts) == 1:
                if 1 in counts or list(counts.values())[0] == 1:
                    ans = i+1
                    break

            v = nums[i]
            l = wc[v]
            counts[l] -= 1
            if counts[l] == 0:
                del counts[l]
            if l > 1:
                counts[l-1] += 1
            wc[v] -= 1


        # print(counts)
        return max(ans, len(nums) if len(nums) <= 2 else 0)

s = Solution()
print(s.maxEqualFreq([1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,42,21,45,27,78,39,78,24,47,60,22,33,45,18,56,91,93,66,79,65,43,7,57,63,74,25,11,14,100,95,19,3,22,18,94,52,91,33,95,16,93,63,65,8,88,51,47,7,51,77,36,48,89,72,81,75,13,69,9,31,16,38,34,76,7,82,10,90,64,28,22,99,40,88,27,94,85,43,75,95,86,82,46,9,74,67,51,93,97,35,2,49]))
print(s.maxEqualFreq([1, 1, 1, 1, 1, 1]))
print(s.maxEqualFreq([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(s.maxEqualFreq(nums = [2,2,1,1,5,3,3,5]), 7)
print(s.maxEqualFreq(nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]))
print(s.maxEqualFreq(nums = [1,1,1,2,2,2]))
print(s.maxEqualFreq(nums = [10,2,8,9,3,8,1,5,2,3,7,6]))