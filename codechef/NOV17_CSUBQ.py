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
created by shhuan at 2017/11/12 08:18

"""



N, Q, L, R = map(int, input().split())

A = [0] * (N+1)

M = 0
while 2 ** M < N:
    M += 1
M += 1

RMQ = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        RMQ[i][j] = i

def update(index, val):
    A[index] = val
    for l in range(index):
        # l + 2^j > index => j > log((index-l))
        for r in range(int(math.ceil(max(1, math.log(index-l, 2)))), M):
            if l + 2**r > N:
                break

            a, b = RMQ[l][r-1], RMQ[l+2**(r-1)][r-1]
            c = a if A[a] >= A[b] else b
            if A[c] > A[RMQ[l][r]]:
                RMQ[l][r] = c
            else:
                break

def query(L, R, x, y):
    # print(L, R)
    if L > R:
        return 0
    if L == R:
        return 1 if A[L] == L else 0

    a = int(math.log(R-L+1, 2))
    b, c = RMQ[L][a], RMQ[R-2**a+1][a]
    d = b if A[b] >= A[c] else c
    mx = A[d]

    ans = 0
    if mx < x:
        ans = 0
    elif mx > y:
        return query(L, d-1, x, y) + query(d+1, R, x, y)
    else:
        ans = (d-L) * (R-d) + R - d + L - d + 1
    # print(L, R, ans)
    return ans

for i in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
        # print(A)
    else:
        print(query(b, c, b, c))

# print(A)
