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
created by shhuan at 2019/12/15 23:08

"""


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:

        ffrom = collections.defaultdict(list)
        N, K = len(flights), len(days[0])
        for i in range(N):
            for j in range(N):
                if flights[i][j] == 1:
                    ffrom[j].append(i)

        dp = [[float('-inf') for _ in range(N)] for _ in range(K)]
        dp[0][0] = days[0][0]
        for city in range(N):
            if flights[0][city]:
                dp[0][city] = days[city][0]

        for k in range(1, K):
            for city in range(N):
                dp[k][city] = dp[k-1][city] + days[city][k]
                for pre in ffrom[city]:
                    dp[k][city] = max(dp[k][city], dp[k-1][pre] + days[city][k])

        return max(dp[K-1])

s = Solution()
print(s.maxVacationDays(flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]))
print(s.maxVacationDays(flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]))
print(s.maxVacationDays(flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]))