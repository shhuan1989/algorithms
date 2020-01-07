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
created by shhuan at 2020/1/5 10:50

"""


class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)

        dp = [[N*N for _ in range(N+1)] for _ in range(N)]
        for i in range(N):
            dp[i][0] = 0
            dp[i][1] = 0

        for l in range(2, N+1):
            for i in range(N-l+1):
                if s[i] == s[i+l-1]:
                    dp[i][l] = min(dp[i][l], dp[i+1][l-2])
                else:
                    dp[i][l] = min(dp[i][l], dp[i+1][l-1] + 1, dp[i][l-1] + 1)

        # for row in dp:
        #     print(row)
        return dp[0][N]


s = Solution()
print(s.minInsertions('zzazz'))
print(s.minInsertions('mbadm'))
print(s.minInsertions('leetcode'))
print(s.minInsertions('g'))
print(s.minInsertions('no'))

