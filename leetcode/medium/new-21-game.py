# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/5/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution(object):
    def new21Game(self, N, K, W):
        dp = [0.0] * (N + W + 1)
        # dp[x] = the answer when Alice has x points
        for k in range(K, N + 1):
            dp[k] = 1.0

        S = min(N - K + 1, W)
        # S = dp[k+1] + dp[k+2] + ... + dp[k+W]
        for k in range(K - 1, -1, -1):
            dp[k] = S / float(W)
            S += dp[k] - dp[k + W]

        return dp[0]
    
s = Solution()
print(s.new21Game(10, 1, 10))
print(s.new21Game(6, 1, 10))
print(s.new21Game(21, 17, 10))
print(s.new21Game(10000, 10000, 10000))