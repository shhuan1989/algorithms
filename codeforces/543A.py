# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/7/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A, M, bugs, MOD):
    dp = [[[0 for _ in range(bugs + 1)] for _ in range(M + 1)] for _ in range(2)]
    for j in range(1, M + 1):
        if A[0] * j <= bugs:
            dp[1][j][A[0] * j] = 1
    dp[1][0][0] = 1
    dp[0][0][0] = 1
    for i in range(2, N + 1):
        for j in range(1, M + 1):
            for b in range(bugs + 1):
                s = dp[i % 2][j - 1][b - A[i - 1]] if b >= A[i - 1] else 0
                s += dp[(i + 1) % 2][j][b]
                s %= MOD
                dp[i % 2][j][b] = s

    return sum(dp[N % 2][M]) % MOD


N, M, B, MOD = map(int, input().split())
A = [int(x) for x in input().split()]
print(solve(N, A, M, B, MOD))