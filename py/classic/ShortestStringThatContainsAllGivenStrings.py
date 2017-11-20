# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/8 09:18

"""

# N = int(input())
#
# A = set()
# for i in range(N):
#     A.add(input().strip())

N = random.randint(1, 15)
A = set()
for i in range(N):
    s = ''.join([chr(ord('a') + random.randint(0, 25)) for _ in range(random.randint(1, 100))])
    A.add(s)

print(N)
print(A)

rem = set()
for v in A:
    for u in A:
        if u != v and u.find(v) >= 0:
            rem.add(v)

A -= rem
A = list(A)
N = len(A)

overlap = collections.defaultdict(int)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        u, v = A[i], A[j]
        l = 0
        for k in range(min(len(u), len(v)), 0, -1):
            if u[-k:] == v[:k]:
                l = k
                break
        overlap[(i, j)] = l

# f(i, j) => f(i, k)
# f(i|(1<<k), k) = max{f(i|(1<<k), k), f(i, j)+overlap(j, k)}

dp = [[float('-inf') for _ in range(N)] for _ in range(2 ** N + 1)]

for i in range(N):
    dp[1 << i][i] = 0

for i in range(2 ** N + 1):
    for j in range(N):
        if i & (1 << j) == 0:
            continue
        for k in range(N):
            if i & (1 << k):
                continue
            ni = i | (1 << k)
            dp[ni][k] = max(dp[ni][k], dp[i][j] + overlap[(j, k)])

# print(A)
# print(overlap)
# print(sum([len(v) for v in A] or [0]))
# print(max(dp[2**N-1]))

print(sum([len(v) for v in A] or [0]) - max(dp[2 ** N - 1]))


















