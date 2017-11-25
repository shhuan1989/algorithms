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
created by shhuan at 2017/11/24 18:15

"""

N = int(input())

A = [[0 for _ in range(2*N+1)] for _ in range(2*N+1)]


q = [(N, N, N)]
A[N][N] = N
while q:
    r, c, v = q.pop(0)
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r+d[0], c+d[1]
        if v > 0 and 0 <= nc < 2*N+1 and 0 <= nr < 2*N+1 and A[nr][nc] == 0:
            A[nr][nc] = v-1
            q.append((nr, nc, v-1))

s, l = N, 1
up = True
for row in A:
    print("  " * s + " ".join(map(str, row[s: s+l])))
    if up:
        s -= 1
        l += 2
    else:
        s += 1
        l -= 2
    if s == 0:
        up = False