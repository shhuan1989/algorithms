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
created by shhuan at 2020/7/12 12:45

"""

if __name__ == '__main__':

    N, M = map(int, input().split())
    A = [0] + [int(x) for x in input().split()]
    B = []
    for i in range(M):
        d, s, t = map(int, input().split())
        B.append((d, s, t))

    C = [0 for _ in range(N + 2)]


    def check(v):
        for i in range(N + 2):
            C[i] = 0

        for i in range(min(v, len(B))):
            d, s, t = B[i]
            C[s] += d
            C[t + 1] -= d

        d = 0
        for i in range(1, N + 1):
            d += C[i]
            if d > A[i]:
                return False

        return True


    lo, hi = 0, N
    while lo <= hi:
        m = (lo + hi) // 2
        if check(m):
            lo = m + 1
        else:
            hi = m - 1

    if hi >= N:
        print(0)
    else:
        print(-1)
        print(hi + 1)