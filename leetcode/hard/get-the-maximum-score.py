# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/2 11:03

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List
from functools import lru_cache


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:

        via = {v:i for i, v in enumerate(nums1)}
        vib = {v:i for i, v in enumerate(nums2)}
        na, nb = len(nums1), len(nums2)
        n = max(na, nb)

        nums1 += [0] * (n - len(nums1))
        nums2 += [0] * (n - len(nums2))
        A = [[a, b] for a, b in zip(nums1, nums2)]

        same = []
        for v in set(nums1 + nums2):
            if v in via and v in vib:
                same.append((via[v], vib[v]))
        same.sort()
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = A[0][0]
        dp[0][1] = A[0][1]

        i, j = 0, 0
        for ia, ib in same:
            while i < ia:
                dp[i][0] = max(dp[i][0], dp[i-1][0] + A[i][0])
                i += 1
            while j < ib:
                dp[j][1] = max(dp[j][1], dp[j-1][1] + A[j][1])
                j += 1

            dp[i][0] = max(dp[i][0], (dp[i-1][0] + A[i][0]) if i-1 >= 0 else A[i][0], dp[j-1][1] + A[i][0])
            dp[j][1] = max(dp[j][1], (dp[j-1][1] + A[j][1]) if j - 1 >= 0 else  A[j][1], dp[i-1][0] + A[j][1])

        while i < n:
            dp[i][0] = max(dp[i][0], dp[i-1][0] + A[i][0])
            i += 1
        while j < n:
            dp[j][1] = max(dp[j][1], dp[j-1][1] + A[j][1])
            j += 1

        return max(dp[-1]) % (10**9+7)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]))
    print(s.maxSum(nums1 = [1,3,5,7,9], nums2 = [3,5,100]))
    print(s.maxSum(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]))
    print(s.maxSum(nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]))
