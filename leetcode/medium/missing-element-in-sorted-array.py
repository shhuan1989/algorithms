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
created by shhuan at 2019/12/19 16:23

"""


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] + k

        nums.sort()
        if nums[1] - nums[0] > k:
            return nums[0] + k

        s = nums[0]
        N = len(nums)
        for i, v in enumerate(nums):
            if s + i + k <= v:
                return k - ((nums[i-1] - nums[0] + 1) - i) + nums[i-1]

        return nums[-1] + k - (nums[-1] - nums[0] + 1 - N)


s = Solution()
print(s.missingElement([4, 7, 9, 10], 1))
print(s.missingElement([4, 7, 9, 10], 3))
print(s.missingElement([1, 2, 4], 3))