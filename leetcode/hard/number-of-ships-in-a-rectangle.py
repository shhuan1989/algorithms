# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/16/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
class Sea(object):
    def __init__(self, ships):
        self.ships = ships
        self.called = 0
        
    def hasShips(self, topRight: Point, bottomLeft: Point) -> bool:
        self.called += 1
        xl, xr = bottomLeft.x, topRight.x
        yl, yr = bottomLeft.y, topRight.y
        return any([xl <= ship[0] <= xr and yl <= ship[0] <= yr for ship in self.ships])


class Solution(object):
    def countShips(self, sea: Sea, topRight: Point, bottomLeft: Point) -> int:
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        xl, xr = bottomLeft.x, topRight.x
        yl, yr = bottomLeft.y, topRight.y
        
        if xl == xr and yl == yr:
            return 1 if sea.hasShips(topRight, bottomLeft) else 0
        elif xl == xr:
            my = (yl + yr) // 2
            return self.countShips(sea, Point(xl, my), bottomLeft) + self.countShips(sea, topRight, Point(xl, my+1))
        
        else:
            mx = (xl + xr) // 2
            return self.countShips(sea, Point(mx, yr), bottomLeft) + self.countShips(sea, topRight, Point(mx+1, yl))
            

            
# sea = Sea([[1, 1], [2, 2], [3, 3], [5, 5]])
# s = Solution()
# print(s.countShips(sea, Point(4, 4), Point(0, 0)))

sea = Sea([[556,290],[286,960],[728,419],[770,159],[743,306],[674,140],[37,232],[515,544],[883,449]])
s = Solution()
print(s.countShips(sea, Point(1000, 1000), Point(0, 0)))
print(sea.called)