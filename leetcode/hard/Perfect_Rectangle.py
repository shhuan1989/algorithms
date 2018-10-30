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
created by shhuan at 2017/11/27 20:31

"""


class Solution:
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """

        A = set(rectangles)

        xmin = min([x[0] for x in A])
        xmax = max([x[1] for x in A])
        ymin = min([x[2] for x in A])
        ymax = max([x[3] for x in A])


        rects = [(xmin, xmax, ymin, ymax)]

        while rects and A:
            u = rects[0]
            v = None
            for x in A:
                # v covers left bottom of u
                if v[0] == u[0] and v[1] <= u[1] and v[2] == u[2] and v[3] <= u[3]:
                    v = x
                    break
            if not v:
                return False
            A.remove(v)






        for u in A:
            f = False
            for v in rects:
                # u covers left bottom of v
                if v[0] <= u[0] <= u[1] <= v[1] and v[2] <= u[2] <= u[3] <= v[2]:
                    f = True
                    #

            if not f:
                return False

        if rects:
            return False

        return True


