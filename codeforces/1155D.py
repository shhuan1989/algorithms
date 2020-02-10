# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/7/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve(N, X, A):
    dp = [[[float('-inf') for _ in range(3)] for _ in range(3)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N+1):
        for j in range(3):
            for k in range(3):
                if k < 2:
                    dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k])
                if j < 2:
                    dp[i][j+1][k] = max(dp[i][j+1][k], dp[i][j][k])
                if i < N:
                    dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k] + (A[i] if j == 1 else 0) * (X if k == 1 else 1))
    return dp[N][2][2]
    

N, X = map(int, input().split())
A = [int(x) for x in input().split()]
print(solve(N, X, A))