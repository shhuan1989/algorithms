
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
created by shhuan at 2019/12/1 10:46

"""

from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        N, M = len(matrix), len(matrix[0])
        H = [0] * M

        ans = 0
        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 1:
                    H[c] += 1
                else:
                    H[c] = 0
            for c in range(M):
                h = float('inf')
                w = 1
                for cr in range(c, M):
                    h = min(h, H[cr])
                    if h < w:
                        break
                    ans += 1
                    w += 1

        return ans

s = Solution()
print(s.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))
# print(s.countSquares([
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]))
# print(s.countSquares([
#     [0,0,0],
#     [0,1,0],
#     [0,1,0],
#     [1,1,1],
#     [1,1,0]]))