# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/22 09:52

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
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        N, M = len(grid), len(grid[0])
        up, down, left, right = [0] * M, [0] * M, [0] * N, [0] * N

        # up
        for r in range(N):
            for c in range(M):
                up[c] = max(up[c], grid[r][c])

        # down
        for r in range(N-1, -1, -1):
            for c in range(M):
                down[c] = max(down[c], grid[r][c])

        # left
        for c in range(M):
            for r in range(N):
                left[r] = max(left[r], grid[r][c])

        # right
        for c in range(M-1, -1, -1):
            for r in range(N):
                right[r] = max(right[r], grid[r][c])


        ans = 0
        for r in range(N):
            for c in range(M):
                ans += max(0, min(left[r], right[r], up[c], down[c]) - grid[r][c])

        return ans


s = Solution()
print(s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))


