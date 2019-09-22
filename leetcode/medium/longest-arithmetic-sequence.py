# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/20 19:47

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
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0

        N = len(A)
        dp = [collections.defaultdict(int) for _ in range(N)]

        for i in range(1, N):
            for j in range(i):
                d = A[i]-A[j]
                dp[i][d] = max(dp[i][d], dp[j][d]+1)

        # print(dp)
        return max([max(v.values() or [0]) for v in dp] or [0]) + 1


s = Solution()
print(s.longestArithSeqLength([3, 6, 9, 12]))
print(s.longestArithSeqLength([9,4,7,2,10]))
print(s.longestArithSeqLength([20,1,15,3,10,5,8]))