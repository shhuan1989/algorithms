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
created by shhuan at 2019/12/5 20:32

"""

class Solution:
    def numTilings_dp(self, N: int) -> int:
        a, b, c, d = 0, 0, 0, 1
        M = 10**9 + 7
        for i in range(1, N+1):
            na = d % M
            nb = (a + c) % M
            nc = (a + b) % M
            nd = (a + b + c + d) % M
            a, b, c, d = na, nb, nc, nd

        return d

    def numTilings(self, N):
        MOD = 10 ** 9 + 7

        def matrix_mult(A, B):
            return [[sum([a*b for a, b in zip([a[c] for a in A], row)]) % MOD for c in range(len(A[0]))] for r, row in enumerate(B)]

        def matrix_expo(A, K):
            if K == 0:
                return [[+(i == j) for j in range(len(A))]
                        for i in range(len(A))]
            if K == 1:
                return A
            elif K % 2:
                return matrix_mult(matrix_expo(A, K - 1), A)
            B = matrix_expo(A, K / 2)
            return matrix_mult(B, B)

        T = [[1, 0, 0, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 0],
             [1, 1, 1, 0]]

        return matrix_expo(T, N)[0][0]

s = Solution()
print(s.numTilings(3))
print(s.numTilings(4))
print(s.numTilings(1000))