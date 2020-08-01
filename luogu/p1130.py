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
created by shhuan at 2020/7/17 23:43

"""



if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        row = [int(x) for x in input().split()]
        A.append(row)

    INF = 10**9+7
    dp = [[INF for _ in range(M)] for _ in range(N+1)]
    for j in range(M):
        dp[0][j] = 0

    for i in range(1, N+1):
        for j in range(M):
            dp[i][j] = min(dp[i-1][j], dp[i-1][(j+M-1)%M]) + A[j][i-1]

    # for row in dp:
    #     print(row)

    print(min(dp[N]))