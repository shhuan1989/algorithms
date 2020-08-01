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
created by shhuan at 2020/7/14 19:21

"""

MAXN = 10**3
isprime = [True for _ in range(MAXN)]
for i in range(2, MAXN):
    if not isprime[i]:
        continue
    v = i + i
    while v < MAXN:
        isprime[v] = False
        v += i

primes = [i for i in range(2, MAXN) if isprime[i]]


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def defact(x):
    wc = collections.defaultdict(int)
    pi = 0
    while pi < len(primes) and x > 1:
        p = primes[pi]
        while x % p == 0:
            x //= p
            wc[p] += 1
        pi += 1
    if x > 1:
        wc[x] += 1

    return wc


def mypow(x, y, b):
    # return a, b that x**a == y ** b

    wcx = defact(x)
    wcy = defact(y)

    wy = list(sorted(wcy.keys()))

    for w in wy:
        if wcx[w] <= 0:
            return -1

    if not wy:
        return 0

    cx = [wcx[v] for v in wy]
    cy = [wcy[v] for v in wy]

    return max([j*b//i if (j*b) % i == 0 else j*b//i+1 for i, j in zip(cx, cy)] or [-1])


if __name__ == '__main__':
    N = int(input())
    m1, m2 = map(int, input().split())
    X = [int(x) for x in input().split()]

    ans = float('inf')
    for x in X:
        a = mypow(x, m1, m2)
        if a < 0:
            continue
        ans = min(ans, a)
    ans = ans if ans < float('inf') else -1
    print(ans)


