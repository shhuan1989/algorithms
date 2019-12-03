# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/10/20 18:08

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N = len(A)
        dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

        presum = [0] * (N+1)
        for i in range(N):
            presum[i+1] = presum[i] + A[i]

        def avg(i, j):
            l = j-i
            s = presum[j] - presum[i]

            return s/l

        s = 0
        for i in range(1, N+1):
            s += A[i-1]
            v = s / i
            dp[i][1] = v

        for i in range(1, N + 1):
            for j in range(2, min(i + 1, K + 1)):
                for k in range(1, i - j + 2):
                    dp[i][j] = max(dp[i][j], dp[i - k][j - 1] + avg(i - k, i))

        return dp[N][K]


s = Solution()
print(s.largestSumOfAverages([9, 1, 2, 3, 9], 3))
print(s.largestSumOfAverages([1, 2, 3, 4, 5, 6, 7], 4))