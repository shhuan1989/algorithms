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
created by shhuan at 2019/12/22 17:08

"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        dp = [[float('inf') for _ in range(31)] for _ in range(N + 1)]
        for i in range(3):
            dp[0][i] = 0
        ticket = [1, 7, 30]
        for t in range(3):
            dp[1][ticket[t]-1] = costs[t]
        for i in range(2, N+1):
            d, pd = days[i-1], days[i-2]
            for j in range(31):
                if 0 < d - pd + j < 31:
                    dp[i][j] = dp[i-1][d-pd+j]
            for t in range(3):
                dp[i][ticket[t] - 1] = min(dp[i][ticket[t] - 1], min(dp[i-1]) + costs[t])

        return min(dp[N])

s = Solution()
print(s.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
print(s.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))
