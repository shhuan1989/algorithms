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
created by shhuan at 2019/12/16 22:05

"""

class Solution:
    def numberOfWays(self, num_people: int) -> int:

        MOD = 10**9+7
        dp = [0] * (num_people + 1)
        dp[0] = dp[2] = 1

        # 卡特兰数 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190
        # h(n) = h(1)*h(n-1) + h(2)*h(n-2) + ... + h(n-1)*h(1)
        # h(2n) = c(2n, n) // (n+1) = c(2n, n) - c(2n, n-1)

        # 卢卡斯定理：c(n, m) % p = c(n/p, m/p) * c(n%p, m%p) % p
        # https://oi-wiki.org/math/lucas/
        for i in range(4, num_people + 1, 2):
            dp[i] = sum(dp[j] * dp[i-j-2] for j in range(0, i-1, 2)) % MOD

        return dp[num_people]


s = Solution()

for i in range(2, 10, 2):
    print(i, s.numberOfWays(i))