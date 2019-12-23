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
created by shhuan at 2019/12/20 20:21

|a1-a2| + |b1-b2| = a1-a2+b1-b2 or (a1-a2)-(b1-b2) or -(a1-a2)+(b1-b2) or -(a1-a2)-(b1-b2)
"""

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:

        # max, min of a + b - i
        a1, a2 = arr1[0] + arr2[0], arr1[0] + arr2[0]

        # max, min of a-b-i
        b1, b2 = arr1[0] - arr2[0], arr1[0] - arr2[0]

        N = min(len(arr1), len(arr2))
        ans = float('-inf')
        for i in range(1, N):
            u, v = arr1[i], arr2[i]

            w1 = u + v + i - a2
            w2 = u - v + i - b2
            w3 = - (u - v) + i + b1
            w4 = -(u + v) + i + a1

            ans = max(ans, w1, w2, w3, w4)

            a1 = max(a1, u + v - i)
            a2 = min(a2, u + v + i)
            b1 = max(b1, u - v - i)
            b2 = min(b2, u - v + i)

        return ans

s = Solution()
print(s.maxAbsValExpr(arr1 = [1,2,3,4], arr2 = [-1,4,5,6]))
print(s.maxAbsValExpr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]))