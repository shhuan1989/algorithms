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
created by shhuan at 2019/12/15 21:04

"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:

        a, e, i, o, u = 1, 1, 1, 1, 1
        MOD = 10**9+7
        for _ in range(1, n):
            na = (e + i + u) % MOD
            ne = (a + i) % MOD
            ni = (e + o) % MOD
            no = i % MOD
            nu = (i + o) % MOD

            a, e, i, o, u = na, ne, ni, no, nu

        return (a+e+i+o+u) % MOD

s = Solution()
# print(s.countVowelPermutation(1))
# print(s.countVowelPermutation(2))
print(s.countVowelPermutation(5))