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
created by shhuan at 2019/12/24 23:35

"""

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if start == destination:
            return 0

        N, M = len(maze), len(maze[0])
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dexp = ['U', 'D', 'L', 'R']
        q = [(0, start[0], start[1], d) for d in range(4)]
        vis = {(x, y, d) for _, x, y, d in q}
        while q:
            dist, x, y, direction = heapq.heappop(q)
            nx, ny = x + dxy[direction][0], y + dxy[direction][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or maze[nx][ny] == 1:
                if x == destination[0] and y == destination[1]:
                    return dist
                for d in range(4):
                    k = (x, y, d)
                    if k not in vis:
                        vis.add(k)
                        heapq.heappush(q, (dist, x, y, d))

            else:
                k = (nx, ny, direction)
                if k not in vis:
                    vis.add(k)
                    heapq.heappush(q, (dist+1, nx, ny, direction))

        return -1

s = Solution()
print(s.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]))