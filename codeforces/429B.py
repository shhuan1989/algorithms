# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/7 09:47

"""


def meet(N, M, A, R, C):

    dp = [[0 for _ in range(M)] for _ in range(N)]
    sa, sb = 0, 0
    for r in range(N):
        for c in range(M):
            dp[r][c] = max(dp[r-1][c] if r-1>=0 else 0, dp[r][c-1] if c-1 >= 0 else 0) + A[r][c]
            if r == R and c == C:
                sa += dp[r][c]
                break
    dp = [[0 for _ in range(M)] for _ in range(N)]
    for r in range(R, N):
        for c in range(C, M):
            dp[r][c] = max(dp[r-1][c] if r-1>=0 else 0, dp[r][c-1] if c-1 >= 0 else 0) + A[r][c]
    sa += dp[N-1][M-1]
    sa -= 2 * A[R][C]

    dpb = [[0 for _ in range(M)] for _ in range(N)]
    for r in range(N-1, -1, -1):
        for c in range(M):
            dpb[r][c] = max(dpb[r+1][c] if r+1 < N else 0, dpb[r][c-1] if c - 1 >= 0 else 0) + A[r][c]
            if r == R and c == C:
                sb += dpb[r][c]
                break

    dpb = [[0 for _ in range(M)] for _ in range(N)]
    for r in range(R, -1, -1):
        for c in range(C, M):
            dpb[r][c] = max(dpb[r + 1][c] if r + 1 < N else 0, dpb[r][c - 1] if c - 1 >= 0 else 0) + A[r][c]
    sb += dp[0][M-1]
    sb -= 2 * A[R][C]

    return sa + sb


def solve(N, M, A):
    ans = 0
    meet(N, M, A, 2, 2)
    for r in range(N):
        for c in range(M):
            m = meet(N, M, A, r, c)
            ans = max(ans, m)
    return ans


N, M = map(int, input().split())
A = []
for i in range(N):
    row = [int(x) for x in input().split()]
    A.append(row)

print(solve(N, M, A))