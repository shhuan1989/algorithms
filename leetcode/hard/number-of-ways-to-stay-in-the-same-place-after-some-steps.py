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
created by shhuan at 2019/11/24 10:48

"""


from typing import List

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        if not A or len(A) < 2:
            return False

        sa = sum(A)
        N = len(A)

        count, target = min(N//2+2, N-1), sa
        dp = [[[float('-inf') for _ in range(target + 1)] for _ in range(count + 1)] for _ in range(N + 1)]

        z = 0
        for i in range(N + 1):
            if A[i - 1] == 0:
                z = +1
            for j in range(z + 1):
                dp[i][j][0] = 0

        for i in range(1, N + 1):
            for c in range(1, min(i, count) + 1):
                for v in range(1, target + 1):
                    dp[i][c][v] = dp[i - 1][c][v]
                    if v - A[i - 1] >= 0:
                        dp[i][c][v] = max(dp[i][c][v], dp[i - 1][c - 1][v - A[i - 1]] + A[i - 1])

                    if dp[i][c][v] == v and v * N == sa * c:
                        return True
        return False


s = Solution()
print(s.numWays(3, 2))
print(s.numWays(2, 4))
print(s.numWays(4, 2))
print(s.numWays(430, 148488))