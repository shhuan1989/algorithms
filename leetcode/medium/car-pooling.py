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
created by shhuan at 2019/12/4 23:36

"""

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        onoff = collections.defaultdict(int)
        for v, s, t in trips:
            onoff[s] += v
            onoff[t] -= v

        onoff = [(k, v) for k, v in onoff.items()]
        onoff.sort()

        count = 0
        for t, v in onoff:
            count += v
            if count > capacity:
                return False

        return True

s = Solution()
print(s.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4))
print(s.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5))
print(s.carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3))
print(s.carPooling(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11))