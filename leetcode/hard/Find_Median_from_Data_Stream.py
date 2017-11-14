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
created by shhuan at 2017/11/10 16:09

"""


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        self.median = None

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """

        if not self.median:
            self.large.append(num)
            self.median = num
        else:
            if num > self.median:
                heapq.heappush(self.large, num)
            else:
                heapq.heappush(self.small, -num)

            while len(self.large) > len(self.small)+1:
                v = heapq.heappop(self.large)
                heapq.heappush(self.small, -v)

            while len(self.small) > len(self.large):
                v = heapq.heappop(self.small)
                heapq.heappush(self.large, -v)

            if len(self.small) == len(self.large):
                self.median = (-self.small[0] + self.large[0]) / 2.0
            else:
                self.median = self.large[0]

    def findMedian(self):
        """
        :rtype: float
        """

        return self.median

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(5)
print(obj.findMedian())
