# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/2/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

import random

class Solution:
    
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        
        self.rects = rects
        self.areas = [(c - a + 1) * (d - b + 1) for (a, b, c, d) in rects]
        self.totalAreas = [0] * (len(rects) + 1)
        
        for i, a in enumerate(self.areas):
            self.totalAreas[i + 1] = self.totalAreas[i] + a
        
        self.totalArea = sum(self.areas)
    
    def pick(self):
        """
        :rtype: List[int]
        """
        
        area = random.randint(1, self.totalArea)
        index = bisect.bisect_left(self.totalAreas, area)

        # print(area, index, self.totalAreas)
        
        a, b, c, d = self.rects[index - 1]
        
        x = random.randint(a, c)
        y = random.randint(b, d)
        
        return [x, y]
