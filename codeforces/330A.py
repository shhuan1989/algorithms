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
created by shhuan at 2017/11/24 13:43

"""

N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(input()))

for r in range(N):
    if all([A[r][c] != 'S' for c in range(M)]):
        for c in range(M):
            A[r][c] = '1'

for c in range(M):
    if all([A[r][c] != 'S' for r in range(N)]):
        for r in range(N):
            A[r][c] = '1'

ans = 0
for r in range(N):
    for c in range(M):
        if A[r][c] == '1':
            ans += 1
print(ans)