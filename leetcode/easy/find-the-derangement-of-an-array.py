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
created by shhuan at 2019/12/22 01:15

"""

class Solution:
    def findDerangement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        MOD = 10**9 + 7
        a, b = 1, 2
        for i in range(4, n+1):
            a, b = b, ((i-1) * (a + b)) % MOD
            print(b)
        return b

s = Solution()
print(s.findDerangement(6))
# print(s.findDerangement(10**6))
