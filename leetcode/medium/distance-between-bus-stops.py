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
created by shhuan at 2019/12/19 17:24

"""

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        N = len(distance)
        i = start
        sa = 0
        while i != destination:
            sa += distance[i]
            i = (i + 1) % N

        sb = 0
        i = start
        while i != destination:
            sb += distance[(i-1) % N]
            i = (i-1) % N

        return min(sa, sb)

s = Solution()
print(s.distanceBetweenBusStops([1, 2, 3, 4], 0, 1))
print(s.distanceBetweenBusStops([1, 2, 3, 4], 0, 2))
print(s.distanceBetweenBusStops([1, 2, 3, 4], 3, 2))