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
created by shhuan at 2019/12/16 00:24

"""

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        dist = []

        INF = 10**9
        N, M = len(grid), len(grid[0])
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    ds = [[INF for _ in range(M)] for _ in range(N)]
                    q = [(r, c, 0)]
                    while q:
                        nq = []
                        for x, y, d in q:
                            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0 and ds[nx][ny] == INF:
                                    ds[nx][ny] = d + 1
                                    nq.append((nx, ny, d+1))
                        q = nq
                    dist.append(ds)
        ans = INF
        for r in range(N):
            for c in range(M):
                d = sum([d[r][c] for d in dist])
                ans = min(ans, d)
        return ans if ans < INF else -1

s = Solution()
print(s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))