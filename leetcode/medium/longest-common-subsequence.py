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
created by shhuan at 2019/12/9 21:08

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
        # pre = [[(0, 0) for _ in range(M+1)] for _ in range(N+1)]

        for i, v in enumerate(text1):
            for j, u in enumerate(text2):
                if v == u:
                    dp[i+1][j+1] = dp[i][j] + 1
                    # pre[i+1][j+1] = (i, j)
                else:
                    if dp[i][j+1] > dp[i+1][j]:
                        dp[i+1][j+1] = dp[i][j+1]
                        # pre[i+1][j+1] = (i, j+1)
                    else:
                        dp[i+1][j+1] = dp[i+1][j]
                        # pre[i+1][j+1] = (i+1, j)

        # i, j = N, M
        # ans = []
        # while i > 0 and j > 0:
        #     if text1[i-1] == text2[j-1]:
        #         ans.append(text1[i-1])
        #     i, j = pre[i][j]
        #
        # return ''.join(ans[::-1])
        return dp[N][M]

s = Solution()
print(s.longestCommonSubsequence('abcde', 'ace'))
print(s.longestCommonSubsequence('abc', 'abc'))
print(s.longestCommonSubsequence('abc', 'def'))
