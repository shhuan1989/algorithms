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
created by shhuan at 2019/12/12 23:52

"""

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:

        q = [((width-1-i)//sideLength+1)*((height-1-j)//sideLength + 1) for i in range(sideLength) for j in range(sideLength)]

        return sum(sorted(q, reverse=True)[:maxOnes])

s = Solution()
print(s.maximumNumberOfOnes(width = 3, height = 3, sideLength = 2, maxOnes = 1))