# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/22 10:12

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if not A:
            return []


        N = len(A)
        rightmin = float('inf')
        for i in range(N-1, -1, -1):
            if A[i] > rightmin:
                rj = -1
                for j in range(i, N):
                    if A[i] > A[j]:
                        if rj < 0 or A[j] > A[rj]:
                            rj = j
                A[i], A[rj] = A[rj], A[i]
                break

            rightmin = min(A[i], rightmin)

        return A


s = Solution()
print(s.prevPermOpt1([3, 2, 1]))
print(s.prevPermOpt1([1, 2, 3]))
print(s.prevPermOpt1([1, 9, 4, 6, 7]))
print(s.prevPermOpt1([3, 1, 1, 3]))
