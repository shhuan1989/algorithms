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
created by shhuan at 2019/12/11 23:22

"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1

        N, M = len(grid), len(grid[0])
        if grid[N-1][M-1] == 1:
            return -1
        if N == M == 1:
            return 1

        MAXD = 10000
        a, b = [[MAXD for _ in range(M)] for _ in range(N)], [[MAXD for _ in range(M)] for _ in range(N)]
        q, p = [(1, 0, 0)], [(1, N-1, M-1)]
        a[0][0] = 1
        b[N-1][M-1] = 1

        def neighbors(r, c):
            return [(nr, nc) for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1), (r-1, c-1), (r+1, c-1), (r-1, c+1), (r+1, c+1)] if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0]


        while p or q:
            nq, np = [], []
            for d, r, c in q:
                a[r][c] = d
                if b[r][c] < MAXD:
                    return a[r][c] + b[r][c] - 1
                for nr, nc in neighbors(r, c):
                    if a[nr][nc] > d + 1:
                        a[nr][nc] = d + 1
                        nq.append((d+1, nr, nc))
            for d, r, c in p:
                b[r][c] = d
                if a[r][c] < MAXD:
                    return a[r][c] + b[r][c] - 1
                for nr, nc in neighbors(r, c):
                    if b[nr][nc] > d + 1:
                        b[nr][nc] = d + 1
                        np.append((d + 1, nr, nc))
            p, q = np, nq

        return -1

    def shortestPathBinaryMatrix_dijkstra(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1

        N, M = len(grid), len(grid[0])
        dist = [[float('inf') for _ in range(M)] for _ in range(N)]
        dist[0][0] = 0
        q = [(1, r, c) for r, c in [(0, 1), (1, 0), (1, 1)] if r < N and c < M and grid[r][c] == 0]
        heapq.heapify(q)
        while q:
            d, r, c = heapq.heappop(q)
            dist[r][c] = min(dist[r][c], d)
            nd = d + 1
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1), (r-1, c-1), (r+1, c-1), (r-1, c+1), (r+1, c+1)]:
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        heapq.heappush(q, (nd, nr, nc))

        return (1 + dist[N-1][M-1]) if dist[N-1][M-1] < float('inf') else -1


s = Solution()
print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(s.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
print(s.shortestPathBinaryMatrix([[0]]))
print(s.shortestPathBinaryMatrix([[0, 0]]))
print(s.shortestPathBinaryMatrix([[0], [0]]))