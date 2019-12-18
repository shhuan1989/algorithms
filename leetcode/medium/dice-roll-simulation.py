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
created by shhuan at 2019/12/18 22:45

"""

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        dp = [[[0 for _ in range(16)] for _ in range(6)] for _ in range(n+1)]
        MOD = 10**9 + 7
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n+1):
            for j in range(6):
                dp[i][j][1] = sum([sum(dp[i-1][prej]) % MOD for prej in range(6) if prej != j]) % MOD
                for k in range(2, rollMax[j]+1):
                    dp[i][j][k] = dp[i-1][j][k-1]

        return sum([sum(dp[n][j]) % MOD for j in range(6)]) % MOD

s = Solution()
print(s.dieSimulator(n = 2, rollMax = [1,1,2,2,2,3]))
print(s.dieSimulator(n = 2, rollMax = [1,1,1,1,1,1]))
print(s.dieSimulator(n = 3, rollMax = [1,1,1,2,2,3]))
