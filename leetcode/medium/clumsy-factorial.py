# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/12/3 21:59

"""

class Solution:
    def clumsy(self, N: int) -> int:
        ans = 0
        v = N
        op = 1
        while v > 0:
            if v > 2:
                ans += op * (v * (v-1) // (v-2))
            elif v > 1:
                ans += op * (v * (v-1))
            else:
                ans += op

            if v > 3:
                ans += v-3
            v = v-4
            op = -1

        return ans







s = Solution()
print(s.clumsy(4))
print(s.clumsy(10))
print(s.clumsy(10000))