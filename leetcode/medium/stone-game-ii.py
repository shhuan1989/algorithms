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
created by shhuan at 2019/12/6 19:53

"""

from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        N = len(piles)
        presum = [0] * N
        for i in range(N-1, -1, -1):
            presum[i] = (presum[i+1] if i + 1 < N else 0) + piles[i]


        @lru_cache(maxsize=None)
        def dfs(start, m):
            if start >= N:
                return 0

            if start + 2 * m >= N:
                return presum[start]

            ans = 0
            for p in range(1, 2*m+1):
                ans = max(ans, presum[start] - dfs(start+p, max(m, p)))

            return ans

        return dfs(0, 1)


s = Solution()
print(s.stoneGameII([2, 7, 9, 4, 4]))

