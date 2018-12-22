# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/15 22:46

"""

N = int(input())
B = [int(x) for x in input().split()]

A = [0] * N

i, j = N//2-1, N//2
A[i] = B[-1] // 2
A[j] = B[-1] // 2 if B[-1] % 2 == 0 else B[-1] // 2 + 1
l, r = A[i], A[j]
for bi in range(len(B)-2, -1, -1):
    b = B[bi]
    i -= 1
    j += 1

    if b-l >= A[j-1]:
        A[i] = l
        A[j] = b-l
        r = b-l
    else:
        A[j] = r
        A[i] = b-r
        l = b-r

print(' '.join(map(str, A)))
