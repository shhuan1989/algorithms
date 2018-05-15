# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 3/8/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


# M, N, K = map(int, input().split())


M, N, K = 500, 500, 50


# A = []
# for i in range(M):
#     A.append(input())

A = [''.join(['1' if random.randint(0, 10) > 5 else '0' for _ in range(N)]) for _ in range(M)]

t0 = time.time()


def time_day(day, skipped):
    day -= 1
    hours = A[day]

    count = hours.count('1')
    if count <= skipped:
        return 0

    # return random.randint(0, count)

    ts = []
    for i, v in enumerate(hours):
        if v == '1':
            ts.append(i)

    ans = float('inf')
    for l in range(1, skipped):
        r = skipped - l
        ans = min(ans, ts[-r-1] - ts[l] + 1)

    ans = min(ans, ts[-skipped-1] - ts[0] + 1)
    ans = min(ans, ts[-1] - ts[skipped] + 1)

    return ans


dp = [[float('inf') for _ in range(K+1)] for _ in range(M+1)]

for i in range(K+1):
    dp[0][i] = 0

for d in range(1, M+1):
    for k in range(K+1):
        dp[d][k] = min([dp[d-1][v] + time_day(d, k-v) for v in range(k+1)])

print(dp[M][K])

print(time.time() - t0)