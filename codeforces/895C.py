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
created by shhuan at 2017/11/27 12:15

"""

MOD  = 10**9+7
N = int(input())
A = [int(x) for x in input().split()]

# x1*x2*...*xi = y*y
# every number occurs even times

wc = collections.defaultdict(int)
for i, v in enumerate(A):
    wc[v] += 1


def ncr(m, n):
    return 0

# c(n1, v1) * c(n2, v2) * ... * c(ni, vi)
# = sigma(c(n1, {0, 2, 4, 6...}))* c2(n2, v2)...
# = sigma(c(n1, {0, 2, 4, 6...})) * sigma(c(n2, {0, 2,..}))...

def my_pow(a, b, p):
    if b == 0:
        return 1
    h = my_pow(a, b//2, p)
    if b & 1 == 1:
        return (h*h*a) % p
    else:
        return (h*h) % p

nums = list(sorted(wc.keys()))


MAXN = 10 ** 5
fac = [0] * MAXN


def init(p):
    fac[0] = 1
    for i in range(1, MAXN):
        fac[i] = (fac[i-1] * i) % p


def my_pow(a, b, p):
    a %= p
    ans = 1

    while b > 0:
        if b & 1:
            ans = (ans * a) % p
        a = (a * a) % p
        b >>= 1

    return ans

def ncr(n, m, p):
    if m > n:
        return 0

    return (fac[n] * my_pow(fac[m] * fac[n-m], p-2, p)) % p

init(MOD)



# 4 = 2*2, 9, 16, 25, 36, 49, 64
# 6 = 2*3           => 2, 3
# 8 = 2*2*2         => 2
# 10 = 2 * 5        => 2, 5
# 12 = 2*2*3        => 3
# 14 = 2*7          => 2, 7
# 15 = 3*5          => 3, 5
# 18 = 2*3*3        => 2
# 20 = 2*2*5        => 5
# 21 = 3*7          => 3, 7
# 22 = 2*11         => 2, 11
# 24 = 2*2*2*3      => 2, 3
# 26 = 2*13         => 2, 13
# 27 = 3*3*3        => 3
# 28 = 2*2*7        => 7
# 30 = 2*3*5        => 2, 3, 5
# 32 = 2*4*4        => 2
# 33 = 3*11         => 3, 11
# 34 = 2*17         => 2, 17
# 35 = 5*7          => 5, 7
# 38 = 2*19         => 2, 19
# 39 = 3*13         => 3, 13
# 40 = 2*2*2*5      => 2, 5
# 42 = 2*3*7        => 2, 3, 7
# 44 = 2*2*11       => 11
# 45 = 3*3*5        => 5
# 46 = 2*23         => 23
# 48 = 2*2*2*2*3    => 2, 3
# 50 = 2*5*5        => 2
# 52 = 2*2*13       => 13
# 54 = 2*3*3*3      => 2, 3
# 55 = 5*11         => 5, 11
# 56 = 2*2*2*7      => 2, 7
# 58 = 2*29         => 2, 29
# 60 = 2*2*3*5      => 3, 5
# 62 = 2*31         => 2, 31
# 63 = 3*21         => 3, 21
# 65 = 5*13         => 5, 13
# 66 = 2*3*11       => 2, 3, 11
# 68 = 2*2*17       => 17
# 70 = 2*5*7        => 2, 5, 7

same = {
    8: 2,
    12: 3,
    18: 2,
    20: 5,
    27: 3,
    28: 7,
    32: 2,
    44: 11,
    45: 5,
    48: 3,
    50: 2,
    52: 13,
    63: 7,
    68: 17
}

pw = {1, 4, 9, 16, 25, 36, 49, 64}

eff = {
    6: [2, 3],
    10: [2, 5],
    14: [2, 7],
    15: [3, 5],
    21: [3, 7],
    22: [2, 11],
    24: [2, 3],
    26: [2, 13],
    30: [2, 3, 5],
    33: [3, 11],
    34: [2, 17],
    35: [5, 7],
    38: [2, 19],
    39: [3, 13],
    40: [2, 5],
    42: [2, 3, 7],
    46: [2, 23],
    54: [2, 3],
    55: [5, 11],
    56: [2, 7],
    58: [2, 29],
    60: [3, 5],
    62: [2, 31],
    65: [5, 13],
    66: [2, 3, 11],
    70: [2, 5, 7]
}

for k1, v1 in eff.items():
    for k2, v2 in eff.items():
        if k1 < k2 and v1 == v2:
            same[k2] = k2


# CN = 71
# count = [0] * CN
# for k, v in wc.items():
#     count[k] = v


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 51, 53, 57, 59, 61, 67]

for p in primes:
    eff[p] = [p]

ans = 1
for k in pw:
    if k in wc:
        # use 0-wc[k] number of k, k is square of some number
        ans *= 2**wc[k] - 1
        ans %= MOD

nwc = collections.defaultdict(int)
for k, v in wc.items():
    if k not in pw:
        if k in same:
            nwc[same[k]] += v
        else:
            nwc[k] += v


eff = {k: v for k, v in eff.items() if k in nwc}

effk = list(sorted(eff.keys()))
neff = len(effk)

def check(status):
    primepower = [0] * 71
    ans = 1
    for i in range(neff):
        k = effk[i]
        if (status >> i) & 1 == 1:
            if k not in nwc:
                return 0
            # 1, 3, 5,... number of k, max is nwc[k]

            y = 0
            for x in range(1, nwc[k], 2):
                y += ncr(nwc[k], x, MOD)
                y %= MOD

            ans *= y
            ans %= MOD
            vs = eff[k]
            for v in vs:
                primepower[v] += 1
        else:
            #0, 2, 4, 6..., number of k
            y = 0
            for x in range(0, nwc[k], 2):
                y += ncr(nwc[k], x, MOD)
                y %= MOD
            ans *= y
            ans %= MOD

    if all([x % 2 == 0 for x in primepower]):
        return ans

    return 0


if neff > 0:
    ans2 = 0
    for status in range(2**neff):
        # the ith digit of status is 1 means odds number of eff[i]
        ans2 += check(status)
        ans2 %= MOD

    ans *= ans2
ans %= MOD
print(ans)


















