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
created by shhuan at 2019/12/22 19:53

"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0: return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i+1)
            ans += j - i - 1
        return ans

s = Solution()
# print(s.numSubarrayProductLessThanK([1, 1, 1], 1))
print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
