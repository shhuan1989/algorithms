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
created by shhuan at 2020/1/6 22:24

"""


def ones(val):
    count = 0
    while val > 0:
        count += 1 if val & 1 > 0 else 0
        val >>= 1
    return count


def solve(N, M, A, G):
    dp = [[0 for _ in range(N)] for _ in range(1 << N)]

    b = [0 for _ in range(N+1)]
    b[0] = 1
    for i in range(1, N+1):
        b[i] = 2 * b[i-1]

    for i in range(N):
        dp[b[i]][i] = A[i]
    for s in range(1 << N):
        for k in range(N):
            if s & b[k] > 0:
                for w in range(N):
                    if w != k and s & b[w] > 0:
                        dp[s][k] = max(dp[s][k], dp[s ^ b[k]][w] + G[w][k] + A[k])

    ans = max([max(dp[v]) for v in range(b[N]) if ones(v) == M])

    return ans


N, M, K = map(int, input().split())
A = [int(x) for x in input().split()]
G = [[0 for _ in range(N)] for _ in range(N)]
for i in range(K):
    u, v, w = map(int, input().split())
    G[u-1][v-1] = w

print(solve(N, M, A, G))