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
created by shhuan at 2020/7/12 10:30

"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 0
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] == nums[j]:
                    ans += 1
        return ans



s = Solution()
print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))