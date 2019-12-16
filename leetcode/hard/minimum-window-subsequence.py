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
created by shhuan at 2019/12/16 00:36

"""


class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m = len(T)
        n = len(S)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = j + 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if T[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        start = 0
        l = n + 1
        for j in range(1, n + 1):
            if dp[m][j]:
                if j - dp[m][j] + 1 < l:
                    start = dp[m][j] - 1
                    l = j - dp[m][j] + 1
        return "" if l == n + 1 else S[start:start + l]