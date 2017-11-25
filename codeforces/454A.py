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
created by shhuan at 2017/11/24 22:15

"""

N = int(input())


A = [["*" for _ in range(N)] for _ in range(N)]

s, l = N // 2, 1

for r in range(N//2+1):
    for c in range(s, s+l):
        A[r][c] = 'D'
    s -= 1
    l += 2

for r in range(N//2, N):
    s += 1
    l -=2
    for c in range(s, s+l):
        A[r][c] = 'D'

for row in A:
    print("".join(row))

