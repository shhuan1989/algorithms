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
created by shhuan at 2019/12/22 22:06

"""


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        N, M = len(workers), len(bikes)

        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        dist = []
        for i, u in enumerate(workers):
            for j, v in enumerate(bikes):
                dist.append((manhattan(u, v), i, j))

        seenWorker, seenBike = set(), set()
        ans = [-1 for _ in range(N)]
        dist.sort()
        for d, i, j in dist:
            if i in seenWorker or j in seenBike:
                continue
            seenWorker.add(i)
            seenBike.add(j)
            ans[i] = j

        return ans

s = Solution()
print(s.assignBikes(workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]))
print(s.assignBikes(workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]))


