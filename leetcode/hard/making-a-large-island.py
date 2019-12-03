    # -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/28/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        area = {0: 0}
        id = 2
        N, M = len(grid), len(grid[0])
        
        zeros = []
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    id += 1
                    grid[r][c] = id
                    q = [(r, c)]
                    s = 0
                    while q:
                        s += 1
                        x, y = q.pop()
                        for nr, nc in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1:
                                grid[nr][nc] = id
                                q.append((nr, nc))
                    area[id] = s
                elif grid[r][c] == 0:
                    zeros.append((r, c))
                    
        ans = max([(1 + sum([area[b] for b in
                             {grid[nr][nc] for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)] if
                              0 <= nr < N and 0 <= nc < M}
                             ] or [0])) for r, c in zeros] or [0])
        ans = max(ans, max(area.values() or [0]))
        return ans
    
    
s = Solution()
print(s.largestIsland([[1, 0], [0, 1]]))
print(s.largestIsland([[1, 1], [1, 0]]))
print(s.largestIsland( [[1, 1], [1, 1]]))
