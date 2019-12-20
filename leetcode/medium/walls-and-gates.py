# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/20/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        
        N, M = len(rooms), len(rooms[0])

        def neighbors(x, y):
            return [(nx, ny) for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if 0 <= nx < N and 0 <= ny < M]
        
        q = []
        for r in range(N):
            for c in range(M):
                if rooms[r][c] == 0:
                    q.append((0, r, c))
        
        while q:
            d, r, c = heapq.heappop(q)
            for nr, nc in neighbors(r, c):
                if rooms[nr][nc] != -1 and d + 1 < rooms[nr][nc]:
                    rooms[nr][nc] = d + 1
                    heapq.heapify(q, (d+1, nr, nc))
        
