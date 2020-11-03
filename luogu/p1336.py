# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, M = map(int, input().split())
    A, B = [], []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    dp = [[float('inf') for _ in range(N+1)] for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(1, M+1):
        for j in range(N+1):
            for k in range(j+1):
                dp[i][j] = min(dp[i][j], dp[i-1][j-k] + A[i-1] * k ** B[i-1])
    
    print(dp[M][N])