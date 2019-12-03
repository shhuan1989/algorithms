# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/10 10:53

"""

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        mark = [[0 for _ in range(M)] for _ in range(N)]
        iid = 1
        ans = 0

        for r in range(N):
            for c in range(M):
                if mark[r][c] == 0 and grid[r][c] == 0:
                    area = []
                    q = [(r, c)]
                    mark[r][c] = iid

                    while q:
                        x, y = q.pop()
                        area.append((x, y))
                        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                            if 0 <= nx < N and 0 <= ny < M and mark[nx][ny] == 0 and grid[nx][ny] == 0:
                                mark[nx][ny] = iid
                                q.append((nx, ny))

                    isolated = True
                    for x, y in area:
                        if any([nx < 0 or nx >= N or ny < 0 or ny >=M for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]]):
                            isolated = False
                            break
                    if isolated:
                        ans += 1

                    iid += 1
        # for row in mark:
        #     print(row)
        return ans


s = Solution()
print(s.closedIsland(grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
print(s.closedIsland(grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))


