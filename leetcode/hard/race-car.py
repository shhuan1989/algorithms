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
created by shhuan at 2019/12/8 23:11

"""

class Solution(object):
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * target
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]



s = Solution()
# print(s.racecar(3))
# print(s.racecar(6))
print(s.racecar(5))