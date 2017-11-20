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
created by shhuan at 2017/11/20 09:58

"""

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

def lucas(n, m, p):
    if m == 0:
        return 1

    return (ncr(n%p, m%p, p) * lucas(n//p, m//p, p)) % p


if __name__ == '__main__':
    p = 10**9+7
    init(p)
    print(ncr(131, 13, p))
    print(lucas(131, 13, p))

    print(ncr(5, 2, p))
    print(lucas(5, 2, p))