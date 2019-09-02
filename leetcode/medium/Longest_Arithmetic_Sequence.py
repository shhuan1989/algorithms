# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/1 15:16

求数组的所有子序列中，最长的等差数列的长度

设以当前元素A[i]为最后一个元素的所有等差数列为B[i]，那么

B[i] = {d: max(B[i][d], B[j][d]+1 for all j less than i}，其中d=A[i]-A[j]


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

        N = len(A)
        dp = [collections.defaultdict(int) for _ in range(N)]

        for i in range(1, N):
            a = A[i]
            for j in range(i):
                d = a-A[j]
                dp[i][d] = max(dp[i][d], dp[j][d]+1)
        print(dp)
        return max([max(d.values()) for d in dp]) + 1


s = Solution()
print(s.longestArithSeqLength([3, 6, 9, 12]))
print(s.longestArithSeqLength([9,4,7,2,10]))
print(s.longestArithSeqLength([20,1,15,3,10,5,8]))