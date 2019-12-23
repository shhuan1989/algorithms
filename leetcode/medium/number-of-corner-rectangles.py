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
created by shhuan at 2019/12/19 17:01

"""


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        N, M = len(grid), len(grid[0])
        cols = collections.defaultdict(set)
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    cols[r].add(c)

        ans = 0
        cols = list(cols.values())
        ncols = len(cols)
        for i in range(ncols):
            for j in range(i+1, ncols):
                s = len(cols[i].intersection(cols[j]))
                ans += s * (s - 1) // 2

        return ans


s = Solution()
print(s.countCornerRectangles(
    [[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]))
print(s.countCornerRectangles(
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
))