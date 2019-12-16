
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
created by shhuan at 2019/12/15 21:22

"""


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0

        N, M = len(costs), len(costs[0])
        dp = [[float('inf') for _ in range(M)] for _ in range(N)]

        for c in range(M):
            dp[0][c] = costs[0][c]

        for r in range(1, N):
            ma, mb, mai, mbi = float('inf'), float('inf'), -1, -1
            for i in range(M):
                v = dp[r - 1][i]
                if v < ma:
                    mb = ma
                    ma = v
                    mai = i
                elif v < mb:
                    mb = v

            for c in range(M):
                dp[r][c] = (ma if c != mai else mb) + costs[r][c]

        return min(dp[N - 1])

s = Solution()
print(s.minCostII([[1,5,3],[2,9,4]]))