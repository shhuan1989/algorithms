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
created by shhuan at 2020/7/20 20:18

"""

if __name__ == '__main__':

    N, M = map(int, input().split())
    A = []
    while len(A) < N:
        A += [int(x) for x in input().strip().split()]

    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(M+1):
            dp[i][j] += dp[i-1][j] + (dp[i-1][j-A[i-1]] if j >= A[i-1] else 0)

    print(dp[N][M])