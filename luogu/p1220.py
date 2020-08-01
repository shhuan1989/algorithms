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
created by shhuan at 2020/7/27 19:21

"""


if __name__ == '__main__':
    N, C = map(int, input().split())

    A = []
    for i in range(N):
        x, p = map(int, input().split())
        A.append((x, p))

    presum = [0]
    for x, p in A:
        presum.append(presum[-1] + p)

    C -= 1
    dp = [[[float('inf') for _ in range(2)] for _ in range(N)] for _ in range(N)]
    dp[C][C][0] = 0
    dp[C][C][1] = 0
    for l in range(2, N+1):
        for i in range(N-l+1):
            j = i + l - 1
            d = presum[i] + presum[N] - presum[j+1]
            # print(i, j, d)
            dp[i][j][0] = min(dp[i+1][j][0] + (A[i+1][0]-A[i][0]) * (d + A[i][1]), dp[i+1][j][1] + (A[j][0]-A[i][0]) * (d + A[i][1]))
            dp[i][j][1] = min(dp[i][j-1][1] + (A[j][0] - A[j-1][0]) * (d + A[j][1]), dp[i][j-1][0] + (A[j][0] - A[i][0]) * (d + A[j][1]))

    print(min(dp[0][N-1]))