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
created by shhuan at 2019/12/8 22:59

"""


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        H = [0] * M

        ans = 0
        for r, row in enumerate(grid):
            for c in range(M):
                if row[c] == 0:
                    H[c] = 0
                else:
                    ans = max(ans, 1)
                    H[c] += 1
                    for c2 in range(c+1, M):
                        if row[c2] == 0:
                            break
                        w = c2-c+1
                        if w > H[c]:
                            break
                        if r-w+1 < 0:
                            break
                        if H[c2]+1 >= w and all([grid[r-w+1][c3] == 1 for c3 in range(c, c2+1)]):
                            ans = max(ans, w)
        return ans * ans

s = Solution()
print(s.largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))
print(s.largest1BorderedSquare([[1, 1], [0, 0]]))