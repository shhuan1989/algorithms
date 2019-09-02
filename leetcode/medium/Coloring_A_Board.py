# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/1 15:55


指定一个位置，把同一个联通块（颜色一样的上下左右相连的）的边界涂成指定的颜色
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
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        q = [(r0, c0)]
        vis = {(r0, c0)}

        ocolor = grid[r0][c0]
        m, n = len(grid), len(grid[0])
        ans = [[grid[r][c] for c in range(n)] for r in range(m)]
        while q:
            r, c = q.pop()
            if r in {0, m-1} or c in {0, n-1} or any([grid[nr][nc] != grid[r0][c0] for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]]):
                ans[r][c] = color

            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                nrc = (nr, nc)
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == ocolor and nrc not in vis:
                    vis.add(nrc)
                    q.append(nrc)

        return ans

