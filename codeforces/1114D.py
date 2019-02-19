# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/13/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

N = int(input())
C = [int(x) for x in input().split()]

# import random
# N = 5000
# C = [random.randint(1, 2000) for _ in range(N)]


A = []
for c in C:
    if not A or A[-1] != c:
        A.append(c)


colors = list(set(C))
colors.sort()
cmap = {c: i+1 for i, c in enumerate(colors)}
A = [cmap[a] for a in A]

N = len(A)
C = len(colors)
dp = [[[float('inf') for _ in range(2)] for _ in range(N+1)] for _ in range(N+1)]

# print(A)

for i in range(N):
    dp[i][i][0] = 0
    dp[i][i][1] = 0
    
for r in range(N):
    for l in range(r, -1, -1):
        for i in range(2):
            c = A[l] if i == 0 else A[r]
            if l:
                dp[l-1][r][0] = min(dp[l-1][r][0], dp[l][r][i] + (1 if c != A[l-1] else 0))
            if r+1 < N:
                dp[l][r+1][1] = min(dp[l][r+1][1], dp[l][r][i] + (1 if c != A[r+1] else 0))
        
print(min(dp[0][N-1]))


