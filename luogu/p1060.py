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
created by shhuan at 2020/7/10 19:02

"""


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        v, p = map(int, input().split())
        A.append((v, p))

    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

    for i in range(1, M+1):
        w, p = A[i-1]
        for v in range(N+1):
            dp[i][v] = max(dp[i][v], dp[i-1][v])
            if v >= w:
                dp[i][v] = max(dp[i][v], dp[i-1][v-w] + w * p)
    print(dp[M][N])