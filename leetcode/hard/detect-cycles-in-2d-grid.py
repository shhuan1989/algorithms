# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


sys.setrecursionlimit(2000)
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        id = [[0 for _ in range(m)] for _ in range(n)]
        vis = [[False for _ in range(m)] for _ in range(n)]
        
        def dfs(r, c, i):
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == grid[r][c]:
                    if vis[nr][nc] and 0 < id[nr][nc] < i-2:
                        return True
                    
                    if not vis[nr][nc]:
                        vis[nr][nc] = True
                        id[nr][nc] = i
                        if dfs(nr, nc, i+1):
                            id[nr][nc] = 0
                            return True
                        id[nr][nc] = 0
            return False
        
        for r in range(n):
            for c in range(m):
                if vis[r][c]:
                    continue
                if dfs(r, c, 1):
                    return True
                
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))
    print(s.containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))
    print(s.containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]]))
    print(s.containsCycle([
        ["d","b","b"],
        ["c","a","a"],
        ["b","a","c"],
        ["c","c","c"],
        ["d","d","a"]]))