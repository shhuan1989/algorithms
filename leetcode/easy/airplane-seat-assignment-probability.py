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
created by shhuan at 2019/12/20 00:01

"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0

        dp = [0] * (n + 2)
        dp[2] = 0.5
        ps = 0.5
        for k in range(3, n):
            dp[k] = 1.0 / k + ps / k
            ps += dp[k]

        return (1 + sum(dp[:n])) / n

# class Solution:
#     def nthPersonGetsNthSeat(self, n: int) -> float:
#         ps = 0
#         for k in range(2, n):
#             ps += (1 + ps) / k
#
#         return (1 + ps) / n

# class Solution:
#     def nthPersonGetsNthSeat(self, n: int) -> float:
#         return 1 if n == 1 else 0.5

s = Solution()
print(s.nthPersonGetsNthSeat(1))
print(s.nthPersonGetsNthSeat(2))
print(s.nthPersonGetsNthSeat(4))