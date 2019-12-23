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
created by shhuan at 2019/12/19 21:22

"""


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        N = len(prob)
        if target > N:
            return 0
        dp = [[0 for _ in range(N+1)] for _ in range(N)]
        dp[0][0] = 1 - prob[0]
        dp[0][1] = prob[0]
        for i in range(1, N):
            dp[i][0] = dp[i-1][0] * (1-prob[i])
            for j in range(1, min(target, i+1) + 1):
                dp[i][j] = dp[i-1][j-1] * prob[i] + dp[i-1][j] * (1-prob[i])

        return dp[N-1][target]


s = Solution()
print(s.probabilityOfHeads([0.2,0.8,0,0.3,0.5], 3))
print(s.probabilityOfHeads([0.4], 1))
print(s.probabilityOfHeads([0.5, 0.5, 0.5, 0.5, 0.5], 0))