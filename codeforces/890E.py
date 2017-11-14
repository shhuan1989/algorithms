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
created by shhuan at 2017/11/13 00:46

"""


N, K = map(int, input().split())


def my_pow(a, b, m):
    if b == 0:
        return 1
    p = my_pow(a, b//2, m)
    p *= p
    p %= m
    if b % 2 == 1:
        return (p*a) % m

    return p


MOD = 10**9+7
M = 1000006

D = [0] * M
part = [0] * M # prefix sum for values D(h)/(h-1)!
fac = [0] * M

fac[0] = 1
for i in range(1, M):
    fac[i] = (fac[i-1] * i) % MOD

for i in range(K+1, N+1):
    D[i] = ((i-K-1) * fac[i-2]) % MOD
    D[i] += ((part[i-1] - part[i-K-1] + MOD) * fac[i-2]) % MOD

    # part[i] = part[i-1] + D[i]/(i-1)!
    part[i] = part[i-1] + (D[i] * my_pow(fac[i-1], MOD-2, MOD)) % MOD

print((part[N] * fac[N-1]) % MOD)
