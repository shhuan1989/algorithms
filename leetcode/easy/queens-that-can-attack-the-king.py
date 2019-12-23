# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/21 23:41

"""

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        left = [(x, y) for x, y in queens if y == king[1] and x < king[0]]
        if left:
            ans.append(max(left))

        right = [(x, y) for x, y in queens if y == king[1] and x > king[0]]
        if right:
            ans.append(min(right))

        up = [(x, y) for x, y in queens if x == king[0] and y > king[1]]
        if up:
            ans.append(min(up))

        down = [(x, y) for x, y in queens if x == king[0] and y < king[1]]
        if down:
            ans.append(max(down))

        leftup = [(x, y) for x, y in queens if abs(x-king[0]) == abs(y-king[1]) and x < king[0] and y > king[1]]
        if leftup:
            ans.append(max(leftup))

        rightup = [(x, y) for x, y in queens if abs(x-king[0]) == abs(y-king[1]) and x > king[0] and y > king[1]]
        if rightup:
            ans.append(min(rightup))

        leftdown = [(x, y) for x, y in queens if abs(x-king[0]) == abs(y-king[1]) and x < king[0] and y < king[1]]
        if leftdown:
            ans.append(max(leftdown))

        rightdown = [(x, y) for x, y in queens if abs(x-king[0]) == abs(y-king[1]) and x > king[0] and y < king[1]]
        if rightdown:
            ans.append(min(rightdown))

        return ans
