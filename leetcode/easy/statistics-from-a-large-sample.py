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
created by shhuan at 2019/12/22 00:22

"""

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        N = len(count)
        minv = min([i for i in range(N) if count[i] > 0])
        maxv = max([i for i in range(N) if count[i] > 0])
        avg = sum([i*v for i, v in enumerate(count)]) / sum(count)

        median = 0
        l = sum(count)
        c = 0
        for i in range(N):
            c += count[i]
            if l % 2 == 1:
                if c * 2 > l:
                    median = i
                    break
            else:
                if c * 2 > l:
                    median = i
                    break
                elif c * 2 == l:
                    median = (i + i + 1) / 2
                    break
        most = max([(v, i) for i, v in enumerate(count)])[1]

        return [minv, maxv, avg, median, most]

s = Solution()
print(s.sampleStats([0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))