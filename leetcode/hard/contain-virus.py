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
created by shhuan at 2019/12/16 12:42

"""


class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:

        closed = set()
        infects = collections.defaultdict(int)
        barries = collections.defaultdict(list)
        id = 1
        N, M = len(grid), len(grid[0])
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    id += 1
                    grid[r][c] = id
                    q = [(r, c)]
                    inf = set()
                    bar = 0
                    while q:
                        x, y = q.pop()
                        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                            if 0 <= nx < N and 0 <= ny < M:
                                if grid[nx][ny] == 1:
                                    grid[nx][ny] = id
                                    q.append((nx, ny))
                                elif grid[nx][ny] == 0:
                                    inf.add((nx, ny))
                                    bar += 1
                    infects[id] = len(inf)
                    barries[id] = bar

        ans = 0
        while True:
            infects = {k: v for k, v in infects.items() if k not in closed}
            if not infects:
                break

            maxinfect = [k for k, v in infects.items() if v == max(infects.values())][0]
            ans += barries[maxinfect]
            for r in range(N):
                done = False
                for c in range(M):
                    if grid[r][c] == maxinfect:
                        closed.add(grid[r][c])
                        checked = set()
                        for x in range(N):
                            for y in range(M):
                                if grid[x][y] > 1 and grid[x][y] not in closed and grid[x][y] not in checked:
                                    checked.add(grid[x][y])
                                    # start infecting
                                    cid = grid[x][y]
                                    q = [(x, y)]
                                    vis = {(x, y)}
                                    neighbors = []
                                    while q:
                                        u, v = q.pop()
                                        for nu, nv in [(u + 1, v), (u - 1, v), (u, v + 1), (u, v - 1)]:
                                            if 0 <= nu < N and 0 <= nv < M:
                                                if grid[nu][nv] == 0 and (nu, nv) not in vis:
                                                    vis.add((nu, nv))
                                                    neighbors.append((nu, nv))
                                                elif grid[nu][nv] == cid and (nu, nv) not in vis:
                                                    vis.add((nu, nv))
                                                    q.append((nu, nv))
                                    for u, v in neighbors:
                                        grid[u][v] = cid

                                    ninf = set()
                                    bar = 0
                                    for u, v in neighbors:
                                        for nu, nv in [(u + 1, v), (u - 1, v), (u, v + 1), (u, v - 1)]:
                                            if 0 <= nu < N and 0 <= nv < M and grid[nu][nv] == 0:
                                                ninf.add((nu, nv))
                                                bar += 1
                                    infects[cid] = len(ninf)
                                    barries[cid] = bar
                        done = True
                        break
                if done:
                    break
        return ans

s = Solution()
print(s.containVirus(grid =
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]))