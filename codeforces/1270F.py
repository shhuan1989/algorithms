# -*- coding: utf-8 -*-
"""

created by shuangquan.huang at 12/31/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import math


def solve(A):
    N = len(A)
    K = max(int(math.log2(N)), 1)
    # K = N
    presum = [0 for _ in range(N + 1)]
    for i, v in enumerate(A):
        presum[i + 1] = presum[i] + v
    ans = 0
    for k in range(1, K + 1):
        wc = collections.defaultdict(int)
        for i in range(N + 1):
            v = i - k * presum[i]
            wc[v] += 1
        # print(wc)
        for v in wc.values():
            ans += v * (v - 1) // 2

    K += 1

    ones = [N for i in range(N + 1)]
    for i in range(N - 1, -1, -1):
        if A[i] == 1:
            ones[i] = i
        else:
            ones[i] = ones[i + 1]

    ksv = [i - K * presum[i] for i in range(N + 1)]
    rightmax = [N for i in range(N + 1)]
    for i in range(N - 1, -1, -1):
        if ksv[i] > ksv[rightmax[i + 1]]:
            rightmax[i] = i
        else:
            rightmax[i] = rightmax[i + 1]

    for i in range(N, -1, -1):
        j = ones[i]
        k = rightmax[j]
        if ksv[k] > ksv[i]:
            for k in range(j, N + 1):
                l = k - i
                d = presum[k] - presum[i]
                if d > 0 and l % d == 0 and l // d >= K:
                    ans += 1

    return ans


test = True
if test:
    A = [int(x) for x in list('00001100000000000000')]
    print(solve(A) == 58)
    A = [int(x) for x in list('0110110011011111001110000110010010000111111001100001011101101000001011001101100111011111100111101110')]
    print(solve(A) == 791)

    t0 = time.time()
    A = [0 for _ in range(2*10**5)]
    print(solve(A))
    print(time.time() - t0)

    t0 = time.time()
    A = [0 for _ in range(2 * 10 ** 5)] + [1]
    print(solve(A))
    print(time.time() - t0)

    t0 = time.time()
    A = [1] + [0 for _ in range(2 * 10 ** 5)] + [1]
    print(solve(A))
    print(time.time() - t0)

    t0 = time.time()
    A = [1] + [0 for _ in range(2 * 10 ** 5)]
    print(solve(A))
    print(time.time() - t0)

    t0 = time.time()
    A = [1 for _ in range(2 * 10 ** 5)]
    print(solve(A))
    print(time.time() - t0)

    A = [random.randint(0, 1) for _ in range(2 * 10 ** 5)]
    print('Starting')
    t0 = time.time()
    print(solve(A))
    print(time.time() - t0)

    print('DONE')

import random
A = [1] + [random.randint(0, 1) for _ in range(2*10**5)] + [1]
t0 = time.time()
solve(A)
print(time.time() - t0)