# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def base(N, A):
    dp = [[0 for _ in range(300)] for _ in range(300)]
    ans = 0
    for i in range(2, 2 * N):
        j = i - 1
        while i-j < N and j >= 1:
            for k in range(j, i):
                dp[j][i] = max(dp[j][i], dp[j][k] + dp[k+1][i] + A[j] * A[k+1] * A[i+1])
                ans = max(ans, dp[j][i])
            j -= 1
    return ans


def solve(N, A):
    dp = [[0 for _ in range(300)] for _ in range(300)]
    ans = 0
    
    for l in range(1, N):
        for i in range(1, 2 * N):
            j = i + l
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j] + A[i] * A[k + 1] * A[j + 1])
                ans = max(ans, dp[i][j])
                
    return ans


if __name__ == '__main__':
    N = int(input())
    A = [0 for _ in range(300)]
    B = [int(x) for x in input().split()]
    for i in range(1, N + 1):
        v = B[i - 1]
        A[i] = v
        A[i + N] = v
        
    # print(base(N, A))
    print(solve(N, A))
        
    