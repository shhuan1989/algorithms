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
created by shhuan at 2020/7/16 21:49

"""


SIMILAR = [
    [5, -1, -2, -1, -3],
    [-1, 5, -3, -2, -4],
    [-2, -3, 5, -2, -2],
    [-1, -2, -2, 5, -1],
    [-3, -4, -2, -1, 0]
]

if __name__ == '__main__':
    N, A = input().split()
    M, B = input().split()

    VI = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3,
        ' ': 4
    }

    N, M = int(N), int(M)
    dp = [[float('-inf') for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0
    A = [VI[v] for v in A]
    B = [VI[v] for v in B]

    for i in range(1, N+1):
        dp[i][0] = dp[i-1][0] + SIMILAR[A[i-1]][4]
    for i in range(1, M+1):
        dp[0][i] = dp[0][i-1] + SIMILAR[B[i-1]][4]

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = max(dp[i-1][j] + SIMILAR[A[i-1]][4], dp[i][j-1] + SIMILAR[B[j-1]][4], dp[i-1][j-1] + SIMILAR[A[i-1]][B[j-1]])

    print(dp[N][M])

