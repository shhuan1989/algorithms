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
created by shhuan at 2019/12/10 22:54

"""


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = [start]

        b = start
        while start >> 1:
            start >>= 1
            b ^= start

        n = (1 << n) - 1
        for i in range(1, n+1):
            ans.append(b + i & n ^ (b + i & n) >> 1)

        return ans

s = Solution()
print(s.circularPermutation(2, 3))
print(s.circularPermutation(3, 2))