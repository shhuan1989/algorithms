# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/23 15:44

"""

class Solution:
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """

        memo = {}

        def dfs(t):
            if t == 0:
                return 0
            if t in memo:
                return memo[t]

            g = 1
            cnt = 0
            while g * x < t:
                g *= x
                cnt += 1

            ans = dfs(t-g) + (2 if cnt == 0 else cnt)
            if g < t and g*x - t < t:
                ans = min(ans, dfs(g*x-t)+cnt+1)

            memo[t] = ans

            return ans

        return dfs(target)-1