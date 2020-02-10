# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        
        N, M = len(seats), len(seats[0])
        S = 1 << M
        dp = [[0 for _ in range(S)] for _ in range(N+1)]
        
        def checkrow(s):
            for i in range(1, M):
                j = i -1
                if 0 <= j < M and (s & (1 << i)) > 0 and (s & (1 << j)) > 0:
                    return False
            return True
        
        def checkpre(s, ps):
            for i in range(M):
                if s & (1 << i):
                    for j in [i-1, i+1]:
                        if 0 <= j < M and (ps & (1 << j)) > 0:
                            return False
            return True
        
        def checkseat(s, r):
            for i in range(M):
                if s & (1 << i) > 0 and seats[r][i] != '.':
                    return False
            return True
        
        def count(s):
            return len([i for i in range(M) if (s & (1 << i)) > 0])
            
        
        row = [s for s in range(S) if checkrow(s)]
        for i in range(1, N+1):
            for s in row:
                if not checkseat(s, i-1):
                    continue
                for ps in range(S):
                    if checkpre(s, ps):
                        dp[i][s] = max(dp[i][s], dp[i-1][ps] + count(s))
        
        return max(dp[N])
        
        
        
        


s = Solution()
print(s.maxStudents([["#",".","#","#",".","#"],
                     [".","#","#","#","#","."],
                     ["#",".","#","#",".","#"]]))
print(s.maxStudents([[".","#"],
                     ["#","#"],
                     ["#","."],
                     ["#","#"],
                     [".","#"]]))
print(s.maxStudents([["#",".",".",".","#"],
                     [".","#",".","#","."],
                     [".",".","#",".","."],
                     [".","#",".","#","."],
                     ["#",".",".",".","#"]]))
print(s.maxStudents([[".",".",".",".","#",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".","#","."],[".",".",".",".",".",".",".","."],[".",".","#",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","#",".",".","#","."]]))