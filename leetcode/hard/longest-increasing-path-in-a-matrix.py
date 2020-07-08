# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        
        g, d = [[[] for _ in range(m)] for _ in range(n)], [[0 for _ in range(m)] for _ in range(n)]
        
        def check(r, c):
            return not (r < 0 or r >= n or c < 0 or c >= m)
        
        for r in range(n):
            for c in range(m):
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if check(nr, nc) and matrix[nr][nc] > matrix[r][c]:
                        g[r][c].append((nr, nc))
                        d[nr][nc] += 1
        
        memo = [[0 for _ in range(m)] for _ in range(n)]
        
        def dfs(r, c):
            if not check(r, c):
                return 0
            if memo[r][c] > 0:
                return memo[r][c]
            memo[r][c] = 1 + max([dfs(nr, nc) for nr, nc in g[r][c]] or [0])
            return memo[r][c]
        
        ans = 0
        for r in range(n):
            for c in range(m):
                if d[r][c] == 0:
                    ans = max(ans, dfs(r, c))
        
        return ans
    
    
    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        
        def check(r, c):
            return not (r < 0 or r >= n or c < 0 or c >= m)
        
        @lru_cache(maxsize=None)
        def dfs(r, c, pv):
            if not check(r, c) or matrix[r][c] <= pv:
                return 0
            
            return 1 + max([dfs(nr, nc, matrix[r][c]) for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]])
            
        ans = 0
        for r in range(n):
            for c in range(m):
                ans = max(ans, dfs(r, c, float('-inf')))
                
        return ans
    
    
s = Solution()
print(s.longestIncreasingPath(
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
))
print(s.longestIncreasingPath(
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
))
