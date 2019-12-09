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
created by shhuan at 2019/12/7 18:37

"""


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        vis = set()

        q = [(0, 0, 0, 1, 0)]
        step = 0
        while q:
            nq = []
            for a, b, c, d, e in q:
                if a == N-1 and b == M-2 and c == N-1 and d == M-1:
                    return step
                ns = []
                if e == 0:
                    # horizontal
                    # right
                    if d + 1 < M and grid[c][d+1] == 0:
                        ns.append((c, d, c, d+1, e))
                    if a + 1 < N and grid[a+1][b] == 0 and grid[c+1][d] == 0:
                        # down
                        ns.append((a+1, b, c+1, d, e))
                        # clockwise rotate
                        ns.append((a, b, c+1, d-1, 1))
                elif e == 1:
                    # vertical
                    if b + 1 < M and grid[a][b+1] == 0 and grid[c][d+1] == 0:
                        # right
                        ns.append((a, b+1, c, d+1, e))
                        # anti-clockwise rotate
                        ns.append((a, b, a, d+1, 0))
                    # down
                    if c + 1 < N and grid[c+1][d] == 0:
                        ns.append((a+1, b, c+1, d, e))

                for s in ns:
                    if s not in vis:
                        vis.add(s)
                        nq.append(s)
            q = nq
            step += 1

        return -1


s = Solution()
print(s.minimumMoves( [
    [0,0,0,0,0,1],
    [1,1,0,0,1,0],
    [0,0,0,0,1,1],
    [0,0,1,0,1,0],
    [0,1,1,0,0,0],
    [0,1,1,0,0,0]
]))