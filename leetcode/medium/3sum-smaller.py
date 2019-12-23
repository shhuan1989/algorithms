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
        l, r, N = 0, len(nums)-1, len(nums)
        nums.sort()

        ans = 0
        while l < r:
            s = nums[l] + nums[r]
            while s >= target and r > l:
                r -= 1
                s = nums[l] + nums[r]
            if r == l:
                break
            for i in range(l+1, r+1):
                s = nums[l] + nums[i]
                t = target-s-1
                j = bisect.bisect_right(nums, t)
                j = min(j, l-1)
                ans += j + 1
            l += 1

        return ans


s = Solution()
print(s.threeSumSmaller([3,1,0,-2], 4))
print(s.threeSumSmaller([1, 1, -2], 1))
print(s.threeSumSmaller([-2, 0, 1, 3], 2))





