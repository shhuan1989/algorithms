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


if __name__ == '__main__':
    N = int(input())
    A = []
    diff = 0
    for _ in range(N):
        a, b = map(int, input().split())
        d = a - b
        diff += d
        A.append((a, b))
    
    INF = N * 10
    maxd = 10 * N
    mid = 5 * N
    dp = [[INF for _ in range(maxd + 1)] for _ in range(N+1)]
    dp[0][mid] = 0
    
    
    for i in range(1, N+1):
        d = A[i-1][0] - A[i-1][1]
        for pred in range(mid - 5 * i, mid + 5 * i + 1):
            nd = pred + d
            if 0 <= nd < maxd:
                dp[i][nd] = min(dp[i][nd], dp[i-1][pred])
            nd = pred - d
            if 0 <= nd < maxd:
                dp[i][nd] = min(dp[i][nd], dp[i-1][pred] + 1)
    
    for d in range(mid):
        if dp[N][mid + d] < INF:
            print(dp[N][mid + d])
            exit(0)
        if dp[N][mid - d] < INF:
            print(dp[N][mid - d])
            exit(0)
    
    
    
    
    