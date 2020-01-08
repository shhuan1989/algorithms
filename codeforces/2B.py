# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/3/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import math


def check(val, div, pow):
    return val % (div ** pow) == 0


def count(val, div):
    if val % div == 0:
        lo, hi = 1, 0 if val <= 0 else int(math.log(val, div) + 1)
        while lo <= hi:
            m = (lo + hi) // 2
            if check(val, div, m):
                lo = m + 1
            else:
                hi = m - 1
        
        return hi
    
    return 0


def solved(A, N, div):
    dp = [[float('inf') for _ in range(N)] for _ in range(N)]
    pre = [['' for _ in range(N)] for _ in range(N)]
    dp[0][0] = count(A[0][0], div)
    for r in range(N):
        for c in range(N):
            dc = count(A[r][c], div)
            if r > 0 and dp[r-1][c] + dc < dp[r][c]:
                dp[r][c] = dp[r-1][c] + dc
                pre[r][c] = 'U'
            if c > 0 and dp[r][c-1] + dc < dp[r][c]:
                pre[r][c] = 'L'
                dp[r][c] = dp[r][c-1] + dc
    
    path = []
    r, c = N-1, N-1
    while r >= 0 and c >= 0:
        if pre[r][c] == 'U':
            path.append('D')
            r, c = r-1, c
        else:
            path.append('R')
            r, c = r, c-1
    
    return dp[N-1][N-1], ''.join(path[::-1][1:])


def haszero():
    for r in range(N):
        for c in range(N):
            if A[r][c] == 0:
                return True, r, c
    return False, -1, -1

def solve(A, N):
    aa, b = solved(A, N, 2)
    ac, d = solved(A, N, 5)
    
    h, r, c = haszero()
    if h and min(aa, ac) > 1:
        print(1)
        path = []
        for i in range(r):
            path.append('D')
        for i in range(c):
            path.append('R')
        for i in range(r, N-1):
            path.append('D')
        for i in range(c, N-1):
            path.append('R')
        print(''.join(path))
        
    elif aa < ac:
        print(aa)
        print(b)
    else:
        print(ac)
        print(d)


N = int(input())
A = []
for i in range(N):
    row = [int(x) for x in input().split()]
    A.append(row)
solve(A, N)
    
# import random
# while True:
#     N = 1000
#     A = []
#     for i in range(N):
#         row = [random.randint(0, 10 ** 9) for _ in range(N)]
#         A.append(row)
#     solve(A, N)
    
    