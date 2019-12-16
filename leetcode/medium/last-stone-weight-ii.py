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
created by shhuan at 2019/12/10 23:13

"""


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        N = len(stones)
        dp = [[0 for _ in range(target+1)] for _ in range(2)]

        for i in range(1, N+1):
            for t in range(min(stones[i-1], target+1)):
                dp[i % 2][t] = dp[(i-1) % 2][t]
            for t in range(stones[i-1], target+1):
                dp[i % 2][t] = max(dp[(i-1) % 2][t], dp[(i-1) % 2][t-stones[i-1]] + stones[i-1])

        return abs(sum(stones) - 2 * dp[N % 2][target])

s = Solution()
print(s.lastStoneWeightII([2,7,4,1,8,1]))
print(s.lastStoneWeightII([31,26,33,21,40]))