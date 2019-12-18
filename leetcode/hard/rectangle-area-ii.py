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
created by shhuan at 2019/12/17 20:17

"""


class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        xs = {r[0] for r in rectangles}
        xs |= {r[2] for r in rectangles}
        xs = list(xs)
        xs.sort()
        rectangles.sort()

        ans = 0

        for i in range(len(xs)-1):
            x1, x2 = xs[i], xs[i+1]
            ys = [(r[1], r[3]) for r in rectangles if r[0] <= x1 and r[2] >= x2]
            if not ys:
                continue
            ys.sort()

            ysum = 0
            y1, y2 = ys[0]
            for j in range(1, len(ys)):
                yp1, yp2 = ys[j]

                if y1 <= yp1 <= y2:
                    y2 = max(y2, yp2)
                else:
                    ysum += y2 - y1
                    y1, y2 = yp1, yp2

            ysum += y2-y1


            ans += (x2-x1) * ysum
            ans %= 10**9 + 7

        return ans
