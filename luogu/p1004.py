# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

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
    A = [[0 for _ in range(N+2)] for _ in range(N+2)]
    while True:
        x, y, v = map(int, input().split())
        if x == 0 and y == 0 and v == 0:
            break
        A[x][y] = v

    dp = [[[[0 for _ in range(N+2)] for _ in range(N+2)] for _ in range(N+2)] for _ in range(N+2)]

    for x1 in range(1, N+1):
        for y1 in range(1, N+1):
            for x2 in range(1, N+1):
                y2 = x1+y1-x2
                if y2 <= 0 or y2 > N:
                    continue
                dp[x1][y1][x2][y2] = max(dp[x1-1][y1][x2-1][y2], dp[x1-1][y1][x2][y2-1], dp[x1][y1-1][x2-1][y2], dp[x1][y1-1][x2][y2-1])
                pb = A[x1][y1] if (x1 == x2 and y1 == y2) else (A[x1][y1] + A[x2][y2])
                dp[x1][y1][x2][y2] += pb
    
    print(str(dp[N][N][N][N]))