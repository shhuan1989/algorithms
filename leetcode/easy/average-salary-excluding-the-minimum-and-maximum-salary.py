# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        a, b = min(salary), max(salary)
        
        if a == b:
            return a
        
        ai, bi = -1, -1
        for i, v in enumerate(salary):
            if v == a:
                ai = i
            if v == b:
                bi = i
                
        s = sum([v for i, v in enumerate(salary) if i != ai and i != bi])
        return s / (len(salary) -2)
        
        
s = Solution()
print(s.average([4000,3000,1000,2000]))
print(s.average([1000,2000,3000]))
print(s.average([6000,5000,4000,3000,2000,1000]))
print(s.average([8000,9000,2000,3000,6000,1000]))
        
        
        