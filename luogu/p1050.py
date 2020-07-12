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
created by shhuan at 2020/7/10 21:54

"""


def mul(x, y, z, k):
    for i in range(k+1):
        z[i] = 0
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if i + j - 1 > k:
                break
            v = x[i] * y[j]
            z[i+j-1] += v
            if i + j <= K:
                z[i+j] += z[i+j-1]//10
            z[i+j-1] %= 10


def mul2(x, y, z, k):
    for i in range(k+1):
        z[i] = 0
    for i in range(1, len(x)):
        if z[i] > k:
            break
        z[i] += x[i] * y
        if i + 1 <= k:
            z[i+1] += z[i] // 10
        z[i] %= 10

    return z


def copy(a, b):
    for i in range(len(a)):
        b[i] = a[i]


CYCLE = [1, 1, 4, 4, 2, 1, 1, 4, 4, 2]

if __name__ == '__main__':
    C, K = input().split()
    K = int(K)
    B = [0] + [int(v) for v in C[-K:][::-1]]

    b = B.copy()
    d = [0 for _ in range(K+1)]
    for i in range(1, CYCLE[B[1]]):
        mul(b, B, d, K)
        copy(d, b)
    cycle = [0 for _ in range(K+1)]
    cycle[1] = CYCLE[B[1]]


    p, q = b.copy(), b.copy()
    for ki in range(2, K+1):
        copy(B, b)
        t = 0
        while t < 11:
            # b = B * p ** t
            mul(b, p, d, K)
            copy(d, b)
            t += 1
            if b[ki] == B[ki]:
                break
            mul(q, p, d, K)
            copy(d, q)
        if t >= 11:
            print(-1)
            exit(0)
        copy(q, p)
        mul2(cycle, t, d, K)
        copy(d, cycle)

    for i in range(K, -1, -1):
        if cycle[i] != 0:
            print(''.join(map(str, cycle[1:i+1][::-1])))
            exit()





