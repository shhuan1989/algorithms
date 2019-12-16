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
created by shhuan at 2019/12/10 23:06

"""

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        q = [(r, c) for r in range(N) for c in range(M) if grid[r][c] == 1]
        if len(q) == N * M:
            return -1

        dist = 0
        while q:
            dist += 1
            nq = []
            for r, c in q:
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        nq.append((nr, nc))
            q = nq

        return dist - 1

s = Solution()
print(s.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
print(s.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))
