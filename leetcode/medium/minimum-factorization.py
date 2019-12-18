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
created by shhuan at 2019/12/18 22:54

"""


class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a == 1:
            return 1

        digits = []
        for d in range(9, 1, -1):
            while a % d == 0:
                digits.append(d)
                a //= d

        if not digits:
            return 0

        ans = int(''.join(map(str, digits[::-1])))

        return ans if a == 1 and ans <= (1 << 31) - 1 else 0


s = Solution()
print(s.smallestFactorization(48))
print(s.smallestFactorization(15))
print(s.smallestFactorization(18000000))
print(s.smallestFactorization(11))