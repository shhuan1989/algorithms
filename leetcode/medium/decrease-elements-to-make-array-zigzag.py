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
created by shhuan at 2019/12/4 23:29

"""
from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        N = len(nums)
        a = sum([max(0, nums[i] - min(nums[i-1], nums[i+1] if i+1 < N else float('inf')) + 1) for i in range(1, N, 2)])
        b = sum([max(0, nums[i] - min(nums[i-1] if i > 0 else float('inf'), nums[i+1] if i+1 < N else float('inf')) + 1) for i in range(0, N, 2)])

        return min(a, b)

s = Solution()
print(s.movesToMakeZigzag([1, 2, 3]))
print(s.movesToMakeZigzag([9, 6, 1, 6, 2]))