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
created by shhuan at 2019/11/10 10:44

"""

from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        N = len(colsum)
        A = [[0 for _ in range(N)] for _ in range(2)]
        oupper, olower = upper, lower

        for i, v in enumerate(colsum):
            if v == 2:
                A[0][i] = 1
                A[1][i] = 1
                upper -= 1
                lower -= 1
            elif v > 2 or v < 0:
                return []

        for i, v in enumerate(colsum):
            if v == 1:
                if upper > 0:
                    upper -= 1
                    A[0][i] = 1
                elif lower > 0:
                    lower -= 1
                    A[1][i] = 1
        if upper > 0 or lower > 0:
            return []
        if sum([A[0][i] for i in range(N)]) != oupper or sum([A[1][i] for i in range(N)]) != olower:
            return []
        for i, v in enumerate(colsum):
            if v != A[0][i] + A[1][i]:
                return []

        return A

s = Solution()
print(s.reconstructMatrix(upper = 2, lower = 1, colsum = [1,1,1]))
print(s.reconstructMatrix(upper = 2, lower = 3, colsum = [2,2,1,1]))
print(s.reconstructMatrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]))