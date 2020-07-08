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
    def isPathCrossing(self, path: str) -> bool:
        
        points = {(0, 0)}
        
        x, y = 0, 0
        for v in path:
            if v == 'N':
                y += 1
            elif v == 'S':
                y -= 1
            elif v == 'E':
                x += 1
            else:
                x -= 1
                
            if (x, y) in points:
                return True
            points.add((x, y))
            
        return False
    
s = Solution()
print(s.isPathCrossing('NES'))
print(s.isPathCrossing('NESWW'))