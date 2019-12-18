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
created by shhuan at 2019/12/19 01:05

"""

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        q = sticks
        heapq.heapify(q)

        ans = 0
        while len(q) > 1:
            a, b = heapq.heappop(q), heapq.heappop(q)
            ans += a + b
            heapq.heappush(q, a+b)

        return ans

s = Solution()
print(s.connectSticks([3354,4316,3259,4904,4598,474,3166,6322,8080,9009]))
print(s.connectSticks([1, 8, 3, 5]))