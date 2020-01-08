# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/6/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve(N, W, H, A):
    A = [(w, h, i) for i, (w, h) in enumerate(A) if w > W and h > H]
    A.sort()
    N = len(A)
    if N <= 0:
        return 0, []
    
    dp = [1 for _ in range(N)]
    pre = [-1 for _ in range(N)]
    dp[0] = 1
    
    maxsize, maxi = 1, 0
    for i in range(1, N):
        for j in range(i):
            if A[j][0] < A[i][0] and A[j][1] < A[i][1]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre[i] = j
        if dp[i] > maxsize:
            maxsize = dp[i]
            maxi = i
            
    path = []
    i = maxi
    while i >= 0:
        path.append(A[i][2] + 1)
        i = pre[i]
        
    return maxsize, path[::-1]


N, W, H = map(int, input().split())
A = []
for i in range(N):
    w, h = map(int, input().split())
    A.append((w, h))

c, p = solve(N, W, H, A)
print(c)
if c > 0:
    print(' '.join(map(str, p)))
    