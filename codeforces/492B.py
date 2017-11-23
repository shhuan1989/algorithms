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
created by shhuan at 2017/11/22 10:41

"""

N, L = map(int, input().split())

A = [int(x) for x in input().split()]

A = list(set(A))
A.sort()
N = len(A)

def check(r):
    if r < A[0] or r < L - A[N-1]:
        return False
    for i in range(1, N):
        if A[i] - A[i-1] > 2*r:
            return False

    return True


lo = 0
hi = 10**10

for i in range(120):
    m = (lo + hi) /2

    if check(m):
        hi = m
    else:
        lo = m

print(lo)