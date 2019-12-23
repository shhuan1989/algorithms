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
created by shhuan at 2019/12/20 20:57

"""

from functools import lru_cache

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def manhatten(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        @lru_cache(maxsize=None)
        def dfs(index, bikeSet):
            if index >= len(workers):
                return 0

            mask = 1
            ans = float('inf')
            for bi, b in enumerate(bikes):
                if bikeSet & mask == 0:
                    ans = min(ans, manhatten(workers[index], b) + dfs(index+1, bikeSet | mask))
                mask <<= 1
            return ans

        return dfs(0, 0)

    def assignBikes2(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def manhatten(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        N, M = len(workers), len(bikes)
        dp = [[float('inf') for _ in range(1 << M)] for _ in range(N+1)]
        for i in range(1<<M):
            dp[0][i] = 0

        for i in range(1, N+1):
            for s in range(1 << M):
                mask = 1
                for j in range(M):
                    if s & mask:
                        d = manhatten(workers[i-1], bikes[j])
                        dp[i][s] = min(dp[i][s], dp[i-1][s ^ mask] + d)
                    mask <<= 1

        return dp[N][-1]


s = Solution()
print(s.assignBikes2([[0,0],[2,1]], [[1,2],[3,3]]))
print(s.assignBikes2([[239,904],[191,103],[260,117],[86,78],[747,62]], [[660,8],[431,772],[78,576],[894,481],[451,730],[155,28]]))
# print(s.assignBikes(workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]))
# print(s.assignBikes(workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]))