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
created by shhuan at 2020/1/11 22:32

"""


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        A = mat
        if not A or not A[0]:
            return [[]]

        N, M = len(A), len(A[0])
        ans = [[0 for _ in range(M)] for _ in range(N)]

        for r in range(N):
            s = 0
            for x in range(max(0, r - K), min(r + K + 1, N)):
                for y in range(0, min(K + 1, M)):
                    s += A[x][y]
            ans[r][0] = s
            for c in range(1, M):
                if c + K < M:
                    for x in range(max(0, r - K), min(r + K + 1, N)):
                        s += A[x][c+K]
                if c - K - 1 >= 0:
                    for x in range(max(0, r - K), min(r + K + 1, N)):
                        s -= A[x][c - K - 1]
                ans[r][c] = s

        return ans


s = Solution()
print(s.matrixBlockSum([[76,4,73],[21,8,56],[4,56,61],[70,32,38],[31,94,67]], 1))
print(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1))
print(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2))
print(s.matrixBlockSum([], 1))
print(s.matrixBlockSum([[1]], 1))
