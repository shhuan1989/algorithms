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
created by shhuan at 2019/12/4 23:05

"""

from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        N, M = len(grid), len(grid[0])

        conn = set()

        def dfs(r, c):
            if not (0 <= r < N and 0 <= c < M and grid[r][c] == grid[r0][c0]):
                return

            conn.add((r, c))

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (nr, nc) not in conn:
                    dfs(nr, nc)

        dfs(r0, c0)

        border = {(r, c) for r, c in conn if sum([1 if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == grid[r0][c0] else 0
                                 for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]]) != 4}

        for r, c in border:
            grid[r][c] = color

        return grid

s = Solution()
print(s.colorBorder([
    [1,2,1,2,1,2],
    [2,2,2,2,1,2],
    [1,2,2,2,1,2]
], 1, 3, 1))
print(s.colorBorder(grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3))
print(s.colorBorder(grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3))
print(s.colorBorder(grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2))
