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
created by shhuan at 2019/12/15 13:39

"""

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        q = []
        ans = 0
        for i, v in enumerate(nums):
            while q and q[-1][1] > v:
                ans += i - q[-1][0]
                q.pop()
            q.append((i, v))

        n = len(nums)
        ans += sum([n-i for i, v in q] or [0])

        return ans


s = Solution()
print(s.validSubarrays([1, 4, 2, 5, 3]))