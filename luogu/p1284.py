# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/31

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

import math

if __name__ == '__main__':
    # sys.stdin = open('p1284.in', 'r')
    N = int(input())
    A = []
    for i in range(N):
        x = int(input())
        A.append(x)
        
    def check(a, b, c):
        return a + b > c and a + c > b and b + c > a
    
    def area(a, b, c):
        if not check(a, b, c):
            return -1
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        # print(a, b, c, s)
        return int(s * 100)
    
    M = sum(A) // 2 + 1
    dp = [[False for _ in range(M)] for _ in range(M)]
    
    dp[0][0] = True
    for v in A:
        ndp = [[False for _ in range(M)] for _ in range(M)]
        for i in range(M):
            for j in range(M):
                ndp[i][j] = dp[i][j] or (i-v >= 0 and dp[i-v][j]) or (j-v >= 0 and dp[i][j-v])
        
        dp = ndp
    
    L = sum(A)
    ans = -1
    for i in range(M):
        for j in range(M):
            if dp[i][j]:
                ans = max(ans, area(i, j, L-i-j))
    
    print(ans)
    
    