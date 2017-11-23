# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/23 10:11

"""


N = int(input())
A = [int(x) for x in input().split()]

M = int(input())
B = [int(x) for x in input().split()]


A.sort()
B.sort()


dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        if abs(B[i-1] - A[j-1]) <= 1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

print(dp[M][N])

