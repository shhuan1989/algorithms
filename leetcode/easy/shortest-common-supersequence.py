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
created by shhuan at 2019/12/12 00:09

"""

class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        N, M = len(s1), len(s2)
        dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
        pre = [[(0, 0) for _ in range(M+1)] for _ in range(N+1)]
        for i in range(1, M+1):
            dp[0][i] = i
            pre[0][i] = (0, i-1)
        for i in range(1, N+1):
            dp[i][0] = i
            pre[i][0] = (i-1, 0)

        for i in range(1, N+1):
            for j in range(1, M+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    pre[i][j] = (i-1, j-1)
                else:
                    a, b = dp[i-1][j] + 1, dp[i][j-1] + 1
                    dp[i][j] = min(a, b)
                    if a < b:
                        pre[i][j] = (i-1, j)
                    else:
                        pre[i][j] = (i, j-1)

        i, j = N, M
        ans = ''
        while i > 0 or j > 0:
            pi, pj = pre[i][j]
            if pi == i - 1 and pj == j - 1:
                ans += s1[pi]
            elif pi == i - 1:
                ans += s1[pi]
            else:
                ans += s2[pj]
            i, j = pre[i][j]

        return ans[::-1]


s = Solution()
# print(s.shortestCommonSupersequence('abac', 'cab'))
print(s.shortestCommonSupersequence("bbbaaaba", "bbababbb"))