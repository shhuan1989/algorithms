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
created by shhuan at 2019/12/19 16:46

"""


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum =0
        g = {0: -1}
        ans = 0
        for i, v in enumerate(nums):
            presum += v
            v = presum - k
            if v in g:
                ans = max(ans, i - g[v])
            if presum not in g:
                g[presum] = i

        return ans


s = Solution()
print(s.maxSubArrayLen([1, -1, 5, -2, 3], 3))
print(s.maxSubArrayLen([-2, -1, 2, 1], 1))