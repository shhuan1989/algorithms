# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/17 11:06

"""

N, M = map(int, input().split())


ls = {l for l in range(2, N//2+2) if N % l == 0}

rm = set()
for l in ls:
    v = l * 2
    f = True
    while v < N:
        if v in ls:
            f = False
            break
        v += l
    if not f:
        rm.add(l)

ls -= rm

def mypow2(x, mod):

    if x == 0:
        return 1

    half = mypow2(x//2, mod)

    if x % 2 == 0:
        return (half * half) % mod
    else:
        return (half * half * 2) % mod


def gcx(x, y):
    if x < y:
        return gcx(y, x)
    if y == 0:
        return x

    return gcx(y, x%y)


g = collections.defaultdict(int)
for l in rm:
    for m in ls:
        if m % l == 0:
            g[l] += 1


ans = 0
for l in ls:
    ans += mypow2(l, M)
    ans = (ans + M - 2) % M

for v, c in g.items():
    if c > 1:
        c -= 1
        t = (mypow2(v, M) + M - 2) % M
        ans = (ans + M * c - t*c) % M


ans = mypow2(N, M) + 2*M - ans - 2
ans %= M
print(ans)
