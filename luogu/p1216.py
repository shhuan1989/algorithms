# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/27

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
    for i in range(N):
        row = [int(x) for x in input().strip().split()]
        A.append(row)
    
    dp = [[0 for _ in range(N+1)] for _ in range(N)]
    dp[0][0] = A[0][0]
    for r in range(1, N):
        for c in range(r+1):
            dp[r][c] = max(dp[r-1][c-1] if c-1 >= 0 else 0, dp[r-1][c]) + A[r][c]
    # for row in dp:
    #     print(row)
    print(max(dp[N-1]))