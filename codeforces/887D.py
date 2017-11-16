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
created by shhuan at 2017/11/4 01:08

"""

N, a, b, c, d, start, l = map(int, input().split())

A = []
for i in range(N):
    t, q = map(int, input().split())
    A.append((t, q))


# fashion show, -b, -d
# photo shoot, +a, +c

N += 1
A = [(-1, -1)] + A
left1 = [0] * N
left2 = [0] * N
left1[0] = start
left2[0] = start

for i in range(1, N):
    _, q = A[i]
    # q=0, fashion show
    # q=1, photo shoot
    if q == 0:
        left1[i] = left1[i-1] - b
        left2[i] = left2[i-1] - d
    else:
        left1[i] = left1[i-1] + a
        left2[i] = left2[i-1] + c

# rmq
M = 1
while 2**M <= N:
    M += 1

RMQ = [[float('inf') for _ in range(M)] for _ in range(N)]
for i in range(N):
    RMQ[i][0] = left2[i]

for k in range(1, M):
    for i in range(N):
        h = k-1
        m = i+2**h
        if m >= N:
            break
        # print(i, h, m)
        RMQ[i][k] = min(RMQ[i][h], RMQ[m][h])


def rmq(l, r):
    if l > r:
        return float('inf')
    if r-l == 1:
        return RMQ[l][0]
    k = 0
    while l+2**k < r:
        k += 1

    if l + 2**k == r:
        return RMQ[l][k]

    k -= 1

    return min(rmq(l, l+2**k), rmq(l+2**k, r))


for i in range(0, N):
    if left1[i] < 0:
        print(-1)
        exit(0)
    t, q = A[i]
    t += 1
    uk = bisect.bisect_left(A, (t+l, float('-inf')))
    if uk <= i+1:
        print(t)
        exit(0)
    # v = min(left2[i+1: uk])
    v = rmq(i+1, uk)
    v += left1[i] - left2[i]
    if v >= 0:
        print(t)
        exit(0)
print(-1)