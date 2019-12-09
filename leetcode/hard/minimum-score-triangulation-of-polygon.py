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
created by shhuan at 2019/12/5 22:42

"""


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        length = len(A)
        inf = float('inf')
        dp = [[inf for _ in range(length)] for _ in range(length)]

        for i in range(length - 1):
            dp[i][i + 1] = 0

        for d in range(2, length):
            for i in range(0, length - d):
                j = i + d
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[k] * A[j])

        return dp[0][length - 1]

s = Solution()
print(s.minScoreTriangulation([1, 2, 3]))
print(s.minScoreTriangulation([3, 7, 4, 5]))
print(s.minScoreTriangulation([1, 3, 1, 4, 1, 5]))
print(s.minScoreTriangulation([5,2,1,1,3,6,1,7,5]))
print(s.minScoreTriangulation([random.randint(1, 100) for _ in range(50)]))