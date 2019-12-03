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
created by shhuan at 2019/11/30 14:44

"""

N, S = map(int, input().split())
E = [int(x) for x in input().split()]

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

st = [S]
s = S
for i in range(N):
    ds, ts = 0, s
    while ts > 0:
        ds += ts % 10
        ts //= 10
    s += ds ** 3
    st.append(s)

print(st)


for i in range(1, N+1):
    dp[i][0] = sum(E[:i]) * S
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], (dp[i-1][j] + st[j] * E[i-1]) if i-1 >= j else 0)

print(max(dp[N]))