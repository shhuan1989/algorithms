# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/19/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



class Solution:
    def findNthDigit(self, n: int) -> int:
        
        
        def totalLen(val):
            nval = 0
            u = val
            while u > 0:
                u //= 10
                nval += 1
            
            w = 1
            for i in range(1, nval):
                w += i * (10**i - (10**(i-1)))
            
            