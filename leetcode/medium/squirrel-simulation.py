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
created by shhuan at 2019/12/19 21:41

"""

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        nuts = {(x, y) for x, y in nuts}
        dist = {}
        q = [(tree[0], tree[1])]
        step = 0
        vis = set()
        while q:
            nq = []
            for x, y in q:
                k = (x, y)
                if k in nuts:
                    dist[k] = step

                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nx < height and 0 <= ny < width:
                        k = (nx, ny)
                        if k not in vis:
                            vis.add(k)
                            nq.append(k)
            q = nq
            step += 1

        ans = float('inf')
        dt = sum(dist.values()) * 2
        for start in nuts:
            d = abs(squirrel[0] - start[0]) + abs(squirrel[1] - start[1])
            d += dt
            d -= dist[start]
            ans = min(ans, d)

        return ans

s = Solution()
# print(s.minDistance(5, 7, [2, 2], [4, 4], [[3, 0], [2, 5]]))
print(s.minDistance(1, 3, [0,1], [0,0], [[0,2]]))