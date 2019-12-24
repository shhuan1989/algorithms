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
created by shhuan at 2019/12/24 22:48

"""


class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        if len(points) < 3:
            return False

        if len(points) == 3:
            return True

        N = len(points)
        points += [points[0], points[1]]
        pre = 0
        for i in range(N):
            dx1 = points[i+1][0] - points[i][0]
            dy1 = points[i+1][1] - points[i][1]
            dx2 = points[i+2][0] - points[i][0]
            dy2 = points[i+2][1] - points[i][1]
            curr = dx1 * dy2 - dx2 * dy1
            if curr != 0:
                if curr * pre < 0:
                    return False
                pre = curr

        return True


s = Solution()
print(s.isConvex([[0,0],[0,1],[1,1],[1,0]]))
print(s.isConvex([[0,0],[0,10],[10,10],[10,0],[5,5]]))
print(s.isConvex([[0,0],[1,1],[0,2],[-1,2],[-1,1]]))