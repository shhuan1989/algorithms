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
created by shhuan at 2019/12/1 10:50

"""


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        N = len(s)
        dp = [[10000 for _ in range(k+1)] for _ in range(N+1)]
        dp[0][0] = 0

        def f(l, r):
            ans = 0
            for i in range((r-l)//2):
                if s[i+l] != s[r-i-1]:
                    ans += 1
            return ans

        for i in range(1, N+1):
            for j in range(1, min(i, k) + 1):
                for ii in range(j-1, i):
                    dp[i][j] = min(dp[i][j], dp[ii][j-1] + f(ii, i))

        return dp[N][k]


s = Solution()
print(s.palindromePartition('abc', 2))
print(s.palindromePartition('aabbc', 3))
print(s.palindromePartition('leetcode', 8))
