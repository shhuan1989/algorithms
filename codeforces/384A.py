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
created by shhuan at 2017/11/24 22:46

"""

N = int(input())
A = [['.' for _ in range(N)] for _ in range(N)]
if N % 2 == 0:
    print(N*N//2)
else:
    a = N//2+1
    print(a*a + (a-1)**2)

for r in range(N):
    s = 1 if r % 2 == 1 else 0
    for c in range(s, N, 2):
        A[r][c] = 'C'

for row in A:
    print("".join(row))