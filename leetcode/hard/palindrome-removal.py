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
created by shhuan at 2019/12/15 23:29

"""

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        A = arr
        N = len(A)
        dp = [[N for _ in range(N+1)] for _ in range(N)]

        for i in range(N):
            dp[i][1] = 1
        for l in range(2, N+1):
            for i in range(N-l+1):
                j = i + l - 1
                if A[i] == A[j]:
                    if l == 2:
                        dp[i][l] = 1
                    else:
                        dp[i][l] = dp[i+1][l-2]
                else:
                    dp[i][l] = min(dp[i][l], min([dp[i][k] + dp[i+k][l-k] for k in range(1, l)]))

        return dp[0][N]

s = Solution()
print(s.minimumMoves([1, 2]))
print(s.minimumMoves([1, 3, 4, 1, 5]))
t0 = time.time()
print(s.minimumMoves([14,12,3,16,3,7,5,16,17,20,19,4,18,19,16,7,18,17,8,3,4,19,14,16,18,8,16,5,6,13,19,16,3,7,18,10,18,12,17,3,14,1,8,13,5,16,4,20,3,17,9,8,17,18,19,13,12,11,8,9,19,11,9,12,8,5,9,13,13,7,19,2,11,18,17,14,20,11,17,18,1,1,4,10,3,14,18,16,19,20,15,5,9,1,1,14,17,1,15,20]))
print(time.time() - t0)