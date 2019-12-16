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
created by shhuan at 2019/12/15 19:16

"""

class Solution:
    def newInteger(self, n: int) -> int:
        def dlen(val):
            d10, v = 0, val
            while v > 0:
                v //= 10
                d10 += 1
            return d10

        def numsWith9ofSameLen(val, checkfirst):
            if val < 9:
                return 0
            elif val < 10:
                return 1

            d10 = dlen(val)
            d10 -= 1
            a = 10 ** d10
            first = val // a

            if checkfirst and first == 1:
                return numsWith9ofSameLen(val - a, False)
            elif first == 9:
                return (8 if checkfirst else 9) * (10**d10 - 9**d10) + val % a
            else:
                return (first-1 if checkfirst else first) * (10**d10 - 9**d10) + numsWith9ofSameLen(val % a, False)

        def numsWith9(val):
            d10 = dlen(val) - 1
            ans = 0
            if d10 >= 1:
                ans += 1

            for i in range(2, d10+1):
                ans += 10**(i-1) + 8 * (10**(i-1) - 9**(i-1))

            ans += numsWith9ofSameLen(val, True)

            return ans

        lo, hi = 0, 10**10
        while lo <= hi:
            mid = (lo + hi) // 2
            check = mid - numsWith9(mid) >= n
            if check:
                hi = mid - 1
            else:
                lo = mid + 1

        left = lo
        x = []
        v = left
        while v > 0:
            x.append(v % 10)
            v //= 10

        x = [0] + x[::-1]
        for i in range(len(x)-1, 0, -1):
            if x[i] > 9:
                x[i] -= 10
                x[i-1] += 1
            if x[i] == 9:
                x[i] = 0
                x[i-1] += 1
        return int(''.join(map(str, x))) if x[0] > 0 else int(''.join(map(str, x[1:])))



s = Solution()
print(s.newInteger(111))
print(s.newInteger(9))
print(s.newInteger(1232))
print(s.newInteger(1000000))
print(s.newInteger(123222222))