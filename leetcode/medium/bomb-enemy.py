# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        N, M = len(grid), len(grid[0])
        updown = [[0 for _ in range(M)] for _ in range(N)]
        
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 'W':
                    updown[r][c] = 0
                else:
                    updown[r][c] += (updown[r-1][c] if r-1 >= 0 else 0) + (1 if grid[r][c] == 'E' else 0)
                    
        downup = [[0 for _ in range(M)] for _ in range(N)]
        for r in range(N-1, -1, -1):
            for c in range(M):
                if grid[r][c] == 'W':
                    downup[r][c] = 0
                else:
                    downup[r][c] += (downup[r+1][c] if r+1 < N else 0) + (1 if grid[r][c] == 'E' else 0)
        
        ans = 0
        for r in range(N):
            c = 0
            e = 0
            maxh = 0
            hasBlank = False
            while c < M:
                if grid[r][c] == 'W':
                    if hasBlank:
                        ans = max(ans, maxh + e)
                    maxh = 0
                    e = 0
                    hasBlank = False
                elif grid[r][c] == 'E':
                    e += 1
                else:
                    maxh = max(maxh, (updown[r - 1][c] if r - 1 >= 0 else 0) + (downup[r + 1][c] if r + 1 < N else 0))
                    hasBlank = True
                c += 1
            if hasBlank:
                ans = max(ans, maxh+e)
        return ans

    
s = Solution()
print(s.maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))
print(s.maxKilledEnemies([]))
print(s.maxKilledEnemies([['E']]))
print(s.maxKilledEnemies([['0', 'E']]))
print(s.maxKilledEnemies([["0"],["E"],["0"],["W"]]))
print(s.maxKilledEnemies([
    ["W","E","E","E","E","0"],
    ["E","E","E","E","E","W"]]))
