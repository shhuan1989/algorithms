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
created by shhuan at 2019/12/16 23:48

"""

class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def count(val, d):
            cnt, k = 0, 0
            i = 1
            while val // i != 0:
                k = val // i
                h = k // 10
                if d == 0:
                    if h != 0:
                        h -= 1
                    else:
                        break

                cnt += h * i
                cur = k % 10
                if cur > d:
                    cnt += i
                elif cur == d:
                    cnt += val - k * i + 1
                i *= 10
            return cnt

        return count(high, d) - count(low-1, d)


s = Solution()
print(s.digitsCount(1, 1, 13))
print(s.digitsCount(3, 100, 250))