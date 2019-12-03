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
created by shhuan at 2019/11/17 10:31

"""

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        for i in range(k):
            right = [row[:-1] for row in grid]
            col = [row[-1] for row in grid]
            col = [col[-1]] + col[:-1]
            grid = [[col[i]] + right[i] for i in range(n)]

        for row in grid:
            print(row)
        return grid

s = Solution()
s.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)
s.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4)
s.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9)
