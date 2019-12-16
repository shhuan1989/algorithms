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
created by shhuan at 2019/12/9 23:06

"""

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def maxsum(A):
            N = len(A)
            pre = [0] * (N + 1)
            for i, v in enumerate(A):
                pre[i + 1] = pre[i] + v

            maxpre = [0] * (N + 1)
            for i in range(N, -1, -1):
                maxpre[i] = max(maxpre[i + 1] if i + 1 <= N else float('-inf'), pre[i])

            ans = 0
            for i in range(N + 1):
                ans = max(ans, maxpre[i] - pre[i])
            return ans

        MOD = 10 ** 9 + 7
        if k == 1:
            return maxsum(arr) % MOD
        elif k == 2:
            return maxsum(arr + arr) % MOD

        s = sum(arr)
        if s > 0:
            ans = s * (k-2)
            c, d = 0, 0
            for v in (arr):
                c += v
                d = max(d, c)
            ans += d
            c, d = 0, 0
            for v in reversed(arr):
                c += v
                d = max(d, c)
            ans += d
            return ans % MOD
        else:
            return maxsum(arr + arr + arr) % MOD

s = Solution()
print(s.kConcatenationMaxSum([1, 2], 3))
print(s.kConcatenationMaxSum([1, -2, 1], 5))
print(s.kConcatenationMaxSum([-1, -1], 7))
print(s.kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4], 5))
