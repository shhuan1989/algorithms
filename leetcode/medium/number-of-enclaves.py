# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        
        N, M = len(A), len(A[0])
        
        edge = []
        for i in range(N):
            if A[i][0] == 1:
                edge.append((i, 0))
            if A[i][-1] == 1:
                edge.append((i, M-1))
        for c in range(M):
            if A[0][c] == 1:
                edge.append((0, c))
            if A[-1][c] == 1:
                edge.append((N-1, c))
        
        total = sum([sum(row) for row in A])
        sea = 0
        for r, c in edge:
            if A[r][c] == 1:
                q = [(r, c)]
                A[r][c] = -1
                count = 0
                while q:
                    x, y = q.pop()
                    count += 1
                    
                    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == 1:
                            A[nx][ny] = -1
                            q.append((nx, ny))
                sea += count

        return total - sea
    
    
s = Solution()
print(s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))