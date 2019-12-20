# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/17/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def cheapestJump(self, A: List[int], B: int) -> List[int]:
        
        N = len(A)
        INF = float('inf')
        A = [0] + A
        dp = [INF for _ in range(N+1)]
        path = [[] for _ in range(N+1)]
        dp[1] = A[1]
        path[1] = [1]
        for i in range(1, N+1):
            if A[i] < 0:
                continue
                
            for b in range(1, min(B, N-i)+1):
                j = i+b
                if A[j] >= 0:
                    cost = dp[i] + A[j]
                    if cost <= dp[j]:
                        newpath = path[i] + [j]
                        if cost < dp[j] or not path[j] or path[j] > newpath:
                            path[j] = newpath
                        dp[i + b] = cost
                            
        if dp[N] < INF:
            return path[N]
        
        return []
    
s = Solution()
print(s.cheapestJump([84,31,75,96,48,91,1,4,17,69,97,71,75,92,20,4,66,39,66,71,30,21,45,72,91,70,22,14,47,76,77,92,95,55,47,39,14,22,54,9,12,58,5,1,45,63,40,-1,28,17,52,31,80,41,51,24,97,50,55,50,35,52,97,-1,36,73,9,72,94,36,39,40,23,78,84], 49))
# print(s.cheapestJump([0,-1,0,0,0,0], 3))
# print(s.cheapestJump([1, 0, 1], 2))
# print(s.cheapestJump([1, 2, 4, -1, 2], 2))
# print(s.cheapestJump([1,2,4,-1,2], 1))
# print(s.cheapestJump([0,0,0,0,0,0], 3))