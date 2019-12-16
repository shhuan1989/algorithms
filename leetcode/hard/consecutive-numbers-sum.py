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
created by shhuan at 2019/12/12 21:03

"""

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        M = int(math.sqrt(2* N + 1)) + 2

        ans = 0
        for l in range(M, 1, -1):
            a = (2 * N // l - l + 1) // 2
            if a > 0 and l * (a + a + l - 1) // 2 == N:
                ans += 1
        return ans + 1

s = Solution()
print(s.consecutiveNumbersSum(5))
print(s.consecutiveNumbersSum(9))
print(s.consecutiveNumbersSum(15))
print(s.consecutiveNumbersSum(4))
print(s.consecutiveNumbersSum(10**9))