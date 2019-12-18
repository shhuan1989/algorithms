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
created by shhuan at 2019/12/19 00:06

"""

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N = len(A)
        presum = [0] * (N+1)
        for i, v in enumerate(A):
            presum[i+1] = presum[i] + v

        ans = float('-inf')

        for i in range(N-M-L+1):
            sa = presum[i+L] - presum[i]
            for j in range(i+L, N-M+1):
                sb = presum[j+M] - presum[j]
                ans = max(ans, sa + sb)

        for i in range(N-M-L+1):
            sa = presum[i+M] - presum[i]
            for j in range(i+M, N-L+1):
                sb = presum[j+L] - presum[j]
                ans = max(ans, sa + sb)

        return ans

s = Solution()
print(s.maxSumTwoNoOverlap(A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2))
print(s.maxSumTwoNoOverlap(A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2))
print(s.maxSumTwoNoOverlap(A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3))