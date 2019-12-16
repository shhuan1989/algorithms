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
created by shhuan at 2019/12/12 23:58

"""

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        islands = []
        N, M = len(grid), len(grid[0])
        id = 2
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    id += 1
                    grid[r][c] = id
                    area = 0
                    q = [(r, c)]
                    vis = {(r, c)}
                    while q:
                        area += 1
                        x, y = q.pop()
                        vis.add((x, y))
                        for nr, nc in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1:
                                grid[nr][nc] = id
                                q.append((nr, nc))

                    a, b = max([x for x, y in vis]), min([x for x, y in vis])
                    c, d = max([y for x, y in vis]), min([y for x, y in vis])
                    w, h = a-b+1, c-d+1
                    land = [[0 for _ in range(h)] for _ in range(w)]
                    for x, y in vis:
                        land[x-b][y-d] = 1
                    islands.append(land)


        def rot(island):
            s = []
            n, m = len(island), len(island[0])
            for c in range(m-1, -1, -1):
                col = [row[c] for row in island]
                s.append(col)
            return s

        def rot2(island):
            return rot(rot(island))

        def rot3(island):
            return rot(rot2(island))

        def updown(island):
            n, m = len(island), len(island[0])
            s = [[0 for _ in range(m)] for _ in range(n)]
            for r in range(n):
                for c in range(m):
                    s[r][c] = island[n-r-1][c]
            return s

        def leftright(island):
            n, m = len(island), len(island[0])
            s = [[0 for _ in range(m)] for _ in range(n)]
            for c in range(m):
                for r in range(n):
                    s[r][c] = island[r][m-c-1]
            return s


        def stringifyIsland(island):
            s = []
            for row in island:
                s.append(''.join(map(str, row)))

            return '_'.join(s)

        reps = set()
        for island in islands:
            si = stringifyIsland(island)
            states = {si}
            q = [island]
            while q:
                land = q.pop()
                for newland in [updown(land), rot(land), rot2(island), rot3(island), leftright(land)]:
                    nsi = stringifyIsland(newland)
                    if nsi not in states:
                        states.add(nsi)
                        q.append(newland)
            reps.add(min(states))

        return len(reps)

s = Solution()
print(s.numDistinctIslands2([[1, 1, 0, 0, 0],
                             [1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1],
                             [0, 0, 0, 1, 1]]))
print(s.numDistinctIslands2([[1, 1, 1, 0, 0],
                             [1, 0, 0, 0, 1],
                             [0, 1, 0, 0, 1],
                             [0, 1, 1, 1, 0]]))


