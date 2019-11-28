# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/28/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

from typing import List

class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        N = len(A)
        A.sort()
        
        MOD = 10**9 + 7
        vi = {v: i for i, v in enumerate(A)}
        fac = collections.defaultdict(list)
        for i in range(N):
            for j in range(i, N):
                v = A[i] * A[j]
                if v > A[-1]:
                    break
                if v in vi:
                    fac[vi[v]].append((i, j))

        dp = [0] * N
        for k in range(N):
            dp[k] = (1 + sum([dp[i]*dp[j]*(1 if i == j else 2) for i, j in fac[k]])) % MOD

        return sum(dp) % MOD
        
        
s = Solution()
print(s.numFactoredBinaryTrees(A = [2, 4, 5, 10]))
print(s.numFactoredBinaryTrees(A = [2, 4]))