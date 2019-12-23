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
created by shhuan at 2019/12/22 11:30

"""

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def check(a):
            if not a:
                return False
            n, m = len(a), len(a[0])
            if n != 3 or m != 3:
                return False

            vs = set()
            for r in range(n):
                for c in range(m):
                    vs.add(a[r][c])

            if any([i not in vs for i in range(1, 10)]):
                return False


            s = sum(a[0])
            if any([sum(row) != s for row in a]):
                return False
            if any([sum([a[r][c] for r in range(n)]) != s for c in range(m)]):
                return False
            if sum([a[i][i] for i in range(3)]) != s:
                return False
            if sum([a[i][2-i] for i in range(3)]) != s:
                return False

            return True
        N, M = len(grid), len(grid[0])
        ans = 0
        for r in range(N-2):
            for c in range(M-2):
                if check([[grid[x][y] for y in range(c, c+3)] for x in range(r, r+3)]):
                    ans += 1
        return ans

s = Solution()
print(s.numMagicSquaresInside( [[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]]))
print(s.numMagicSquaresInside([[5,5,5],[5,5,5],[5,5,5]]))
