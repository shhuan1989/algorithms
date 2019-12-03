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
created by shhuan at 2019/11/24 10:32

"""

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        def dist(a, b):
            dx, dy = abs(a[0]-b[0]), abs(a[1]-b[1])

            return min(dx, dy) + abs(dx-dy)


        ans = 0
        for a, b in zip(points[:-1], points[1:]):
            ans += dist(a, b)

        return ans


s = Solution()
print(s.minTimeToVisitAllPoints( [[1,1],[3,4],[-1,0]]))
print(s.minTimeToVisitAllPoints([[3,2],[-2,2]]))
