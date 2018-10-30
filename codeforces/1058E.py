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
created by shhuan at 2018/10/22 21:35

"""


def countOne(num):
    return len([x for x in bin(num)[2:] if x == '1'])


def solve(nums):
    N = len(nums)
    ones = [countOne(x) for x in nums]

    res = 0
    sufSum = 0
    # cnt = [[0 for _ in range(N+1)] for _ in range(2)]
    # cnt[0][N] = 1
    s0, s1 = 1, 0

    for i in range(N-1, -1, -1):
        sm, mx, add = 0, 0, 0
        for j in range(i, min(N, i+65)):
            sm += ones[j]
            mx = max(mx, ones[j])
            if mx > sm - mx and sm & 1 == 0:
                add -= 1

        sufSum += ones[i]
        # add += cnt[sufSum & 1][i+1]
        add += s0 if sufSum & 1 == 0 else s1
        res += add

        # cnt[0][i] = cnt[0][i+1]
        # cnt[1][i] = cnt[1][i+1]

        if sufSum & 1:
            # cnt[1][i] += 1
            s1 += 1
        else:
            # cnt[0][i] += 1
            s0 += 1

    # print(cnt[0])
    # print(cnt[1])
    return res







# N = int(input())
# A = [int(x) for x in input().split()]
# A = [1, 2, 1, 16]

A = [random.randint(10**16, 10**18) for _ in range(300000)]
t0 = time.time()
print(solve(A))
print(time.time() - t0)