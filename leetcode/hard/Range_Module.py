# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/19/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """

        l = bisect.bisect_left(self.ranges, [left, float('-inf')])
        l = max(0, l-1)
        r = bisect.bisect_right(self.ranges, [right, float('inf')])




    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)