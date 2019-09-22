# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/22 10:05

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
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if not s1 and not s2:
            return 0
        elif not s1:
            return sum([ord(c) for c in s2])
        elif not s2:
            return sum([ord(c) for c in s1])

        N, M = len(s1), len(s2)
        dp = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]
        dp[0][0] = 0

        s = 0
        for i in range(1, N+1):
            s += ord(s1[i-1])
            dp[i][0] = s

        s = 0
        for i in range(1, M+1):
            s += ord(s2[i-1])
            dp[0][i] = s

        for i in range(1, N+1):
            for j in range(1, M+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + ord(s1[i-1]), dp[i][j-1]+ord(s2[j-1]))

        return dp[N][M]


s = Solution()
print(s.minimumDeleteSum('sea', 'eat'))
print(s.minimumDeleteSum('delete', 'leet'))