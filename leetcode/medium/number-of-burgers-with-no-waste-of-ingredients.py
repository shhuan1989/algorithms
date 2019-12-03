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
created by shhuan at 2019/12/1 10:39

"""

from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
         x = (tomatoSlices - 2 * cheeseSlices) // 2
         y = cheeseSlices - x

         if x >= 0 and y >= 0 and 4*x+2*y == tomatoSlices:
             return [x, y]

         return []

s = Solution()
print(s.numOfBurgers(16, 7))
print(s.numOfBurgers(17, 4))
print(s.numOfBurgers(4, 17))
print(s.numOfBurgers(0, 0))
print(s.numOfBurgers(2, 1))