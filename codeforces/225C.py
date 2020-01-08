# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/7/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve(N, M, X, Y, A):
    Y = min(Y, M)
    whites = []
    for c in range(M):
        w = sum([1 if A[r][c] == '.' else 0 for r in range(N)])
        whites.append(w)
    black = [N-v for v in whites]
    
    dp = [[[N*M for _ in range(2)] for _ in range(Y+1)] for _ in range(M)]
    dp[0][1][0] = black[0]
    dp[0][1][1] = whites[0]
    for c in range(1, M):
        dp[c][1][0] = min([dp[c - 1][y][1] + black[c] for y in range(X, Y + 1)])
        dp[c][1][1] = min([dp[c - 1][y][0] + whites[c] for y in range(X, Y + 1)])
        for y in range(2, Y+1):
            dp[c][y][0] = dp[c-1][y-1][0] + black[c]
            dp[c][y][1] = dp[c-1][y-1][1] + whites[c]
        
    ans = N*M
    for y in range(X, Y+1):
        ans = min(ans, min(dp[M-1][y]))
    return ans


N, M, X, Y = map(int, input().split())
A = []
for i in range(N):
    A.append(input())

print(solve(N, M, X, Y, A))