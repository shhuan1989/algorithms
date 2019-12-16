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
created by shhuan at 2019/12/15 13:15

"""


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        def dist1d(x, mid):
            return sum([abs(v-mid) for v in x])

        def best1d(x):
            q = []
            heapq.heapify(q)
            n = len(x)
            for i, v in enumerate(x):
                heapq.heappush(q, -v)
                if i > n // 2:
                    heapq.heappop(q)

            if n % 2 == 1:
                mid = abs(heapq.heappop(q))
            else:
                mid = (abs(heapq.heappop(q)) + abs(heapq.heappop(q))) // 2

            return dist1d(x, mid)

        points = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    points.append((r, c))
        return best1d([x for x, y in points]) + best1d([y for x, y in points])

s = Solution()
print(s.minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))