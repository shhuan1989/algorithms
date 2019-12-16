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
created by shhuan at 2019/12/15 22:46

"""

from functools import lru_cache

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        def lcs(a, b):
            n = len(a)
            dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

            for i in range(1, n+1):
                for j in range(1, n+1):
                    if a[i-1] == b[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            return dp[n][n]

        return len(s) - lcs(s, s[::-1]) <= k

    def isValidPalindrome2(self, s: str, k: int) -> bool:

        @lru_cache(maxsize=None)
        def dfs(l, r, rem):
            if l >= r:
                return True
            if rem < 0:
                return False

            if rem == 0:
                i, j = l, r
                while i < j:
                    if s[i] != s[j]:
                        return False
                    i += 1
                    j -= 1
                return True

            if s[l] == s[r]:
                return dfs(l+1, r-1, rem)
            else:
                if s[l+1] == s[r]:
                    return dfs(l+1, r, rem-1) or dfs(l, r-1, rem-1)
                else:
                    return dfs(l, r - 1, rem - 1) or dfs(l + 1, r, rem - 1)

        return dfs(0, len(s)-1, k)

s = Solution()
print(s.isValidPalindrome('abcdeca', 2))
