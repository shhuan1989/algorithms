# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/15 19:02

"""


class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """

        while tx > 0 and ty > 0:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                d = tx - max(sx, ty)
                k = max(d // ty, 1)
                tx, ty = tx - k * ty, ty
            elif tx < ty:
                d = ty - max(tx, sy)
                k = max(d // tx, 1)
                tx, ty = tx, ty - k * tx
            else:
                return False

        return False


s = Solution()
print(s.reachingPoints(9, 5, 12, 8))