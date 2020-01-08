# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/2/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

# N = int(input())
# A = []
# for i in range(N):
#     row = [int(x) for x in input().split()]
#     A.append(row)


import random
N = 2000
A = []
for i in range(N):
    row = [random.randint(1, 10**9) for _ in range(N)]
    A.append(row)
    
print('starting')
t0 = time.time()


diagonal1 = [0 for _ in range(2*N)]
diagonal2 = [0 for _ in range(2*N)]

for r in range(N):
    for c in range(N):
        i1 = N+c-r-1
        i2 = r+c
        diagonal1[i1] += A[r][c]
        diagonal2[i2] += A[r][c]

va, ra, ca = 0, 0, 0
vb, rb, cb = 0, 0, 1
for r in range(N):
    for c in range(N):
        i1 = N + c - r - 1
        i2 = r + c
        v = diagonal1[i1] + diagonal2[i2] - A[r][c]
        if (r + c) % 2 == 0:
            if v > va:
                va = v
                ra, ca = r, c
        else:
            if v > vb:
                vb = v
                rb, cb = r, c

print(va + vb)
print('{} {} {} {}'.format(ra+1, ca+1, rb+1, cb+1))
print(time.time() - t0)