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
created by shhuan at 2018/10/18 21:24

"""


def check(N, M, A, B, C):
    total = 0
    for i in range(N):
        #(A[i]-x)*B[i] <= C
        # A[i]*B[i] - C <= x*B[i]
        # x >= (A[i]*B[i]-C)//B[i]
        a = max(0, A[i]*B[i]-C)
        if a % B[i] == 0:
            total += a // B[i]
        else:
            total += a // B[i] + 1
        if total > M:
            return False

    return total <= M


def solve(N, M, A, B):

    lo, hi = 0, max([A[i]*B[i] for i in range(N)])

    while lo < hi:
        maxc = lo + (hi-lo)//2
        if check(N, M, A, B, maxc):
            hi = maxc
        else:
            lo = maxc + 1

    return lo

N, M = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

print(solve(N, M, A, B))



