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
created by shhuan at 2019/12/3 21:46

"""

from typing import List

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # for speed-up
        if target <= 0 or target > d * f:
            return 0

        # for speed-up
        if target == d or target == d * f:
            return 1

        dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
        dp[0][0] = 1
        M = 10**9 + 7
        for i in range(1, d+1):
            # for speed-up
            dp[i][i] = 1
            if target >= i * f:
                dp[i][i*f] = 1

            for t in range(i+1, min(i*f-1, target)+1):
                dp[i][t] = sum([dp[i-1][t-v] for v in range(1, min(t, f)+1)]) % M

        return dp[d][target]


s = Solution()
print(s.numRollsToTarget(1, 6, 3))
print(s.numRollsToTarget(2, 6, 7))
print(s.numRollsToTarget(2, 5, 10))
print(s.numRollsToTarget(1, 2, 3))
print(s.numRollsToTarget(30, 30, 500))