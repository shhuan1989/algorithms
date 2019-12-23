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
created by shhuan at 2019/12/22 11:11

"""


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0 for _ in range(N+1)]

        for i in range(1, N+1):
            mx = A[i-1]
            for l in range(1, min(K, i)+1):
                mx = max(mx, A[i-l])
                dp[i] = max(dp[i], dp[i-l] + l * mx)
            # for j in range(i-1, max(i-K-1, -1), -1):
            #     dp[i] = max(dp[i], dp[j] + (i-j) * max(A[j: i]))

        return dp[-1]

s = Solution()
print(s.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
