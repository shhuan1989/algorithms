# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        if len(mines) == N * N:
            return 0
        A = [[1 for _ in range(N)] for _ in range(N)]
        H = [[0 for _ in range(N)] for _ in range(N)]
        W = [[0 for _ in range(N)] for _ in range(N)]
        H2 = [[0 for _ in range(N)] for _ in range(N)]
        W2 = [[0 for _ in range(N)] for _ in range(N)]
        
        for r, c in mines:
            A[r][c] = 0
        
        for r in range(N):
            for c in range(N):
                H[r][c] = (H[r-1][c] if r-1 >= 0 else 0) + 1 if A[r][c] == 1 else 0
                
        for c in range(N):
            for r in range(N):
                W[r][c] = (W[r][c-1] if c-1 >= 0 else 0) + 1 if A[r][c] == 1 else 0
                
        for r in range(N-1, -1, -1):
            for c in range(N):
                H2[r][c] = (H2[r+1][c] if r+1 < N else 0) + 1 if A[r][c] == 1 else 0
        
        ans = 1
        for c in range(N-1, -1, -1):
            for r in range(N):
                W2[r][c] = (W2[r][c+1] if c+1 < N else 0) + 1 if A[r][c] == 1 else 0
                ans = max(ans, min([W[r][c], W2[r][c], H[r][c], H2[r][c]]))
                
        return ans
        
        
    
    
s = Solution()
print(s.orderOfLargestPlusSign(5, [[0,0],[0,1],[0,4],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[2,3],[2,4],[3,0],[4,0],[4,1],[4,3],[4,4]]))
# print(s.orderOfLargestPlusSign(3, [[0,2],[1,0],[2,0]]))
# print(s.orderOfLargestPlusSign(3, [[0, 0]]))
# print(s.orderOfLargestPlusSign(2, []))
# print(s.orderOfLargestPlusSign(5, [[4, 2]]))
# print(s.orderOfLargestPlusSign(1, [[0, 0]]))
# print(s.orderOfLargestPlusSign(2, [[0,1],[1,0],[1,1]]))

