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
created by shhuan at 2019/12/17 20:27

"""


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        if ball == hole:
            return ''

        vis = set()
        N, M = len(maze), len(maze[0])
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        OPS = ['u', 'd', 'l', 'r']
        q = []
        x, y = ball
        for d in range(4):
            dx, dy = dxy[d]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 0:
                q.append((1, OPS[d], nx, ny, d))
        for l, op, x, y, d in q:
            vis.add((x, y, d, op))
        heapq.heapify(q)
        while q:
            l, op, x, y, d = heapq.heappop(q)

            dx, dy = dxy[d]
            nx, ny = x + dx, y + dy

            if x == hole[0] and y == hole[1]:
                return op

            if nx < 0 or ny < 0 or nx >= N or ny >= M or maze[nx][ny] == 1:
                for nd in range(4):
                    if nd != d:
                        ns = (x, y, nd, op[0])
                        if ns not in vis:
                            vis.add(ns)
                            heapq.heappush(q, (l, op + OPS[nd], x, y, nd))
            else:
                ns = (nx, ny, d, op[0])
                if ns not in vis:
                    vis.add(ns)
                    heapq.heappush(q, (l+1, op, nx, ny, d))

        return 'impossible'

s = Solution()
print(s.findShortestWay([[0,1],[1,0]], [0,0], [1,1]))
print(s.findShortestWay([
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0]], [4, 3], [0, 1]))

print(s.findShortestWay([
                            [0,0,0,0,0,0,0],
                            [0,0,1,0,0,1,0],
                            [0,0,0,0,1,0,0],
                            [0,0,0,0,0,0,1]
                        ], [0,4], [3,0]))