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
created by shhuan at 2017/11/23 23:44

"""

MOD = 10**9+7


MAXN = 2*10**6 + 10
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


vis = [1] * MAXN
for i in range(2, MAXN):
    if vis[i]:
        v = i*2
        while v < MAXN:
            vis[v] = 0
            v += i
primes = []
for i in range(2, MAXN):
    if vis[i]:
        primes.append(i)


# print(primes[:10])


init(MOD)
Q = int(input())
for i in range(Q):
    x, y = map(int, input().split())

    A = [0] * y

    factors = collections.defaultdict(int)
    while x > 1:
        f = False
        for v in primes:
            if v > x:
                break
            if x % v == 0:
                factors[v] += 1
                x //= v
                f = True
                break
        if not f:
            factors[x] +=1
            break

    # print(factors)

    ans = my_pow(2, y-1, MOD)
    for k, v in factors.items():
        ans = ans * ncr(y+v-1, v, MOD)
        ans %= MOD

    print(ans)




