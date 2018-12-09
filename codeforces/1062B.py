# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/19 19:03

"""

N = int(input())

factors = collections.defaultdict(int)

primes = [True for _ in range(max(1+N//2, 10))]
primes[0] = primes[1] = False

for i in range(2, N//2+1):
    if primes[i]:
        t = 2
        while i * t <= N//2:
            primes[i*t] = False
            t += 1

n = N
for i in range(2, N//2+1):
    if not primes[i]:
        continue

    while i <= n and n % i == 0:
        n //= i
        factors[i] += 1

def dpow(x):
    u = int(math.log2(x))
    p = 1 << u
    if p < x:
        return u + 1
    else:
        return u


vals = list(factors.values())
U = [dpow(a) for a in vals]

if not U:
    print(N, 0)
else:
    ans = 1
    for v in factors.keys():
        ans *= v
    # print(vals, U)
    u = max(U)
    if all(2**u == vals[i] for i in range(len(vals))):
        print(ans, u)
    else:
        print(ans, u+1)





