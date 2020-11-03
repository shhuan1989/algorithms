# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/17

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[float('-inf') for _ in range(m)] for _ in range(m)]
        dp[0][-1] = grid[0][0] + grid[0][-1]
        for r in range(1, n):
            ndp = [[0 for _ in range(m)] for _ in range(m)]
            for x in range(min(r + 1, m)):
                for y in range(max(0, m - r - 1), m):
                    for nx in [x - 1, x, x + 1]:
                        for ny in [y - 1, y, y + 1]:
                            if 0 <= nx < m and 0 <= ny < m:
                                add = grid[r][nx] + grid[r][ny] if nx != ny else grid[r][nx]
                                ndp[nx][ny] = max(ndp[nx][ny], add + dp[x][y])
            
            dp = ndp
        
        return max(max(row) for row in dp)
    
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.cherryPickup([
        [0,8,7,10,9,10,0,9,6],
        [8,7,10,8,7,4,9,6,10],
        [8,1,1,5,1,5,5,1,2],
        [9,4,10,8,8,1,9,5,0],
        [4,3,6,10,9,2,4,8,10],
        [7,3,2,8,3,3,5,9,8],
        [1,2,6,5,6,2,0,10,0]]))