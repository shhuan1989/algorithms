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
    
    m = min(m, n-m)
    
    key = (n, m)
    if key in memo:
        return memo[key]

    ans = -1
    prekey = (n, m-1)
    if prekey in memo:
        preval = memo[prekey]
        ans = preval * (n-m+1) // m
    else:
        numer = reduce(op.mul, range(n, n - m, -1), 1)
        denom = reduce(op.mul, range(1, m + 1), 1)
        ans = numer // denom

    memo[key] = ans

    return ans

MOD = 10 ** 9 + 7

# memo = {}
# def ncr(n, m):
#     if m > n:
#         return 0
#
#     m = min(m, n-m)
#
#     if m == 1:
#         return n
#     if m == 0:
#         return 1
#
#     key = (n, m)
#     if key in memo:
#         return memo[key]
#
#     ans = ncr(n-1, m) + ncr(n-1, m-1)
#     ans %= MOD
#     memo[key] = ans
#
#     return ans
#



def solve(A):
    ans = 0
    A = list(sorted(collections.Counter(A).items()))
    N = len(A)
    
    if max([v[1] for v in A]) == 1:
        for i in range(1, N+1, 2):
            ans += ncr(N, i)
            ans %= MOD
        
        return ans
        
    left, right = [0] * (N+1), [0] * (N+1)
    for i in range(N):
        left[i+1] = left[i] + A[i][1]
    for i in range(N-1, -1, -1):
        right[i] = right[i+1] + A[i][1]

    for i, v in enumerate(A):
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
        
        nrcs = [1] * (r+1)
        for c in range(1, r+1):
            nrcs[c] = nrcs[c-1] + ncr(r, c)

        for b in range(1, m + 1):
            nb = ncr(m, b)
            for a in range(min(l, r+b-1)+1):
                mxc = min(a+b-1, r)
                na = ncr(l, a)
                nc = nrcs[mxc] - (nrcs[a - b] if a-b >= 0 else 0)
                ans += na * nb * nc
                ans %= MOD

    return ans % MOD


# import random
# t0 = time.time()
# A = [i+1 for i in range(1000)]
# for i in range(30):
#     random.shuffle(A)
#     print(solve(A))
#
# print(time.time() - t0)

T = int(input())
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    print(solve(A))