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
created by shhuan at 2019/12/15 11:00

"""


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = [(0, 0, 0, 0)]
        vis = {}
        N, M = len(grid), len(grid[0])
        heapq.heapify(q)
        while q:
            step, r, c, rem = heapq.heappop(q)
            if r == N-1 and c == M-1:
                return step
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < N and 0 <= nc < M:
                    if grid[nr][nc] == 1:
                        if rem + 1 > k:
                            continue
                        vk = (nr, nc, rem+1)
                        if vk not in vis or step + 1 < vis[vk]:
                            vis[vk] = step+1
                            heapq.heappush(q, (step+1, nr, nc, rem+1))
                    else:
                        vk = (nr, nc, rem)
                        if vk not in vis or step + 1 < vis[vk]:
                            vis[vk] = step + 1
                            heapq.heappush(q, (step+1, nr, nc, rem))
        return -1

s = Solution()
print(s.shortestPath([[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 1))
print(s.shortestPath(grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1))