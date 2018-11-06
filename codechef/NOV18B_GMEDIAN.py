# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from functools import reduce
import operator as op

"""
created by shhuan at 2018/11/6 21:53

"""


memo = {}
def ncr(n, m):
    if m > n:
        return 0
    key = (n, m)
    if key in memo:
        return memo[key]

    ans = -1
    prekey = (n, m-1)
    if prekey in memo:
        preval = memo[prekey]
        ans = preval * (n-m+1) // m
    else:
        m = min(m, n-m)
        numer = reduce(op.mul, range(n, n - m, -1), 1)
        denom = reduce(op.mul, range(1, m + 1), 1)
        ans = numer // denom

    memo[key] = ans

    return ans


def solve(A, N):
    A.sort()
    mod = 10**9 + 7
    ans = 0

    B = list(sorted(collections.Counter(A).items()))
    LB = len(B)
    left, right = [0] * (LB+1), [0] * (LB+1)

    for i in range(LB):
        left[i+1] = left[i] + B[i][1]
    for i in range(LB-1, -1, -1):
        right[i] = right[i+1] + B[i][1]

    for i, v in enumerate(B):
        l, m, r = left[i], v[1], right[i+1]

        # consist array with 3 parts,
        # left contains a elements less than current val v[0]
        # mid contains b elements equals v[0]
        # right contains c elements greater than v[0]
        # na = ncr(l, a), nb = ncr(m, b), nc = ncr(r, c)

        # for b in range(1, m + 1):
        #     nb = ncr(m, b)
        #     for a in range(l+1):
        #         na = ncr(l, a)
        #         for c in range(max(0, a-b+1), a+b):
        #             ans += na * nb * ncr(r, c)
        #             ans %= mod

        nlas = [1] * (l+1)
        nmbs = [1] * (m+1)
        nrcs = [1] * (r+1)

        for c in range(1, r+1):
            nrcs[c] = nrcs[c-1] + ncr(r, c)

        for a in range(1, l+1):
            nlas[a] = nlas[a-1] + ncr(l, a)

        for b in range(1, m+1):
            nmbs[b] = nmbs[b-1] + ncr(m, b)

        for b in range(1, m + 1):
            nb = ncr(m, b)
            for a in range(l+1):
                if a + b - 1 > r:
                    break
                na = ncr(l, a)
                ans += na * nb * (nrcs[a+b-1] - nrcs[max(0, a-b+1)] + ncr(r, max(0, a-b+1)))
                ans %= mod

    return ans % mod


T = int(input())
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    print(solve(A, N))