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
created by shhuan at 2020/7/13 20:18

"""


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = []
    for i in range(N):
        h, w = map(int, input().split())
        A.append((h, w))

    A.sort()
    W = [w for h, w in A]
    K = N - K
    INF = 10**5
    dp = [[INF for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 0
    dp[0][1] = 0

    for i in range(1, N):
        dp[i][0] = 0
        dp[i][1] = 0
        for k in range(2, i+2):
            for pi in range(i):
                dp[i][k] = min(dp[i][k], dp[pi][k-1] + abs(W[i] - W[pi]))

    print(min([dp[i][K] for i in range(N)]))