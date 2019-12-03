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
created by shhuan at 2019/11/24 10:34

"""

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]

        for r in range(n):
            w = len([c for c in range(m) if grid[r][c] == 1])
            if w > 1:
                for c in range(m):
                    if grid[r][c] == 1:
                        ans[r][c] = 1

        for c in range(m):
            w = len([r for r in range(n) if grid[r][c] == 1])
            if w > 1:
                for r in range(n):
                    if grid[r][c] == 1:
                        ans[r][c] = 1

        ret = sum([sum(row) for row in ans] or [0])

        return ret

s = Solution()
print(s.countServers( [[1,0],[0,1]]))
print(s.countServers([[1,0],[1,1]]))
print(s.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
print(s.countServers([[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]))