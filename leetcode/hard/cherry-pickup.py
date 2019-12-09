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
created by shhuan at 2019/12/8 21:56

"""
from functools import lru_cache

from functools import lru_cache

class Solution(object):
    def cherryPickup(self, grid: list) -> int:
        N = len(grid)

        @lru_cache(maxsize=N * N * N)
        def dp(x1, y1, x2):
            if x1 == 0 and y1 == 0:
                return grid[0][0]

            y2 = x1 + y1 - x2

            if x1 < 0 or x1 >= N or x2 < 0 or x2 >= N or y1 < 0 or y1 >= N or y2 < 0 or y2 >= N or grid[x1][y1] < 0 or \
                    grid[x2][y2] < 0:
                return float('-inf')

            c = grid[x1][y1] + grid[x2][y2] if x1 != x2 else grid[x1][y1]

            return c + max(dp(x1 - 1, y1, x2), dp(x1 - 1, y1, x2 - 1), dp(x1, y1 - 1, x2), dp(x1, y1 - 1, x2 - 1))

        return max(dp(N - 1, N - 1, N - 1), 0)


s = Solution()
print(s.cherryPickup([[0, 1, -1],
                      [1, 0, -1],
                      [1, 1,  1]]))

print(s.cherryPickup([[1,-1,-1,-1,-1],[1,0,1,-1,-1],[0,-1,1,0,1],[1,0,1,1,0],[-1,-1,-1,1,1]]))
