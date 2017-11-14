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
created by shhuan at 2017/11/9 23:24

"""

N, M = map(int, input().split())
A = [int(x) for x in input().split()]
#
# N, M = 35, 10**9
# A = [random.randint(10**2, 10**9) for _ in range(N)]

# t0 = time.time()
if N == 1:
    print(A[0] % M)
else:
    B = A[:N//2]
    C = A[N//2:]

    bs = {B[0], 0}
    for i in range(1, len(B)):
        bs |= {(v+B[i]) % M for v in bs}

    cs = {C[0], 0}
    for i in range(1, len(C)):
        cs |= {(v+C[i]) % M for v in cs}

    # bs = list(sorted(bs))
    cs = list(sorted(cs))

    ans = 0
    for b in bs:
        k = 1
        while True:
            i = bisect.bisect_left(cs, k*M - b)
            if i > 0:
                ans = max(ans, (b + cs[i - 1]) % M)
            if i < len(cs):
                ans = max(ans, (b + cs[i]) % M)

            if ans == M-1:
                print(ans)
                exit(0)
            if i == len(cs):
                break
            k += 1
    print(ans)

# print(time.time() - t0)
