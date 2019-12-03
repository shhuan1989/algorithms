
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
created by shhuan at 2019/12/2 19:16

"""

from typing import List

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        if not A or len(A) < 2:
            return False

        sa = sum(A)
        N = len(A)

        dp = [0 for _ in range(sa+1)]

        def dfs(index, pre, count):
            if index >= N or count >= min(N-1, N//2+1):
                return

            dp[pre] |= 1 << count

            dfs(index+1, pre, count)
            dfs(index+1, pre+A[index], count+1)

        dfs(0, 0, 0)

        for v in range(1, sa+1):
            # v/c == sa / n
            if (v * N) % sa == 0:
                c = v * N // sa
                if dp[v] & (1 << c) > 0:
                    return True

        return False








s = Solution()
# print(s.splitArraySameAverage([10,29,13,53,33,48,76,70,5,5]) == True)
# print(s.splitArraySameAverage([2,12,18,16,19,3]) == False)
# print(s.splitArraySameAverage([18,10,5,3]) == False)
print(s.splitArraySameAverage([3, 1, 2]) == True)
print(s.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]) == True)
print(s.splitArraySameAverage([3, 1]) == False)
print(s.splitArraySameAverage([6,8,18,3,1]) == False)
print(s.splitArraySameAverage([18, 0, 16, 2]) == True)
print(s.splitArraySameAverage([60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]) == False)
t0 = time.time()
print(s.splitArraySameAverage([9990,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))
print(time.time() - t0)