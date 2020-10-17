# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/15 20:13

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


from functools import cmp_to_key
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:

        def getangle(x1, y1, x2, y2):
            a = x1 * x2 + y1 * y2
            b = math.sqrt(x1**2 + y1**2) * math.sqrt(x2**2 + y2**2)
            return math.acos(a/b) * 



        x1, y1 = 1, 0

        def mycmp(p1, p2):
            alpha = getangle(x1, y1, p1[0]-location[0], p1[1]-location[1])
            beta = getangle(x1, y1, p2[0]-location[0], p2[1]-location[1])
            return alpha-beta

        pointsbyangle = [(getangle(x1, y1, p[0]-location[0], p[1]-location[1]), p[0], p[1]) for p in points]
        pointsbyangle.sort()

        print(pointsbyangle)


if __name__ == '__main__':
    s = Solution()
    print(s.visiblePoints([[2,1],[2,2],[3,3], [1, 2], [0, 1], [0, 0], [1, -1], [2, -1]], angle = 90, location = [1,1]))