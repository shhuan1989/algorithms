# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/9/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        N, M = len(board), len(board[0])
        ans = 0
        for r in range(N):
            for c in range(M):
                if board[r][c] == 'R':
                    # up
                    for nr in range(r-1, -1, -1):
                        if board[nr][c] == 'p':
                            ans += 1
                            break
                        elif board[nr][c] != '.':
                            break
                    
                    # down
                    for nr in range(r+1, N):
                        if board[nr][c] == 'p':
                            ans += 1
                            break
                        elif board[nr][c] != '.':
                            break
                    
                    # left
                    for nc in range(c-1, -1, -1):
                        if board[r][nc] == 'p':
                            ans += 1
                            break
                        elif board[r][nc] != '.':
                            break
                            
                    # right
                    for nc in range(c+1, M):
                        if board[r][nc] == 'p':
                            ans += 1
                            break
                        elif board[r][nc] != '.':
                            break
                    break
        
        return ans
    
    
s = Solution()
# print(s.numRookCaptures([
#     [".",".",".",".",".",".",".","."],
#     [".",".",".","p",".",".",".","."],
#     [".",".",".","R",".",".",".","p"],
#     [".",".",".",".",".",".",".","."],
#     [".",".",".",".",".",".",".","."],
#     [".",".",".","p",".",".",".","."],
#     [".",".",".",".",".",".",".","."],
#     [".",".",".",".",".",".",".","."]]))

print(s.numRookCaptures([[".",".",".",".",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         ["p","p",".","R",".","p","B","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".","B",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".",".",".",".",".","."]
                         ]))