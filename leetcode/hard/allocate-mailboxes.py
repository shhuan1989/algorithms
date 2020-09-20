# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/26 22:38

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:

        houses.sort()
        n = len(houses)
        INF = 10**9

        index = [i for i in range(k)]
        points = [houses[i] for i in index]
        groups = [[] for _ in range(k)]
        for _ in range(1000):
            ngroups = [[] for _ in range(k)]
            pi = 0
            for i, x in enumerate(houses):
                if pi == k - 1:
                    ngroups[-1].append(x)
                else:
                    if abs(x - points[pi]) > abs(x - points[pi + 1]):
                        pi += 1
                    ngroups[pi].append(x)
            points = [sum(g)//len(g) for g in ngroups]
            if groups == ngroups:
                break
            groups = ngroups
        # print(groups)
        # print(points)
        points = [g[len(g)//2] if len(g) % 2 == 1 else (g[len(g)//2-1] + g[len(g)//2]) // 2 for g in groups]
        return sum([sum([abs(x-points[i]) for x in g]) for i, g in enumerate(groups)])




if __name__ == '__main__':
    s = Solution()
    print(s.minDistance([14,2,5,7,10], 2))
    print(s.minDistance([1,3,13,7,6], 2))
    print(s.minDistance([19,10,14,1,4,26,18,28,20], 3))
    print(s.minDistance([1, 4, 8, 10, 20], 3))
    print(s.minDistance([2, 3, 5, 12, 18], 2))
    print(s.minDistance([7, 4, 6, 1], 1))
    print(s.minDistance([3, 6, 14, 10], 4))