# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/31

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


import itertools
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def getgroups(a):
            groups = [[0 for _ in range(m)] for _ in range(n)]
            gid = 1
            for r in range(n):
                for c in range(m):
                    if a[r][c] == 1 and groups[r][c] == 0:
                        gid += 1
                        groups[r][c] = gid
                        q = [(r, c)]
                        while q:
                            x, y = q.pop()
                            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                                if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1 and groups[nx][ny] == 0:
                                    groups[nx][ny] = 1
                                    q.append((nx, ny))
            
            return gid > 2 or gid == 1
        
        
        if getgroups(grid):
            return 0
          
        s = sum([sum(row) for row in grid])
        if s <= 1:
            return s
        
        rows = []
        for r in range(n):
            if sum(grid[r]) > 0:
                rows.append(r)
        ans = max(m, n)
        for i in range(1, len(rows)-1):
            ans = min(ans, sum(grid[rows[i]]))
        
        cols = []
        for c in range(m):
            if sum([grid[r][c] for r in range(n)]) > 0:
                cols.append(c)
        for i in range(1, len(cols) - 1):
            ans = min(ans, sum([grid[r][cols[i]] for r in range(n)]))
            
        if len(rows) <= 2 and len(cols) <= 2:
            ans = 2
            
        
        
        def toid(r, c):
            return r * m + c
        
        def torc(id):
            return id // m, id % m
        
        
        islands = []
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    islands.append(toid(r, c))
        
        
        def newgrid(pos):
            a = [[0 for _ in range(m)] for _ in range(n)]
            for r in range(n):
                for c in range(m):
                    a[r][c] = grid[r][c]
            for id in pos:
                r, c = torc(id)
                a[r][c] = 0
            return a
        
        def check(count):
            for pos in itertools.combinations(islands, count):
                a = newgrid(pos)
                if getgroups(a):
                    return True
            return False
        
        lo, hi = 1, ans
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
                
        return lo
                
        
        
if __name__ == '__main__':
    s = Solution()
    print(s.minDays([[0,0,0,0],[0,1,1,0],[0,0,0,0]]))
    # print(s.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]))
    # print(s.minDays([[1,1]]))
    # print(s.minDays([[1, 0, 1, 0]]))
    # print(s.minDays([
    #     [1,1,0,1,1],
    #      [1,1,1,1,1],
    #      [1,1,0,1,1],
    #      [1,1,0,1,1]]))
    # print(s.minDays([
    #     [1,1,0,1,1],
    #      [1,1,1,1,1],
    #      [1,1,0,1,1],
    #      [1,1,1,1,1]]))
    # print(s.minDays([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))