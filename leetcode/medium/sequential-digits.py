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
created by shhuan at 2019/12/15 10:32

"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        q = [i for i in range(1, 10)]
        while q:
            v = q.pop()
            if low <= v <= high:
                ans.append(v)

            if v % 10 < 9:
                nv = v * 10 + (v % 10 + 1)
                q.append(nv)

        return list(sorted(ans))

s = Solution()
print(s.sequentialDigits(100, 300))
print(s.sequentialDigits(1000, 13000))
