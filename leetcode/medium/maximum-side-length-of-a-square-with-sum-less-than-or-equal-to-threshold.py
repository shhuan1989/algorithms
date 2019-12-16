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
created by shhuan at 2019/12/15 10:35

"""


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        A = mat
        N, M = len(A), len(A[0])

        presum = [[0 for _ in range(M+1)] for _ in range(N+1)]
        for r in range(1, N+1):
            for c in range(1, M+1):
                presum[r][c] = presum[r][c-1] + A[r-1][c-1]
            for c in range(M+1):
                presum[r][c] += presum[r-1][c]

        maxw = min(M, N)

        def check(w):
            for r1 in range(N-w+1):
                r2 = r1 + w
                for c1 in range(M-w+1):
                    c2 = c1 + w
                    s = presum[r2][c2] - presum[r2][c1] - (presum[r1][c2] - presum[r1][c1])
                    if s <= threshold:
                        return True
            return False

        lo, hi = 0, maxw
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return hi

s = Solution()
print(s.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4))
print(s.maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1))
print(s.maxSideLength([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6))
print(s.maxSideLength( [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184))

