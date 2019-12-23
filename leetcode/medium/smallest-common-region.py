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
created by shhuan at 2019/12/19 21:16

"""

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        parent = {}
        for reg in regions:
            for v in reg[1:]:
                parent[v] = reg[0]

        p1 = []
        u = region1
        while True:
            p1.append(u)
            if u not in parent:
                break
            u = parent[u]

        p2 = []
        u = region2
        while True:
            p2.append(u)
            if u not in parent:
                break
            u = parent[u]

        p1, p2 = p1[::-1], p2[::-1]
        for i in range(min(len(p1), len(p2))):
            if p1[i] != p2[i]:
                return p1[i-1]

        print(p1, p2)

        if len(p1) < len(p2):
            return p1[-1]
        else:
            return p2[-1]

s = Solution()
print(s.findSmallestRegion(regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"))