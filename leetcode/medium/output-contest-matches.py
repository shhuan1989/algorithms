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
created by shhuan at 2019/12/19 22:02

"""

class Solution:
    def findContestMatch(self, n: int) -> str:

        q = [([i+1, n-i],'({},{})'.format(i+1, n-i)) for i in range(n//2)]
        q.sort()
        while len(q) > 1:
            nq = [(q[i][0] + q[len(q)-i-1][0], '({},{})'.format(q[i][1], q[len(q)-i-1][1])) for i in range(len(q)//2)]
            nq.sort()
            q = nq

        return q[0][1]

s = Solution()
print(s.findContestMatch(32))
print("(((((1,32),(16,17)),((8,25),(9,24))),(((4,29),(13,20)),((5,28),(12,21)))),((((2,31),(15,18)),((7,26),(10,23))),(((3,30),(14,19)),((6,27),(11,22)))))")
