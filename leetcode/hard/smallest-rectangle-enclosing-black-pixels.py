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
created by shhuan at 2019/12/15 11:54

"""

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:

        q = [(x, y)]
        vis = {(x, y)}
        minx, miny, maxx, maxy = x, y, x, y
        N, M = len(image), len(image[0])
        while q:
            x, y = q.pop()
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < N and 0 <= ny < M and image[nx][ny] == '1' and (nx, ny) not in vis:
                    vis.add((nx, ny))
                    q.append((nx, ny))
                    minx = min(minx, nx)
                    miny = min(miny, ny)
                    maxx = max(maxx, nx)
                    maxy = max(maxy, ny)

        return (maxx - minx + 1) * (maxy - miny + 1)

s = Solution()
print(s.minArea(["0010", "0110", "0100"], 0, 2))