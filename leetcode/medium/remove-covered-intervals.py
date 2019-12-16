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
created by shhuan at 2019/12/14 22:31

"""


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        N = len(intervals)
        rem = [0] * N
        for i in range(N):
            a = intervals[i]
            for j in range(i+1, N):
                b = intervals[j]
                if b[1] <= a[1]:
                    rem[j] = 1
                if b[0] > a[1]:
                    break

        return N - sum(rem)


s = Solution()
print(s.removeCoveredIntervals([[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]))