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
created by shhuan at 2019/12/22 10:32

"""


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False

        N = len(nums)
        if N % k != 0:
            return False

        wc = collections.Counter(nums)

        for s in sorted(wc.keys()):
            if wc[s] <= 0:
                continue
            for c in range(wc[s]):
                for i in range(k):
                    v = s + i
                    if v not in wc or wc[v] <= 0:
                        return False
                    wc[v] -= 1

        return True

s = Solution()
print(s.isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4))
print(s.isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))
print(s.isPossibleDivide(nums = [3,3,2,2,1,1], k = 3))
print(s.isPossibleDivide(nums = [1,2,3,4], k = 3))