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
created by shhuan at 2017/11/22 21:13

"""

N = int(input())

A = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    A[i][0] = 1
    A[0][i] = 1

for i in range(N):
    for j in range(N):
        if A[i][j] == 0:
            A[i][j] = A[i-1][j] + A[i][j-1]

ans = 0
for row in A:
    ans = max(ans, max(row))

print(ans)