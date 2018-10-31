# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/11/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        
        def canFinish(speed):
            
            t = sum([p//speed if p % speed == 0 else p//speed+1 for p in piles])
            
            return t <= H
        
        l, r = 1, max(piles)
        
        while l < r:
            
            m = (l + r) // 2
            if canFinish(m):
                r = m
            else:
                l = m+1
        
        return l



s = Solution()
print(s.minEatingSpeed([30,11,23,4,20], 6))
print(s.minEatingSpeed([30,11,23,4,20], 5))
print(s.minEatingSpeed([3,6,7,11], 8))