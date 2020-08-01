# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/7/21 20:02

"""




def split(N, A, M, K):
    l, r, c, s = 0, 0, 0, 0
    while r < N:
        if A[r] + s > K:
            c += 1
            if c > M:
                return False
            l = r
            s = A[r]
        else:
            s += A[r]
        r += 1

    if l < N:
        c += 1

    return c <= M




if __name__ == '__main__':
    N, M = map(int, input().split())

    A = []
    while len(A) < N:
        A += [int(x) for x in input().split()]

    lo, hi = max(A), sum(A)
    while lo <= hi:
        k = (lo + hi) // 2
        if split(N, A, M, k):
            hi = k - 1
        else:
            lo = k + 1

    print(lo)