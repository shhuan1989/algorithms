# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/23 13:22

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List



if __name__ == '__main__':
    A = input().strip()
    B = input().strip()
    K = int(input())

    N, M = len(A), len(B)
    dp = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(1, N+1):
        dp[i][0] = i * K
    for i in range(1, M+1):
        dp[0][i] = i * K

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = min(dp[i-1][j] + K, dp[i][j-1] + K, dp[i-1][j-1]+abs(ord(A[i-1])-ord(B[j-1])))

    # for row in dp:




    #     print(row)
    print(dp[N][M])
