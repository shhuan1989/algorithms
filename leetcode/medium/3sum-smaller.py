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
created by shhuan at 2019/12/22 23:37

"""


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()

        def twoSumSmaller(nums, startIndex, target):
            s = 0
            left = startIndex
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    s += right - left
                    left += 1
                else:
                    right -= 1
            return s

        s = 0
        for i in range(len(nums)-1):
            s += twoSumSmaller(nums, i+1, target-nums[i])

        return s

s = Solution()
print(s.threeSumSmaller([3,1,0,-2], 4))
print(s.threeSumSmaller([1, 1, -2], 1))
print(s.threeSumSmaller([-2, 0, 1, 3], 2))





